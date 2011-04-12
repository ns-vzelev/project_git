import sys, os, re

def switch(path,fn):
	temp = ""	
	i1 = len(fn) - 1
	i = 0
	l = []
	for ch in fn:
		l += [ch]
	while i<len(l) - 1:
		if (l[i] == "*" and l[i+1] == "?") or (l[i+1] == "*" and l[i] == "?"):
			l[i] = ".+" 
			del l[i+1] 			
		elif l[i] == "?":
			l[i] = "."
		elif l[i]== "*":
			l[i] = ".*"
		elif l[i] == ".":
			l[i] = "\."
		else: 
			l[i] = fn[i]
		i+=1

	if l[-1] != ".+":
		if l[-1] == "?":
			l[-1] = "."
		elif l[-1]== "*":
			l[-1] = ".*"
		elif l[-1] == ".":
			l[-1] = "\."
		else: 
			l[-1] = fn[-1]
			
	for el in l:
		temp += el
	return findRe(path,temp)
		
def findRe(pth,fn):
	res = []
	l = os.listdir(pth)
	for el in l:
           try:
		if os.path.isfile(pth+"/"+el):
			p = re.compile(fn)
			m = p.match(el)
			if m:
				if m.group() == el:
					res += [pth+"/"+el]	
		elif os.path.isdir(pth+"/"+el):
			res.extend(findRe(pth+"/"+el,fn))
	   except OSError:
		pass
	return res

pth = sys.argv[1]
r = []
print "Search results"
if  not os.path.exists(pth):
	print "Wrong path"
	sys.exit()
r = switch(sys.argv[1], sys.argv[2])
if r == []:
	print "File(s) not found"
for el in r:
	print el
print "\n"
