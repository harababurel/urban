<?php
// $output = "\n\n\n\n" . shell_exec("fortune citate | cowsay -f $(ls /usr/share/cows/ | shuf -n1)");
$output = "\n\n\n\n" . shell_exec("python main.py");
$output = str_replace("\n", "\n        ", $output) . "\n";

echo $output;
?>
