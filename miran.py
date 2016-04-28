import time;
import codecs;
import zipfile;
txtN = input("Please tell me the name of your file(.txt only, include .txt): ") #file name
text = open(txtN, "r").read();
print (text);
txtN=txtN[:-4];
#required
if ":t:" in text:
    text = str(text);
    text = text.replace(":t:","<h3>",1);
    text = text.replace(":t:","</h3>",1);

while ":p:" in text:
    text = str(text);
    text = text.replace(":p:","<p>",1);
    text = text.replace(":p:","</p>",1);
#required

#optional
if ":d:" in text:
    text = text.replace(":d:", "Date:"+time.strftime("%d/%m/%y"));

while ":b:" in text:
    text = str(text);
    text = text.replace(":b:","<b>",1);
    text = text.replace(":b:","</b>",1);

while ":i:" in text:
    text = str(text);
    text = text.replace(":i:","<i>",1);
    text = text.replace(":i:","</i>",1);
#Add-ons


#Add-ons close
temp = codecs.open("template.html","r").read();
print(temp);

#buidling the site
if "<miran/>" in temp:
    tem = str(temp).replace("<miran/>",text);
    open(txtN +".html","w").write(tem);
i = text.splitlines();
o = open("index.html","r").read()
open("index.html","w").write(o +"<a href=\""+txtN+".html\">"+i[0]+"</a>" + "<p>Date:"+time.strftime("%d/%m/%y")+"</p>");
print("");
print ("Finished.");
