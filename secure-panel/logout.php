<?php
require_once __DIR__ . '/../api/auth.php';
session_destroy();
header('Location: /secure-panel/login.php');
