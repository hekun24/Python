import requests
import re
def getHTMLText(url):#requests库得到页面文本内容
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		return r.text
	except:
		return " "

def get(huya,html):#正则表达式得到筛选信息
	huya1=re.findall('"nick" title="(.*?)">.*?game-type.*?title="(.*?)">',html,re.S)
	huya2=re.findall('totalCount":"(.*?),"roomName.*?fileRoom":"(.*?)","',html,re.S)
	huya=list(zip(huya1,huya2))
	sortt(huya)
	return huya

def stringnum(s1,s2):#字符数字排序
	if len(s1)>len(s2):
		return True
	if len(s1)<len(s2):
		return False
	else :
		return s1>s2

def sortt(huya):#排序
	num=len(huya)
	i=0
	for i in range(num):
		j=i+1
		for j in range(num):
			if stringnum(huya[i][1][0],huya[j][1][0]):
				t=huya[i]
				huya[i]=huya[j]
				huya[j]=t;

def printlist(huya):#打印
	i=0
	for i in range(len(huya)):
		u=huya[i]
		print('排名'+str(i+1)+':'+u[0][0]+'   '+'人气'+':'+u[1][0]+'   '+'房间号:'+u[1][1]+' '+'分区:'+u[0][1])

def print_txt(huya):#输出到txt文本
	file=open('huya.txt','w')
	i=0
	for a in huya:
		i=i+1
		atxt='排名{}:{}, 人气:{}, 房间号:{}, 分区:{}'.format(i,a[0][0],a[1][0],a[1][1],a[0][1])
		file.write(atxt)
		file.write('\n')
	file.close() 


def main():
	huya=[]
	url='https://www.huya.com/l'
	html=getHTMLText(url)
	huya=get(huya,html)
	printlist(huya)
	if True:#默认关闭
		print_txt(huya)


main()

