<?php
require_once __DIR__ . '/../api/auth.php';
session_destroy();
header('Location: /admin/login.php');
