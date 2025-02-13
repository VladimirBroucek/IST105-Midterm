<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculation Result</title>
</head>
<body>
    <h1>Calculation Result</h1>
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $number1 = escapeshellcmd($_POST['number1']);
    $number2 = escapeshellcmd($_POST['number2']);
    $operation = escapeshellcmd($_POST['operation']);

    $command = "python3 math_operations.py $number1 $number2 $operation";
    $output = shell_exec($command);

    if ($output === null) {
        echo "<p>Error: Unable to execute script</p>";
    } else {
        echo "<pre>$output</pre>";
    }
} else {
    echo "<p>Error: Invalid request method</p>";
}

?>
</body>
</html>
