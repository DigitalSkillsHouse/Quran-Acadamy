<?php
define('STORAGE_DIR', __DIR__ . '/data');
define('LEADS_FILE', STORAGE_DIR . '/leads.jsonl');
define('USERS_FILE', STORAGE_DIR . '/users.json');

function initStorage() {
    if (!is_dir(STORAGE_DIR)) {
        if (!mkdir(STORAGE_DIR, 0755, true)) {
            return false;
        }
    }
    if (!file_exists(LEADS_FILE)) {
        touch(LEADS_FILE);
    }
    if (!file_exists(USERS_FILE)) {
        file_put_contents(USERS_FILE, json_encode([]));
    }
    return true;
}

function appendLead($data) {
    if (!initStorage()) return false;
    $fp = fopen(LEADS_FILE, 'a');
    if (!$fp) return false;
    if (flock($fp, LOCK_EX)) {
        $json = json_encode($data, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "\n";
        fwrite($fp, $json);
        flock($fp, LOCK_UN);
        fclose($fp);
        return true;
    }
    fclose($fp);
    return false;
}

function getLeads() {
    if (!file_exists(LEADS_FILE)) return [];
    $leads = [];
    $fp = fopen(LEADS_FILE, 'r');
    if (!$fp) return [];
    if (flock($fp, LOCK_SH)) {
        while (($line = fgets($fp)) !== false) {
            $line = trim($line);
            if (empty($line)) continue;
            $data = json_decode($line, true);
            if (is_array($data)) {
                $leads[] = $data;
            }
        }
        flock($fp, LOCK_UN);
    }
    fclose($fp);
    return array_reverse($leads);
}

function updateLead($id, $updates) {
    if (!file_exists(LEADS_FILE)) return false;
    $tmpFile = LEADS_FILE . '.tmp.' . bin2hex(random_bytes(8));
    $fp = fopen(LEADS_FILE, 'r+');
    if (!$fp) return false;
    if (flock($fp, LOCK_EX)) {
        $out = fopen($tmpFile, 'w');
        if (!$out) {
            flock($fp, LOCK_UN);
            fclose($fp);
            return false;
        }
        $updated = false;
        while (($line = fgets($fp)) !== false) {
            $line = trim($line);
            if (empty($line)) continue;
            $data = json_decode($line, true);
            if (is_array($data) && isset($data['id']) && (string)$data['id'] === (string)$id) {
                foreach ($updates as $k => $v) {
                    $data[$k] = $v;
                }
                $updated = true;
            }
            if (is_array($data)) {
                fwrite($out, json_encode($data, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "\n");
            }
        }
        fflush($out);
        fclose($out);
        if ($updated) {
            if (!rename($tmpFile, LEADS_FILE)) {
                unlink($tmpFile);
                $updated = false;
            }
        } else {
            unlink($tmpFile);
        }
        flock($fp, LOCK_UN);
        fclose($fp);
        return $updated;
    }
    fclose($fp);
    return false;
}

function getRecentLeadCountByIp($ip) {
    if (!file_exists(LEADS_FILE)) return 0;
    $count = 0;
    $timeLimit = strtotime('-1 hour');
    $fp = fopen(LEADS_FILE, 'r');
    if (!$fp) return 0;
    if (flock($fp, LOCK_SH)) {
        $lines = [];
        while (($line = fgets($fp)) !== false) {
            $line = trim($line);
            if (!empty($line)) {
                $lines[] = $line;
            }
        }
        for ($i = count($lines) - 1; $i >= 0; $i--) {
            $data = json_decode($lines[$i], true);
            if (is_array($data)) {
                $createdAt = strtotime($data['created_at'] ?? '0');
                if ($createdAt < $timeLimit) {
                    break;
                }
                if (($data['ip_address'] ?? '') === $ip) {
                    $count++;
                }
            }
        }
        flock($fp, LOCK_UN);
    }
    fclose($fp);
    return $count;
}

function getUser($username) {
    if (!file_exists(USERS_FILE)) return null;
    $fp = fopen(USERS_FILE, 'r');
    if (!$fp) return null;
    $found = null;
    if (flock($fp, LOCK_SH)) {
        $content = stream_get_contents($fp);
        $users = $content ? json_decode($content, true) : [];
        if (is_array($users)) {
            foreach ($users as $user) {
                if ($user['username'] === $username) {
                    $found = $user;
                    break;
                }
            }
        }
        flock($fp, LOCK_UN);
    }
    fclose($fp);
    return $found;
}

function getUserById($id) {
    if (!file_exists(USERS_FILE)) return null;
    $fp = fopen(USERS_FILE, 'r');
    if (!$fp) return null;
    $found = null;
    if (flock($fp, LOCK_SH)) {
        $content = stream_get_contents($fp);
        $users = $content ? json_decode($content, true) : [];
        if (is_array($users)) {
            foreach ($users as $user) {
                if ((string)$user['id'] === (string)$id) {
                    $found = $user;
                    break;
                }
            }
        }
        flock($fp, LOCK_UN);
    }
    fclose($fp);
    return $found;
}

function createUser($username, $hash) {
    initStorage();
    $tmpFile = USERS_FILE . '.tmp.' . bin2hex(random_bytes(8));
    $fp = fopen(USERS_FILE, 'r+');
    if (!$fp) return false;
    if (flock($fp, LOCK_EX)) {
        $content = stream_get_contents($fp);
        $users = $content ? json_decode($content, true) : [];
        if (!is_array($users)) $users = [];

        if (!empty($users)) {
            flock($fp, LOCK_UN);
            fclose($fp);
            return false;
        }

        $id = bin2hex(random_bytes(16));
        $users[] = [
            'id' => $id,
            'username' => $username,
            'password_hash' => $hash,
            'created_at' => date('Y-m-d H:i:s'),
            'last_login' => null
        ];

        $out = fopen($tmpFile, 'w');
        if ($out) {
            fwrite($out, json_encode($users, JSON_PRETTY_PRINT));
            fflush($out);
            fclose($out);
            if (rename($tmpFile, USERS_FILE)) {
                flock($fp, LOCK_UN);
                fclose($fp);
                return true;
            }
            unlink($tmpFile);
        }
        flock($fp, LOCK_UN);
        fclose($fp);
        return false;
    }
    fclose($fp);
    return false;
}

function updateUserPassword($id, $hash) {
    $tmpFile = USERS_FILE . '.tmp.' . bin2hex(random_bytes(8));
    $fp = fopen(USERS_FILE, 'r+');
    if (!$fp) return false;
    if (flock($fp, LOCK_EX)) {
        $content = stream_get_contents($fp);
        $users = $content ? json_decode($content, true) : [];
        if (!is_array($users)) {
            flock($fp, LOCK_UN);
            fclose($fp);
            return false;
        }
        $updated = false;
        foreach ($users as &$user) {
            if ((string)$user['id'] === (string)$id) {
                $user['password_hash'] = $hash;
                $updated = true;
                break;
            }
        }
        if ($updated) {
            $out = fopen($tmpFile, 'w');
            if ($out) {
                fwrite($out, json_encode($users, JSON_PRETTY_PRINT));
                fflush($out);
                fclose($out);
                if (rename($tmpFile, USERS_FILE)) {
                    flock($fp, LOCK_UN);
                    fclose($fp);
                    return true;
                }
                unlink($tmpFile);
            }
        }
        flock($fp, LOCK_UN);
        fclose($fp);
        return false;
    }
    fclose($fp);
    return false;
}

function updateLastLogin($id) {
    $tmpFile = USERS_FILE . '.tmp.' . bin2hex(random_bytes(8));
    $fp = fopen(USERS_FILE, 'r+');
    if (!$fp) return false;
    if (flock($fp, LOCK_EX)) {
        $content = stream_get_contents($fp);
        $users = $content ? json_decode($content, true) : [];
        if (!is_array($users)) {
            flock($fp, LOCK_UN);
            fclose($fp);
            return false;
        }
        $updated = false;
        foreach ($users as &$user) {
            if ((string)$user['id'] === (string)$id) {
                $user['last_login'] = date('Y-m-d H:i:s');
                $updated = true;
                break;
            }
        }
        if ($updated) {
            $out = fopen($tmpFile, 'w');
            if ($out) {
                fwrite($out, json_encode($users, JSON_PRETTY_PRINT));
                fflush($out);
                fclose($out);
                rename($tmpFile, USERS_FILE);
            }
        }
        flock($fp, LOCK_UN);
        fclose($fp);
        return true;
    }
    fclose($fp);
    return false;
}

function hasUsers() {
    if (!file_exists(USERS_FILE)) return false;
    $fp = fopen(USERS_FILE, 'r');
    if (!$fp) return false;
    $has = false;
    if (flock($fp, LOCK_SH)) {
        $content = stream_get_contents($fp);
        $users = $content ? json_decode($content, true) : [];
        $has = !empty($users);
        flock($fp, LOCK_UN);
    }
    fclose($fp);
    return $has;
}
