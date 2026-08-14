<?php
require_once __DIR__ . '/../api/auth.php';
requireAuth();

$type_filter = $_GET['type'] ?? 'all';
$status_filter = $_GET['status'] ?? 'all';

$query = "SELECT * FROM leads WHERE 1=1";
$params = [];

if ($type_filter !== 'all') {
    $query .= " AND event_type = ?";
    $params[] = $type_filter;
}
if ($status_filter !== 'all') {
    $query .= " AND status = ?";
    $params[] = $status_filter;
}

$query .= " ORDER BY created_at DESC LIMIT 500";
$stmt = $pdo->prepare($query);
$stmt->execute($params);
$leads = $stmt->fetchAll();

// Stats
$stats = [
    'TOTAL' => $pdo->query("SELECT COUNT(*) FROM leads")->fetchColumn(),
    'FORMS' => $pdo->query("SELECT COUNT(*) FROM leads WHERE event_type = 'FORM_SUBMISSION'")->fetchColumn(),
    'PHONE' => $pdo->query("SELECT COUNT(*) FROM leads WHERE event_type = 'PHONE_CLICK'")->fetchColumn(),
    'WHATSAPP' => $pdo->query("SELECT COUNT(*) FROM leads WHERE event_type = 'WHATSAPP_CLICK'")->fetchColumn(),
    'NEW' => $pdo->query("SELECT COUNT(*) FROM leads WHERE status = 'new'")->fetchColumn(),
];
?>
<!DOCTYPE html>
<html>
<head>

    <meta name="csrf-token" content="<?= htmlspecialchars($_SESSION['csrf_token']) ?>">
    <title>Dashboard - Quran Academy</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; background: #f4f4f9; margin: 0; padding: 20px; color: #333; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .stats { display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }
        .stat-card { background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); flex: 1; min-width: 120px; text-align: center; border-top: 3px solid #0A3A2A; }
        .stat-card.gold { border-top-color: #D4AF37; }
        .stat-card h3 { margin: 0 0 10px 0; font-size: 14px; color: #666; text-transform: uppercase; }
        .stat-card .val { font-size: 24px; font-weight: bold; color: #0A3A2A; }
        
        .filters { margin-bottom: 20px; display: flex; gap: 10px; }
        select, button { padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
        .btn-logout { background: #d9534f; color: white; border: none; text-decoration: none; padding: 8px 15px; border-radius: 4px; }
        
        table { width: 100%; border-collapse: collapse; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; font-size: 14px; }
        th { background: #0A3A2A; color: white; }
        .type-badge { padding: 4px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; background: #eee; }
        .type-FORM_SUBMISSION { background: #d4edda; color: #155724; }
        .type-PHONE_CLICK { background: #cce5ff; color: #004085; }
        .type-WHATSAPP_CLICK { background: #fff3cd; color: #856404; }
        
        .notes-area { width: 100%; height: 60px; box-sizing: border-box; resize: vertical; }
        
        @media(max-width: 768px) {
            table, thead, tbody, th, td, tr { display: block; }
            th { display: none; }
            tr { border: 1px solid #ccc; margin-bottom: 10px; border-radius: 4px; }
            td { position: relative; padding-left: 120px; border-bottom: none; border-top: 1px solid #eee; }
            td::before { content: attr(data-label); position: absolute; left: 10px; width: 100px; font-weight: bold; }
        }
    </style>
</head>
<body>
    <div class="header">
        <h2>Admin Dashboard</h2>
        <a href="logout.php" class="btn-logout">Logout</a>
    </div>
    
    <div class="stats">
        <div class="stat-card"><h3>Total Leads</h3><div class="val"><?= $stats['TOTAL'] ?></div></div>
        <div class="stat-card"><h3>New</h3><div class="val"><?= $stats['NEW'] ?></div></div>
        <div class="stat-card gold"><h3>Forms</h3><div class="val"><?= $stats['FORMS'] ?></div></div>
        <div class="stat-card gold"><h3>Phone</h3><div class="val"><?= $stats['PHONE'] ?></div></div>
        <div class="stat-card gold"><h3>WhatsApp</h3><div class="val"><?= $stats['WHATSAPP'] ?></div></div>
    </div>
    
    <div class="filters">
        <form method="GET">
            <select name="type">
                <option value="all" <?= $type_filter==='all'?'selected':'' ?>>All Types</option>
                <option value="FORM_SUBMISSION" <?= $type_filter==='FORM_SUBMISSION'?'selected':'' ?>>Forms</option>
                <option value="PHONE_CLICK" <?= $type_filter==='PHONE_CLICK'?'selected':'' ?>>Phone</option>
                <option value="WHATSAPP_CLICK" <?= $type_filter==='WHATSAPP_CLICK'?'selected':'' ?>>WhatsApp</option>
            </select>
            <select name="status">
                <option value="all" <?= $status_filter==='all'?'selected':'' ?>>All Status</option>
                <option value="new" <?= $status_filter==='new'?'selected':'' ?>>New</option>
                <option value="contacted" <?= $status_filter==='contacted'?'selected':'' ?>>Contacted</option>
                <option value="qualified" <?= $status_filter==='qualified'?'selected':'' ?>>Qualified</option>
                <option value="converted" <?= $status_filter==='converted'?'selected':'' ?>>Converted</option>
                <option value="closed" <?= $status_filter==='closed'?'selected':'' ?>>Closed</option>
            </select>
            <button type="submit">Filter</button>
        </form>
    </div>
    

    <div style="background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
        <h3>Change Password</h3>
        <div style="display:flex; gap:10px;">
            <input type="password" id="cp_current" placeholder="Current Password">
            <input type="password" id="cp_new" placeholder="New Password (min 12)">
            <input type="password" id="cp_confirm" placeholder="Confirm Password">
            <button onclick="changePassword()">Update Password</button>
        </div>
        <div id="cp_msg" style="margin-top: 10px; font-size: 14px;"></div>
    </div>
    
    <table>

        <thead>
            <tr>
                <th>Date</th>
                <th>Type</th>
                <th>Contact</th>
                <th>Details</th>
                <th>Source</th>
                <th>Status</th>
                <th>Notes</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($leads as $l): ?>
            <tr>
                <td data-label="Date"><?= htmlspecialchars($l['created_at']) ?></td>
                <td data-label="Type"><span class="type-badge type-<?= $l['event_type'] ?>"><?= str_replace('_', ' ', $l['event_type']) ?></span></td>
                <td data-label="Contact">
                    <strong><?= htmlspecialchars($l['name'] ?? '-') ?></strong><br>
                    <?= htmlspecialchars($l['phone'] ?? '-') ?><br>
                    <?= htmlspecialchars($l['email'] ?? '') ?>
                </td>
                <td data-label="Details">
                    <?= htmlspecialchars($l['course'] ?? '-') ?><br>
                    <small><?= htmlspecialchars(substr($l['message'] ?? '', 0, 50)) ?></small>
                </td>
                <td data-label="Source"><a href="<?= htmlspecialchars($l['source_url']) ?>" target="_blank">Link</a></td>
                <td data-label="Status">
                    <select onchange="updateStatus(<?= $l['id'] ?>, this.value)">
                        <option value="new" <?= $l['status']==='new'?'selected':'' ?>>New</option>
                        <option value="contacted" <?= $l['status']==='contacted'?'selected':'' ?>>Contacted</option>
                        <option value="qualified" <?= $l['status']==='qualified'?'selected':'' ?>>Qualified</option>
                        <option value="converted" <?= $l['status']==='converted'?'selected':'' ?>>Converted</option>
                        <option value="closed" <?= $l['status']==='closed'?'selected':'' ?>>Closed</option>
                    </select>
                </td>
                <td data-label="Notes">
                    <textarea class="notes-area" onblur="updateNotes(<?= $l['id'] ?>, this.value)"><?= htmlspecialchars($l['notes'] ?? '') ?></textarea>
                </td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

    
    <script>
    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    
    function updateStatus(id, status) {
        fetch('api.php', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({action: 'update_status', id: id, status: status, csrf_token: csrfToken})
        });
    }
    function updateNotes(id, notes) {
        fetch('api.php', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({action: 'update_notes', id: id, notes: notes, csrf_token: csrfToken})
        });
    }
    async function changePassword() {
        const cur = document.getElementById('cp_current').value;
        const newP = document.getElementById('cp_new').value;
        const conf = document.getElementById('cp_confirm').value;
        const msg = document.getElementById('cp_msg');
        
        msg.textContent = 'Updating...';
        msg.style.color = 'black';
        
        try {
            const res = await fetch('api.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    action: 'change_password', 
                    current_password: cur, 
                    new_password: newP, 
                    confirm_password: conf,
                    csrf_token: csrfToken
                })
            });
            const data = await res.json();
            if (data.success) {
                msg.textContent = 'Password updated successfully!';
                msg.style.color = 'green';
                document.getElementById('cp_current').value = '';
                document.getElementById('cp_new').value = '';
                document.getElementById('cp_confirm').value = '';
            } else {
                msg.textContent = data.error || 'Failed to update';
                msg.style.color = 'red';
            }
        } catch (e) {
            msg.textContent = 'Connection error';
            msg.style.color = 'red';
        }
    }
    </script>

</body>
</html>
