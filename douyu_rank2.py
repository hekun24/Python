import requests
import re
from multiprocessing import Pool

def getHtmlText(url):
	try:

		r=requests.get(url,timeout=30)
		r.encoding=r.apparent_encoding
		r.raise_for_status()
		return r.text
	except:
		return " "


def parse_page(html):
	pattern=re.compile('"rid":(\d+),"rn.*?nn":"(.*?)","cid1.*?"ol":(.*?),"url".*?c2name":"(.*?)","icdata',re.S)
	douyu=re.findall(pattern,html)
	return douyu


def get_page_count():
	url='https://www.douyu.com/directory/all'
	html=getHtmlText(url)
	pattern = re.compile('pageCount":(\d+),"pagePath',re.S)
	page=re.findall(pattern,html)
	return page


def print_txt(douyu):
	file=open('douyu.xls','w',encoding='gbk')
	file.write('房间号\t主播\t人气\t分区\n')
	for i in range(len(douyu)):
		for j in range(len(douyu[i])):
			file.write(douyu[i][j])
			file.write('\t')
		file.write('\n')
	file.close() 

def main(offset):
	a=[]
	url2='https://www.douyu.com/gapi/rkc/directory/0_0/'+str(offset)
	html2=getHtmlText(url2)
	a=parse_page(html2)
	print('{:.2f}%'.format(offset*100/count))
	douyu.extend (a)


count=int(get_page_count()[0])-5
douyu=[]

if __name__ == '__main__':
	for i in range(count):
		main(i+1)
	print_txt(douyu)
	

