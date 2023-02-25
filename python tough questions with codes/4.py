'''
A team has maximum 7 members. They have to fill a form indicating their name and age in the
format of name:age. The data collector task is convert all the team members given data to list and
give it as input to network admin. The Network admin will perform modifications in the given list
based on the following conditions. (Dictionary)
• If anyone shares same age, their names are merged together as single name and their ages
should be cube rooted.
• If anyone shares same name, their ages should be merged together and the duplicate names are
to be removed.
• If any of the input is in wrong format (say age:name instead of name:age), that should be
verified and modified in the correct format (name: age)
'''

def modify(x):
    l=[]
    for i in list(x):
        if i not in list(x):
            continue
        x.remove(i)
        d={}
        key=str(list(i.keys())[0])
        value=i[str(list(i.keys())[0])]
        for j in list(x):
            if list(i.values())[0]==list(j.values())[0]:
                key+=str(list(j.keys())[0])
                value=int(value**(1/3))
                x.remove(j)
            elif list(i.keys())[0]==list(j.keys())[0]:
                value=int(str(value)+str(list(j.values())[0]))
                x.remove(j)
        d[key]=value
        l.append(d)
    print(l)

inp=eval(input())
for i in inp:
    if type(i[list(i.keys())[0]])==str:
        i[list(i.values())[0]]=list(i.keys())[0]
        i.pop(list(i.keys())[0])
if len(inp)>7:
    print('Invalid')
else:
    modify(inp)