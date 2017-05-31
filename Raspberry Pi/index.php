<?php
$page = $_SERVER['PHP_SELF'];
$sec = "2";
session_start();
$dolu = 0;
?>

<html>
 <head>
 <meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
 </head>
 <body bgcolor="#E6E6FA">

<?php
$con=mysqli_connect("localhost","root","root","akilliOtopark");
// Bağlantı kontrolü
if (mysqli_connect_errno())
{
echo "MySql baglanti hatasi: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT * FROM park");

echo "<center><table  width='100%' height='100%' border='1' cellspacing='0' cellpadding='0'>
<tr>
<th width='30%' bgcolor='#AAAA30'>Yer</th>
<th width='30%' bgcolor='#AAAA30'>Durum</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td><center>" . $row['ID'] . "</center></td>";
	if ($row['Durum']== "D"){
		$dolu = $dolu +1;
		echo "<td bgcolor='#FF0000'><center>Dolu</center></td>";
	} else {
		echo "<td bgcolor='#00FF00'><center>Boş</center></td>";
	}


echo "</tr>";
}
echo "</table></center>";
if ($_SESSION["dolu"]== $dolu){
	
	} else {
		$kalan = 8 - $dolu;
		echo "<script>alert(' ".$kalan." Park alanı kaldı');</script>";
	}
$_SESSION["dolu"] = $dolu;

mysqli_close($con);
?>

</body>
</html>