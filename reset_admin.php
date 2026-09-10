<?php
require_once __DIR__ . '/api/storage.php';

echo "<h2>Admin Password Reset</h2>";

// Ensure storage is initialized
initStorage();

$usersFile = __DIR__ . '/api/data/users.json';
$password = 'QuranAdmin!2026#Safe';
$hash = password_hash($password, PASSWORD_DEFAULT);

$foundUser = false;

if (file_exists($usersFile)) {
    $content = file_get_contents($usersFile);
    $users = json_decode($content, true);
    
    if (is_array($users) && !empty($users)) {
        // Find the first user to update
        $user = $users[0];
        $username = $user['username'];
        $foundUser = true;
        
        // Use the existing storage function to safely update just the password
        if (updateUserPassword($user['id'], $hash)) {
            echo "<p style='color:green;'>Successfully updated password for existing admin: <strong>" . htmlspecialchars($username) . "</strong></p>";
        } else {
            echo "<p style='color:red;'>Failed to update password for existing admin: " . htmlspecialchars($username) . "</p>";
        }
    }
}

if (!$foundUser) {
    echo "<p>No existing users found in storage. Creating new admin account...</p>";
    if (createUser('admin', $hash)) {
        echo "<p style='color:green;'>Successfully created new admin account: <strong>admin</strong></p>";
    } else {
        echo "<p style='color:red;'>Failed to create new admin account.</p>";
    }
}

echo "<hr>";
echo "<p><strong>IMPORTANT:</strong> Delete this script immediately after verifying login!</p>";
echo "<a href='/admin/login.php'>Go to Login Page</a>";
?>
