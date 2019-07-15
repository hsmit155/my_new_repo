#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
df.head()


# In[6]:


df.head(10)


# In[7]:


df.tail(4)


# In[8]:


df.shape


# In[9]:


df.size


# In[10]:


len(df)


# In[11]:


df.columns


# In[12]:


df['Hired']


# In[13]:


df['Hired'][:5]


# In[14]:


df['Hired'][5]


# In[15]:


df[['Years Experience', 'Hired']]


# In[16]:


df[['Years Experience', 'Hired']][:5]


# In[17]:


df.sort_values(['Years Experience'])


# In[18]:


degree_counts = df['Level of Education'].value_counts()
degree_counts


# In[19]:


degree_counts.plot(kind='bar')


# In[20]:


import numpy as np
import pandas as pd


# In[21]:


labels = ['a', 'b', 'c',]
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b':20, 'c':30}


# In[22]:


pd.Series(data=my_list)


# In[23]:


pd.Series(data=my_list, index=labels)


# In[24]:


pd.Series(my_list,labels)


# In[25]:


pd.Series(arr)


# In[26]:


pd.Series(arr, labels)


# In[27]:


pd.Series(d)


# In[31]:


pd.Series(data=labels)


# In[32]:


pd.Series([sum,print,len])


# In[34]:


ser1 = pd.Series([1,2,3,4,],index=['USA', 'Germany', 'USSR', 'Japan'])


# In[35]:


ser1


# In[36]:


ser2 = pd.Series([1,2,5,4], index = ['USA', 'Germany', 'Italy', 'Japan'])


# In[37]:


ser2


# In[38]:


ser1['USA']


# In[39]:


ser1 + ser2


# In[40]:


import pandas as pd
import numpy as np


# In[41]:


from numpy.random import randn
np.random.seed(101)


# In[42]:


df = pd.DataFrame(randn(5,4,), index='A B C D E'.split(), columns='W X Y Z'.split())


# In[43]:


df


# In[44]:


df['W']


# In[45]:


df[['W', 'Z']]


# In[46]:


df.W


# In[47]:


type(df['W'])


# In[48]:


df['new'] = df['W'] + df['Y']


# In[49]:


df


# In[50]:


df.drop('new', axis=1)


# In[51]:


df


# In[53]:


df.drop('new', axis=1, inplace=True)


# In[54]:


df


# In[55]:


df.drop('E', axis=0)


# In[56]:


df.drop('E', axis=0)


# In[57]:


df.loc['A']


# In[58]:


df.iloc[2]


# In[59]:


df.loc['B','Y']


# In[60]:


df.loc['B', 'Y']


# In[61]:


df.loc[['A', 'B'],['W','Y']]


# In[62]:


df


# In[63]:


df>0


# In[64]:


df[df>0]


# In[65]:


df[df['W']>0]


# In[66]:


df[df['W']>0]['Y']


# In[68]:


df[df['W']>0][['Y','X']]


# In[69]:


df[(df['W']>0) & (df['Y'] > 1)]


# In[70]:


df


# In[71]:


df.reset_index()


# In[72]:


newind = 'CA NY WY OR CO'.split()


# In[73]:


df['States'] = newind


# In[74]:


df


# In[75]:


df.set_index('States')


# In[76]:


df.set_index('States',inplace=True)


# In[77]:


df


# In[78]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[79]:


hier_index


# In[80]:


df = pd.DataFrame(np.random.randn(6,2), index=hier_index,columns=['A','B'])
df


# In[81]:


df.loc['G1']


# In[82]:


df.loc['G1'].loc[1]


# In[83]:


df.index.names


# In[84]:


df.index.names = ['Group', 'Num']


# In[85]:


df


# In[86]:


df.xs('G1')


# In[87]:


df.xs(1,level='Num')


# In[88]:


import numpy as np
import pandas as pd


# In[89]:


df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]}) 


# In[90]:


df


# In[91]:


df.dropna()


# In[92]:


df.dropna(axis=1)


# In[93]:


df.dropna(thresh=2)


# In[94]:


df.fillna(value='FILL VALUE')


# In[97]:


df['A'].fillna(value=df['A'].mean())


# In[98]:


import pandas as pd
# Create dataframe
data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
       'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[99]:


df = pd.DataFrame(data)


# In[100]:


df


# In[101]:


df.groupby('Company')


# In[102]:


by_comp = df.groupby("Company")


# In[103]:


by_comp.mean()


# In[104]:


by_comp.std()


# In[105]:


by_comp.min()


# In[106]:


by_comp.max()


# In[107]:


by_comp.count()


# In[108]:


