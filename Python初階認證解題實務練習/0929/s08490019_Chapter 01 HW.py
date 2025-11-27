#洪琪媛 s08490019 資管四 
# In[1] 
#請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。
#提示1：歐式距離 =√((x1−x2)2+(y1−y2)2)
#提示2：兩座標的歐式距離，輸出到小數點後第4位
#解答:
    
x1=eval(input("輸入x1:"))
y1=eval(input("輸入y1:"))
x2=eval(input("輸入x2:"))
y2=eval(input("輸入y2:"))

dist=(x1-x2)**2+(y1-y2)**2 
print(  "(",   x1,  ",",   y1,   ")")
print(  "(",   x2,  ",",   y2,   ")")
print("距離為 %.4f"%dist)




# In[2] 
#請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。
#提示1：建議使用import math模組的math.pow及math.tan
#提示2：正n邊形面積的公式如下：  
#Area=(n∗s2)/(4∗tan(pi/n)) 
#提示3：輸出浮點數到小數點後第四位
#解答:

import math
n = eval(input("輸入邊形:"))
s = eval(input("輸入邊長:"))
area = (n*math.pow(s,2)) / (4*math.tan(math.pi/n))
print("Area = %.4f" % area)
print("邊長為",s,"的",n,"邊形，面積為 %.4f"%area)

    



# In[3] 
#請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）
#提示1：正五邊形面積的公式：Area=(5∗s2)/(4∗tan(pi/5))

import math
s = eval(input("輸入邊長:"))
area = (5*math.pow(s,2)) / (4*math.tan(math.pi/5))
print("面積為 %.4f" % area)


# In[4] 
#在數學中，函數（伽瑪函數；Gamma函數），是階乘函數在實數與複數域上的擴展。
#對於實數部份為正的複數z，伽瑪函數定義為： 
#請幫我計算出0.55的Gamma值為何?
#提示1：建議使用import math模組的函數
#解答:

import math
print(math.gamma(0.55))


# In[5] 
#請撰寫一程式，讓使用者輸入一個正數s，代表距離，輸入一個正數t，代表時間，輸入一個正數v0，代表初速度，計算並輸出加速度
#解答:
s=eval(input("輸入距離:")) 
t=eval(input("輸入時間:")) 
v0=eval(input("輸入初速度:")) 

#s=v0*t+(1/2)*a*t**2

a=(v0*t-s)*(-2)/t**2
#可以寫成a=2*(s-v0*t)/t**2
print("加速度為%.4f"%a)


# In[6] 
#請撰寫一程式，讓使用者輸入三個數字，計算並輸出這三個數字之數值、總和及平均數。
#提示：總和與平均數皆輸出到小數點後第1位。
#解答:

x=eval(input("輸入數字:")) 
y=eval(input("再輸入數字:")) 
z=eval(input("再輸入數字:")) 

average=(x+y+z)/3  #計算平均
print("x=",x,",y=",y,",z=",z)
print("總合為",x+y+z)
print("平均為%.1f"%average)


# In[7] 
#假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。
#提示：輸出浮點數到小數點後第一位。
#解答:
    
x=eval(input("輸入分鐘:")) #分
y=eval(input("輸入秒數:")) #秒
z=eval(input("輸入公里:")) #公里

speed= (z/1.6)/(x*60+y)*60*60
print("每小時 %.1f 英里"%a)




# In[8] 
#任意N次方計算器，請撰寫一程式，讓使用者輸入一個正數s，代表底數，輸入一個正數t，代表次方，計算並輸出其結果。
#解答:

s=int(input("輸入底數:")) #底數
t=int(input("輸入次方:")) #次方

print(s**t)


# In[9] 
#請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。
#提示1：建議使用import math模組的math.pow及math.tan
#提示2：正五邊形面積的公式： Area=(5∗s2)/(4∗tan(pi/5))
#提示3：輸出浮點數到小數點後第四位。
#解答:
    
import math
s = eval(input("輸入邊長:"))
area = (5*math.pow(s,2)) / (4*math.tan(math.pi/5))
print("Area = %.4f" % area)


#math.pow(s,2) = s**2



# In[10] 
#請撰寫一程式,請使用者輸入攝氏溫度,然後輸出其對應的華氏溫度。
#請使用者輸入華氏溫度,然後輸出其對應的攝氏溫度
#提示1:華氏溫度 = (9/5) * 攝氏溫度+ 32。
#提示2:攝氏溫度 = (華氏溫度-32)*5/9


f = eval(input("輸入攝氏溫度:"))  #攝氏
c = eval(input("輸入華氏溫度:"))  #華氏
cc = (9/5) * f+ 32  #轉華氏
ff =(c-32)*5/9      #轉攝氏
print("華氏=", cc)
print("攝氏=", ff)


