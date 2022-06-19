<?php
include "header.php";
session_start();
include "config.php";

$connection = new PDO("mysql:host=".HOST.";dbname=".DATABASE, USER, PASSWORD);

if(isset($_SESSION['user_id']) == false){
    echo " <h2> Вы не авторизованных для доступа к этой странице.</h2> ";
}
else{
    if(isset($_SESSION['access_lvl']) == false || $_SESSION['access_lvl'] == 0){
        echo " <h2> У вас нет доступа к этой странице.</h2> ";
    }
    else{
        echo " <h2> Добро пожаловать в админ-панель " . $_SESSION['login'] . ".</h2> ";

        $query = $connection->prepare("SELECT username,history FROM users");
        $query->execute();
        $outUser = $query->fetchAll(PDO::FETCH_ASSOC);

        //print_r($outUser);
        echo "
        
        <div class='blockAllUserHistory'>
        ";
        for($i = 0; $i < count($outUser);$i++){
            echo " <li class='user ". $i ."'>
                <h4>" . $outUser[$i]['username'] . " </h4>";

                $arrayOutPutHs = explode(',', $outUser[$i]['history']);
                $arrayOutPutHs = array_slice($arrayOutPutHs, 0,count($arrayOutPutHs) - 1);
                for($j = 0;$j < count($arrayOutPutHs);$j++){
                    $whatArray = explode(";", $arrayOutPutHs[$j]);
                    $arrayNeedSearch = explode(" ",$whatArray[0]);

                    if($whatArray[1] == "T")
                        $hrefToSearch = "/tech.php?searchPlace=";
                    else
                        $hrefToSearch = "/drugs.php?searchPlace=";

                    for($k = 0; $k < count($arrayNeedSearch);$k++){
                        $hrefToSearch = $hrefToSearch . $arrayNeedSearch[$k] . "+";
                    }
                    $hrefToSearch = substr($hrefToSearch, 0, -1);

                    $hrefToSearch = $hrefToSearch . "&repRequest=Y&searchClick=";
                    echo " <a href='" . $hrefToSearch ."'> 
                            <p class='hs". $j . "'>" . $whatArray[0] . "
                           </p>
                       </a>
                ";
                }
            echo "</li>
            ";
        }
        echo "
        </div>
        
        ";
    }

}