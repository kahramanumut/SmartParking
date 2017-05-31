<?php
/**
 * Created by PhpStorm.
 * User: Umut
 * Date: 30.05.2017
 * Time: 17:35
 */
$page = $_SERVER['PHP_SELF'];
$sec = "2";
session_start();
$dolu = 0;
$con=mysqli_connect("localhost","root","root","akilliOtopark");
// Bağlantı kontrolü
if (mysqli_connect_errno())
{
    echo "MySql baglanti hatasi: " . mysqli_connect_error();
}
$result = mysqli_query($con,"SELECT * FROM park");
?>

<html>
<head>
    <meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
    <meta name=”viewport” content=”width=device-width, initial-scale=1″>
    <title>AKILLI OTOPARK | UMUT KAHRAMAN</title>
    <link rel="stylesheet" href="bootstrap-3.3.7-dist/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="style.css" />
</head>

<?php
while($row = mysqli_fetch_array($result)) {
    if ($row['Durum'] == "D" && $row['ID'] == 1) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 8%; top:35%; position: fixed\">
<img src=\"img/car1.png\" width=\"120\" height=\"240\" >
</div>";
    } else if ($row['Durum'] == "D" && $row['ID'] == 2) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 32%; top:35%; position: fixed\">
    <img src=\"img/car2.png\" width=\"120\" height=\"240\" >
</div>";
    } else if ($row['Durum'] == "D" && $row['ID'] == 3) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 56%; top:35%; position: fixed\">
    <img src=\"img/car3.png\" width=\"120\" height=\"240\" >
</div>";
    } else if ($row['Durum'] == "D" && $row['ID'] == 4) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 80%; top:35%; position: fixed\">
    <img src=\"img/car4.png\" width=\"120\" height=\"240\" >
</div>";
    } else if ($row['Durum'] == "D" && $row['ID'] == 5) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 8%; top:55%; position: fixed\">
    <img src=\"img/car3.png\" width=\"120\" height=\"240\" >
</div>";
    } else if ($row['Durum'] == "D" && $row['ID'] == 6) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 32%; top:55%; position: fixed\">
    <img src=\"img/car1.png\" width=\"120\" height=\"240\" >
</div>";
    } else if ($row['Durum'] == "D" && $row['ID'] == 7) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 56%; top:55%; position: fixed\">
    <img src=\"img/car2.png\" width=\"120\" height=\"240\" >
</div>";
    } else if ($row['Durum'] == "D" && $row['ID'] == 8) {
        $dolu = $dolu + 1;
        echo "<div style=\"left: 80%; top:55%; position: fixed\">
    <img src=\"img/car4.png\" width=\"120\" height=\"240\" >
</div>";
    }
}

if ($_SESSION["dolu"]==$dolu){
	} else {
		$kalan = 8 - $dolu;
		echo "<script>alert(' ".$kalan." Park alanı kaldı');</script>";
	}
$_SESSION["dolu"] = $dolu;
mysqli_close($con);

?>
<!--
<div style="left: 8%; top:35%; position: fixed">
    <img src="img/car1.png" width="120" height="240" >
</div>

<div style="left: 32%; top:35%; position: fixed">
    <img src="img/car2.png" width="120" height="240" >
</div>
<div style="left: 56%; top:35%; position: fixed">
    <img src="img/car3.png" width="120" height="240" >
</div>
<div style="left: 80%; top:35%; position: fixed">
    <img src="img/car4.png" width="120" height="240" >
</div>
<div style="left: 8%; top:55%; position: fixed">
    <img src="img/car3.png" width="120" height="240" >
</div>
<div style="left: 32%; top:55%; position: fixed">
    <img src="img/car1.png" width="120" height="240" >
</div>
<div style="left: 56%; top:55%; position: fixed">
    <img src="img/car2.png" width="120" height="240" >
</div>
<div style="left: 80%; top:55%; position: fixed">
    <img src="img/car3.png" width="120" height="240" >
</div>
-->

</html>