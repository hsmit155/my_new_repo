#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Hello World")


# In[3]:


1+1


# In[5]:


# Variable Assignment - cannot start with number or special characters
num_of_var = 2


# In[6]:


x = 2
y = 3


# In[7]:


z = x + y


# In[8]:


z


# In[9]:


'single quotes'


# In[10]:


"double quotes"


# In[11]:


"wrap lot's of other quotes"


# In[12]:


x = 'hello'


# In[13]:


x


# In[14]:


print(x)


# In[15]:


num = 12
name = 'Sam'


# In[16]:


print('My number is {one}, and my name is {two}'.format(one = num, two = name)


# In[21]:


print('My number is {one}, and my name is {two}'.format(one=num, two=name))


# In[23]:


print('My number is {}, and my name is {}'.format(num, name))


# In[24]:


[1 ,2, 3]


# In[25]:


['hi', 1, [1, 2]]


# In[26]:


my_list = ['a', 'b', 'c']


# In[29]:


my_list.append('d')


# In[31]:


my_list.remove('d')


# In[32]:


my_list


# In[33]:


my_list[0]


# In[34]:


my_list[1:]


# In[35]:


my_list[:1]


# In[36]:


my_list[0] = 'NEW'


# In[37]:


my_list


# In[38]:


nest = [1, 2, 3, [4, 5,['target']]]


# In[39]:


nest[3]


# In[40]:


nest[3][2]


# In[42]:


nest[3][2][0]


# In[43]:


nest[3][2]


# In[44]:


d = {'key1': 'item1', 'key2': 'item2'}


# In[45]:


d


# In[46]:


d['key1']


# In[47]:


True


# In[48]:


False


# In[49]:


t=(1,2,3)


# In[50]:


t[0]


# In[51]:


t[0]='NEW'


# In[52]:


{1, 2, 3}


# In[53]:


{1,2,3,1,2,1,2,1,1,3,3,3,3,3,3,3,3,2,1,2}


# In[54]:


1 > 2


# In[55]:


1 < 2


# In[56]:


1>=2


# In[57]:


1>=1


# In[58]:


1<=4


# In[59]:


1==1


# In[60]:


'hi' == 'bye'


# In[61]:


(1 > 2) and (2 <3)


# In[62]:


(1 < 2) and (2 < 3)


# In[63]:


(1 == 2) or (2 == 3) or (4 == 4)


# In[64]:


if 1 < 2:
    print('Yep!')


# In[1]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[2]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('last')


# In[3]:


seq = [1,2,3,4,5]


# In[4]:


for item in seq:
    print(item)


# In[5]:


for item in seq:
    print('yep')


# In[6]:


for jelly in seq:
    print(jelly+jelly)


# In[8]:


i = 1
while i < 5:
    print('i is:{}'.format(i))
    i = i+1


# In[9]:


range(5)


# In[10]:


for i in range(5):
    print(i)


# In[11]:


list(range(5))


# In[12]:


x = [1,2,3,4]


# In[13]:


out = []
for item in x:
    out.append(item**2)
print(out)


# In[14]:


[item**2 for item in x]


# In[15]:


def my_func(param='default'):
    """
    Docstring goes here.
    """
    print(param)


# In[16]:


my_func


# In[17]:


my_func()


# In[18]:


my_func('new param')


# In[19]:


def square(x):
    return x**2


# In[20]:


out = squre(2)


# In[21]:


print(out)


# In[22]:


def squre(x):
    return x**2


# In[23]:


out = square(2)


# In[24]:


print(out)


# In[25]:


def times2(var):
    return var*2


# In[26]:


times2(2)


# In[27]:


lamda var: var*2


# In[28]:


lambda var: var*2


# In[29]:


seq = [1,2,3,4,5]


# In[30]:


def times2(var):
    return var*2


# In[31]:


map(times2,seq)


# In[32]:


list(map(times2,seq))


# In[33]:


filter(lambda item: item%2 == 0, seq)


# In[36]:


list(filter(lambda item: item%2 == 0, seq))


# In[37]:


st = 'hello my name is Sam'


# In[38]:


st.lower()


# In[39]:


st.upper()


# In[40]:


st.split()


# In[42]:


tweet = 'Go Sports! #Sports'


# In[43]:


tweet.split('#')


# In[44]:


tweet.split('#')[1]


# In[46]:


d = {'key1':'item1', 'key2': 'item2'}


# In[47]:


d


# In[48]:


d.keys()


# In[49]:


d.items()


# In[50]:


lst = [1,2,3]


# In[51]:


lst.pop()


# In[52]:


lst.pop()


# In[53]:


lst


# In[54]:


'x' is [1,2,3]


# In[55]:


'x' in ['x', 'y', 'z']


# In[56]:


7**4


# In[57]:


eq = 7**4


# In[58]:


eq


# In[59]:


s = "Hi there Sam!"


# In[60]:


s.split()


# In[61]:


planet = "Earth"
diameter = 12742


# In[62]:


print("The diameter of the {} is {} kilometers".format(planet, diameter))


# In[65]:


lst = [1,2[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[72]:


lst = [1,2[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[73]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[81]:


d


# In[82]:


print(d)


# In[106]:


print(d['tricky'][3])


# In[107]:


d


# In[108]:


print(d)


# In[110]:


print(d['k1'][3])


# In[113]:


d


# In[141]:


email = 'user@domain.com'

def domainGet():
    print(email)


# In[142]:


domainGet()


# In[ ]:




