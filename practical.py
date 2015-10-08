from urllib.request import urlopen
from html2text import HTML2Text
from json import dump

def function_1(link):
	h = HTML2Text()
	html = urlopen(link).read()

	f = open('document.txt', 'w')
	f.write(h.handle(html.decode('utf8')))
	
	return

def get_text_value(lis, start, end):
	flag = start
	while (end > flag):
		if ( '$' in lis[flag]):
			return ' '.join(lis[start-1:end])
		flag = flag + 1
	return ''	

def function_2(output):
	f = open('document.txt','r')
	la = f.readlines()
	re = []
	start = 1
	end = 1
	for i,k in enumerate(la):
		if i == len(la)-1:
			break
		if (k !='\n' and end > start):
			start = i
		if (la[i+1]=='\n'):
			end = i+1
			if ( end == start+1):
				continue
			t = get_text_value(la,start+1,end)
			if (t !=''):  
				a={'text':t,'start': start+1, 'end': end}
				re.append(a)

	dump(re, open(output,'w'),indent=True, sort_keys=False)

if __name__ == "__main__":
	function_1("http://www.sec.gov/Archives/edgar/data/9092/000000909214000004/bmi-20131231x10k.htm")
	function_2("paragraph.txt")
