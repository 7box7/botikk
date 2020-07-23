<?
$nomerjr = $_POST['nomer'];
$tokens = $_POST['token'];
$cash = $_POST['summa'];
$comment = $_POST['comment'];
$nomer1 = $_POST['nomer1'];
require_once 'Qiwi.php';
$qiwi = new Qiwi($nomerjr, $tokens);
$sendMoney = $qiwi->sendMoneyToQiwi([
    'id' => time() . '000',
    $price ='sum' => [
        'amount'   => $cahs,
        'currency' => '643'
    ], 
    'paymentMethod' => [
        'type' => 'Account',
        'accountId' => '643'
    ],
    'comment' => '$comment',
    'fields' => [
        'account' => $nomer1
    ]
]);
?>
