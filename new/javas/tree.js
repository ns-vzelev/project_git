var mainArr = new Array();
function file(name,size)
{
	this.name = name;
	this.size = size;
}
function dir(name, list, isOpen)
{
	this.name = name;
	this.list = list;
	this.isOpen = isOpen;
}
function createTree()
{
	var i;
	for(i = 0;i<3;i++)
	mainArr[i] = new file("hello"+i,5*i);
	for( ;i<6; i++)
	mainArr[i] = new dir("Dirrr"+i,new Array(),false);
	for(i = 0; i<4; i+=2)
	{
		mainArr[3].list[i] = new dir("D"+i,new Array(),false);
		mainArr[3].list[i+1] = new file("min4o"+i,5+i);
 	}
 	mainArr[4].list[0] = new dir("Papka",new Array(),false);
 	mainArr[4].list[1] = new dir("Paa",new Array(),false);
 	mainArr[4].list[2] = new dir("Paaaa",new Array(),false);
    mainArr[5].list[0] = new file("hipe",89);
    mainArr[5].list[1] = new file("pio",90);
    mainArr[4].list[0].list[0] = new file("wtf",10000);
}

function printTree(root,shift,r)
{
	if(root == null|| root.hasOwnProperty("size"))
	return "";
	var res = "";
	var temp = "";
	var i = 0;
	for(i = 0;i<shift; i++)
	 temp+="&nbsp;";
	i = 0;
	while(root[i]!=null)
	{
		if(root[i].hasOwnProperty("size"))
		{
			res += "<p>"+temp+root[i].name+"&nbsp;"+root[i].size+"</p>";
		}
		else if(root[i].hasOwnProperty("list"))
		{
			res += "<p>"+temp+addButton(root[i].isOpen? "-":"+",r+"["+i+"]")+"&nbsp;"+root[i].name+"</p>";
			if(root[i].isOpen)
			{
		     res += printTree(root[i].list,shift+8,r+"["+i+"]"+".list");
		    }
		}
		i++;
	}
	return res;
}
function addButton(val,ob)
{
return "<input class = 'sm' type = \"button\" value =\""+val+"\" onclick = 'op("+ob+")'></input>";
}
function printT(res)
{
	document.getElementById("tree").innerHTML = res;
}
function op(ob)
{
	ob.isOpen = ob.isOpen? false:true;
	printT(printTree(mainArr,0,"mainArr"));
}

function exe()
{
	createTree();
	printT(printTree(mainArr,0,"mainArr"));
}
