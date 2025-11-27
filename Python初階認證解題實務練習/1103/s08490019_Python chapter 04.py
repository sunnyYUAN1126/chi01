# In[1]
'''
1. 某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，
輸入五張選票，輸入值如為1即表示針對1號候選人投票；輸入值如為2即表示針對2號
候選人投票，如輸入其他值則視為廢票。每次投完後需印出目前每位候選人的得票數
，最後印出最高票者為當選人；如最終計算有相同的最高票數者或無法選出最高票者
，顯示【=> No one won the election.】。

輸入與輸出會交雜如下，輸出的部份以粗體字表示
2
Total votes of No.1: Nami =  0
Total votes of No.2: Chopper =  1
Total null votes =  0
1
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  0
8
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  2
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  3
Total null votes =  1
=> No.2 Chopper won the election.

'''
no1=0
no2=0
no3=0
for i in range(1,6):
    a=eval(input("input:"))
    if a==1:
        no1+=1
    elif a==2:
        no2+=1
    else:
        no3+=1
    print("Total votes of No.1: Nami =",no1)
    print("Total votes of No.2: Chopper =",no2)
    print("Total null votes =",no3)
if no1>no2:
    print(" No.1 Nami won the election.")
elif no2>no1:
    print(" No.2 Chopper won the election.")
elif no1==no2 or no3>no1 or no3>no2:
    print("No one won the election.")



# In[2]
'''
(1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，
然後判斷它是否為閏年（leap year）或平年。其判斷規則如下：
每四年一閏，每百年不閏，但每四百年也一閏。
(2) 假設此不定數迴圈輸入-9999則會結束此迴圈。
輸入與輸出會交雜如下，輸出的部份以粗體字表示
2017
2017 is not a leap year.
2000
2000 is a leap year.
2016
2016 is a leap year.
2009
2009 is not a leap year.
2018
2018 is not a leap year.
-9999
'''

while True:
    a=eval(input("input:"))
    if a%400==0 or (a%4==0 and a%100!=0):
        print("%d is a leap year"%a)
    elif a==-9999:
        break
    else:
        print("%d is not a leap year"%a)
        
        
# In[3]
'''
3. 請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。
範例輸入
7
範例輸出
      *
     ***
    *****
   *******
  *********
 ***********
*************

'''
a=eval(input("input:"))
a2=a
for i in range(1,a+1):
    a2-=1
    print(" "*(a2) + "*"*(i*2-1))




# In[4]
'''
輸入某年某月某日，判斷這一天是這一年的第幾天?
p.s.閏年時須考慮二月多加一天
'''
sumDay=0
a,b,c=eval(input("input:"))
if b==1:
    sumDay=0
elif b==2:
    sumDay=31
elif b==3:
    sumDay=59
elif b==4:
    sumDay=90
elif b==5:
    sumDay=120
elif b==6:
    sumDay=151
elif b==7:
    sumDay=181
elif b==8:
    sumDay=212
elif b==9:
    sumDay=243
elif b==10:
    sumDay=273
elif b==11:
    sumDay=304
elif b==12:
    sumDay=334
sumDay=sumDay+c    
 

if (a%400==0 or (a%4==0 and a%100!=0) ) and b>2:
    sumDay=sumDay+1
 
print(sumDay)
    
    
# In[5] ****
'''
有四個數字:1,2,3,4,能組成多少個互不相同且重複數字的三位數?各是多少?
'''

for x in range(1,5):
     for y in range(1,5):
         for z in range(1,5):
                 if (x!=y) and (y!=z) and (z!=x):
                         print("%d%d%d" % (x, y, z),end=" ")
                         
                         

#解
a=["1","2","3","4"]
b=[]
for i in a:
    print(i)
    for j in [x for x in a  if x!=i]:
        print(j)
        for m in [x for x in a  if x!=i and x!=j]:
            print(m)
            b.append(int(i+j+m))
print(len(b))       
    



# In[6]
'''
將一個整數分解質因數，EX:輸入90,印出90=233*5
p.s.可以試試看用break寫

'''

n = int(input('请输入一个整数：'))
print('%d='%n,end='')
while n>1:
 for i in range(2,n+1):
     if n%i==0:  #因數
         n=int(n/i)
         if n==1:
             print('%d'%i,end='') #尾
             break
         else:
             print('%d*'%i,end='')
             break
         
# In[7]
'''
一球從100米的高度自由烙下，每次落地後反跳回原高度的一半，
在落地，求它在第10次落地時共經過多少米?第十次反彈多高?
'''
a=100
num=100
for i in range(1,11):   
    num=num+a
    a=a/2     
print(num-a*2,a) # num-a*2 第十次落地要減去地10次的高度

# In[8]
'''
使用迴圈完成剪刀石頭布遊戲，提示使用者輸入要出的拳 ：
石頭（1）／剪刀（2）／布（3）/退出（4）。
電腦隨機出拳比較勝負，顯示使用者勝、負還是平局。
E.X.:
----石頭剪刀布遊戲開始----
請按下面提示出拳
石頭[1],剪刀[2],布[3],退出[4]
請玩家出拳：1
玩家出拳為1，電腦出拳為3，電腦勝利
請玩家出拳：4
遊戲退出
遊戲結束

'''
import random
print("石頭（1）／剪刀（2）／布（3）/退出（4）")
while True:
    a=eval(input("請玩家出拳:"))
    num=random.randint(1,3)
    if a!=4:
        print("玩家出拳為%d"%a,"電腦出拳為%d，"%num,end='')
    if a==num:
        print("雙方平手")
    elif a==4:
        print("遊戲退出\n遊戲結束")
        break
    elif a==1 and num==2:
        print("使用者勝利")
    elif a==2 and num==3:
        print("使用者勝利")
    elif a==3 and num==1:
        print("使用者勝利")
    else:
        print("電腦勝利")


# In[9]
'''
撲克牌發牌，自動生成一幅撲克牌組；洗牌；發牌到玩家手中

E.X.
♠7  ♣6  ♦4  ♣3  ♦6  ♥A  ♦8  ♣4  ♠3  ♥8  ♣5  ♠Q  ♦2  
♥K  ♥9  ♦K  ♣K  ♥3  ♥5  ♣8  ♥2  ♠9  ♣J  ♠J  ♦9  ♦A  
♠5  ♥6  ♣10  ♣7  ♥7  ♠8  ♠4  ♦7  ♦3  ♦J  ♦10  ♠A  ♣A  
♠6  ♠K  ♦5  ♦Q  ♥4  ♥10  ♥J  ♠2  ♣Q  ♣2  ♥Q  ♠10  ♣9

'''
import random
a=['♠1','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K',
   '♥1','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K',
   '♦1','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K',
   '♣1','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K'] 
random.shuffle(a)
for i in a:
    print(i,end=" ")
    
#解
a=["♠","♥","♦","♣"]
b=['1','2','3','4','5','6','7','8','10','J','Q','K']
card=[]
for i in a:
    for q in b:
        card+= [i+q]

for a in card:
    print(a)



# In[10]
'''
求輸入數字的平方，如果平方運算後小於50則退出，如輸入特殊符號則輸出:輸入錯誤

E.X.:
輸入一個數字：@@
輸入錯誤
輸入一個數字：2
其平方為： 4.0
平方小於50，退出
'''
while True:
    a=input("input:")
    if a.isdigit()==True:
        a=float(a)
        a=a**2
        print("其平方為：%.1f"%a)
        if a<50:
            print("平方小於50，退出")
            break
    else:
        print("輸入錯誤")     