<?php
define('STORAGE_DIR', __DIR__ . '/data');
define('USERS_FILE', STORAGE_DIR . '/users.json');

// Ensure directory exists with writable permissions
if (!is_dir(STORAGE_DIR)) {
    @mkdir(STORAGE_DIR, 0755, true);
}

// Fixed Administrator Credentials
$username = 'admin';
$password = 'QatarAdmin2026!';

$hash = password_hash($password, PASSWORD_DEFAULT);

$users = [
    [
        'id' => bin2hex(random_bytes(16)),
        'username' => $username,
        'password_hash' => $hash,
        'created_at' => date('Y-m-d H:i:s'),
        'last_login' => null
    ]
];

$success = file_put_contents(USERS_FILE, json_encode($users, JSON_PRETTY_PRINT));
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Admin Credentials Reset - Quran Academy</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0A3A2A; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; box-sizing: border-box; }
        .card { background: #fff; padding: 36px; border-radius: 12px; max-width: 480px; width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
        h2 { color: #0A3A2A; margin-top: 0; font-size: 24px; text-align: center; }
        .cred-box { background: #FAF9F6; border: 2px solid #D4AF37; padding: 20px; border-radius: 8px; margin: 24px 0; }
        .cred-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-size: 15px; }
        .cred-row:last-child { margin-bottom: 0; }
        .badge { background: #0A3A2A; color: #D4AF37; padding: 6px 12px; border-radius: 6px; font-family: monospace; font-size: 16px; font-weight: bold; letter-spacing: 0.5px; }
        .btn { display: block; text-align: center; background: #D4AF37; color: #111827; padding: 14px; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 16px; margin-top: 24px; transition: background 0.2s; }
        .btn:hover { background: #e5c354; }
        .note { color: #856404; background-color: #fff3cd; border: 1px solid #ffeeba; padding: 12px 14px; border-radius: 6px; font-size: 13px; margin-top: 20px; line-height: 1.5; }
        .status-ok { color: #0f5132; background-color: #d1e7dd; border: 1px solid #badbcc; padding: 12px; border-radius: 6px; text-align: center; font-weight: 600; font-size: 15px; }
        .status-err { color: #842029; background-color: #f8d7da; border: 1px solid #f5c2c7; padding: 12px; border-radius: 6px; text-align: center; font-weight: 600; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Admin Panel Reset</h2>
        
        <?php if ($success !== false): ?>
            <div class="status-ok">✓ Administrator Reset Successfully!</div>
            
            <div class="cred-box">
                <div class="cred-row">
                    <strong>Admin ID / User:</strong>
                    <span class="badge"><?= htmlspecialchars($username) ?></span>
                </div>
                <div class="cred-row">
                    <strong>Password:</strong>
                    <span class="badge"><?= htmlspecialchars($password) ?></span>
                </div>
            </div>

            <a class="btn" href="/admin/login.php">Go to Admin Login &rarr;</a>

            <div class="note">
                <strong>Security Reminder:</strong> Now that your credentials are reset, delete <code>api/reset_admin.php</code> from your server via cPanel or FTP so nobody else can reset it.
            </div>
        <?php else: ?>
            <div class="status-err">✕ Could not write to <code>api/data/users.json</code>. Please check folder permissions in cPanel (set <code>api/data/</code> to 755).</div>
        <?php endif; ?>
    </div>
</body>
</html>
