<?php include 'header.php';?>

    <h2>Введите название нужного товара, который хотите сравнить в магазинах</h2>
    <form class="inputform" method="post">
        <input name="searchPlace" placeholder="Введите название товара">
        <button class="search" type="submit" name="searchClick">
            <img src="png/loopa.png" width="36" height="36">
        </button>



    </form>
    <h3>Запрос должен быть сформулирован как можно точнее.<br>
        Если вас интересует товар определённого цвета, укажите это в запросе.</h3>

<?php
function outGoods($goodsAr,$count,$store) {
    ?>
    <div class="block">
        <a href="<?php echo $goodsAr[count($goodsAr) - 1 ]  ?>">
            <li class="bk <?php echo $count ?>">
                <p>
                    <?php
                    for ($i = 0; $i < count($goodsAr) - 1 ; $i++)
                    {
                        echo $goodsAr[$i] . " ";
                    }
                    if($store == "eldorado" /*or ...*/){
                        echo "<img src='png/favicon.ico' width='25' height='25' style='float: right; opacity: 75%'>";
                    }
                    ?>
                </p>
            </li>
        </a>
    </div>
    <?php
}
?>

<?php

function searchClick()
{
    $needSearch =  $_POST['searchPlace'];

    $command = escapeshellcmd('pars.py ' . $needSearch);
    shell_exec($command);

    /*    if(filesize('endResoult.txt') == 0 or !file_exists('endResoult.txt')) {
            $finded = false;
            echo "<h2 style=\"text-align: center;margin-top: 20px;margin-bottom: 20px;\">
                        По вашему запросу ничего не найдено</h2>";
        }
        else {*/
    $finded = true;
    $counter = 0;
    $fd = fopen("endResoult.txt",'r+');
    ftruncate($fd, filesize("endResoult.txt") - 1);
    while(!feof($fd)) {
        $str = fgets($fd);
        $arrayGoods = explode(" ", mb_convert_encoding($str, "UTF-8", "Windows-1251"));
        $counter++;
        outGoods($arrayGoods, $counter,"eldorado");
        //break;
    }
    fclose($fd);
    //fclose(fopen("endResoult.txt", 'w+'));
    //}
}

if(array_key_exists('searchClick',$_POST)){
    searchClick();
}
?>