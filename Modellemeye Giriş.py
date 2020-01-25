#!/usr/bin/env python
# coding: utf-8

# Onur
# # Modellemeye Giriş

# In[1]:


import pandas as pd


# Notlar

# ## Örnek Model Daisy Firması Wozac Ürünü

# In[23]:


V=2
P=300
T=150
A=0.4
B=0.3
C=0.1

z=300+0.8*V+0.01*P+0.06*T+0.001*T*P-0.01*T*T- .001*P*P+11.7*A+ 9.4*B+16.4*C+19*A*B+11.4*A*C-9.6*B*C

print("Kısıtları kontrol ediyoruz : ",V <= 5 ,
V >= 1,
P <= 400
,P >= 200
,T <= 200
,T >= 100
,A >= 0
,B >= 0
,C >= 0
,A + B + C == 1
,A <= 5 )

# Not feasible 

print("Amaç Değeri ",z)


# In[24]:


V=5
P=200
T=100
A=0.294
B=0
C=0.706

z=300+0.8*V+0.01*P+0.06*T+0.001*T*P-0.01*T*T- .001*P*P+11.7*A+ 9.4*B+16.4*C+19*A*B+11.4*A*C-9.6*B*C

print("Kısıtları kontrol ediyoruz : ",V <= 5 ,
V >= 1,
P <= 400
,P >= 200
,T <= 200
,T >= 100
,A >= 0
,B >= 0
,C >= 0
,A + B + C == 1
,A <= 5 )


print("Amaç Değeri ",z)


# In[20]:
# Gökhan
# # Modellemeye giriş

# Matematiksel model bir açıklama verir.Olayı ölçülebilir bir hale getirir.Prescriptive 'önerici'
# Descriptive-İstatistik,EDA (explore data analysis)
# Predictive-Machine Learning constrainlerini veriyor optimizasyon için
# Prescriptive-Optimizasyon
# 
# 

# ## Amaç Fonksiyonu,Kısıtlar,Karar Değişkenleri

# Amaç Fonksiyonu:Bu modeli kurarken neyi hedefliyorum
# Karar değişkenleri:Modelimde nerde olduğumu gösteren değişkenler    
# Kısıtlar:Modelimin sınırlarını belirleyen değerler
#     Bunlar sonucunda 
#     stochastic:olasılığa bağlılık   

 





# In[ ]:




