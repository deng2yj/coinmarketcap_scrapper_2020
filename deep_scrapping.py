import urllib.request
import os
import pandas as pd
import time

if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")

df = pd.read_csv("parsed_files/coinmarketcap_dataset.csv")


for link in df['link']:
	filename = link.replace("/","").replace("currencies", "")
	# print(filename)
	# print(link)
	if os.path.exists("deep_link_html/" + filename + ".html"):
		print(filename + " exists")
	else:

		f = open("deep_link_html/" + filename + ".html.temp", "wb")
		response = urllib.request.urlopen('https://coinmarketcap.com/' + link)
		html = response.read()
		print("downloading:" + filename)
		f.write(html)
		f.close()
		os.rename("deep_link_html/" + filename + ".html.temp", "deep_link_html/" + filename + ".html")
		time.sleep(10)