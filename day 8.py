Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#DICTIONARY
data={'name':'sk','bloodgroup': "b+",'age':40}
data
{'name': 'sk', 'bloodgroup': 'b+', 'age': 40}
data.fromkeys(name)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data.fromkeys(name)
NameError: name 'name' is not defined
data.fromkeys('name')
{'n': None, 'a': None, 'm': None, 'e': None}
for i in range(5)
SyntaxError: incomplete input
for in in range(5):
    
SyntaxError: invalid syntax
for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
for i in range(10,0,-1):
    print(i,end=' ')

    
10 9 8 7 6 5 4 3 2 1 
for i in range(10,0,-2):
    print(i,end=' ')

    
10 8 6 4 2 
for i in range(10,0,-1):
    print(i,end=' ')

    
10 9 8 7 6 5 4 3 2 1 
for i in range(10,-1,-1):
    print(i,end=' ')

    
10 9 8 7 6 5 4 3 2 1 0 

#While Loop
a=5
while a>0:
    print(a)
    a-=1

    
5
4
3
2
1
while a>0:
    print(a)
    a-=2

    

a
0
dict={'brand':'car','model':'punch','cost':2026}
print(dict)
{'brand': 'car', 'model': 'punch', 'cost': 2026}
print(dict['model'])
punch
dict={'brand':'car','model':'punch','cost':2026,'cost':2001}
print(dict)
{'brand': 'car', 'model': 'punch', 'cost': 2001}
print(len(dict))
3
dict={'brand':'car','model':'punch','cost':2001,'colours':['red','white','blue']}
print(dict)
{'brand': 'car', 'model': 'punch', 'cost': 2001, 'colours': ['red', 'white', 'blue']}
print(type(dict))
<class 'dict'>
dict=dict{'brand':'car','model':'punch','cost':2001,'colours':['red','white','blue']}
SyntaxError: invalid syntax
dict={'brand':'car','model':'punch','cost':2026}
dict
SyntaxError: multiple statements found while compiling a single statement
print(dict)
{'brand': 'car', 'model': 'punch', 'cost': 2001, 'colours': ['red', 'white', 'blue']}
x=dict['model']
print(dict)
{'brand': 'car', 'model': 'punch', 'cost': 2001, 'colours': ['red', 'white', 'blue']}
print(x)
punch
x=dict.get('model')
print(x)
punch
x=dict.keys()
print(x)
dict_keys(['brand', 'model', 'cost', 'colours'])
x=dict('values')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x=dict('values')
TypeError: 'dict' object is not callable
x=dict.values()
print(x)
dict_values(['car', 'punch', 2001, ['red', 'white', 'blue']])
car={'brand': 'car', 'model': 'punch', 'cost': 2001}
x=car.values()
print(x)
dict_values(['car', 'punch', 2001])
car['color']='blue'
print(x)
dict_values(['car', 'punch', 2001, 'blue'])
x=car.items()
print(x)
dict_items([('brand', 'car'), ('model', 'punch'), ('cost', 2001), ('color', 'blue')])
if 'model' in dict:
    print("yes,'model' in keys)
          
SyntaxError: incomplete input
if 'model' in dict:
          print("YES,'model' in keys")

          
YES,'model' in keys
dict['model']=atar
          
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dict['model']=atar
NameError: name 'atar' is not defined. Did you mean: 'aiter'?
dict['model']="Nexon"
          
print(dict)
          
{'brand': 'car', 'model': 'Nexon', 'cost': 2001, 'colours': ['red', 'white', 'blue']}
dict['year']=2006
          
print(dict)
          
{'brand': 'car', 'model': 'Nexon', 'cost': 2001, 'colours': ['red', 'white', 'blue'], 'year': 2006}
dict.update({'me':'Menu'})
          
print(dict)
          
{'brand': 'car', 'model': 'Nexon', 'cost': 2001, 'colours': ['red', 'white', 'blue'], 'year': 2006, 'me': 'Menu'}
dict.pop('me')
          
'Menu'
print(dict)
          
{'brand': 'car', 'model': 'Nexon', 'cost': 2001, 'colours': ['red', 'white', 'blue'], 'year': 2006}
dict.popitem()
          
('year', 2006)
print(dict)
          
{'brand': 'car', 'model': 'Nexon', 'cost': 2001, 'colours': ['red', 'white', 'blue']}
del dict("model")
          
SyntaxError: incomplete input
del dict['model']
          
print(dict)
          
{'brand': 'car', 'cost': 2001, 'colours': ['red', 'white', 'blue']}
dict.clear()
          
print(dict)
          
{}
for x in dict:
    print(x)

          

dict
          
{}
dict={'brand': 'car', 'model': 'Nexon', 'cost': 2001}
          
dict
          
{'brand': 'car', 'model': 'Nexon', 'cost': 2001}
for x in dict:
          print(x)

          
brand
model
cost
for x in dict:
          print(dict[x])

          
car
Nexon
2001
for x in dict.values():
          print(x)

          
car
Nexon
2001
for x in dict.keys():
          print(keys)

          
Traceback (most recent call last):
  File "<pyshell#106>", line 2, in <module>
    print(keys)
NameError: name 'keys' is not defined
>>> for x in dict.keys():
...           print(x)
... 
...           
brand
model
cost
>>> for x,y in dict.items():
...           print(x,y)
... 
...           
brand car
model Nexon
cost 2001
>>> mydict=dict.copy()
...           
>>> print(dict)
...           
{'brand': 'car', 'model': 'Nexon', 'cost': 2001}
>>> print(mydict)
...           
{'brand': 'car', 'model': 'Nexon', 'cost': 2001}
>>> mydict=thisdict(dict)
...           
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    mydict=thisdict(dict)
NameError: name 'thisdict' is not defined
>>> thisdict=mydict(dict)
...           
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    thisdict=mydict(dict)
TypeError: 'dict' object is not callable
>>> thisdict=dict(mydict)
...           
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    thisdict=dict(mydict)
TypeError: 'dict' object is not callable
