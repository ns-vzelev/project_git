var ids = 0;
var list = new Array();
var noch = new Array();

function addLi()
{
	var r = "";
	do
	r = prompt("Type name");
	while(r=="")
	if(r != null)
	{
		list[ids] = addTxt(r);
		ids++;
	}
	return printLi();
}
function addButton(val,oncl,id)
{
	return "<input id =\""+id+"\" type = \"button\" value =\""+val+"\" onclick = \""+oncl+"\" />";
}
function delLi(i)
{
	list[i] = null;
	return printLi();
}
function printLi()
{
	var i = 0;
	var t = "";
	for(i=0;i<=ids;i++)
	{
		if(list[i] != null)
		t+="<p>"+"<div class= \"nums\" id =\"num"+i+"\">"+list[i]+addButton("Delete","delLi("+i+")","b2")+addButton("Edit","edLi("+i+")","b1")+"</div>"+" </p>";
	}
	document.getElementById("ul1").innerHTML = t;
	return t;
}

function addTxt(val)
{
	return val
}
function addInput(i)
{
	return "<input type=\"text\" id=\"input1\" onChange=\" change(this.value,"+i+")\" onkeypress = \"nochange("+i+",event)\" value ='"+list[i]+"'></input>"
}
function edLi(i)
{
	noch[i] = list[i];
	list[i] = addInput(i);
	printLi();
}
function change(val,i)
{
	list[i] = val;
	printLi();
}
function nochange(i,e)
{
if(e.keyCode == 27)
{
list[i] = noch[i];
printLi();	
}
}
