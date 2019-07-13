import requests
import re
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return " "

def get(douyu,html):
	douyu=re.findall('"nn":"(.*?)","od.*?"ol":(.*?),"ot".*?,"rgrpt":1.*?rid":(.*?),"rkic"',html,re.S)
	sortt(douyu)
	return douyu

def printlist(douyu):
	for i in range(len(douyu)):
		u=douyu[i]
		print('排名'+str(i+1)+':'+u[0]+'   '+'人气'+':'+u[1]+'   '+'房间号'+u[2])
	
def print_txt(douyu):
	file=open('douyu.txt','w')
	i=0
	for a in douyu:
		i=i+1
		atxt='排名:{} {},人气:{},房间号:{}'.format(i,a[0],a[1],a[2])
		file.write(atxt)
		file.write('\n')
	file.close() 

def stringnum(s1,s2):
	if len(s1)>len(s2):
		return True
	if len(s1)<len(s2):
		return False
	else :
		return s1>s2
	
def sortt(douyu):
	num=len(douyu)
	i=0
	for i in range(num):
		j=i+1
		for j in range(num):
			if stringnum(douyu[i][1],douyu[j][1]):
				t=douyu[i]
				douyu[i]=douyu[j]
				douyu[j]=t;
        

def main():
	douyu=[]
	url='https://www.douyu.com/directory/all'
	html=getHTMLText(url)
	douyu=get(douyu,html)
	printlist(douyu)
	if True:
		print_txt(douyu)

main()
