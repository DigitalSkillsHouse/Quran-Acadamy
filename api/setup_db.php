<?php
require_once __DIR__ . '/db.php';

$pdo->exec("
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL,
    name TEXT NULL,
    email TEXT NULL,
    phone TEXT NULL,
    course TEXT NULL,
    message TEXT NULL,
    source_url TEXT NULL,
    referrer TEXT NULL,
    ip_address TEXT NULL,
    user_agent TEXT NULL,
    created_at TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'new',
    notes TEXT NULL
);
CREATE INDEX IF NOT EXISTS idx_leads_created ON leads(created_at);
CREATE INDEX IF NOT EXISTS idx_leads_event ON leads(event_type);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL,
    last_login TEXT NULL
);
");

// Check if a user already exists
$stmt = $pdo->query("SELECT id FROM users LIMIT 1");
if ($stmt->fetch()) {
    die("Database already initialized and administrator exists. For security, please delete this setup_db.php file immediately.");
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
        $stmt = $pdo->prepare("INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)");
        $stmt->execute([$username, $hash, date('Y-m-d H:i:s')]);
        $success = true;
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
        .warning { background: #fff3cd; color: #856404; padding: 10px; border-radius: 4px; font-size: 14px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Administrator Setup</h2>
        <?php if ($success): ?>
            <div class="success">Administrator created successfully!</div>
            <div class="warning">CRITICAL SECURITY ACTION REQUIRED:<br>You MUST delete this <code>setup_db.php</code> file from your server immediately.</div>
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
