<?php
require_once __DIR__ . '/../api/auth.php';
requireAuth();
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = json_decode(file_get_contents('php://input'), true);
    if (!$input) { $input = $_POST; }
    
    $csrf = $input['csrf_token'] ?? '';
    if (!verifyCsrfToken($csrf)) {
        http_response_code(403);
        echo json_encode(['success' => false, 'error' => 'Invalid CSRF token']);
        exit;
    }
    
    $action = $input['action'] ?? '';
    
    if ($action === 'update_status') {
        $id = $input['id'] ?? 0;
        $status = $input['status'] ?? '';
        $valid_statuses = ['new', 'contacted', 'qualified', 'converted', 'closed'];
        if (in_array($status, $valid_statuses)) {
            $stmt = $pdo->prepare("UPDATE leads SET status = ? WHERE id = ?");
            $stmt->execute([$status, $id]);
            echo json_encode(['success' => true]);
            exit;
        }
    }
    if ($action === 'update_notes') {
        $id = $input['id'] ?? 0;
        $notes = htmlspecialchars($input['notes'] ?? '', ENT_QUOTES, 'UTF-8');
        $stmt = $pdo->prepare("UPDATE leads SET notes = ? WHERE id = ?");
        $stmt->execute([$notes, $id]);
        echo json_encode(['success' => true]);
        exit;
    }
    if ($action === 'change_password') {
        $current = $input['current_password'] ?? '';
        $new = $input['new_password'] ?? '';
        $confirm = $input['confirm_password'] ?? '';
        
        if (strlen($new) < 12) {
            echo json_encode(['success' => false, 'error' => 'New password must be at least 12 characters']);
            exit;
        }
        if ($new !== $confirm) {
            echo json_encode(['success' => false, 'error' => 'Passwords do not match']);
            exit;
        }
        
        $stmt = $pdo->prepare("SELECT password_hash FROM users WHERE id = ?");
        $stmt->execute([$_SESSION['admin_user_id']]);
        $user = $stmt->fetch();
        
        if ($user && password_verify($current, $user['password_hash'])) {
            $hash = password_hash($new, PASSWORD_DEFAULT);
            $stmt = $pdo->prepare("UPDATE users SET password_hash = ? WHERE id = ?");
            $stmt->execute([$hash, $_SESSION['admin_user_id']]);
            session_regenerate_id(true);
            echo json_encode(['success' => true]);
            exit;
        } else {
            echo json_encode(['success' => false, 'error' => 'Incorrect current password']);
            exit;
        }
    }
    
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid action']);
}
