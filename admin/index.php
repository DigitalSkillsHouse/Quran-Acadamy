<?php
require_once __DIR__ . '/../api/auth.php';
require_once __DIR__ . '/../api/storage.php';
requireAuth();

$view = $_GET['view'] ?? 'active';
$type_filter = $_GET['type'] ?? 'all';
$status_filter = $_GET['status'] ?? 'all';
$search = trim(strtolower($_GET['search'] ?? ''));

$all_leads = getLeads();

$active_leads = [];
$deleted_leads = [];

$stats = [
    'TOTAL' => 0,
    'FORMS' => 0,
    'PHONE' => 0,
    'WHATSAPP' => 0,
    'NEW' => 0,
];

foreach ($all_leads as $l) {
    if (!empty($l['deleted_at'])) {
        $deleted_leads[] = $l;
        continue;
    }

    $stats['TOTAL']++;
    if (($l['event_type'] ?? '') === 'FORM_SUBMISSION') $stats['FORMS']++;
    if (($l['event_type'] ?? '') === 'PHONE_CLICK') $stats['PHONE']++;
    if (($l['event_type'] ?? '') === 'WHATSAPP_CLICK') $stats['WHATSAPP']++;
    if (($l['status'] ?? '') === 'new') $stats['NEW']++;

    $active_leads[] = $l;
}

$target_leads = ($view === 'recycle_bin') ? $deleted_leads : $active_leads;

$leads = [];
foreach ($target_leads as $l) {
    if ($type_filter !== 'all' && ($l['event_type'] ?? '') !== $type_filter) continue;
    if ($status_filter !== 'all' && ($l['status'] ?? '') !== $status_filter) continue;

    if ($search !== '') {
        $searchable = strtolower(($l['name']??'') . ' ' . ($l['email']??'') . ' ' . ($l['phone']??'') . ' ' . ($l['course']??''));
        if (strpos($searchable, $search) === false) continue;
    }

    $leads[] = $l;
}

$leads = array_slice($leads, 0, 500);

function formatBadge($type) {
    if ($type === 'FORM_SUBMISSION') return '<span class="badge badge-form">Form Submission</span>';
    if ($type === 'PHONE_CLICK') return '<span class="badge badge-phone">Phone Click</span>';
    if ($type === 'WHATSAPP_CLICK') return '<span class="badge badge-whatsapp">WhatsApp Click</span>';
    return '<span class="badge badge-default">'.htmlspecialchars($type).'</span>';
}

function formatStatus($status) {
    $s = strtolower($status);
    $cls = 'status-default';
    if ($s === 'new') $cls = 'status-new';
    else if ($s === 'contacted') $cls = 'status-contacted';
    else if ($s === 'qualified') $cls = 'status-qualified';
    else if ($s === 'converted') $cls = 'status-converted';
    else if ($s === 'closed') $cls = 'status-closed';
    return '<span class="status-badge '.$cls.'">'.ucfirst(htmlspecialchars($status)).'</span>';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="csrf-token" content="<?= htmlspecialchars($_SESSION['csrf_token']) ?>">
    <title>Lead Dashboard - Quran Academy</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --emerald: #0A3A2A;
            --emerald-light: #125740;
            --gold: #D4AF37;
            --navy: #1e293b;
            --gray-light: #f4f7f6;
            --gray-border: #e2e8f0;
            --white: #ffffff;
            --text-main: #334155;
            --text-muted: #64748b;
        }

        * { box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--gray-light);
            color: var(--text-main);
            margin: 0;
            padding: 0;
            line-height: 1.5;
        }

        .container { max-width: 1400px; margin: 0 auto; padding: 24px; }

        /* Header */
        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--white);
            padding: 20px 24px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            margin-bottom: 24px;
        }
        .header-title h1 { margin: 0; font-size: 24px; color: var(--navy); font-weight: 700; }
        .header-title p { margin: 4px 0 0; color: var(--text-muted); font-size: 14px; }
        .header-actions { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
        .tracking-status {
            display: flex; align-items: center; gap: 8px;
            font-size: 13px; font-weight: 600; color: #10b981;
            background: #ecfdf5; padding: 6px 12px; border-radius: 20px;
        }
        .tracking-status::before {
            content: ""; display: block; width: 8px; height: 8px;
            background: #10b981; border-radius: 50%; box-shadow: 0 0 0 3px #d1fae5;
        }

        /* Buttons */
        .btn {
            display: inline-flex; align-items: center; justify-content: center;
            padding: 8px 16px; font-size: 14px; font-weight: 500;
            border-radius: 8px; cursor: pointer; border: 1px solid transparent;
            transition: all 0.2s; text-decoration: none;
        }
        .btn-sm { padding: 6px 12px; font-size: 13px; }
        .btn-primary { background: var(--emerald); color: var(--white); }
        .btn-primary:hover { background: var(--emerald-light); }
        .btn-secondary { background: #f1f5f9; color: var(--navy); border-color: #cbd5e1; }
        .btn-secondary:hover { background: #e2e8f0; }
        .btn-danger { background: #fee2e2; color: #b91c1c; border-color: #fecaca; }
        .btn-danger:hover { background: #fecaca; }
        .btn-danger-solid { background: #ef4444; color: white; }
        .btn-danger-solid:hover { background: #dc2626; }
        .btn-warning { background: #fef3c7; color: #b45309; border-color: #fde68a; }
        .btn-warning:hover { background: #fde68a; }
        .btn-success { background: #dcfce7; color: #15803d; border-color: #bbf7d0; }
        .btn-success:hover { background: #bbf7d0; }

        /* Stats */
        .stats-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px; margin-bottom: 24px;
        }
        .stat-card {
            background: var(--white); padding: 20px; border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            border-top: 4px solid var(--emerald); transition: transform 0.2s;
        }
        .stat-card:hover { transform: translateY(-2px); }
        .stat-card.gold { border-top-color: var(--gold); }
        .stat-card-title { font-size: 12px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; margin: 0 0 8px; }
        .stat-card-val { font-size: 32px; font-weight: 700; color: var(--navy); margin: 0 0 4px; }
        .stat-card-desc { font-size: 13px; color: var(--text-muted); margin: 0; }

        /* Toolbar */
        .toolbar {
            display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;
            background: var(--white); padding: 16px 20px; border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 24px; gap: 16px;
        }
        .filters { display: flex; gap: 12px; flex-wrap: wrap; flex: 1; }
        .filters select, .filters input {
            padding: 8px 12px; border: 1px solid var(--gray-border); border-radius: 8px;
            font-size: 14px; font-family: inherit; color: var(--navy); outline: none;
        }
        .filters select:focus, .filters input:focus { border-color: var(--emerald); box-shadow: 0 0 0 2px rgba(10,58,42,0.1); }

        .view-toggle { display: flex; gap: 8px; }
        .view-toggle .btn { border-radius: 8px; }
        .view-toggle .active { background: var(--navy); color: white; border-color: var(--navy); }

        /* Table */
        .table-container {
            background: var(--white); border-radius: 12px; overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 40px;
            overflow-x: auto;
        }
        table { width: 100%; border-collapse: collapse; text-align: left; }
        th { background: #f8fafc; color: var(--text-muted); font-weight: 600; font-size: 13px; padding: 16px; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid var(--gray-border); }
        td { padding: 16px; border-bottom: 1px solid var(--gray-border); font-size: 14px; vertical-align: top; }
        tr:last-child td { border-bottom: none; }
        tr:hover { background: #f8fafc; }

        /* Badges */
        .badge { display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-form { background: #dcfce7; color: #166534; }
        .badge-phone { background: #dbeafe; color: #1e40af; }
        .badge-whatsapp { background: #fef3c7; color: #92400e; }
        .badge-default { background: #f1f5f9; color: #475569; }

        .status-badge { display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; border: 1px solid transparent; }
        .status-new { background: #ecfdf5; color: #059669; border-color: #a7f3d0; }
        .status-contacted { background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }
        .status-qualified { background: #fdf4ff; color: #c026d3; border-color: #f5d0fe; }
        .status-converted { background: #fefce8; color: #ca8a04; border-color: #fef08a; }
        .status-closed { background: #f1f5f9; color: #475569; border-color: #cbd5e1; }

        select.status-select {
            padding: 6px; border: 1px solid var(--gray-border); border-radius: 6px;
            font-size: 13px; font-weight: 500; font-family: inherit; width: 100%; max-width: 120px; outline: none;
        }

        /* Notes */
        .notes-wrapper { display: flex; flex-direction: column; gap: 6px; }
        .notes-area {
            width: 100%; min-width: 180px; min-height: 60px; padding: 8px;
            border: 1px solid var(--gray-border); border-radius: 6px; font-size: 13px;
            font-family: inherit; resize: vertical; outline: none;
        }
        .notes-area:focus { border-color: var(--emerald); }
        .notes-actions { display: flex; gap: 6px; }

        /* Action Buttons Grid */
        .actions-col { display: flex; gap: 6px; flex-wrap: wrap; }

        /* Modals */
        .modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px);
            display: none; align-items: center; justify-content: center; z-index: 1000;
        }
        .modal-overlay.active { display: flex; }
        .modal {
            background: var(--white); border-radius: 16px; width: 100%; max-width: 500px;
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); overflow: hidden;
            transform: translateY(20px); opacity: 0; transition: all 0.3s;
        }
        .modal-overlay.active .modal { transform: translateY(0); opacity: 1; }
        .modal-header { padding: 20px 24px; border-bottom: 1px solid var(--gray-border); display: flex; justify-content: space-between; align-items: center; }
        .modal-header h3 { margin: 0; font-size: 18px; color: var(--navy); }
        .modal-close { background: none; border: none; font-size: 24px; cursor: pointer; color: var(--text-muted); }
        .modal-body { padding: 24px; max-height: 70vh; overflow-y: auto; }
        .modal-footer { padding: 16px 24px; border-top: 1px solid var(--gray-border); display: flex; justify-content: flex-end; gap: 12px; background: #f8fafc; }

        .detail-row { display: flex; border-bottom: 1px solid #f1f5f9; padding: 12px 0; }
        .detail-row:last-child { border-bottom: none; }
        .detail-label { width: 35%; font-weight: 600; color: var(--text-muted); font-size: 13px; }
        .detail-value { width: 65%; color: var(--navy); font-size: 14px; word-break: break-word; }

        /* Toasts */
        .toast-container { position: fixed; bottom: 24px; right: 24px; display: flex; flex-direction: column; gap: 10px; z-index: 2000; }
        .toast {
            background: var(--navy); color: white; padding: 12px 20px; border-radius: 8px;
            font-size: 14px; font-weight: 500; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
            transform: translateX(120%); transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex; align-items: center; gap: 10px;
        }
        .toast.show { transform: translateX(0); }
        .toast.success { border-left: 4px solid #10b981; }
        .toast.error { border-left: 4px solid #ef4444; }

        /* Empty State */
        .empty-state { text-align: center; padding: 60px 20px; }
        .empty-state h3 { color: var(--navy); margin-bottom: 8px; }
        .empty-state p { color: var(--text-muted); margin: 0; }

        /* Mobile Cards */
        @media(max-width: 992px) {
            table, thead, tbody, th, td, tr { display: block; }
            th { display: none; }
            .table-container { background: transparent; box-shadow: none; overflow-x: visible; }
            tr { background: var(--white); margin-bottom: 16px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); padding: 16px; border: 1px solid var(--gray-border); }
            tr:hover { background: var(--white); }
            td { padding: 8px 0; border-bottom: 1px solid #f1f5f9; display: flex; flex-direction: column; gap: 4px; }
            td:last-child { border-bottom: none; }
            td::before { content: attr(data-label); font-size: 12px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; }

            .actions-col { flex-direction: row; }
        }

    </style>
</head>
<body>

<div class="container">

    <!-- Header -->
    <header class="dashboard-header">
        <div class="header-title">
            <h1>Lead Dashboard</h1>
            <p>Manage and track enquiries, calls and WhatsApp leads</p>
        </div>
        <div class="header-actions">
            <div class="tracking-status">Tracking Active</div>
            <a href="logout.php" class="btn btn-secondary">Logout</a>
        </div>
    </header>

    <!-- Stats -->
    <div class="stats-grid">
        <div class="stat-card">
            <h3 class="stat-card-title">Total Leads</h3>
            <div class="stat-card-val"><?= $stats['TOTAL'] ?></div>
            <p class="stat-card-desc">All captured leads</p>
        </div>
        <div class="stat-card">
            <h3 class="stat-card-title">New</h3>
            <div class="stat-card-val"><?= $stats['NEW'] ?></div>
            <p class="stat-card-desc">Requires attention</p>
        </div>
        <div class="stat-card gold">
            <h3 class="stat-card-title">Forms</h3>
            <div class="stat-card-val"><?= $stats['FORMS'] ?></div>
            <p class="stat-card-desc">Website enquiries</p>
        </div>
        <div class="stat-card gold">
            <h3 class="stat-card-title">Phone</h3>
            <div class="stat-card-val"><?= $stats['PHONE'] ?></div>
            <p class="stat-card-desc">Phone interactions</p>
        </div>
        <div class="stat-card gold">
            <h3 class="stat-card-title">WhatsApp</h3>
            <div class="stat-card-val"><?= $stats['WHATSAPP'] ?></div>
            <p class="stat-card-desc">WhatsApp interactions</p>
        </div>
    </div>

    <!-- Toolbar -->
    <div class="toolbar">
        <form class="filters" method="GET">
            <input type="hidden" name="view" value="<?= htmlspecialchars($view) ?>">
            <input type="text" name="search" placeholder="Search leads..." value="<?= htmlspecialchars($search) ?>" style="flex:1; min-width:200px;">
            <select name="type">
                <option value="all" <?= $type_filter==='all'?'selected':'' ?>>All Types</option>
                <option value="FORM_SUBMISSION" <?= $type_filter==='FORM_SUBMISSION'?'selected':'' ?>>Form Submission</option>
                <option value="PHONE_CLICK" <?= $type_filter==='PHONE_CLICK'?'selected':'' ?>>Phone Click</option>
                <option value="WHATSAPP_CLICK" <?= $type_filter==='WHATSAPP_CLICK'?'selected':'' ?>>WhatsApp Click</option>
            </select>
            <select name="status">
                <option value="all" <?= $status_filter==='all'?'selected':'' ?>>All Statuses</option>
                <option value="new" <?= $status_filter==='new'?'selected':'' ?>>New</option>
                <option value="contacted" <?= $status_filter==='contacted'?'selected':'' ?>>Contacted</option>
                <option value="qualified" <?= $status_filter==='qualified'?'selected':'' ?>>Qualified</option>
                <option value="converted" <?= $status_filter==='converted'?'selected':'' ?>>Converted</option>
                <option value="closed" <?= $status_filter==='closed'?'selected':'' ?>>Closed</option>
            </select>
            <button type="submit" class="btn btn-secondary">Filter</button>
            <?php if($search!=='' || $type_filter!=='all' || $status_filter!=='all'): ?>
            <a href="?view=<?= htmlspecialchars($view) ?>" class="btn btn-secondary">Clear</a>
            <?php endif; ?>
        </form>
        <div class="view-toggle">
            <a href="?view=active" class="btn btn-secondary <?= $view==='active'?'active':'' ?>">Active Leads</a>
            <a href="?view=recycle_bin" class="btn btn-secondary <?= $view==='recycle_bin'?'active':'' ?>">Recycle Bin</a>
        </div>
    </div>

    <!-- Table -->
    <div class="table-container">
        <?php if(empty($leads)): ?>
            <div class="empty-state">
                <?php if($view==='active'): ?>
                    <h3>No leads found</h3>
                    <p>Form submissions, phone clicks and WhatsApp interactions will appear here.</p>
                <?php else: ?>
                    <h3>Recycle Bin is empty</h3>
                    <p>No deleted leads are currently waiting here.</p>
                <?php endif; ?>
            </div>
        <?php else: ?>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Type</th>
                        <th>Location</th>
                        <th>Contact Info</th>
                        <th>Details</th>
                        <?php if($view==='recycle_bin'): ?>
                            <th>Deleted At</th>
                        <?php else: ?>
                            <th>Status & Notes</th>
                        <?php endif; ?>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach($leads as $l): ?>
                    <tr id="row-<?= htmlspecialchars($l['id']) ?>">
                        <td data-label="Date">
                            <strong><?= htmlspecialchars(date('M j, Y', strtotime($l['created_at'] ?? 'now'))) ?></strong><br>
                            <span style="color:var(--text-muted); font-size:12px;"><?= htmlspecialchars(date('g:i A', strtotime($l['created_at'] ?? 'now'))) ?></span>
                        </td>
                        <td data-label="Type">
                            <?= formatBadge($l['event_type'] ?? '') ?>
                        </td>
                        <td data-label="Location">
                            <?php
                            if (isset($l['geo']) && is_array($l['geo']) && ($l['geo']['country'] ?? 'Unknown') !== 'Unknown') {
                                $geo = $l['geo'];
                                echo '<strong style="color:var(--navy); font-size:14px;">' . htmlspecialchars($geo['city'] ?? 'Unknown') . ', ' . htmlspecialchars($geo['country'] ?? 'Unknown') . '</strong><br>';
                                echo '<span style="color:var(--text-muted); font-size:13px;">' . htmlspecialchars($geo['region'] ?? 'Unknown') . '</span><br>';
                                $zip = ($geo['postal_code'] ?? 'Unknown');
                                echo '<span style="color:var(--text-muted); font-size:12px;">ZIP: ' . htmlspecialchars($zip) . '</span>';
                            } else {
                                echo '<span style="color:var(--text-muted); font-style:italic; font-size:13px;">Location unavailable</span>';
                            }
                            ?>
                        </td>
                        <td data-label="Contact Info">
                            <strong style="color:var(--navy); font-size:15px;"><?= htmlspecialchars($l['name'] ?? '-') ?></strong><br>
                            <?= htmlspecialchars($l['phone'] ?? '-') ?><br>
                            <span style="color:var(--text-muted);"><?= htmlspecialchars($l['email'] ?? '') ?></span>
                        </td>
                        <td data-label="Details">
                            <span style="font-weight:500;"><?= htmlspecialchars($l['course'] ?? '-') ?></span><br>
                            <span style="color:var(--text-muted); font-size:13px; display:block; max-width: 250px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="<?= htmlspecialchars($l['message'] ?? '') ?>">
                                <?= htmlspecialchars($l['message'] ?? '-') ?>
                            </span>
                        </td>

                        <?php if($view === 'recycle_bin'): ?>
                            <td data-label="Deleted At">
                                <span style="color:#ef4444; font-weight:500;"><?= htmlspecialchars($l['deleted_at'] ?? '') ?></span>
                            </td>
                        <?php else: ?>
                            <td data-label="Status & Notes" style="min-width: 200px;">
                                <div style="margin-bottom: 8px;">
                                    <select class="status-select" onchange="updateStatus('<?= htmlspecialchars($l['id']) ?>', this.value)">
                                        <option value="new" <?= ($l['status']??'')==='new'?'selected':'' ?>>New</option>
                                        <option value="contacted" <?= ($l['status']??'')==='contacted'?'selected':'' ?>>Contacted</option>
                                        <option value="qualified" <?= ($l['status']??'')==='qualified'?'selected':'' ?>>Qualified</option>
                                        <option value="converted" <?= ($l['status']??'')==='converted'?'selected':'' ?>>Converted</option>
                                        <option value="closed" <?= ($l['status']??'')==='closed'?'selected':'' ?>>Closed</option>
                                    </select>
                                </div>
                                <div class="notes-wrapper">
                                    <textarea class="notes-area" id="note-<?= htmlspecialchars($l['id']) ?>" placeholder="Add a note..."><?= htmlspecialchars($l['notes'] ?? '') ?></textarea>
                                    <div class="notes-actions">
                                        <button class="btn btn-sm btn-primary" onclick="saveNote('<?= htmlspecialchars($l['id']) ?>')">Save</button>
                                        <?php if(!empty($l['notes'])): ?>
                                        <button class="btn btn-sm btn-secondary" onclick="confirmClearNote('<?= htmlspecialchars($l['id']) ?>')">Clear</button>
                                        <?php endif; ?>
                                    </div>
                                </div>
                            </td>
                        <?php endif; ?>

                        <td data-label="Actions">
                            <div class="actions-col">
                                <button class="btn btn-sm btn-secondary" onclick="viewLead(<?= htmlspecialchars(json_encode($l)) ?>)">View</button>

                                <?php if($view === 'active'): ?>
                                    <button class="btn btn-sm btn-danger" onclick="confirmSoftDelete('<?= htmlspecialchars($l['id']) ?>')">Delete</button>
                                <?php else: ?>
                                    <button class="btn btn-sm btn-success" onclick="restoreLead('<?= htmlspecialchars($l['id']) ?>')">Restore</button>
                                    <button class="btn btn-sm btn-danger-solid" onclick="confirmPermanentDelete('<?= htmlspecialchars($l['id']) ?>')">Perm Delete</button>
                                <?php endif; ?>
                            </div>
                        </td>
                    </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php endif; ?>
    </div>

</div>

<!-- Modal: View Lead -->
<div class="modal-overlay" id="viewModal" onclick="closeModal('viewModal')">
    <div class="modal" onclick="event.stopPropagation()">
        <div class="modal-header">
            <h3>Lead Details</h3>
            <button class="modal-close" onclick="closeModal('viewModal')">&times;</button>
        </div>
        <div class="modal-body" id="viewModalBody">
            <!-- Populated via JS -->
        </div>
        <div class="modal-footer">
            <button class="btn btn-secondary" onclick="closeModal('viewModal')">Close</button>
        </div>
    </div>
</div>

<!-- Modal: Confirm Soft Delete -->
<div class="modal-overlay" id="softDeleteModal" onclick="closeModal('softDeleteModal')">
    <div class="modal" onclick="event.stopPropagation()">
        <div class="modal-header">
            <h3>Move to Recycle Bin?</h3>
            <button class="modal-close" onclick="closeModal('softDeleteModal')">&times;</button>
        </div>
        <div class="modal-body">
            <p>This lead will be removed from the active dashboard but can be restored later.</p>
        </div>
        <div class="modal-footer">
            <button class="btn btn-secondary" onclick="closeModal('softDeleteModal')">Cancel</button>
            <button class="btn btn-danger-solid" id="btnConfirmSoftDelete">Move to Recycle Bin</button>
        </div>
    </div>
</div>

<!-- Modal: Confirm Permanent Delete -->
<div class="modal-overlay" id="permDeleteModal">
    <div class="modal">
        <div class="modal-header">
            <h3 style="color:#ef4444;">Permanently Delete Lead?</h3>
            <button class="modal-close" onclick="closeModal('permDeleteModal')">&times;</button>
        </div>
        <div class="modal-body">
            <p><strong>This action cannot be undone.</strong></p>
            <p>The lead record will be permanently removed from storage.</p>
        </div>
        <div class="modal-footer">
            <button class="btn btn-secondary" onclick="closeModal('permDeleteModal')">Cancel</button>
            <button class="btn btn-danger-solid" id="btnConfirmPermDelete">Delete Permanently</button>
        </div>
    </div>
</div>

<!-- Modal: Confirm Clear Note -->
<div class="modal-overlay" id="clearNoteModal" onclick="closeModal('clearNoteModal')">
    <div class="modal" onclick="event.stopPropagation()">
        <div class="modal-header">
            <h3>Delete this note?</h3>
            <button class="modal-close" onclick="closeModal('clearNoteModal')">&times;</button>
        </div>
        <div class="modal-body">
            <p>Are you sure you want to clear the note for this lead?</p>
        </div>
        <div class="modal-footer">
            <button class="btn btn-secondary" onclick="closeModal('clearNoteModal')">Cancel</button>
            <button class="btn btn-danger-solid" id="btnConfirmClearNote">Delete Note</button>
        </div>
    </div>
</div>

<!-- Toasts -->
<div class="toast-container" id="toastContainer"></div>

<script>
    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

    // Toast System
    function showToast(message, type = 'success') {
        const container = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.innerHTML = `<span>${message}</span>`;
        container.appendChild(toast);

        // Trigger reflow to start animation
        toast.offsetHeight;
        toast.classList.add('show');

        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    // Modal System
    function openModal(id) {
        document.getElementById(id).classList.add('active');
    }
    function closeModal(id) {
        document.getElementById(id).classList.remove('active');
    }
    document.addEventListener('keydown', (e) => {
        if(e.key === 'Escape') {
            document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('active'));
        }
    });

    // API Helper
    async function apiCall(action, data) {
        try {
            const res = await fetch('api.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({action, csrf_token: csrfToken, ...data})
            });
            return await res.json();
        } catch (err) {
            return { success: false, error: 'Connection error' };
        }
    }

    // Actions
    async function updateStatus(id, status) {
        const res = await apiCall('update_status', { id, status });
        if(res.success) {
            showToast('Status updated successfully');
        } else {
            showToast(res.error || 'Failed to update status', 'error');
        }
    }

    async function saveNote(id) {
        const note = document.getElementById(`note-${id}`).value;
        const res = await apiCall('update_notes', { id, notes: note });
        if(res.success) {
            showToast('Note saved');
            setTimeout(() => window.location.reload(), 1000); // Reload to show clear button if newly added
        } else {
            showToast(res.error || 'Failed to save note', 'error');
        }
    }

    // Clear Note Flow
    let currentClearNoteId = null;
    function confirmClearNote(id) {
        currentClearNoteId = id;
        openModal('clearNoteModal');
    }
    document.getElementById('btnConfirmClearNote').addEventListener('click', async () => {
        if(!currentClearNoteId) return;
        closeModal('clearNoteModal');
        const res = await apiCall('update_notes', { id: currentClearNoteId, notes: '' });
        if(res.success) {
            showToast('Note deleted');
            document.getElementById(`note-${currentClearNoteId}`).value = '';
            setTimeout(() => window.location.reload(), 1000); // Reload to hide clear button
        } else {
            showToast(res.error || 'Failed to delete note', 'error');
        }
        currentClearNoteId = null;
    });

    // View Lead
    function viewLead(lead) {
        let hasGeo = lead.geo && lead.geo.country !== 'Unknown';

        const fields = [
            { label: 'Date', val: lead.created_at },
            { label: 'Type', val: lead.event_type },
            { label: 'Name', val: lead.name },
            { label: 'Email', val: lead.email },
            { label: 'Phone', val: lead.phone },
            { label: 'Course', val: lead.course },
            { label: 'Message', val: lead.message },
            { label: 'Location', val: hasGeo ? 'Available' : 'Location unavailable' },
            { label: 'Country', val: hasGeo ? lead.geo.country : null },
            { label: 'Region/State', val: hasGeo ? lead.geo.region : null },
            { label: 'City', val: hasGeo ? lead.geo.city : null },
            { label: 'Postal/ZIP', val: hasGeo ? lead.geo.postal_code : null },
            { label: 'Timezone', val: hasGeo ? lead.geo.timezone : null },
            { label: 'Source', val: lead.source_url },
            { label: 'Referrer', val: lead.referrer },
            { label: 'Visitor IP', val: lead.ip_address },
            { label: 'User Agent', val: lead.user_agent },
            { label: 'Status', val: lead.status },
            { label: 'Notes', val: lead.notes }
        ];

        let html = '';
        fields.forEach(f => {
            if (f.val) {
                html += `<div class="detail-row">
                            <div class="detail-label">${f.label}</div>
                            <div class="detail-value">${escapeHtml(f.val)}</div>
                         </div>`;
            }
        });

        document.getElementById('viewModalBody').innerHTML = html;
        openModal('viewModal');
    }

    function escapeHtml(unsafe) {
        if(!unsafe) return '-';
        return (unsafe+'').replace(/[&<"']/g, function(m) {
            switch (m) {
                case '&': return '&amp;';
                case '<': return '&lt;';
                case '"': return '&quot;';
                default: return '&#039;';
            }
        });
    }

    // Soft Delete
    let currentSoftDeleteId = null;
    function confirmSoftDelete(id) {
        currentSoftDeleteId = id;
        openModal('softDeleteModal');
    }
    document.getElementById('btnConfirmSoftDelete').addEventListener('click', async () => {
        if(!currentSoftDeleteId) return;
        closeModal('softDeleteModal');
        const res = await apiCall('soft_delete', { id: currentSoftDeleteId });
        if(res.success) {
            showToast('Lead moved to recycle bin');
            document.getElementById(`row-${currentSoftDeleteId}`).style.display = 'none';
        } else {
            showToast(res.error || 'Failed to delete lead', 'error');
        }
        currentSoftDeleteId = null;
    });

    // Restore
    async function restoreLead(id) {
        const res = await apiCall('restore_lead', { id });
        if(res.success) {
            showToast('Lead restored');
            document.getElementById(`row-${id}`).style.display = 'none';
        } else {
            showToast(res.error || 'Failed to restore lead', 'error');
        }
    }

    // Permanent Delete
    let currentPermDeleteId = null;
    function confirmPermanentDelete(id) {
        currentPermDeleteId = id;
        openModal('permDeleteModal');
    }
    document.getElementById('btnConfirmPermDelete').addEventListener('click', async () => {
        if(!currentPermDeleteId) return;
        closeModal('permDeleteModal');
        const res = await apiCall('permanent_delete', { id: currentPermDeleteId });
        if(res.success) {
            showToast('Lead permanently deleted');
            document.getElementById(`row-${currentPermDeleteId}`).style.display = 'none';
        } else {
            showToast(res.error || 'Failed to delete lead permanently', 'error');
        }
        currentPermDeleteId = null;
    });

</script>
</body>
</html>
