<?php
header('Content-Type: application/json');
require_once __DIR__ . '/storage.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
    exit;
}

$input = json_decode(file_get_contents('php://input'), true);
if (!$input) {
    $input = $_POST;
}

$event_type = $input['event_type'] ?? '';
$valid_events = ['FORM_SUBMISSION', 'PHONE_CLICK', 'WHATSAPP_CLICK'];

if (!in_array($event_type, $valid_events)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid event type']);
    exit;
}

$ip_address = $_SERVER['REMOTE_ADDR'] ?? '';

// Basic Abuse Protection / Rate Limiting (Max 20 events per IP per hour)
$recent_count = getRecentLeadCountByIp($ip_address);
if ($recent_count > 20) {
    http_response_code(429);
    echo json_encode(['success' => false, 'error' => 'Too many requests. Please try again later.']);
    exit;
}

// Data Handling: Validate and store WITHOUT html escaping
$name = mb_substr(trim($input['name'] ?? ''), 0, 255, 'UTF-8');
$email = mb_substr(trim($input['email'] ?? ''), 0, 255, 'UTF-8');
$phone = mb_substr(trim($input['phone'] ?? ''), 0, 255, 'UTF-8');
$course = mb_substr(trim($input['course'] ?? ''), 0, 255, 'UTF-8');
$message = mb_substr(trim($input['message'] ?? ''), 0, 2000, 'UTF-8');
$source_url = mb_substr(trim($input['source_url'] ?? $_SERVER['HTTP_REFERER'] ?? ''), 0, 500, 'UTF-8');
$referrer = mb_substr(trim($input['referrer'] ?? ''), 0, 500, 'UTF-8');
$user_agent = mb_substr($_SERVER['HTTP_USER_AGENT'] ?? '', 0, 500, 'UTF-8');
$created_at = date('Y-m-d H:i:s');
$id = bin2hex(random_bytes(16));

if ($event_type === 'FORM_SUBMISSION' && !empty($email)) {
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Invalid email format']);
        exit;
    }
}

$leadData = [
    'id' => $id,
    'event_type' => $event_type,
    'name' => $name,
    'email' => $email,
    'phone' => $phone,
    'course' => $course,
    'message' => $message,
    'source_url' => $source_url,
    'referrer' => $referrer,
    'ip_address' => $ip_address,
    'user_agent' => $user_agent,
    'created_at' => $created_at,
    'status' => 'new',
    'notes' => ''
];

if (appendLead($leadData)) {
    http_response_code(201);
    echo json_encode(['success' => true, 'id' => $id]);
} else {
    error_log("JSONL Insert Error: Failed to write to leads.jsonl");
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'storage_write_failed']);
}
