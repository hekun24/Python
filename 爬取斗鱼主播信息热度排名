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

def fillList(ulist,html):
	ulist=re.findall('"nn":"(.*?)","od.*?"ol":(.*?),"ot".*?,"rgrpt":1.*?rid":(.*?),"rkic"',html,re.S)
	num=len(ulist)
	sortt(ulist)
	for i in range(num):
		u=ulist[i]
		print('排名'+str(i+1)+':'+u[0]+'   '+'人气'+':'+u[1]+'   '+'房间号'+u[2])

def stringnum(s1,s2):
	if len(s1)>len(s2):
		return True
	if len(s1)<len(s2):
		return False
	else :
		return s1>s2
	
def sortt(ulist):
	num=len(ulist)
	i=0
	for i in range(num-1):
		j=i+1
		for j in range(num):
			if stringnum(ulist[i][1],ulist[j][1]):
				t=ulist[i]
				ulist[i]=ulist[j]
				ulist[j]=t;
        

def main():
	unifo=[];
	url='https://www.douyu.com/g_LOL'
	html=getHTMLText(url)
	fillList(unifo,html)

	

main()
