<?php
header('Content-Type: text/plain');

echo "PHP: " . PHP_VERSION . PHP_EOL;
echo "PDO: " . (class_exists('PDO') ? 'YES' : 'NO') . PHP_EOL;
echo "PDO SQLite: " . (extension_loaded('pdo_sqlite') ? 'YES' : 'NO') . PHP_EOL;
echo "SQLite3: " . (extension_loaded('sqlite3') ? 'YES' : 'NO') . PHP_EOL;

$dbDir = __DIR__ . '/db';
echo "DB directory exists: " . (is_dir($dbDir) ? 'YES' : 'NO') . PHP_EOL;
echo "DB directory writable: " . (is_writable($dbDir) ? 'YES' : 'NO') . PHP_EOL;

try {
    $pdo = new PDO('sqlite:' . $dbDir . '/test.sqlite');
    echo "SQLite connection: SUCCESS" . PHP_EOL;
} catch (Throwable $e) {
    echo "SQLite connection: FAILED" . PHP_EOL;
    echo "ERROR: " . $e->getMessage() . PHP_EOL;
}
?>
