<?php

$recepient = "krupin_anton@mail.ru";
$siteName = "проектсрубов.рф";

$name = trim($_POST["name"]);
$phone = trim($_POST["phone"]);
$email = trim($_POST["e-mail"])
$message = "Имя: $name \nТелефон: $phone \nE-mail: $email";

$pagetitle = "Заявка с сайта \"$siteName\"";
mail($recepient, $pagetitle, $message, $email, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");

?>