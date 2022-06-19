<html lang="ru">
<?php session_start(); ?>
<head>
<!--    <meta charset="UTF-8">-->
    <title>  </title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="png/fav.png" type="image/x-icon">
</head>
<body>

<header id="header" class="header">
    <div class="container">
        <div class="nav">
           <a href="index.php">
            <img class="logo" src="png/GoodsLogo.png" alt="GoodsCHECK">
            </a>
            <?php
            if(isset($_SESSION['user_id']) == false):
            ?>


            <li>
                <a href="http://goodscheck.local/register.php">
                    Регистрация
                </a>
            </li>

            <li>
                </a>
                <a href="http://goodscheck.local/login.php">
                    Войти
                </a>
            </li>
            <?php else: ?>
                <li class="nav">
                    <a  href="exit.php">Выход</a>
                </li>
            <li class="history">
                <a href="histoty.php">История</a>
            </li>


            <?php endif;?>
            <p class="discr">Сервис для автоматизации выбора товаров</p>
        </div>

    </div>
</header>
