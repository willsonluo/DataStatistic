
# coding: utf-8

# # 时间序列的演示

# In[1]:


import pandas as pd


# In[2]:


from datetime import datetime


# In[3]:


now = datetime.now()


# In[4]:


now


# In[5]:


now.year


# In[6]:


now.month


# In[7]:


now.hour


# In[8]:


delta = datetime(2017,1,18,11,1,20,110) - datetime(2017,1,18,11,1,10,110)
delta


# **如何获取timedelta的数据，日和秒，要复数**

# In[9]:


delta.days


# In[10]:


delta.seconds


# In[11]:


stamp = datetime(2018,11,11)


# **如何从时间格式变成String格式**

# In[12]:


str(stamp)


# **周的表示**

# In[13]:


stamp.strftime('%U')


# **万能时间识别**

# In[14]:


from dateutil.parser import parse
parse('2018/01/01 10:10:01')


# In[15]:


datetrs = ['2018/01/01','2017/01/02']
datetrs_2datetime = pd.to_datetime(datetrs)
datetrs_2datetime


# In[16]:


import numpy as np
ts = pd.Series(np.random.randn(2),index = datetrs_2datetime)


# **如何变成时间序列的dataframe**

# In[17]:


ts.index


# **直接输入日期也可以找到对应的值**

# In[18]:


ts['2018/01/01']


# In[19]:


ts


# **长时间序列的例子**

# In[20]:


longer_ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2011',periods=1000))


# In[21]:


longer_ts


# **时间切片**

# In[22]:


longer_ts['2013/01/01':]  ##longer_ts[datetime(2013,1,1):] 


# In[23]:


longer_ts['2013/01/01':'2013/02/01']


# In[24]:


longer_ts.truncate(after = '2013/01/01') ## 在日期以后就不要了


# **重复索引的处理办法**

# In[25]:


dates = ['2017/01/01','2017/01/02','2017/01/03','2017/01/02']
dup_ts = pd.Series(np.arange(4),index = dates)
dup_ts


# In[26]:


dup_ts.index.is_unique


# In[27]:


grouped = dup_ts.groupby(level=0) ## level=0，索引的唯一一层
grouped.mean()


# In[28]:


grouped.sum()


# In[29]:


grouped.count()


# In[30]:


ts


# **pd.date_range('4/1/2011','5/2/2011') or period生成日期范围**

# In[31]:


pd.date_range('4/1/2011','5/2/2011')  


# In[32]:


pd.date_range('4/1/2011',periods = 20)  


# In[33]:


pd.date_range('4/1/2011','5/2/2013',freq = 'BM')   ## BM = Business end of Month 每月最后一天


# In[34]:


pd.date_range('4/1/2011 12:00:01',periods = 20) 


# In[35]:


pd.date_range('4/1/2011 12:00:01',periods = 20, normalize=True)  ## 全部规范到0点了


# **freq频率和时间偏移**

# In[36]:


from pandas.tseries.offsets import Hour, Minute, Day, MonthEnd
import pandas as pd


# **需要参考时间序列的基础频率**

# In[37]:


pd.date_range('1/1/2011','1/1/2017',freq = '10d2h30min') ## 以10天2小时30分钟作为一个周期


# In[38]:


pd.date_range('1/1/2011','1/1/2017',freq = 'BM') ## BM是每个月最后一个工作日，M是每个月最后一天


# **WOM 日期 （Week Of Month)**

# In[39]:


ts = pd.Series(np.random.randn(10),index = pd.date_range('2018/01/01',periods=10, freq = 'M'))
ts


# **shift保持索引不变，数据移动（小心，整个datafram会被改变)**

# In[40]:


ts / ts.shift(2) ## 移动的是数据，时间序列没改变


# In[41]:


ts.shift(2,freq ='M') ## 移动的时间序列，数据没有少


# **rollfoware,rollback锚点偏移量**

# In[42]:


offset = MonthEnd(10)
offset


# In[43]:


now


# In[44]:


offset.rollforward(now)


# In[45]:


ts = pd.Series(np.random.randn(100),index=pd.date_range(start = '1/1/2017',periods=100,freq = "4d"))
ts


# In[46]:


ts.groupby(offset.rollforward).sum()


# In[47]:


ts.resample('M').mean() ## 可以使用resample，写法更简单


# **时区调整， pytz库**

# In[48]:


import pytz


# In[49]:


pytz.common_timezones[-6:]


# In[50]:


tz = pytz.timezone('US/Hawaii')
str(tz)


# **pandas画图**

# In[51]:


ts


# In[52]:


import matplotlib.pyplot as plt


# In[53]:


ts.plot()


# In[54]:


ts.loc['2017'].plot() ## 按照时间序列画图


# In[55]:


ts.loc['2017/1/1':'2017/10/1'].plot() ## 时间段画图，中间是:


# In[56]:


ts_q = ts['2017'].resample('Q-DEC').ffill()
ts_q


# In[57]:


ts_q.plot()

