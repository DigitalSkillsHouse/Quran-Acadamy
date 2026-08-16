<?php
session_start();

// Generate CSRF token if not exists
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

function isLoggedIn() {
    return isset($_SESSION['admin_logged_in']) && $_SESSION['admin_logged_in'] === true;
}

function requireAuth() {
    if (!isLoggedIn()) {
        header('Location: /admin/login.php');
        exit;
    }
}

function verifyCsrfToken($token) {
    return hash_equals($_SESSION['csrf_token'], $token);
}
