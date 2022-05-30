<?php
define('USER', 'nekit');
define('PASSWORD', '1479');
define('HOST', 'localhost');
define('DATABASE', 'nekit');
try {
    $connection = new PDO("mysql:host=".HOST.";dbname=".DATABASE, USER, PASSWORD);
} catch (PDOException $e) {
    exit("Error: " . $e->getMessage());
}
?>