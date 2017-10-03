import ast
import time
import requests

def intWithCommas(x):
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)


def main():
	while True:
		re = requests.get("https://vip.bitcoin.co.id/api/btc_idr/ticker")
		if re.status_code != 200:
			print "Please check your connection!"
		else:
			decoded = ast.literal_eval(re.text)
			print intWithCommas(int(decoded['ticker']['last']))
		time.sleep(900)

if __name__ == "__main__":
	main()