import sys, os, re, settings
from operator import itemgetter, attrgetter
def fSize(size):
	if size < 1024:
		return str(size) + "B"
	if size >= 1024 and size < 1024**2:
		return str(round(float(size/1024),2))+ "KB"
	if size >= 1024**2 and size < 1024**3:
		return str(round(float(size/1024**2),2))+ "MB"
	if size >= 1024**3 and size < 1024**4:
		return str(round(float(size/1024**3),2))+ "GB"
	if size >= 1024**4 and size < 1024**5:
		return str(round(float(size/1024**4),2))+"TB"
def listing(path):
	lst = os.listdir(path)
	res = []
	for el in lst:
		t = os.path.join(path,el)
		if os.path.isfile(t):
			i = -1
			while -1*i <= len(el) and el[i]!=".":
				i -=1
			if el[i:] in settings.text_list:
				fileS = '<a href = "/textfiles/'+t[len(settings.Velly_Root):]+'"><img src = "/static/txt_f.png" title = "View" width = "30px" height = "30px"/></a>'
				res += [(fileS+" "+el, fSize(os.path.getsize(t)))]
		   	elif path[:-1] in settings.STATICFILES_DIRS:
				fileS ='<a href ='+'"/static/'+el+'/" >'
				fileS+='<img src ="/static/file.jpeg" width = "30px" height = "30px" title = "Download/Open"/></a>'+" "
				res += [(fileS+" "+el, fSize(os.path.getsize(t)))]
		   	else:
				fileS = '<img src ="/static/file.jpeg" width = "30px" height = "30px"/>'
				res += [(fileS+" "+el, fSize(os.path.getsize(t)))]
		elif os.path.isdir(t):
			DIR = '<a href ='+'"'+el+'/">'+'<img src ="/static/dir.jpeg" width = "30px" height = "30px" title="Open"/></a>'
			res += [(DIR+" "+el, "&nbsp;")]
	return sorted(res, key = lambda r: r[0].lower())

def replaceListing(template, pair):
	result = ""
	for el in template:
		if "#$$$fn$$$#" in el:
			result += el.replace("#$$$fn$$$#", pair[0])
		elif "#$$$fs$$$#" in el:
			result += el.replace("#$$$fs$$$#", pair[1])
		else:
			result += el
	return result

def templ(lst, secL):
	res = ""	
	for el in lst:
	 	res += replaceListing(secL,el)
	return res
def execute(path,mainTemp,secTemp):	
	mainHtml = None
	secHtml = None
	res = ""
	try:
		if not os.path.exists(path):
			return "The path does not exist"
	except OSError:
		return "Access denied"
	try:	
		mainHtml = open(str(mainTemp), "r")
	except IOError:
		return "Cannot open file: " + mainTemp
	try:
		secHtml  = open(str(secTemp), "r")
	except IOError:
		 return "Cannot open file: " + secTemp
	mainL = mainHtml.read()
	mainHtml.close()
	secL = secHtml.readlines()
	mainHtml.close()
	try:
		dirL = listing(path)
	except OSError:
		return "Acces denied"
	tag = "#$$$dir$$$#"
	if tag in mainL:
		mainL = mainL.replace(tag, path[len(settings.Velly_Root):])
	tag = "#$$$list$$$#"
	if tag in mainL:
		mainL = mainL.replace(tag, templ(dirL,secL))
	tag = "#$$$back$$$#"
	if tag in mainL:
		if len(path) <= len(settings.Velly_Root)+1:
			mainL = mainL.replace(tag, '<a href = "/"><img src = "/static/back-icon.png" width = "30px" height = "30px" title="Back"/></a>')
		else:
			b = path[len(settings.Velly_Root):]
			i = 0
			if b[-1] == "/":
				i = -2
			else: i = -1
			while b[i]!="/":
				i -= 1			
			backTag = '<a href = "/dir'+b[:i+1]+'"><img src = "/static/back-icon.png" width = "30px" height = "30px" title ="Back"/></a>'
			mainL = mainL.replace(tag, backTag)		
	
	for el in mainL:
		res += el
	return res			
				
