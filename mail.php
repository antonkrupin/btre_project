<?php

$recepient = "krupin_anton@mail.ru";
$siteName = "Данные с сайта atlantstroy";

$name = trim($_POST["name"]);
$phone = trim($_POST["phone"]);
$message = "Имя: $name \nТелефон: $phone";

$pagetitle = "Переход по форме и скачивание файла - как избежать ошибок \"$siteName\"";
mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");

?>