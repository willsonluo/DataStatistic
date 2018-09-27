
# coding: utf-8

# **产生1个正态分布的随机数据**

# In[12]:


import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(42) # 此命令将会产生一个随机状态种子,在该状态下生成的随机序列（正态分布）一定会有相同的模式。
                                # 但是，不同的随机种子状态将会有不同的数据生成模式。这一特点在随机数据生成的统计格式控制显得很重要。 
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y);


# **导入线性回归模块**

# In[2]:


from sklearn.linear_model import LinearRegression


# **实例化LinearRegression类并用fit_intercept超参数设置是否想要拟合直线的截距**

# In[3]:


model = LinearRegression(fit_intercept=True)
model


# **将数据整理成特征矩阵和目标数组,np.newaxis:为 numpy.ndarray（多维数组）增加一个轴**

# In[4]:


X = x[:, np.newaxis]
X.shape


# **用模型拟合数据**

# In[5]:


model.fit(X, y)


# **fit()命令会在模型内部进行大量运算，运算结果将存储在模型属性中，供用户使用。
# 在Scikit-Learn中，所有通过fit()方法获得的模型参数都带一条下划线。**

# In[6]:


model.coef_   ## 对样本数据拟合直线的斜率


# In[7]:


model.intercept_    ## 对样本数据拟合直线的截距


# **预测新数据的标签**

# In[8]:


xfit = np.linspace(-1, 11)


# In[9]:


xfit


# **将这些x值转换成[n_samples, n_fea-tures]的特征矩阵形式，之后将其输入到模型中**

# In[10]:


Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)


# **把原始数据和拟合结果都可视化出来**

# In[11]:


plt.scatter(x, y)
plt.plot(xfit, yfit);

