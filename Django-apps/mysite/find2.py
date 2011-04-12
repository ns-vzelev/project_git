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

def findReal(path,fn):
	r1 = "Search results:\n"
	if  not os.path.exists(path):
		r1 += "Wrong path\n"
		sys.exit()
	r = switch(path, fn)
	if r == []:
		r1 += "File(s) not found\n"
		return r1
	r2 = ""
        for el in r:
		r2 += el + "\n"	
        return r1+"\n"+r2

