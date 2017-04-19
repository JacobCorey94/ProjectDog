<?PHP
if (isset($_GET['item'])) {
	$item = $_GET['item'];
} else {
	$item = "item";
}

if (isset($_GET['sites'])) {
	$sites = str_replace(","," ",$_GET['sites']);
} else {
	$sites = "bestbuy target walmart amazon";
}

//$arr = explode("\n",shell_exec('python ../scrape.py "' . $item . '" bestbuy target walmart'));

$out = shell_exec('python ../scrape.py "' . $item . '" ' . $sites);
// Remove the debugging strings, they should really be printed to a logfile anyway.
echo substr($out,strrpos($out,"[["));

?>
