<?php include 'header.php';
?>

<h2>Введите название нужного товара, который хотите сравнить в аптеках</h2>
<form class="inputform" method="GET" action="<?=$_SERVER['PHP_SELF'];?>">
    <input name="searchPlace" placeholder="Введите название товара">
    <input name="repRequest" value="N" style="display: none">
    <button class="search" type="submit" name="searchClick">
        <img src="png/loopa.png" width="36" height="36">
    </button>



</form>


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
                    if($store == "eapteka" /*or ...*/){
                        echo "<img src='png/eapteka.jpg' width='35' height='35' style='float: right; opacity: 75%'>";
                    }
                    else if($store == "apteka"){
                        echo "<img src='png/apteka.PNG' width='35' height='35' style='float: right; opacity: 75%'>";
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
include "config.php";
global $connection;

$connection = new PDO("mysql:host=".HOST.";dbname=".DATABASE, USER, PASSWORD);

function outDataSQLUser($select,$where,$like,$connection){
    $arrayOutPut = [];

    $query = $connection->prepare("SELECT $select FROM users WHERE $where LIKE '%$like%'");
    $query->execute();
    $outUser = $query->fetch(PDO::FETCH_ASSOC);
    $arrayOutPut = explode(',', $outUser[$select]);
    $arrayOutPut = array_slice($arrayOutPut, 0,count($arrayOutPut) - 1);

    return $arrayOutPut;
}

function sendStrSearchToDB($needSearch,$hrefGoods,$connection) {

    $historyUserexp = outDataSQLUser('history','username',$_SESSION['login'],$connection);

    if (count($historyUserexp) == 10) {
        array_shift($historyUserexp);
        $historyUserexp[] = $needSearch . ";D";

    } else {
        $historyUserexp[] = $needSearch . ";D";
    }
    for($i = 0; $i < count($historyUserexp);$i++){
        $historyUserexp[$i] = $historyUserexp[$i] . ',';
    }
    $strToWriteDB = implode($historyUserexp);
    //print($strToWriteDB);

    $query = $connection->prepare("UPDATE users SET history = '" . $strToWriteDB . "' WHERE username = '" . $_SESSION['login'] . "'");
    $result = $query->execute();

}

function searchFormDBandOutPut($nameTable,$needSearch){
    $outGoods = [];

    $connection = new PDO("mysql:host=".HOST.";dbname=".$nameTable, USER, PASSWORD);
    $query = $connection->prepare("SHOW TABLES;");
    $query->execute();
    $tables = $query->fetchAll(PDO::FETCH_ASSOC);

    $arrayNeedSearch = explode(" ", $needSearch);

    //Example
    //AND (CONVERT(`name` USING utf8) LIKE '%13%') 
    // И добавлять (AND (CON...) пока не кончатся слова из поля поиска

    $sqlQuery = "WHERE (CONVERT(`name` USING utf8) LIKE '%$arrayNeedSearch[0]%') ";

    $finded = false;

    for ($i = 1; $i < count($arrayNeedSearch); $i++){
        $sqlQuery = $sqlQuery . "AND (CONVERT(`name` USING utf8) LIKE '%$arrayNeedSearch[$i]%') ";
    }

    for($j = 0; $j < count($tables);$j++) {


        $query = $connection->prepare("SELECT *  FROM `$nameTable`.`" . $tables[$j]['Tables_in_'.$nameTable] . "` " . $sqlQuery);
        $query->execute();
        $outGoods = $query->fetchAll(PDO::FETCH_ASSOC);

        if (count($outGoods) != 0) {
            for ($i = 0; $i < count($outGoods); $i++) {
                $arrayGoods = [];
                $arrayGoods[] = $outGoods[$i]['name'];
                $arrayGoods[] = $outGoods[$i]['price'];
                $arrayGoods[] = $outGoods[$i]['link'];
                outGoods($arrayGoods, $i, $nameTable);
                $finded = true;
            }

        }
    }
    return $finded;
}

if (isset($_GET['searchClick'])) {
    searchClick();
}

function searchClick()
{
    $needSearch = $_GET['searchPlace'];
    $repRequest = $_GET['repRequest'];

    $checkEA = false;
    $checkE = false;

    $connectSQL = new PDO("mysql:host=".HOST.";dbname=".DATABASE, USER, PASSWORD);

    if (!empty($needSearch)){
        $checkEA = searchFormDBandOutPut("eapteka",$needSearch);
        $checkE = searchFormDBandOutPut("apteka",$needSearch);

    }
    else if(empty($needSearch)){
        echo "<h2 style=\"text-align: center;margin-top: 20px;margin-bottom: 20px;\">
                      Пустой запрос!</h2>";
    }
    else if(!$checkEA and !$checkE) {
        echo "<h2 style=\"text-align: center;margin-top: 20px;margin-bottom: 20px;\">
                      По вашему запросу ничего не найдено</h2>";
    }

    
    if (isset($_SESSION['user_id']) != false and !empty($needSearch)) {
        if($repRequest == 'N') {
            sendStrSearchToDB($needSearch, "nothing", $connectSQL);
        }
    } 
    else if (isset($_SESSION['user_id']) == false) {
        echo "<h2 style=\"text-align: center;margin-top: 20px;margin-bottom: 20px;\">
                  Если вы хотите, чтобы ваша история запросов сохранялась,вам нужно авторизоваться или зарегистрироваться на нашем сайте</h2>";
    }

}

?>
<!--
"SELECT *  FROM `$nameTable`.`" . $tables[$j]['Tables_in_'.$nameTable] . "` WHERE (CONVERT(`id` USING utf8) REGEXP '$needSearch' OR CONVERT(`name` USING utf8) REGEXP '$needSearch'
OR CONVERT(`price` USING utf8) REGEXP '$needSearch' OR CONVERT(`link` USING utf8) REGEXP '$needSearch');");
SELECT * FROM `dns`.`smartfony` WHERE (CONVERT(`id` USING utf8) REGEXP 'iphone 13 256 ГБ белый' OR CONVERT(`name` USING utf8) REGEXP 'iphone 13 256 ГБ белый'
OR CONVERT(`price` USING utf8) REGEXP 'iphone 13 256 ГБ белый' OR CONVERT(`link` USING utf8) REGEXP 'iphone 13 256 ГБ белый')
-->