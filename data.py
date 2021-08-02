#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import json
import pandas as pd

new_url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(new_url,headers=headers)
#page = requests.get(new_url,headers=headers).jason()
page = json.loads(page.text)
#requests.get(url).json()


# In[5]:


expiry_dt= '28-Jan-2021'
ce_values = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
pe_values = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
ce_dt = pd.DataFrame(ce_values).sort_values(['strikePrice'])
pe_dt = pd.DataFrame(pe_values).sort_values(['strikePrice'])


# In[6]:


expiry_dt= '04-Feb-2021'
ce_values1 = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
pe_values1 = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
ce_dt1 = pd.DataFrame(ce_values1).sort_values(['strikePrice'])
pe_dt1 = pd.DataFrame(pe_values1).sort_values(['strikePrice'])


# In[7]:


expiry_dt= '11-Feb-2021'
ce_values2 = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
pe_values2 = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
ce_dt2 = pd.DataFrame(ce_values2).sort_values(['strikePrice'])
pe_dt2 = pd.DataFrame(pe_values2).sort_values(['strikePrice'])


# In[8]:


expiry_dt= '18-Feb-2021'
ce_values3 = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
pe_values3 = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
ce_dt3 = pd.DataFrame(ce_values3).sort_values(['strikePrice'])
pe_dt3 = pd.DataFrame(pe_values3).sort_values(['strikePrice'])


# In[9]:


expiry_dt= '25-Feb-2021'
ce_values4 = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
pe_values4 = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
ce_dt4 = pd.DataFrame(ce_values4).sort_values(['strikePrice'])
pe_dt4 = pd.DataFrame(pe_values4).sort_values(['strikePrice'])


# In[10]:


expiry_dt= '25-Mar-2021'
ce_values5 = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
pe_values5 = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
ce_dt5 = pd.DataFrame(ce_values5).sort_values(['strikePrice'])
pe_dt5 = pd.DataFrame(pe_values5).sort_values(['strikePrice'])


# In[11]:


n =2
N1=[]
K = [ce_dt,ce_dt1,ce_dt2,ce_dt3,ce_dt4,ce_dt5 ]
for m in range (0,6):
    for i in range (len(K[m])):
        for k in range(m+1,6):
            for j in range(len(K[k])):
                if K[m]["strikePrice"][i] == K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < n  and K[k]["askPrice"][j] >0:
                    x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                      K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                    N1.append(x)


# In[12]:


n =0.1
N5=[]
K = [ce_dt,ce_dt1,ce_dt2,ce_dt3,ce_dt4,ce_dt5 ]
for m in range (0,6):
    for i in range (len(K[m])):
        for k in range(m,6):
            for j in range(len(K[k])):
                if K[m]["strikePrice"][i] > K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < n  and K[k]["askPrice"][j] >0:
                    x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                      K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                    N5.append(x)


# In[13]:


n =2
N3=[]
K = [pe_dt, pe_dt1,pe_dt2,pe_dt3,pe_dt4,pe_dt5]
for m in range (0,6):
    for i in range (len(K[m])):
        for k in range(m+1,6):
            for j in range(len(K[k])):
                if K[m]["strikePrice"][i] == K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < n  and K[k]["askPrice"][j] >0:
                    x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                      K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                    N3.append(x)
      


# In[14]:


n =0.1
N7=[]
K = [pe_dt, pe_dt1,pe_dt2,pe_dt3,pe_dt4,pe_dt5]
for m in range (0,6):
    for i in range (len(K[m])):
        for k in range(m,6):
            for j in range(len(K[k])):
                if K[m]["strikePrice"][i] < K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < n  and K[k]["askPrice"][j] >0:
                    x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                      K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                    N7.append(x)


# In[48]:


def data(N1,N3,N5,N7):
    N2 = pd.DataFrame(data=N1, columns= ("strike1_ce", "strike2_ce","expry1", "expry2","ce1", "ce2"))
    N2["diffrence"] = N2["ce2"]-N2["ce1"]
    N2 = N2.sort_values(by=["diffrence"], ascending=True)
    N4 = pd.DataFrame(data=N3, columns= ("strike_pe", "strike_pe","expry1", "expry2","pe1", "pe2"))
    N4["diffrence"] = N4["pe2"]-N4["pe1"]
    N4 = N4.sort_values(by=["diffrence"], ascending=True)
    print('Call Calender Spread: ')
    print('Put Calender Spread: ')
    return N2 


# In[49]:


data(N1,N3,N5,N7)


# In[16]:


N4 = pd.DataFrame(data=N3, columns= ("strike_pe", "strike_pe","expry1", "expry2","pe1", "pe2"))
N4["diffrence"] = N4["pe2"]-N4["pe1"]
N4 = N4.sort_values(by=["diffrence"], ascending=True)
print('Put Calender Spread: ')
N4


# In[17]:


N6 = pd.DataFrame(data=N5, columns= ("strike1_ce", "strike2_ce","expry1", "expry2","ce1", "ce2"))
N6["diffrence"] = N6["ce2"]-N6["ce1"]
N6 = N6.sort_values(by=["diffrence"], ascending=True)
print('Verticle Call Spread: ')
N6


# In[18]:


N8 = pd.DataFrame(data=N7, columns= ("strike_pe", "strike_pe","expry1", "expry2","pe1", "pe2"))
N8["diffrence"] = N8["pe2"]-N8["pe1"]
N8 = N8.sort_values(by=["diffrence"], ascending=True)
print('Verticle Put Spread: ')
N8


# 
