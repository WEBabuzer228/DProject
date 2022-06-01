<?php include 'header.php';?>
<?php
session_start();
include('config.php');
if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $query = $connection->prepare("SELECT * FROM users WHERE username=:username");
    $query->bindParam("username", $username, PDO::PARAM_STR);
    $query->execute();
    $result = $query->fetch(PDO::FETCH_ASSOC);
    if (!$result) {
        echo '<p class="error">Неверные пароль или имя пользователя!</p>';
    } else {
        if (password_verify($password, $result['password'])) {
            $_SESSION['user_id'] = $result['id'];
            echo '<p class="success">Поздравляем, вы прошли авторизацию!</p>';
            setcookie('username', $username, time()+ 13600);
            header('location:/');
        } else {
            echo '<p class="error"> Неверные пароль или имя пользователя!</p>';
        }
    }
}
?>

<link href="style.css" rel="stylesheet">

<form method="post" action="" name="signin-form">
    <div class="form-element">
        <label>Имя пользователя</label>
        <input type="text" name="username" pattern="[a-zA-Z0-9]+" required />
    </div>
    <div class="form-element">
        <label>Пароль</label>
        <input type="password" name="password" required />
    </div>
    <button type="submit" name="login" value="login">Войти</button>
</form>