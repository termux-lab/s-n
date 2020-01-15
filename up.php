<?php
$sn = file_get_contents("https://raw.githubusercontent.com/termux-lab/smsham/master/smsham.py");
$file = fopen("sn.py", "w");
fwrite($file, $sn);
fclose($file);
?>
