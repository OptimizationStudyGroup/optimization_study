# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# + pycharm={"is_executing": false}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# + pycharm={"is_executing": false}
v1=[1,3]

# + pycharm={"is_executing": false}
v2=[2,4]

# + pycharm={"is_executing": false}
matrix=[v1,v2]

# + pycharm={"is_executing": false}
matrix

# + pycharm={"is_executing": false}
np.array(matrix).shape

# + pycharm={"is_executing": false}
pd.DataFrame(np.array(matrix) )
# -


# #  Matris ve Vektör
#

# + pycharm={"is_executing": false}
1 #Scalar

# + pycharm={"is_executing": false}
[1] # Vektör

# + pycharm={"is_executing": false}
[1,1] # Vektör 1,2

# + pycharm={"is_executing": false}
[[1,1],[1,1]] # Matris 2,2

# + pycharm={"is_executing": false}
a00=1;a01=0;a10=7;a11=3;a20=7;a21=3


# + pycharm={"is_executing": false}
A=np.array([[a00,a01],[a10,a11],[a20,a21]])

# + pycharm={"is_executing": false}
pd.DataFrame(A)

# + pycharm={"is_executing": false}
A.shape[1]

# + pycharm={"is_executing": false}
A[1][1]

# + pycharm={"is_executing": false}
A=np.array([1,2])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
A.shape

# + pycharm={"is_executing": false}
Satır_Vektor=np.array([1,2,3,34,2])

# + pycharm={"is_executing": false}
u=np.array([1,2]);v=np.array([1,-3])
w=np.array([-1,-2])


# + pycharm={"is_executing": false}
u =np.array( [1, 2, 3] )

# + pycharm={"is_executing": false}
v=  np.array( [2,1,2] )

# + pycharm={"is_executing": false}
u.dot(v)

# + pycharm={"is_executing": false}
u.view

# + pycharm={"is_executing": false}
u+v #matris toplama

# + pycharm={"is_executing": false}
u=np.array([1,2]);v=np.array([2,1])
w=u+v;w

# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}
def doğru_parçası(c,u,v):
       return c*u + (1 - c)*v


# + pycharm={"is_executing": false}
c=0
doğru_parçası(c,u,v)


# + pycharm={"is_executing": false}
c=1
doğru_parçası(c,u,v)


# + pycharm={"is_executing": false}
c=0.5
doğru_parçası(c,u,v)

# + pycharm={"is_executing": false}
# Tranpozu, Devrik

# + pycharm={"is_executing": false}
A=np.array([[a00,a01],[a10,a11],[a20,a21]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
A.T

# + pycharm={"is_executing": false}
A.transpose().shape

# + pycharm={"is_executing": false}
A.shape

# + pycharm={"is_executing": false}
A.T.T

# + pycharm={"is_executing": false}
A=np.array([[1,1,2],[2,1,3]])
B=np.array([[1,1],[2,3],[1,2]])
A.dot(B)


# + pycharm={"is_executing": false}
def vektörel_çarpım(A,B):
    return A.dot(B)


# + pycharm={"is_executing": false}
A=np.array([[3],[4]]);B=np.array([[1, 2]]);

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)

# + pycharm={"is_executing": false}
vektörel_çarpım(B,A)

 # LEBG
# -

# ![image.png](attachment:image.png)

# + active=""
# class insan(a,b):
#     adı=a
#     def gökhanfonksiyonu(c):
#         def gökhanfonksiyonu2(q):
#             return a+b
#     
#     

# + active=""
# sum()

# + active=""
# sum="akaka"

# + active=""
# sum([1,2,34])

# + pycharm={"is_executing": false}
A=np.array([[1,2],[3,4]]);B=np.array([[1,1],[0,1],[1,2]]);

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B) # Vektörel çarpımda ilk matrisin sütün sayısı ile ikinci matrisin satır sayısı aynı olmalı

# + pycharm={"is_executing": false}
vektörel_çarpım(B,A)

# + pycharm={"is_executing": false}
PremiumUnleaded=np.array([3/4,1/4])
RegularUnleaded=np.array([2/3,1/3])
RegularLeaded=np.array([1/4,3/4])

# + pycharm={"is_executing": false}
mainTable=np.array([PremiumUnleaded,RegularUnleaded,RegularLeaded])

# + pycharm={"is_executing": false}
mainDataFrame=pd.DataFrame(mainTable,columns=("crude1","crude2"))

# + pycharm={"is_executing": false}
mainDataFrame.index=["PremiumUnleaded","RegularUnleaded","RegularLeaded"]

# + pycharm={"is_executing": false}
mainDataFrame

# + pycharm={"is_executing": false}
Stock=np.array([10,6,5])

# + pycharm={"is_executing": false}
vektörel_çarpım(Stock,mainDataFrame)

# + pycharm={"is_executing": false}
# Kural 1 Satır

# + pycharm={"is_executing": false}
A=np.array([[1,1,2],[2,1,3]]);B=np.array([[1,1],[2,3],[1,2]])

# + pycharm={"is_executing": false}
A[1]

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)[0]

# + pycharm={"is_executing": false}
vektörel_çarpım(A[0],B)

# + pycharm={"is_executing": false}
# Kural 2 Sütün

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B[:,0])

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)[:,0]

# + pycharm={"is_executing": false}
# Geçişkenlik Kuralı

