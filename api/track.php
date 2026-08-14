<?php
header('Content-Type: application/json');
require_once __DIR__ . '/db.php';

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
$stmt = $pdo->prepare("SELECT COUNT(*) FROM leads WHERE ip_address = ? AND created_at > datetime('now', '-1 hour')");
$stmt->execute([$ip_address]);
$recent_count = $stmt->fetchColumn();

if ($recent_count > 20) {
    http_response_code(429);
    echo json_encode(['success' => false, 'error' => 'Too many requests. Please try again later.']);
    exit;
}

$name = htmlspecialchars(substr($input['name'] ?? '', 0, 255), ENT_QUOTES, 'UTF-8');
$email = htmlspecialchars(substr($input['email'] ?? '', 0, 255), ENT_QUOTES, 'UTF-8');
$phone = htmlspecialchars(substr($input['phone'] ?? '', 0, 255), ENT_QUOTES, 'UTF-8');
$course = htmlspecialchars(substr($input['course'] ?? '', 0, 255), ENT_QUOTES, 'UTF-8');
$message = htmlspecialchars(substr($input['message'] ?? '', 0, 2000), ENT_QUOTES, 'UTF-8');
$source_url = htmlspecialchars(substr($input['source_url'] ?? $_SERVER['HTTP_REFERER'] ?? '', 0, 500), ENT_QUOTES, 'UTF-8');
$referrer = htmlspecialchars(substr($input['referrer'] ?? '', 0, 500), ENT_QUOTES, 'UTF-8');
$user_agent = substr($_SERVER['HTTP_USER_AGENT'] ?? '', 0, 500);
$created_at = date('Y-m-d H:i:s');

try {
    $stmt = $pdo->prepare("
        INSERT INTO leads (
            event_type, name, email, phone, course, message, 
            source_url, referrer, ip_address, user_agent, created_at, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'new')
    ");
    $stmt->execute([
        $event_type, $name, $email, $phone, $course, $message,
        $source_url, $referrer, $ip_address, $user_agent, $created_at
    ]);
    
    http_response_code(201);
    echo json_encode(['success' => true, 'id' => $pdo->lastInsertId()]);
} catch (Exception $e) {
    error_log("DB Insert Error: " . $e->getMessage());
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Server error']);
}
