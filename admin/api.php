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
        $notes = trim($input['notes'] ?? '');
        if (updateLead($id, ['notes' => $notes])) {
            echo json_encode(['success' => true]);
        } else {
            echo json_encode(['success' => false, 'error' => 'Failed to update notes']);
        }
        exit;
    }
    if ($action === 'soft_delete') {
        $id = (string)($input['id'] ?? '');
        if (softDeleteLead($id)) {
            echo json_encode(['success' => true]);
        } else {
            echo json_encode(['success' => false, 'error' => 'Failed to delete lead']);
        }
        exit;
    }
    if ($action === 'restore_lead') {
        $id = (string)($input['id'] ?? '');
        if (restoreLead($id)) {
            echo json_encode(['success' => true]);
        } else {
            echo json_encode(['success' => false, 'error' => 'Failed to restore lead']);
        }
        exit;
    }
    if ($action === 'permanent_delete') {
        $id = (string)($input['id'] ?? '');
        if (permanentlyDeleteLead($id)) {
            echo json_encode(['success' => true]);
        } else {
            echo json_encode(['success' => false, 'error' => 'Failed to permanently delete lead']);
        }
        exit;
    }
    
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid action']);
}
