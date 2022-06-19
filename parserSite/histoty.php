<?php include 'header.php';
include ('config.php');
$connection = new PDO("mysql:host=" . HOST . ";dbname=" . DATABASE, USER, PASSWORD);

function outDataSQLUser($select,$where,$like,$connection){
    $arrayOutPut = [];


    $query = $connection->prepare("SELECT $select FROM users WHERE $where LIKE '%$like%'");
    $query->execute();
    $outUser = $query->fetch(PDO::FETCH_ASSOC);
    $arrayOutPut = explode(',', $outUser[$select]);
    $arrayOutPut = array_slice($arrayOutPut, 0,count($arrayOutPut) - 1);

    return $arrayOutPut;
}
$historyUserexp = outDataSQLUser('history','username',$_SESSION['login'],$connection);
//$hrefGoodsSQL = outDataSQLUser('hrefhistory','username',$_SESSION['login'],$connection);

echo "<h2>Здесь выводится Ваша история сравнения:</h2>
    <div class='blockSearchHistory'>
         ";
        for($i = 0;$i < count($historyUserexp);$i++){
            $whatArray = explode(";", $historyUserexp[$i]);
            $arrayNeedSearch = explode(" ",$whatArray[0]);
            if($whatArray[1] == "T")
                $hrefToSearch = "/tech.php?searchPlace=";
            else
                $hrefToSearch = "/drugs.php?searchPlace=";
            for($j = 0; $j < count($arrayNeedSearch);$j++){
                $hrefToSearch = $hrefToSearch . $arrayNeedSearch[$j] . "+";
            }
            $hrefToSearch = substr($hrefToSearch, 0, -1);
            $hrefToSearch = $hrefToSearch . "&repRequest=Y&searchClick=";
            echo "<a href='" . $hrefToSearch ."'>
                  <li class='hs". $i ."'> $whatArray[0]
                  ";
                  echo "</li>
            </a>";
        }
    echo "
    </div> 

";

?>



