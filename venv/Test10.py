import re
import xml.etree.ElementTree
a='Happy Happy Birthday'
result=re.search('^Happy.*Birthday$',a)

print(result)


root=xml.etree.ElementTree.fromstring("""    <bookstore>  
      <book category="COOKING">  
        <title lang="en">Everyday Italian</title>  
        <author>Giada De Laurentiis</author>  
        <year>2005</year>  
        <price>30.00</price>  
      </book>  
      <book category="CHILDREN">  
        <title lang="en">Harry Potter</title>  
        <author>J K. Rowling</author>  
        <year>2005</year>  
        <price>29.99</price>  
      </book>  
      <book category="WEB">  
        <title lang="en">Learning XML</title>  
        <author>Erik T. Ray</author>  
        <year>2003</year>  
        <price>39.95</price>  
      </book>  
    </bookstore>   """)
print(root.tag)
for i in root:
    print(i.tag, i.attrib,)
for i in root.iter():
    print(i.tag)