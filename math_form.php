<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MidTerm Exam</title>
</head>
<body>
    <h1>Welcome to the Mathematical Application</h1>
    <form action="process_math.php" method="POST">
        <label for="number1">Enter a number one:</label>
        <input type="number" id="number1" name="number1" required><br><br>

        <label for="number2">Enter a number two:</label>
        <input type="number" id="number2" name="number2" required><br><br>

        <label for="operation">Operations:</label>
        <select name="operation" id="operation" required>
            <option value="add">Addition</option>
            <option value="subtract">Subtraction</option>
            <option value="multiply">Multiplication</option>
            <option value="divide">Division</option>
        </select>

        <button type="submit">Calculate</button>
    </form>
</body>
</html>
