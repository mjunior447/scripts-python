import time
import requests

def RTT(url):
	t1 = time.time()
	r = requests.get(url)
	t2 = time.time()
	tim = str(t2 - t1)
	print("Tempo em segundos: " + tim)


url = "http://www.google.com"
RTT(url)