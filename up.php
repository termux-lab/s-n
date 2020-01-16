<?php
$sn = file_get_contents("https://raw.githubusercontent.com/termux-lab/s-n/master/sn.py");
$file = fopen("sn.py", "w");
fwrite($file, $sn);
fclose($file);
?>
