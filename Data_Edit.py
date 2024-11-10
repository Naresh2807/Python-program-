str1 = [{'name': "NARESH",'class':'a' 'id': 1}, {'name': "NA",'class':'a' ,'id': 2}, {'name': "NAr",'class':'a' 'id': 3}, {'name': "NARE",'class':'a', 'id': 4}]
val = input("to edit//display: ")
if val == 'display':
    print(str1)
elif val == 'edit':
    val = input("name//class: ")
    if val == 'name':
        id1 = int(input("enter the id: "))
        for i in str1:
            if i['id'] == id1:
                name_chg = input("enter the new name: ")
                i['name'] = name_chg
                break  
    elif val == 'class':
        id1 = int(input("enter the id: "))
        for i in str1:
            if i['id'] == id1:
                name_chg =input("enter the new class: ")
                i['name']=name_chg
                break  
print(str1)
