<?php
require_once __DIR__ . '/storage.php';

if (hasUsers()) {
    die("Database already initialized and administrator exists. For security, setup is disabled.");
}

$error = '';
$success = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';
    $confirm = $_POST['confirm'] ?? '';
    
    if (empty($username) || empty($password)) {
        $error = "All fields are required.";
    } elseif (strlen($password) < 12) {
        $error = "Password must be at least 12 characters long.";
    } elseif ($password !== $confirm) {
        $error = "Passwords do not match.";
    } else {
        $hash = password_hash($password, PASSWORD_DEFAULT);
        if (createUser($username, $hash)) {
            $success = true;
        } else {
            $error = "Failed to create user. Administrator might already exist.";
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>System Setup - Quran Academy</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .box { background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 100%; max-width: 400px; }
        h2 { margin-top: 0; color: #0A3A2A; text-align: center; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; color: #333; }
        input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #D4AF37; color: #fff; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; }
        button:hover { background: #b8972f; }
        .error { color: red; margin-bottom: 15px; font-size: 14px; }
        .success { color: green; font-size: 16px; font-weight: bold; text-align: center; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Administrator Setup</h2>
        <?php if ($success): ?>
            <div class="success">Administrator created successfully! Setup is now complete.</div>
            <br>
            <a href="/admin/login.php"><button>Go to Login</button></a>
        <?php else: ?>
            <?php if ($error): ?><div class="error"><?= htmlspecialchars($error) ?></div><?php endif; ?>
            <form method="POST">
                <div class="form-group">
                    <label>Admin Username</label>
                    <input type="text" name="username" required>
                </div>
                <div class="form-group">
                    <label>Password (Min 12 chars)</label>
                    <input type="password" name="password" minlength="12" required>
                </div>
                <div class="form-group">
                    <label>Confirm Password</label>
                    <input type="password" name="confirm" minlength="12" required>
                </div>
                <button type="submit">Create Administrator</button>
            </form>
        <?php endif; ?>
    </div>
</body>
</html>
