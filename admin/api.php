<?php
require_once __DIR__ . '/../api/auth.php';
require_once __DIR__ . '/../api/storage.php';
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
        $id = (string)($input['id'] ?? '');
        $status = $input['status'] ?? '';
        $valid_statuses = ['new', 'contacted', 'qualified', 'converted', 'closed'];
        if (in_array($status, $valid_statuses)) {
            if (updateLead($id, ['status' => $status])) {
                echo json_encode(['success' => true]);
            } else {
                echo json_encode(['success' => false, 'error' => 'Failed to update status']);
            }
            exit;
        }
    }
    if ($action === 'update_notes') {
        $id = (string)($input['id'] ?? '');
        // Do not HTML escape before storage. Store raw data.
        $notes = trim($input['notes'] ?? '');
        if (updateLead($id, ['notes' => $notes])) {
            echo json_encode(['success' => true]);
        } else {
            echo json_encode(['success' => false, 'error' => 'Failed to update notes']);
        }
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
        
        $user = getUserById($_SESSION['admin_user_id']);
        
        if ($user && password_verify($current, $user['password_hash'])) {
            $hash = password_hash($new, PASSWORD_DEFAULT);
            if (updateUserPassword($_SESSION['admin_user_id'], $hash)) {
                session_regenerate_id(true);
                echo json_encode(['success' => true]);
            } else {
                echo json_encode(['success' => false, 'error' => 'Failed to update password']);
            }
            exit;
        } else {
            echo json_encode(['success' => false, 'error' => 'Incorrect current password']);
            exit;
        }
    }
    
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid action']);
}
