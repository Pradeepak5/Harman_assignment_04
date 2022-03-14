list1=[3.14, 66, "Teddy Bear", True, [], {}]
def checkType(list1):
    for element in list1:
        if isinstance(element,int):
            print("Integer")
        if isinstance(element,str):
            print("String")
        if isinstance(element,float):
            print("Float")
        if isinstance(element,bool):
            print("Boolean")
        if isinstance(element,list):
            print("List")
        if isinstance(element,dict):
            print("Dictionary")

checkType(list1)
list2=[]
for i in list1:
    list2.append(type(i))
print(list2)




