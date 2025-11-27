# In[1]
'''
請撰寫一程式，輸入你的出生年 你的年紀，
將出生年分換算成民國並存成一個新的變數，EX:1996轉換成85
輸出新的變數
判斷新變數大於90輸出"你是九年級生"，小於90輸出"你是八年級生"
等於0輸出"你是1911年出生"
將你的年紀+出生年並存成另一個新的變數，EX:1996+25
輸出另一個變數
如果變數大於2021輸出"你算錯囉"，小於2021輸出"你程式錯了"
等於 2021 "神奇吧把你的出生西元年加上你的年紀等於今年"
最後輸出"Over"

'''
AD_year=eval(input('輸入西元出生年:'))
old=eval(input('輸入年紀:'))
ROC_year=AD_year-1911
new_old= old + AD_year

if ROC_year>90:
    print("你是九年級生")
elif ROC_year==0:
    print("你是1911年出生")
else:
    print("你是八年級生")

if  new_old>2021:
    print("你算錯囉")
elif new_old<2021:
    print("你程式錯了")
elif new_old==2021:
    print("神奇吧!把你的出生西元年加上你的年紀等於去年")
print("over")

# In[2]
'''
請撰寫一程式，輸入你想要的成績， 與你學習的時間
 將想要的成績*0.3，再加上你的學習時間*0.7，並存成一個新的變數
 輸出變數
  最終得分           說明
 < 40             請多花時間學習
 40.1.1~49.9        加油你可以的
 50.0 ~ 54.9      快達到你想要的目標了
 >= 55            好棒你達標了

 輸出結果
 你想要的成績: 100
 學習的時間: 1
 最終得分:  30.70
  請多花時間學習

'''

score=eval(input("輸入想要的成績:"))
learnTime=eval(input("輸入學習時間:"))
new_score=score*0.3
new_learnTime=learnTime*0.7
allNum=new_score+new_learnTime


print("你想要的成績:",score)
print("學習的時間:",learnTime)
print("最終得分:",allNum)

if allNum<40:
    print("請多花時間學習")
elif allNum>=40.1 and allNum<=49.9 :
    print("加油你可以的")
elif allNum>=50.0 and allNum<=54.9  :
    print("快達到你想要的目標了")
elif allNum>= 55  :
    print("好棒你達標了")
    




# In[3]
'''
請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。例如：a為英文字母、9為數字、$為其它字元。

範例輸入1
P
範例輸出1
P is an alphabet.

'''
num=input("請輸入字元:")
if num.isalpha()==True:
    print(num,"是字母")
elif num.isdigit()==True:
    print(num,"是數字")
else:
    print(num,"是其他字元")
    
#寫法二
if ('a'<= num <="z") or ('A'<= num <="Z"):
    print(num,"是字母")
elif ('0'<= num <='9'):
    print(num,"是數字")
else:
    print(num,"是其他字元")

# In[4]
'''
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為奇數。

範例輸入1
57
範例輸出1
57 is an odd number.

'''
num=eval(input("請輸入數字:"))
ans=num%2
if ans==0:
    print(num,"是偶數")
else:
    print(num,"是奇數")
    
    
    
# In[5]
'''
請使用選擇敘述撰寫一程式,讓使用者輸入兩個整數a、b,然後再輸入一
算術運算子(+、-、*、/),但這是奇怪的加減乘除。
說明如下:
如果算術運算子為加(+)那會將a+b-a
如果算術運算子為減(-)那會將a*b-a
如果算術運算子為乘(*)那會將a*b*b
如果算術運算子為除(/)那會將a-b/b
輸出結果:
第一個整數:5
第二個整數:8
算術運算子:+
'''
a=int(input("第一個整數:"))
b=int(input("第二個整數:"))
num=input("算術運算子:")
if num=="+":
    print(a+b-a)
elif  num=="-":
    print(a*b-a)
elif  num=="*":
    print(a*b*b)
elif  num=="/":
    print(a-b/b)
        
# In[6]
'''
請使用選擇敘述撰寫一程式,根據使用者輸入的月份顯示對應的八進位與十六進位
輸入輸出:
(一)
十進位8
0o10 0x8
'''
#使用 oct、hex 類別可以將十進位整數以八進位、十六進位表示字串傳回
month=eval(input("輸入月份(十進位):"))
if month==1:
    print(oct(month),hex(month))
elif month==2:
    print(oct(month),hex(month))
elif month==3:
    print(oct(month),hex(month))
elif month==4:
    print(oct(month),hex(month))
elif month==5:
    print(oct(month),hex(month))
elif month==6:
    print(oct(month),hex(month))
elif month==7:
    print(oct(month),hex(month))
elif month==8:
    print(oct(month),hex(month))
elif month==9:
    print(oct(month),hex(month))
elif month==10:
    print(oct(month),hex(month))
elif month==11:
    print(oct(month),hex(month))
elif month==12:
    print(oct(month),hex(month))
    
    
#解法二
month=eval(input("輸入月份(十進位):"))
if 1<= month <=12:
    print(oct(month),hex(month))
else:
    print("不是月份")

# In[7]
'''
請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於12000（含）以上，並顯示折扣優惠後的實付金額。購物金額折扣方案如下表所示：
12000（含）以上	8折
18,000（含）以上7折
28,000（含）以上	6折
38,000（含）以上	5折
'''

num=int(input("請輸入金額:"))
if num>=12000:
    print("打八折，共",num*0.8)
elif num>=18000:
    print("打七折，共",num*0.7)
elif num>=28000:
    print("打六折，共",num*0.6)
elif num>=38000:
    print("打五折，共",num*0.5)
else:
    print("原價，共",num)


# In[8]
'''
請使用選擇敘述撰寫一程式,根據使用者輸入的成績顯示對應的分數
成績除以3後之餘數
EX: 原本分數為43分除以3之餘數為1那就是不調整
餘數                折扣
0                   *10
1                  不調整
2                   *1.1
輸入輸出:
(一)
分數75
750
'''
num=int(input("請輸入成績:"))
ans=num%3
if ans==0:
    print(num*10)
elif ans==1:
    print(num)
elif ans==2:
    print(num*1.1)



# In[9]
'''
請撰寫一程式,變數word1與變數word2文為小星星。請輸出如下
Ps請不要使用for loop
輸出:
         *
        ***
'''

word1="*"
word2="***"
print('%10s'%word1)
print('%11s'%word2)


# In[10]
'''
請使用選擇敘述撰寫一程式,根據使用者輸入的月份顯示對應的四季
輸入輸出:
(一)
月份11
winter
'''
month=int(input("請輸入月份:"))
if month>=3 and month<=5:
    print('春天')
elif month>=6 and month<=8:
    print('夏天')
elif month>=9 and month<=11:
    print('秋天')
elif month==12 or month==1 or month==2:
    print('冬天')


