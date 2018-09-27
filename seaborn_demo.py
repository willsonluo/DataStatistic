
# coding: utf-8

# In[1]:


import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()       
sns.pairplot(iris, hue='species', height=1.5);


# In[3]:


X_iris = iris.drop('species', axis=1)
X_iris.shape


# In[4]:


y_iris = iris['species']       
y_iris.shape


# In[6]:


from sklearn.model_selection import  train_test_split


# In[7]:


Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,random_state=1)


# In[8]:


from sklearn.naive_bayes import GaussianNB 
# 1.选择模型类        
model = GaussianNB()                       
# 2.初始化模型        
model.fit(Xtrain, ytrain)                  
# 3.用模型拟合数据        
y_model = model.predict(Xtest)             
# 4.对新数据进行预测


# In[9]:


from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

