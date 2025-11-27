# In[1]
'''
1.	迴圈輸出20*20乘法表(請用for loop)
'''
for i in range(1,21):
    for j in range(1,21):
        ans=i*j
        #print(i,"*",j,"=",ans)
        print("%d*%d=%2d"%(i,j,ans))


# In[2]
'''
2.	計算出1+2+…+10的總和(請用for loop)
'''
a=0
for i in range(1,11):
   a=a+i
print("+2+…+10 =",a)

# In[3]
'''
3.	迴圈輸出9*9乘法表中的奇數數字
'''
for i in range(1,10):
    for j in range(1,10):
        ans=i*j
        if ans%2==0:
            continue
        else:
            #print(i,"*",j,"=",ans)
            print("%d*%d=%2d"%(i,j,ans),end=" ")


# In[4]
'''
4.	請輸出100以內的質數
'''
for i in range(2,101):   
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

# In[5]
'''
5.	請印出 *****
           *** 
            * 
'''

i=4
while i>0:  
    i-=1
    print(' '*(3-i)+'*'*(2*i-1)) 
    

    
# In[6]
'''
6. 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值
'''
a=eval(input("請輸入:"))
j=1
for i in range(1,a+1):
    j=i*j
print(j)
    


# In[7]
'''
7. 請使用迴圈敘述撰寫一程式，提示使用者輸入金額（如10,000）、年收益率（如5.75），以及經過的月份數（如5），接著顯示每個月的存款總額。
提示：四捨五入，輸出浮點數到小數點後第二位。
舉例：
假設您存款$10,000，年收益為5.75%。
過了一個月，存款會是：10000 + 10000 * 5.75 / 1200 = 10047.92
過了兩個月，存款會是：10047.92 + 10047.92 * 5.75 / 1200 = 10096.06
過了三個月，存款將是：10096.06 + 10096.06 * 5.75 / 1200 = 10144.44
以此類推。
'''
money=eval(input("請輸入金額:"))
eff=eval(input("請輸入年收益率:"))
mon=eval(input("請輸入月份數:"))
save=money
for i in range(1,4):
    save_temp=save
    save=save+save*eff/1200
    print("過了%d個月，存款會是：%.2f+%.2f*%f/1200=%.2f"%(i,save_temp,save_temp,eff,save))


# In[8]
'''
8. 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間，所有5之倍數數字總和
'''
a=eval(input("請輸入:"))
ans=0
for i in range(1,a+1):
    if i%5==0:
        ans=ans+i
    else:
        continue
print("答案為:",ans)


# In[9]
'''
9. 迴圈輸出20*20乘法表(請用while loop)
'''
i=1
j=1
while i<=20:
    i=i+1
    while j<=20:
        ans=i*j
        print("%d*%d=%d"%(i,j,ans),end=" ")
        j=j+1


# In[10]
'''
10. 請撰寫一程式，讓使用者輸入一個正整數，將此數值以反轉的順序輸出
'''
a=eval(input("請輸入:"))
while a!=0:
    ans=a%10
    a=a//10
    print(ans,end="")
    