# + pycharm={"is_executing": false}
A=np.array([1,2]) ; B=np.array([[2,3],[4,5]]);C=np.array([[2],[1]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
C

# + pycharm={"is_executing": false}
vektörel_çarpım(vektörel_çarpım(A,B),C)

# + pycharm={"is_executing": false}
vektörel_çarpım(A,vektörel_çarpım(B,C))

# + pycharm={"is_executing": false}
vektörel_çarpım(vektörel_çarpım(A,B),C)==vektörel_çarpım(A,vektörel_çarpım(B,C))
# -

# ## Problemler
#

#
# ### 1. Problem

# + pycharm={"is_executing": false}

A=np.array([[1,2,3],[4,5,6],[7,8,9]]);B=np.array([[1,2],[0,-1],[1,2]])

# + pycharm={"is_executing": false}

print("A :\n", A,"\n")



# + pycharm={"is_executing": false}
print("B :\n", B,"\n")


# + pycharm={"is_executing": false}
 
print("-A :\n", A*-1,"\n")



# + pycharm={"is_executing": false}
print("3A :\n", A*3,"\n")


# + pycharm={"is_executing": false}

print("A+2B : \n",A+2*B)


# + pycharm={"is_executing": false}

print("A transpose : \n" , A.T  )


# + pycharm={"is_executing": false}
      
print("B transpose : \n" , B.T  )

# + pycharm={"is_executing": false}
print("AB transpose : \n" , A.dot(B)  )

# + pycharm={"is_executing": false}
print("BA transpose : \n" , B.dot(A)  )
# -

# ### 2. Problem

# + pycharm={"is_executing": false}
Bira1=[.5,.3,.2]
Bira2=[0,.7,.3]
Bira3=[.1,.3,.6]
Bira_dict={"Bira1":Bira1
          ,"Bira2":Bira2,
          "Bira3":Bira3}

# + pycharm={"is_executing": false}
Bira_df=pd.DataFrame(Bira_dict,index=["Bira1","Bira2","Bira3"])

# + pycharm={"is_executing": false}
Bira_df

# + pycharm={"is_executing": false}
x1=pd.DataFrame({"t1":[0,10,90]},index=["Bira1","Bira2","Bira3"])

# + pycharm={"is_executing": false}
x1

# + pycharm={"is_executing": false}
Bira_df.shape

# + pycharm={"is_executing": false}
x1.shape

# + pycharm={"is_executing": false}
y1=Bira_df.dot(x1)

# + pycharm={"is_executing": false}
y1
# -

# ### 3.Problem

# + pycharm={"is_executing": false}
A=np.array([1,2]) ; B=np.array([[2,3],[4,5]]);C=np.array([[2],[1]])
vektörel_çarpım(vektörel_çarpım(A,B),C)==vektörel_çarpım(A,vektörel_çarpım(B,C))
# -

# ### 4.Problem

# + pycharm={"is_executing": false}
A=np.array([1,2]) ; B=np.array([[2,3],[4,5]])
print(" (AB)T :\n", vektörel_çarpım(A,B).T)
print(" BT*AT :\n",vektörel_çarpım(B.T,A.T))
vektörel_çarpım(A,B).T==vektörel_çarpım(B.T,A.T)
# -

# ### 5.Problem

# + pycharm={"is_executing": false}
A=np.array([[1,2],[2,1]]);
print(" A : \n",A)
print(" A.T : \n",A.T)

print(" A==A.T : \n",A==A.T  )

# + pycharm={"is_executing": false}
# a 
print("A*A.T simetrik \n" , A.dot(A.T)==A.dot(A.T).T)

# + pycharm={"is_executing": false}
# b 
print("A+A.T simetrik \n" , (A+A.T)==(A+A.T).T)
# -

# ### 6.Problem

# + pycharm={"is_executing": false}
A=np.array([[1,1],[1,1]]);
B=np.array([[2,1],[1,2]]);

# + pycharm={"is_executing": false}
A.shape

# + pycharm={"is_executing": false}
B.shape

# + pycharm={"is_executing": false}
n=A.shape[0]

# + pycharm={"is_executing": false}
n**3 # Gereken çarpma sayısı

# + pycharm={"is_executing": false}
n**3-n**2 # Gereken toplama sayısı


# -

# ### 7.Problem

# + pycharm={"is_executing": false}
def matriks_izi(A):
    return np.array([A[i][i] for i in range(len(A))])


# + pycharm={"is_executing": false}
# a
matriks_izi(A+B)==(matriks_izi(A)+matriks_izi(B))

# + pycharm={"is_executing": false}
# b
matriks_izi(vektörel_çarpım(A,B))  == matriks_izi(vektörel_çarpım(B,A))
# -

# # Lineer Denklemlerin Matrisleri

# + pycharm={"is_executing": false}
a11=None;a12=None;a13=None;a21=None;a22=None;a23=None; a31=None;a32=None;a33=None;

A=np.array([[a11,a12,a13],
[a21,a22,a23],
[a31,a32,a33]])


# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
x11=None;x12=None;x13=None;x21=None;x22=None;x23=None; x31=None;x32=None;x33=None;

X=np.array([[x11,x12,x13],
[x21,x22,x23],
[x31,x32,x33]])

# + pycharm={"is_executing": false}
b1=None;b2=None;b3=None;
B=np.array([b1,b2,b3])

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
A.dot(X)==B
# -

# <b><i> X değişken , A ve B sabittir. A*X=B </b></i> 

# <b> Örnek Olarak : </b>  

# + pycharm={"is_executing": false}
A=np.array([[1,2],[2,-1]])
B=np.array([[5],[0]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
X=np.array([[1],[2]])

# + pycharm={"is_executing": false}
A.dot(X)==B

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
# A|b
np.concatenate((A,B), axis=1)

# + pycharm={"is_executing": false}
# Problem 

A=np.array([[1,-1],[2,1],[1,3]])
B=np.array([[4],[6],[8]])

np.concatenate((A,B), axis=1)
# -

# # Gauss-Jordan Metodu ile Lineer Denklem Çözümü

# + pycharm={"is_executing": false}
# Durum 1 : Sistemin çözümü yoktur.
# Durum 2 : Sistemin tek bir çözümü vardır.
# Durum 3 : Sistemin sonsuz çözümü vardır.
# -

# ## Satır Operasyonları (ERO)

# + pycharm={"is_executing": false}
# ERO 1  : herhangi bir satırı bir sabit ile çarpmak 
A=np.array([[11,-1],[12,1],[1,37]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
A[0]=A[0]*33

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false, "name": "#%%\n"}
# ERO 2  : herhangi  diğer satıra eklemek
A=np.array([[11,-1],[12,1],[1,37]])
A[2]=A[2]+A[0]*5
A

# + pycharm={"name": "#%%\n", "is_executing": false}
# ERO 3 : İki satırın yerlerini değiştirmek 
A=np.array([[11,-1],[12,1],[1,37]])
Geçici_Değişken=A[0].copy() # .copy() yapmazsak aynı yere kaydediyor.
A[0]=A[2]
A[2]=Geçici_Değişken
A

# -


A=np.array([[11,-1],[12,1],[1,37]])
Geçici_Değişken=A[0] # .copy() yapmazsak aynı yere kaydediyor.
A[0]=A[2]
A[2]=Geçici_Değişken
A





# + pycharm={"name": "#%%\n", "is_executing": false}
# x1+x2 = 2  ve 2x1 + 4x2 =7 denklemini bu öğrendiklerimiz ile çözelim.

A=np.array([[1,1,2],[2,4,7.0]],float)
A




# + pycharm={"name": "#%%\n", "is_executing": false}
A[1]=A[1]/2  # ERO1
A

# + pycharm={"name": "#%%\n", "is_executing": false}
A[1]=A[1]-A[0]  # ERO2
A



# + pycharm={"name": "#%%\n", "is_executing": false}
A[0]=A[0]-A[1]  # ERO2
A


# + pycharm={"name": "#%%\n", "is_executing": false}
[x1,x2]=A[:,2]
print("x1 : {x1} ve x2: {x2}".format(x1=x1,x2=x2))



# -

# ## Gauss Jordan İle Çözüm 

# + pycharm={"name": "#%%\n", "is_executing": false}
A=np.array([[2,2,1],[2,-1,2],[1,-1,2]],float) # Katsayı
b=np.array([[9],[6],[5]],float) # y 

Ab=np.concatenate((A,b),axis=1) # matrisleri birleştirdik

Ab 

# -


Ab1=Ab.copy() # ilk işlem olarak birinci satırın ilk elemanı 1 olacak şekilde ERO işlemi yaptık
Ab1[0]=Ab1[0]/2
Ab1


# + pycharm={"name": "#%%\n", "is_executing": false}
Ab2=Ab1.copy() # Sonrasında 2 ve 3. satırların ilk sütünlarını 0 olacak şekilde ERO işlemleri yapıyoruz.
Ab2[1]=Ab2[1]-Ab1[1][0]*Ab1[0]
Ab2

# + pycharm={"name": "#%%\n", "is_executing": false}
Ab3=Ab2.copy()
Ab3[2]=Ab2[2]-Ab2[2][0]*Ab2[0]

Ab3


# + pycharm={"name": "#%%\n", "is_executing": false}
Ab3[1]=Ab3[1]*(-1/3) # Yukarıda birinci satır için yaptığımız işlemleri 2. ve 3 satırlar için de yapıyoruz.

Ab3[0]=Ab3[0]-Ab3[1]

Ab3[2]=Ab3[2]+2*Ab3[1]
Ab3

# + pycharm={"name": "#%%\n", "is_executing": false}
Ab4=Ab3.copy()

Ab4[2]=Ab4[2]*(6/5)

Ab4[0]=Ab4[0]-Ab4[2]*(5/6)

Ab4[1]=Ab4[1]+Ab4[2]*(1/3)


# -

np.round(Ab4,6) 

[x1,x2,x3]=Ab4[:,3]

print("x1 : {x1} , x2: {x2} ve x3: {x3} olarak bulunmuştur.".format(x1=x1,x2=x2,x3=x3))

# +
## Çözümsüz veya Sonsuz Çözümlü Denklemler
# -

# Örnek 6
A=np.array([[1,2],[2,4]]);b=np.array([[3],[4]])
Ab=np.concatenate((A,b),axis=1)

Ab

Ab[1]=Ab[1]-2*Ab[0]

Ab

Ab[1] # x1 ve x2 ye ne verirsek verelim sonuç -2 olmaz. Bu yüzden ÇÖZÜMSÜZDÜR.

# +
# Eğer A nın bir satırı tamamen 0 oluyor ve buna karşılık b nin o satıra ait değeri 0 olmuyorsa bu sistemin çözümü yoktur.

# +
# Örnek 7
# -
A=np.array([[1,1,0],[0,1,1],[1,2,1]]);b=np.array([[1],[3],[4]]);
Ab=np.concatenate((A,b),axis=1)


Ab[2]=Ab[2]-Ab[0]

Ab

Ab[0]=Ab[0]-Ab[1]

Ab[2]=Ab[2]-Ab[1]

Ab

[i for i in range(5)]


# +
# Gauss Jordan Metodu 

def GaussJordan(A,b):
    """ 
    Gauss Jordan methodu ile satır işlemleri yapıp, değişkenleri 
    hesaplar.Öncelikle katsayı matrisi ile sonuç matrisi birleştirilir.
    İlk olarak köşegen elemanın 0'a eşitliği kontrol edilir.
    Daha sonrasında ona ait sütündaki diğer elemanlar 0 olacak 
    şekilde satır işlemleri yapılır. Bütün satırların üzerinden 
    bu yöntemle geçilir. 
    
    """
    
    # Adım 1 : A|b matrisini oluştur. 
    
    Ab=np.concatenate((A,b),axis=1)
    satır_sayısı=Ab.shape[0]
    sutun_sayısı=Ab.shape[1]
    
    for i in range(satır_sayısı):         
        if Ab[i][i]==0:
            Geçici=Ab[i].copy()
            satır_indisleri=[a for a in range(i,satır_sayısı) if Ab[a][i]!=0]
            if satır_indisleri:
                Ab[i]=Ab[satır_indisleri[0]].copy()
                Ab[satır_indisleri[0]]=Geçici
            else:
                print(str(i)+". satırından sonra işlem yapılamamaktadır")
                return Ab
        Ab[i]=Ab[i]/Ab[i][i]    
        for s in range(satır_sayısı): 
            if i==s:
                pass
            else:
                Ab[s]=Ab[s]-Ab[i]*Ab[s][i]

    return Ab
# +
## Durum 1 

A=np.array([[1,0,0,1],[0,1,0,2],[0,0,1,3],[0,0,0,0],[0,0,0,0]],float)
b=np.array([[1],[1],[-1],[0],[2]],float)

GaussJordan(A,b)

# +
# Durum 2

A=np.array([[2,2, 1],[2,-1,2],[1,-1,2]],float)
b=np.array([[9],[6],[5]],float)
print(np.concatenate((A,b),axis=1))
GaussJordan(A,b)
# -


# Durum 3 
A=np.array([[1,0,0,1,1],[0,1,0,2,0],[0,0,1,0,1],[0,0,0,0,0]],float)
b=np.array([[3],[2],[1],[0]],float)
print(np.concatenate((A,b),axis=1))
GaussJordan(A,b)

A=np.array([[0,1,1],[0,2,5],[0,35,1]],float)
b=np.array([[3],[4],[5]],float)

a=DoğrusalDenklem(A,b)

a.GaussJordan()



# + code_folding=[]
class DoğrusalDenklem():
    
    def __init__(self,A,b):
        self.denklem=np.concatenate((A,b),axis=1)
        self.satır_sayısı=self.denklem.shape[0]
        self.sütün_sayısı=self.denklem.shape[1]
        print("{n} bilinmeyenli doğrusal denklem sistemi oluşturulmuştur.".format(n=A.shape[1],Ab=self.denklem))
    
    def __str__(self):
        return "Denklem sistemi ----> \n {Ab}".format(Ab=self.denklem)
    
    def __len__(self):
        return self.denklem.shape[0]

    def __del__(self):
        return  "Doğrusal denklem silinmiştir." 
    
    def GaussJordan(self):
        """ 
        Gauss Jordan methodu ile satır işlemleri yapıp, değişkenleri 
        hesaplar.Öncelikle katsayı matrisi ile sonuç matrisi birleştirilir.
        İlk olarak köşegen elemanın 0'a eşitliği kontrol edilir.
        Daha sonrasında ona ait sütündaki diğer elemanlar 0 olacak 
        şekilde satır işlemleri yapılır. Bütün satırların üzerinden 
        bu yöntemle geçilir. 

        """

        # Adım 1 : A|b matrisini oluştur. 

        Ab=self.denklem.copy()
        Ab=Ab.astype(float)
        satır_sayısı=Ab.shape[0]
        sutun_sayısı=Ab.shape[1]

        for i in range(satır_sayısı):         
            if Ab[i][i]==0:
                Geçici=Ab[i].copy()
                satır_indisleri=[a for a in range(i,satır_sayısı) if Ab[a][i]!=0]
                if satır_indisleri:
                    Ab[i]=Ab[satır_indisleri[0]].copy()
                    Ab[satır_indisleri[0]]=Geçici
                else:
                    print(str(i)+". satırından sonra işlem yapılamamaktadır")
                    return Ab
            Ab[i]=Ab[i]/Ab[i][i]    
            for s in range(satır_sayısı): 
                if i==s:
                    pass
                else:
                    Ab[s]=Ab[s]-Ab[i]*Ab[s][i]

        return Ab

    def çözüm_durumu(self):
        çözüm=self.GaussJordan()
        satır_sayısı=self.satır_sayısı
        sutun_sayısı= self.sütün_sayısı
        tekÇözüm=False
        
        for i in range(satır_sayısı):      
            if all(çözüm[i,:sutun_sayısı-1]==0) and çözüm[i,sutun_sayısı-1]!=0:
                print("Denklem Kümesi Çözümsüzdür.")
                return "çözümsüz"  
        
        if satır_sayısı==(sutun_sayısı-1):
            i=0
            while i<satır_sayısı and çözüm[i][i]==1:
                i+=1

            if i==satır_sayısı:
                tekÇözüm=True
                print("Denklem Kümesinin Tek Çözümü mevcuttur.")
                return "tek"
        else:
            print("Denklem Kümesinin Sonsuz Çözümü mevcuttur.")
            return "sonsuz"
        
    def rank_sayar(self):
        Ab=self.GaussJordan()
        say=0
        satır_sayısı=Ab.shape[0]
        for i in range(satır_sayısı):
               if Ab[i][i]==1 and Ab[:,i].sum()==1:
                    say+=1
        return say
    
    def doğrusal_bağımsız(self):
        Ab=self.GaussJordan()
        rank=self.rank_sayar()
        m=Ab.shape[0]
        if m==rank:
            return True
        elif m>rank:
            return False
        else:
            return "Error"
# -



# ##  Ana Değişkenler ve Doğrusal Denklemlerde Çözümleri 

# <i> Doğrusal denklem sistemlerini çözdükten sonra eğer bir satırda sadece bir sütünda 1 katsayısı var ve diğer sütünların katsayıları 0 ise bu değişkene <b> esas değişken (BV) </b>  denir.   </i>  <i> Aksi durumdaki değişkenler <b>  esas olmayan  (NBV)</b>  değişkenlerdir  .   </i>

# + active=""
# def çözüm_durumu(örnek_denklem_çözümü):
#         çözümsüz=False
#         sonsuz_çözüm=False
#         tek_çözüm=0
#         tekÇözüm=False
#         for i in range(satır):
#             if sum(örnek_denklem_çözümü[i,:sütün-1])==0 and örnek_denklem_çözümü[i,sütün-1]!=0:
#                 çözümsüz=True
#                 print("Denklem Kümesi Çözümsüzdür.")
#                 return "çözümsüz"
#               
#         for i in range(satır):    
#             if sum(örnek_denklem_çözümü[i,:sütün-1])==1:
#                 tek_çözüm+=1
#                 if tek_çözüm==satır:
#                     print("Denklem Kümesinin Tek Çözümü mevcuttur.")
#                     tekÇözüm=True
#                     return "tek"
#
#         for i in range(satır):
#             if sum(örnek_denklem_çözümü[i,:sütün])==0:
#                 sonsuz_çözüm=True
#                 print("Denklem Kümesinin Sonsuz Çözümü mevcuttur.")
#                 return "sonsuz"
#             elif tekÇözüm==False:
#                 print("Denklem Kümesinin Sonsuz Çözümü mevcuttur.")
#                 return "sonsuz"
# -



# +
## Durum 1 

A=np.array([[1,0,0,1],[0,1,0,2],[0,0,1,3],[0,0,0,0],[0,0,0,0]],float)
b=np.array([[1],[1],[-1],[0],[2]],float)
# -

örnek_denklem_1=DoğrusalDenklem(A,b)

örnek_denklem_1.denklem

örnek_denklem_1.GaussJordan()

sonuç=örnek_denklem_1.çözüm_durumu()

print(sonuç)

# Güncellenmiş Gauss Jordan
GaussJordan(A,b)


# +
# Durum 2

A=np.array([[2,2, 1],[2,-1,2],[1,-1,2]],float)
b=np.array([[9],[6],[5]],float)

# -

örnek_denklem_2=DoğrusalDenklem(A,b)

örnek_denklem_2.GaussJordan()

sonuç=örnek_denklem_2.çözüm_durumu();

print(sonuç)

# Durum 3 
A=np.array([[1,0,0,1,1],[0,1,0,2,0],[0,0,1,0,1],[0,0,0,0,0]],float)
b=np.array([[3],[2],[1],[0]],float)


örnek_denklem_3=DoğrusalDenklem(A,b)

örnek_denklem_3.denklem

örnek_denklem_3.GaussJordan()

sonuç=örnek_denklem_3.çözüm_durumu()

sonuç


# ##  Problemler 
#
#
#

def problem_çözer(A,b):
    denklem=DoğrusalDenklem(A,b)
    print("Çözüm: \n",denklem.GaussJordan(),"\n")
    print("Çözüm durumu : ",denklem.çözüm_durumu(),"\n")


# 1 
A=np.array([[1,1,0,1],[0,1,1,0],[1,2,1,1]],float)
b=np.array([[3],[4],[8]],float)
problem_çözer(A,b)

# 2 
A=np.array([[1,1,1],[1,2,0]],float)
b=np.array([[4],[6]],float)
problem_çözer(A,b)

# 3 
A=np.array([[1,1],[2,1],[3,2]],float)
b=np.array([[1],[3],[4]],float)
problem_çözer(A,b)

# 4 
A=np.array([[2,-1,1,1],[1,1,1,0]],float)
b=np.array([[6],[4]],float)
problem_çözer(A,b)

# 5 
A=np.array([[1,0,0,1],[0,1,0,2],[0,0,1,.5],[0,0,2,1]],float)
b=np.array([[5],[5],[1],[3]],float)
problem_çözer(A,b)

# 6
A=np.array([[0,2,2 ],[1,2,1 ],[0,1,-1 ]],float)
b=np.array([[4],[4],[0]],float)
problem_çözer(A,b)

# 7
A=np.array([[1,1,0 ],[0,-1,2 ],[0,1,1 ]],float)
b=np.array([[2],[3],[3]],float)
problem_çözer(A,b)

# 8
A=np.array([[1,1,1 ,0],[0,1,2,1 ],[0,0,0,1 ]],float)
b=np.array([[1],[2],[3]],float)
problem_çözer(A,b)

# +
# 9 

A=np.array([[1,1,1 ,0],[0,1,2,1 ],[0,0,0,1 ]],float)
b=np.array([[1],[2],[3]],float)
problem_çözer(A,b)
değişken_sayısı=A.shape[1]
# -

bulunabilecek_değişken_sayısı=b.shape[0]

bulunabilecek_değişken_sayısı

değişken_sayısı

if bulunabilecek_değişken_sayısı>değişken_sayısı:
    print("Tek bir çözüm olma şansı mevcuttur.")
else:
    print("Tek bir çözüm olma şansı mevcut değildir.")

# # Doğrusal Bağımsızlık ve Bağımlılık 

# Bu bölümde doğrusal bağımlı/bağımsız doğrular , matrislerin kertesi(rankı) üzerine çalışacağız. Matrislerin tersi üzerine yapılacak çalışmalar da bu konular önemli olmaktadır.

# +
# V={v1,v2,v3,......,vk} vektörler kümesi (aynı uzunluğa sahip)
# -

# <b> Doğrusal kombinasyonda c1*v1+c2*v2+......+ck*vk rastgele sayılardır. </b>

v1=np.array([1,2]);v2=np.array([2,1])

V=np.array([v1,v2])

(2*v1-v2)==(2*V[0]-V[1])  #1

2*V[0]-V[1]==np.array([0,3]) #1

np.array([1,2])+3*np.array([2,1])== 1*V[0]+3*V[1]  #2

# <br><i> * m boyutlu V vektör kümesindeki vektörlerin sıradan doğrusal kombinasyonu 0'a eşitse <b>doğrusal bağımsız </b> dır. </i>

# <br><i> * m boyutlu V vektör kümesindeki vektörlerin sıradan olmayan doğrusal kombinasyonun toplamı 0'a eşitse <b>doğrusal bağımlı</b> dır </i>

# +
# Örnek 8 

V=np.array([[0,0],[1,0],[0,1]])
# -

V

c1=1;
c1!=0

(c1*V[0]+0*V[1]+0*V[2])==np.array([0,0]) ## Doğrusal bağımlıdır.

# +
# Örnek 9

V=np.array([[1,0],[0,1]])

c1=0;c2=0
if c1==0 and c2==0:
    
    print("Doğrusal bağımlı:",c1*V[0]+c2*V[1]==np.array([0,0])) 

    
# Sadece c1=0 ve c2=0 için geçerlidir. Aksi halde doğruluğu sağlayamamaktadırlar. 

# +
# Örnek 10

V=np.array([[1,2],[2,4]])

c1=2;c2=-1

print("Doğrusal bağımlı:",(c1*V[0]+c2*V[1])==np.array([0,0])) 


# -

V=np.array([[1,2],[2,4]])
for i in range(-100,100):
    c1=i
    for j in range(-100,100):
        c2=j
        if ((c1*V[0]+c2*V[1])==np.array([0,0])).mean()==1:
            print("Doğrusal bağımlı: c1={c1} ve c2={c2}".format(c1=c1,c2=c2))

# +
# Resim 7 

# A
# Doğrusal Bağımlı
# Kırmızı  : v2
# Mavi : v1

v1=[1,1]
v2=[2,2]
plt.quiver([0, 0],[0, 0],  [1, 2], [1, 2],color=['b','r'], angles='xy',width=0.015,scale_units='xy', scale=1)
plt.xlim(-3,3)
plt.ylim(-3, 3)
plt.grid(b=True, which='major') 
plt.show()

# +
# B
# Doğrusal Bağımsız
# Kırmızı  : v2
# Mavi : v1

v1=[1,1]
v2=[1,0]
plt.quiver([0, 0],[0, 0],  [1, 1], [1,0],color=['r','b'], angles='xy',width=0.015, scale_units='xy', scale=1)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5, 1.5)
plt.grid(b=True, which='major') 
plt.show()
# -

# ## Matrisin Rankı

# Gauss Jordan metodu bize vektör kümesinin doğrusal bağımlı ya da bağımsız olduğu bilgisini verebilir. 

#  A mXn lik bir matris ise, R={r1,r2,r3,.....,rm} 'den oluşan bir satırlar kümesi olarakta gösterilebilir. 

# <b> A matrisinin rankı R kümesinin en fazla doğrusal bağımsız olan vektör sayısıdır . </b>

# +
# Örnek 11 

A=np.array([[0,0],[0,0]])

R={'r1':A[0],'r2':A[1]}

R # Örnek 8 de olduğu gibi bağımsız olan bir alt küme seçme şansı bulunmamaktadır. 

# +
# Örnek 12

A=np.array([[1,1],[2,2]])

R={'r1':A[0],'r2':A[1]}

R['r1']*2-R['r2']==0

# Dolasıyla r1 ile r2 doğrusal olarak bağımlıdır. 

# Sonuç olarak sadece 1 adet vektör alabiliriz. A'nın rankı 1 dir.

# +
# Örnek 13

A=np.array([[1,0],[0,1]])

R={'r1':A[0],'r2':A[1]}

R['r1']*2-R['r2']!=0

# Dolasıyla r1 ile r2 doğrusal olarak bağımsızdır. 

# A'nın rankı 2 dir.
# -

Örnek13=DoğrusalDenklem(np.array([[1],[0]]),np.array([[0],[1]]))

Örnek13.denklem

Örnek13.GaussJordan()

# +
# Örnek 14 Gauss Jordan ile Çözüm

A=np.array([[1,0,0],[0,2,1],[0,2,3]])

Örnek14=DoğrusalDenklem(A,np.array([[],[],[]]))

Örnek14.denklem
# -

Örnek14.GaussJordan()

# +
# Rank A = Rank -A = 3
# -

# ## Vektör Kümesinin Doğrusal Bağımsız Olduğunu Nasıl Söyleriz ? 

# V={v1,v2,v3,......,vk} vektörler kümesinin her bir vi elamanı bir matrisin satırı olduğunu farz edersek ve m adet satırı varsa, 
# eğer bu matrisin rankı m' e eşitse doğrusal bağımsız , m 'den küçün ise doğrusal bağımlıdır.

# +
# Örnek 15 Doğrusal Bağımlı Vektörler

A=np.array([[1,0,0],[0,1,0],[1,1,0]])

Örnek15=DoğrusalDenklem(A,np.array([[],[],[]]))

Örnek15.denklem
# -

Örnek15.GaussJordan()

# +
# Rank A = 2 , m=3 , dolasıyla doğrusal olarak bağımlıdır.
# -

z=Örnek15.GaussJordan()

# ## Problemler

# +
# Soru 1 

A=np.array([[1,0,1],[1,2,1],[2,2,2]])
m=A.shape[0]
n=A.shape[1]
Empty=np.array([[]*n]*m) 
soru=DoğrusalDenklem(A,Empty)

# -

soru.doğrusal_bağımsız()


def rank_sayar(Ab):
    say=0
    satır_sayısı=Ab.shape[0]
    for i in range(satır_sayısı):
           if Ab[i][i]==1 and Ab[:,i].sum()==1:
                say+=1
    return say


rank_sayısı=soru.rank_sayar()


def doğrusal_bağımsız(Ab):
    rank=rank_sayar(Ab)
    m=Ab.shape[0]
    if m==rank:
        return True
    elif m>rank:
        return False
    else:
        return "Error"


# +
# Soru 2 

A=np.array([[2,1,0],[1,2,0],[3,3,1]])
m=A.shape[0]
n=A.shape[1]
Empty=np.array([[]*n]*m) 
soru=DoğrusalDenklem(A,Empty)
soru.doğrusal_bağımsız()
# -

soru.GaussJordan()

# Soru 3 
A=np.array([[2,1],[1,2]])
def soru_çözer(A):
    m=A.shape[0]
    n=A.shape[1]
    Empty=np.array([[]*n]*m) 
    soru=DoğrusalDenklem(A,Empty)
    print("Çözüm \n",soru.GaussJordan())
    return print("Doğrusal bağımsız:",soru.doğrusal_bağımsız())


soru_çözer(A)

# Soru 4
A=np.array([[2,0],[3,0]])
soru_çözer(A)


# Soru 5
A=np.array([[1,2,3,4,5,6,7,8,9]])
soru_çözer(A)

# Soru 6
A=np.array([[1,0,0,0,2,1,1,0,1]])
soru_çözer(A)

# +
# Soru 7  ÇÖZÜM DE SORUN VAR!

A=np.array([[1,2,3],[0,1,0],[1,1,0]])  
b=np.array([[1],[5],[9]])
# -

soru7=DoğrusalDenklem(A,b)

soru7.denklem

soru7.GaussJordan()  

v0=A[:,0];v1=A[:,1];v2=A[:,2]
v0.shape=(3,1)
v1.shape=(3,1)
v2.shape=(3,1)

c0=3;c1=5;c2=-4 # Eski Çözüm !

c0*v0+c1*v1+c2*v2==b # ÇÖZÜM DE SORUN VAR. Gauss Jordan Metoduna denklemi float'a çeviren bir kod eklenmiştir. 

# yeni çözüm
çözüm=soru7.GaussJordan()[:,3]  


c0=çözüm[0];c1=çözüm[1];c2=çözüm[2]

c0*v0+c1*v1+c2*v2==b 

# Soru 8 
# 3 veya daha fazla 2 boyutlu vektörün doğrusal bağımlı olduğunu göstermek. 
v0=[0,1]
v1=[1,2]
v2=[3,4]


A=np.array([v0,v1,v2])


A

soru_çözer(A)

# +
# Rank A ile rank A'nın tersi birbirine eşit olma şansı yoktur. O yüzden gauss jordan hata vermektedir. 

# +
# Soru 9 
v0=[0,1,0]
v1=[1,2,3]
v2=[2,4,6]

A=np.array([v0,v1,v2])
# -

soru_çözer(A)

# +
# Bir satır diğerinin katı olduğu için gauss jordan işlemi sırasında diğerini yok etmektedir. 
# -

# # Matrisin Tersi

# x*4=3 denkleminde iki tarafı da 4^-1 ile çarparak sonucu buluyoruz. Bu 0^-1 için geçerli değildir. Bu modeli genelleştirerek bilinmeyen sayısı ile denklem sayısının aynı olduğu durumlar için kullanacağız.

# Kare matris satır ve sütün sayısı eşit olan matristir. 
# Matristeki satır ve sütün numaraları aynı olan elemanlara diyagonal elemanlar denilir. 
# Diyagonal elemanların hepsinin 1 ve diyagonal olmayan elemanların 0 olduğu matrise birim matris denilir. 

I2=np.array([[1,0],[0,1]]);I2

# <b>  Im * A= A * Im = A 'dir  </b>

4*(1/4)==(1/4)*4

4*(1/4)==1

# Matrisler içinde mXm matrisler : <b> BA = AB = I ise , A^-1 = B </b>

# +
# Örnek 

A=np.array([[2,0,-1],[3,1,2],[-1,0,1]])
# -

B=np.array([[1,0, 1],[-5,1,-7],[ 1,0,2]])

A.dot(B)

A_tersi=B

A_tersi

# <b> Ax=b -> (A^-1 * A) * x=A^-1 * b  -> Im * x=A^-1 * b -> x=A^-1 * b </b> 

# Gauss Jordan A^-1 i bulmak için kullanılabilinir. 

A=np.array([[2,5],[1,3]])

A

# A*A^-1=I


I=np.array([[1,0],[0,1]])

I

A_tersi=np.array([['a','b'],['c','d']])

I[0,:]

A_tersi[:,0]

# +
# A*A_tersi[:,0] = I[0,:] A nın tersi ile çarpımında bilinmeyenleri aynı daha önce yaptığımız gibi Gauss Jordan ile bulabiliriz. 

# +
# A*A_tersi[:,1] = I[1,:]
# -

A

I_ilk_sütün=I[:,0]

I_ilk_sütün.shape=(2,1)

Denklem_1=DoğrusalDenklem(A,I_ilk_sütün)

Denklem_1.denklem

A_Ters_İlk_Sütün=Denklem_1.GaussJordan()[:,2]

A_Ters_İlk_Sütün

I_İkinci_Sütün=I[:,1]

I_İkinci_Sütün.shape=(2,1)

Denklem_2=Denklem=DoğrusalDenklem(A,I_İkinci_Sütün)

A_Ters_İkinci_Sütün=Denklem_2.GaussJordan()[:,2]

A_Ters_İkinci_Sütün

A_Ters=np.array([A_Ters_İlk_Sütün,A_Ters_İkinci_Sütün]).T

A_Ters

A_Ters.dot(A)


def MatrisTersi(matris):
    satır_sayısı=matris.shape[0]
    sütün_sayısı=matris.shape[1]
    
    if satır_sayısı!=sütün_sayısı:
        return 'Error : Satır sayısı sütün sayısı ile eşit değildir.'
    else:
        birim_matris= np.identity(satır_sayısı)
        matris_ters_list=[]
        for i in range(satır_sayısı):
            birim_sütün=birim_matris[:,i]
            birim_sütün.shape=(satır_sayısı,1)
            denklem=DoğrusalDenklem(A,birim_sütün)
            matris_ters_sütün=denklem.GaussJordan()[:,satır_sayısı]
            matris_ters_list.append(matris_ters_sütün)
        return np.array(matris_ters_list).T


A_ters=MatrisTersi(A)


A_ters

# Daha kolayı
np.linalg.inv(A) 

np.linalg.matrix_rank(A)

# ## Problemler

# Soru 1
A=np.array([[1,3],[2,5]]);np.linalg.inv(A) 

# Soru 2
A=np.array([[1,0,1],[4,1,-2],[3,1,-1]]);np.linalg.inv(A) 

# Soru 3
A=np.array([[1,0,1],[1,1,3],[2,1,2]]);np.linalg.inv(A) 

# Soru 4
A=np.array([[1,2,1],[1,2,0],[2,4,1]]);np.linalg.inv(A) 

MatrisTersi(A)

# Soru 5
A=np.array([[1,3],[2,5]]);np.linalg.inv(A) 

Çözüm=np.linalg.inv(A).dot(np.array([[4],[7]])) ;Çözüm

A.dot(Çözüm)

# +
# Soru 6

A=np.array([[1,0,1],[4,1,-2],[3,1,-1]]);
# -

Çözüm=np.linalg.inv(A).dot(np.array([[4],[0],[2]]))

A.dot(Çözüm)

# +
# Soru 7 

A=np.array([[1,2],[2,4]])
boş_A=np.array([[]*A.shape[1]]*A.shape[0])
Denklem=DoğrusalDenklem(A,boş_A)

# -

print('Doğrusal bağımsız:', Denklem.doğrusal_bağımsız())

np.linalg.inv(Denklem.denklem)

# Soru 8 
# a
B=np.array([[1,0,1],[4,1,-2],[3,1,-1]]);
B_ters=np.linalg.inv(B)


B

B_ters

B_ters=np.linalg.inv(B*100)

B_ters

# +
# b

B_=B.copy()
B_[0,:]=B_[0,:]*2
# -

B_ters=np.linalg.inv(B)

B__ters=B_ters.copy()

B__ters[:,0]=B__ters[:,0]/2 # Satır daki değişiklik tersinde sütünda ve çarpma olarak tersi olarak görünür.

B__ters

np.linalg.inv(B_)

# +
# c

B_=B.copy()
B_[:,0]=B_[:,0]*2

B__ters=B_ters.copy()

B__ters[0,:]=B__ters[0,:]/2
# -

B__ters

np.linalg.inv(B_)

# +
# Soru 9

A=np.array([[ 1,  0,  1],
       [ 4,  1, -2],
       [ 3,  1, -1]])
# -

np.linalg.inv(A.T).round(2)

np.linalg.inv(A).T.round(2)

# +
# Soru 10 
# A*A^1=I ise  A.T*A^-1.T == I.T  ==  (A*A^1).T

#  A.T*A^-1.T  == (A*A^1).T

# +
# Soru 11
# Sütün ve satır birbirine eşittir.
# -

A=np.array([[ 1/3, -2/3,  2/3],
       [ 2/3,  2/3, 1/3],
       [ -2/3,  1/3, 2/3]])

# +
# A^-1=A.T ise ortogonal matristir. 
# -

A.dot(A.T).round(2)

A

A.T

np.linalg.inv(A)

# # Determinant
#


#  Herhangi bir kare matrisi belirleyen sayıya determinant denir. Doğrusal olmayan programlama çalışmalarında kullanılacaktır .


# A= [a11] det A -> a11
    

# +
# A =[[a11 a12],[a21 a22]]  det A -> a11*a22 - a21*a12
# -

A=np.array([[2,4],[3,5]])

2*5-3*4

np.linalg.det(A)

A=np.array([[1,2,3],[4,5,6],[7,8,9]])

A

A02=A[1:,:2]

A02


# Bir matrisin alt matrisi ona ait sütün ve satırların silinmesi ile yazılır.

def alt_matris(A,i,j):    
    a_del = np.delete(A, i, 0)
    a_del=np.delete(a_del, j, 1)
    
    return a_del


# +
def determinant_hesaplayıcı(A,i=0):
    if (A.shape!=(1,)):
        if (A.shape[0] != A.shape[1]) :
            return "Hata: Kare matris değildir."
    m=A.shape[0]
    if m==1:
       detA= A[0]  
       return detA
    else:
        detA=0
        for j in range(m):
            detA+=np.power(-1,i+j)*A[i,j]*determinant_hesaplayıcı(alt_matris(A,i,j))
            
    return detA.item(0)
    








# -

determinant_hesaplayıcı(A,i=0)

A.item(0)

A=np.array([[2,4],[3,5]])
determinant_hesaplayıcı(A,i=0)

# ## Problemler

# Soru 1
A=np.array([[1,2,3],[4,5,6],[7,8,9]])


A[1,:]

determinant_hesaplayıcı(A,i=1) # 2. satır için

determinant_hesaplayıcı(A,i=2) # 3. satır için

A=np.array([[1,2,3],[6,5,3],[7,15,9]])

np.linalg.det(A)

determinant_hesaplayıcı(A,i=0) # 3. satır için

determinant_hesaplayıcı(A,i=1)

determinant_hesaplayıcı(A,i=0)

# +
# Soru 2

A=np.array([[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,5]])
determinant_hesaplayıcı(A,i=0)
# -

np.linalg.det(A)

# +
# Soru 3

# i>j and aij=0

A=np.array([[1,2,3],[0,2,2],[0,0,1]])
# -

A

np.linalg.det(A)

determinant_hesaplayıcı(A,i=0)

np.prod(np.diagonal(A))

# Soru 4
# a
A=np.array([3])
determinant_hesaplayıcı(-A,i=0)

-determinant_hesaplayıcı(A,i=0)

A=np.array([[1,2,3],[0,2,2],[0,0,1]])
determinant_hesaplayıcı(-A,i=0)

-determinant_hesaplayıcı(A,i=0)

# b
A=np.array([[1,2],[0,2]])
determinant_hesaplayıcı(-A,i=0)


determinant_hesaplayıcı(A,i=0)

A=np.array([[1,2,3,11],[0,2,2,3],[0,0,1,9],[0,2,2,5]])
determinant_hesaplayıcı(-A,i=0)

determinant_hesaplayıcı(A,i=0)

# +
# 1-> m e kadar elemanı topladığımız için ve (-1) üzeri (i) ile çarptığımız için m sayısının çift tek olması yüzünden bu durum değişmektedir. 
# -

# # Review Problems

# Soru 1
A=np.array([[1,1,0],[0,1,1],[1,2,1]])
b=np.array([[2],[3],[5]])
soru1=DoğrusalDenklem(A,b)

soru1.GaussJordan()

np.linalg.solve(A,b)

# +
# Soru 2

A=np.array([[0,3],[2,1]])
# -

np.linalg.inv(A)

MatrisTersi(A)

# Soru 3


# +
U=[20,5,75] # t ,q ,r

T=[90,10]  # r , q

[Ut Tt] -> [U T]

U *.75 = Ut

T*0.9+U*0.20=Tt
 U    T
[0.75 0 ] =Ut
[0.2  0.90 ]=Tt
# -

# Soru 4


A=np.array([[2,3],[1,1],[1,2]])
b=np.array([[3],[1],[2]])
soru4=DoğrusalDenklem(A,b)


soru4.GaussJordan()

np.linalg.solve(A,b)

# Soru 5


np.linalg.inv(np.array([[0,2],[1,3]]))

# Soru 6


grades=np.array([[3.6 ,3.8 ,2.6,3.4],[2.7 ,3.1, 2.9, 3.6]])

courses=np.array([4,4,3,3])

grades.dot(courses)/courses.sum()

# +
# Soru 7
# -

A=np.array([[2,1],[3,1],[1,-1]])
b=np.array([[3],[4],[0]])
soru7=DoğrusalDenklem(A,b)

soru7.GaussJordan()

A=np.array([[2,1],[4,0]])
b=np.array([[3],[4]])
soru7=DoğrusalDenklem(A,b)

soru7.GaussJordan()

# +
# Soru 8 

np.linalg.inv([[2,3],[3,5]])
# -