by_comp.describe()


# In[109]:


by_comp.describe().transpose()


# In[110]:


by_comp.describe().transpose()['GOOG']


# In[111]:


import pandas as pd


# In[113]:


df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
                   'B':['B0', 'B1', 'B2', 'B3'],
                   'C':['C0', 'C1', 'C2', 'C3'],
                   'D':['D0', 'D1', 'D2', 'D3']},
                   index=[0,1,2,3])


# In[114]:


df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'],
                   'B':['B4', 'B5', 'B6', 'B7'],
                   'C':['C4', 'C5', 'C6', 'C7'],
                   'D':['D4', 'D5', 'D6', 'D7']},
                   index=[4,5,6,7])


# In[120]:


df3 = pd.DataFrame({'A':['A8', 'A9', 'A10', 'A11'],
                   'B':['B8', 'B9', 'B10', 'B11'],
                   'C':['C8', 'C9', 'C10', 'C11'],
                   'D':['D8', 'D9', 'D10', 'D11']},
                   index=[8,9,10,11])


# In[121]:


df1


# In[122]:


df2


# In[123]:


df3


# In[124]:


pd.concat([df1,df2,df3])


# In[125]:


pd.concat([df1,df2,df3],axis=1)


# In[126]:


left = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                     'C':['C0', 'C1', 'C2', 'C3'],
                     'D':['D0', 'D1', 'D2', 'D3']})


# In[127]:


left


# In[128]:


right


# In[129]:


pd.merge(left, right, how='inner', on='key')


# In[132]:


left = pd.DataFrame({'key1':['K0', 'K0', 'K1', 'K2'],
                    'key2':['K0', 'K1', 'K0', 'K1'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0', 'K1', 'K1', 'K2'],
                    'key2':['K0', 'K0', 'K0', 'K0'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})


# In[133]:


pd.merge(left,right,on=['key1','key2'])


# In[134]:


pd.merge(left, right, how='outer', on=['key1', 'key2'])


# In[135]:


pd.merge(left,right, how='right', on=['key1','key2'])


# In[136]:


pd.merge(left,right,how='left', on=['key1', 'key2'])


# In[138]:


left = pd.DataFrame({'A':['A0', 'A1', 'A2'],
                    'B':['B0', 'B1', 'B2']},
                   index=['K0','K1','K2'])

right = pd.DataFrame({'C':['C0', 'C2', 'C3'],
                    'D':['B0', 'D2', 'D3']},
                   index=['K0','K2','K3'])


# In[139]:


left.join(right)


# In[140]:


left.join(right, how='outer')


# In[142]:


import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4], 'col12':[444,555,666,444],'col13':['abc','def','ghi','xyz']})
df.head()


# In[143]:


df['col12'].unique()


# In[145]:


df['col12'].nunique()


# In[147]:


df['col12'].value_counts()


# In[148]:


#Select from DataFrame using Criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col12']==444)]


# In[149]:


newdf


# In[150]:


def times2(x):
    return x*2


# In[151]:


df['col1'].apply(times2)


# In[152]:


df['col13'].apply(len)


# In[153]:


df['col1'].sum()


# In[154]:


del df['col1']


# In[155]:


df


# In[156]:


df.columns


# In[157]:


df.index


# In[158]:


df


# In[159]:


df.sort_values(by='col12')


# In[160]:


df.isnull()


# In[161]:


df.dropna()


# In[162]:


import numpy as np


# In[163]:


df = pd.DataFrame({'col11':[1,2,3,np.nan],
                  'col12':[np.nan,555,666,444],
                  'col13':['abc','def','ghi','xyz']})
df.head()


# In[164]:


df.isnull()


# In[165]:


df.dropna()


# In[166]:


df.fillna('FILL')


# In[168]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
    'B':['one','one','two','two','one','one'],
    'C':['x','y','x','y','x','y'],
    'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


# In[169]:


df


# In[170]:


df.pivot_table(values='D', index=['A','B'], columns=['C'])


# In[171]:


import numpy as np
import pandas as pd


# In[174]:


df = pd.read_csv('example.csv')
df


# In[175]:


df.to_csv('example.csv', index=False)


# In[177]:


pd.read_excel('Excel_Sample.xlsx', sheetname='Sheet1')


# In[178]:


df.to_excel('Excel_Sample.xlsx', sheet_name='Sheet1')


# In[179]:


from sqlalchemy import create_engine


# In[185]:


engine = create_engine('sqlite:///:memory:')


# In[186]:


df.to_sql('data', engine)


# In[187]:


sql_df = pd.read_sql('data',con=engine)


# In[188]:


sql_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




