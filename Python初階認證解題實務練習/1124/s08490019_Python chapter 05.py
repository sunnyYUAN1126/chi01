# In[1]
'''
1.	請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。
輸入:10
輸出: 0 1 1 2 3 5 8 13 21 34
'''
def fun1(n):
    if n>1:
        n=fun1(n-1)+fun1(n-2)
    return n

n=int(input("input:"))
for i in range(n):
    print(fun1(i), end = ' ') 
       
    
# In[2]  
'''
寫函式，判斷使用者傳入的物件（字串、列表、元組）長度是否大於5
'''
def fun2(n):
    n=len(n)
    if n>5:
        print("YES")
    else:
        print("NO")
        
n=input("input:") 
fun2(n)
# In[3]
'''
3.	請利用以下functione改寫並輸出
def XXX():
    for i in range(1, 10):
		.
		.
		.
輸出:
1
2
3
Hi
5
Hi
7

'''
a=[]
def fun3():   
    for i in range(10):
        a.append(input("input:"))
    for i in a:    
        print(i)
fun3()




# In[4]
'''
4.	寫一個函式，提取指定字串中所有的字母，然後並接在一起產生一個新的字符串
輸入:12a&bc12d-+
輸出:abcd
'''
def fun4(n):
    print("rrr",n)
    for i in n:
        if i.isalpha()==True:
            print(i,end="")
    

n=input("input:")
fun4(n)
# In[5]
'''
有家電影院根據觀眾的年齡收取不同的票價： 
不到3歲的觀眾免費； 
3~12歲的觀眾為10美元； 
超過12歲的觀眾為15美元。 
請編寫一個迴圈， 
在其中詢問使用者的年齡， 
並指出其票價
'''
def fun5(n):
    if 0<=n<3:
        print("free")
    elif 3<=n<=12:
        print("10$")
    elif n>12:
        print("15$")


while True:
    n=eval(input("input:"))
    if n==-9999:
        break
    else:
        fun5(n)


# In[6]
'''
寫一個函式，接收n個數字，求這些参數數字的和
'''
def fun6(n):
    ab=0
    for i in range(n):
        b=int(input("數:"))
        ab=ab+b
    print("總和=",ab)   


a=int(input("值:"))
fun6(a)

#修改
def fun6(*n):
    a=0
    for i in n:
        a+=i
    return a
    
print(fun6(1,2,3,4,5,6))

# In[7]
'''
寫一個函式，統計字串中有幾個字母，幾個數字，幾個空格，並返回結果
'''

def fun7(a):
    con1,con2,con3=0,0,0
    for i in a:
        if i.isalpha()==True:
            con1+=1
        elif i.isdigit()==True:
            con2+=1
        elif i==" ":
            con3+=1
    print("字母有%d"%con1)
    print("數字有%d"%con2)
    print("空格有%d"%con3)    

a=input("input:")
fun7(a)


# In[8]
'''
有一個程式如下，其輸出結果為20 20，請說明輸出之結果為何不是回傳20 30
num = 20
def show_num(x=num):
  print(x)
show_num()
num = 30
show_num()
'''
'''
因為show_num(x=num)會自動判斷num為前一行的num = 20，
而第二個show_num()沒有在裡面加入藥傳遞的值，
所以輸出為原本自動判斷的值，也就是20，
如要修改，如下:
'''
num = 20
def show_num(x=num):
  print(x)
show_num()
num = 30
show_num(num) #這裡要加入傳遞值(num)

# In[9]
'''
寫一個函式，傳入一個參數n，返回n的階層
'''
def fun9():
    n=eval(input("n:"))
    a=1
    for i in range(1,n+1):
        a=a*i
    return a

print(fun9())
    
    
# In[10]
'''
一個數如果恰好等於它的因數之和，
這個數就稱為"完全數"。
例如6=1＋2＋
撰寫一個函式找出1000以内的所有完全數
'''

for i in range(1,1001):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)





