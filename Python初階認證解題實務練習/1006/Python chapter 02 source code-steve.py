### 選擇敘述
#2-2
'''語法

if敘述的語法如下:
if 條件運算式:
   主體敘述
print()   
其中條件運算式用以判斷條件的真、假。
若為真,則執行其對應的主體敘述。
若為假,不理會。
注意,條件運算式的後面要加冒號(:),
而且要執行的主體敘述要內縮,
至於内縮幾格沒有硬性規定,一般是四格。

以下是由使用者輸入一值,指定給變數a,然後判斷
a是否大於0,若是,則印出a大於0的訊息。
若小於等於0,則不加以理會。
» 輸出結果:
Enter a number: 100
100 is great than 0
 Over
'''
a = eval(input('Enter a number: '))
if a > 0:
  print(a, 'is great than 0')
print('Over')

if a != 0:
  print(a, 'is not 0')
print('Over')

if a == 0:
  print(a, 'is 0')
print('Over')

if a == 0:
  print(a, 'is 0')
  print('Over 01')
print('Over')
#2-3
'''語法

if…else 敘述的語法如下:

if  條件運算式:
      主體敘述1
else:
    主體敘述2

其中條件運算式用以判斷條件的真、假。若為真,則執行其對應的主體敘述1。若為假,則執行主體敘述2。
注意,條件運算和 else 的後面都要加冒號(:),而且要執行的主體敘述1和主體敘述2都要内縮。
以下是由使用者輸入一值,指定給變數a,然後判斷 a 是否大於0,若是,則印出 a大於0的訊息。若小於等於0,則印出a小於0的訊息。
» 輸出結果:
(一)
Enter a number: 100
100 is greater than 0
Over

(二)
Enter a number: -100
-100 is less than 0
Over
'''
a = eval(input('Enter a number: '))
if a > 0:
  print(a, 'is greater than 0')
else:
  print(a, 'is less than 0')
print('Over')

#2-4
#範例 01
'''語法
if...elif...else 敘述的語法如下:

if  條件運算式:
    主體敘述1
elif 條件運算式:
    主體敘述2
else:
    主體敘述3

其中條件運算式用以判斷條件的真、假。若為真,則執行其對應的主體敘述1。若為假,再繼續判斷 elif 內的條件運算式,若為真,則執行主體敘述2,否則,
執行主體敘述3。
注意,if 條件運算式、elif 條件運算式和 else 的後面都要加冒號(:),而且要執行 的主體敘述1、主體敘述2,以及主體敘述3都要内縮。

以下是由使用者輸入一值,指定給變數a,然後判斷a是否大於0,若是,則印出
a大於0的訊息。若小於等於0,則印出a小於0的訊息。若a等於0,則印出
a等於0的訊息。
»輸出結果:
(一)
Enter a number: 100
100 is greater than 0
Over

(二)
Enter a number: -100
-100 is less than 0
Over

(三)
Enter a number: 0
0 is equal to 0
Over
'''
a = eval(input('Enter a number: '))
if a > 0:
  print(a, 'is greater than 0')
elif a < 0:
  print(a, 'is less than 0')
else:
  print(a, 'is equal to 0')
print('Over')

## 
a = eval(input('Enter a number of week: '))
if a == 1:
  print(a, '猴子穿新衣')
elif a == 2:
  print(a, '肚子餓猴子')
elif a == 3:
  print(a, '肚子去爬山')
elif a == 4:
  print(a, '肚子去考試')
elif a == 5:
  print(a, '肚子去跳舞')
elif a == 6:
  print(a, '肚子去斗六')
else:
  print(a, '肚子漆油漆')
print('Over')

#範例02
'''在一元二次方程式 ax^2 + bx + c中,求解公式如下:

若 b^2 - 4ac > 0, 則有兩個不同的解;
若 b^2 - 4ac = 0, 則有唯一解;
若 b^2 - 4ac < 0, 則無解。
(一)
Enter a, b, c:  1,  2,  1
Has one solution
Over

(二)
Enter a, b, c:  3,  -2,  1
No solution
Over

(三)
Enter a, b, c:  1,  4,  1
Has two different solutions
Over
'''
a, b, c = eval(input('Enter a, b, c: '))
d = b*b - 4*a*c
print(d)

if d > 0:
  print('Has two different solutions')
elif d == 0:
  print('Has one solution')
else:
  print('No solution')
print('Over')

if d > 0:
  print('Has two different solutions')
  ds = d**0.5
  x1 = (-b + ds)/(2*a)
  x2 = (-b - ds)/(2*a)
  print('X1 = ',x1)
  print('X2 = ',x2)
elif d == 0:
  print('Has one solution')
  ds = d**0.5
  x1 = (-b + ds)/(2*a)
  print('X1 = ',x1)
else:
  print('No solution')
print('Over')

#範例03
'''接下來我們來撰寫根據身高和體重來衡量健康狀況,此稱為BMI (Body Mass Index)。 BMI 的計算如下:
   BMI =  體重 / 〖身高〗^2
其中體重以公斤為單位,而身高以公尺為單位。

BMI 的量測表如下:
表2-2 BMI量測表
   BMI           說明
< 18.5           過輕
18.5~24.9        正常
25.0 ~ 29.9      過重
>= 30           肥胖
 »輸出結果:
Enter height in centimeters: 185
Enter weight in kilograms: 68
Your BMI is 19.87
Normal
'''
height = eval(input('Enter height in centimeters: '))
weight = eval(input('Enter weight in kilograms: '))

bmi = weight / (height/100) ** 2
print('Your BMI is %6.2f'%(bmi))

if bmi < 18.5:
  print('Uderweight')
elif bmi < 25.0:
  print('Normal')
elif bmi < 30:
  print('Overweight')
else:
  print('Obese')

#2-5
#範例 01
'''2-5 邏輯運算子
有時一個條件運算式不足以檢視問題的真假,則需要多個條件運算式時,則必需藉助邏輯運算子(logical operator)。如表2-3 所示:
表2-3 邏輯運算子               
運算子     意義
 and      且
 or       或
 not      反
例如,檢視使用者輸入的數值是否介於85 與 95 之間。以Python 程式撰寫
如下, 其中用到邏輯運算子:
»輸出結果:
(一)
Enter a number: 100
100 is not in the between 85 and 95
Over
(二)
Enter a number: 90
90 is in the between 85 and 95
Over
'''
num = eval(input('Enter a number: '))
if (85 <= num) and (num <= 95):
  print('%d is in the between 85 and 95' %(num))
else:
  print('%d is not in the between 85 and 95' %(num))

  print('Over')

#範例 02
#其實上一程式也可以這樣寫，如下所示:
'''»輸出結果:
(一)
Enter a number: 100
100 is not in the between 85 and 95
Over

(二)
Enter a number: 90
90 is in the between 85 and 95
Over

其中條件運算式
if (85 <=  num <= 95):

相當於
if (85 <= num) and (num<=95):

你喜歡哪一種?
'''
num = eval(input('Enter a number: '))
if (85 <= num <= 95):
  print('%d is in the between 85 and 95' %(num))
else:
  print('%d is not in the between 85 and 95' %(num))

print('Over')

#綜合範例 01
'''偶數判斷

1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,判斷輸入值是否為偶數,使輸
出值符合題意要求。請另存新檔為PYA02.py,作答完成請儲存所有檔案至 C:\ANS. CSF 原資料夾內。
2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入一個正整數,然後判斷它是否
為偶數(even)。
3. 輸入輸出:
(1) 輸入說明: 一個正整數
(2) 輸出說明: 判斷是否為偶數
(3) 範例輸入: 56  (範例輸出: 不Key了)
(4) 範例輸入: 21  (範例輸出: 不Key了)
'''
10%2
10%3
a = int(input("please input an 整數"))

if a%2 == 0:
  print('%d is an even number.' % a)
else:
  print('%d is not an even number.' % a)
  
if a%2 != 0:
  print('%d is an odd number.' % a)
else:
  print('%d is an even number.' % a)

#綜合範例 02
'''倍數判斷
1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,判斷輸入值是否為3或5 的倍 數,使輸出值符合題意要求。請另存新檔為PYA02.py,作答完成請儲存所有檔案至C:\ANS. CSF 原資料夾內。
2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入一個正整數,然後判斷它是3 或5 的倍數,顯示【x is a multiple of 3.】或【x is a multiple of 5.);
若此數值同時為3與5的倍數,顯示【x is a multiple of 3 and 5.】;
如此數值皆不屬於3或5 的倍數,顯示【x is not a multiple of 3 or 5. 】,
將使用者輸入的數值代入x。
3. 輸入輸出:
(1) 輸入說明: 一個正整數
(2) 輸出說明: 判斷是否為3或5 的倍數
(3) 範例輸入: 55   (範例輸出: 不Key了)
(4) 範例輸入: 36   (範例輸出: 不Key了)
(5) 範例輸入: 92   (範例輸出: 不Key了)
(6) 範例輸入: 15   (範例輸出: 不Key了)
'''
a = int(input())

if (a%3 == 0) and (a%5 == 0):
  print('%d is a mutiple of 3 and 5.' % a)
elif a%3 == 0:
  print('%d is a mutiple of 3.' % a)
elif a%5 == 0:
  print('%d is a mutiple of 5.' % a)
else:
  print('%d is not a mutiple of 3 or 5.' % a)

#綜合範例 03
'''閏年判斷

1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,判斷輸入值是否為閏年,使輸出值符合題意要求。
請另存新檔為 PYA02.py,作答完成請儲存所有檔案至 C:\ANS.CSF 原資料夾內。

2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入一個西元年份,然後判斷它是
否為閏年(leap year)或平年。其判斷規則為:每四年一閏,每百年不閏,
但每四百年也一閏。

3. 輸入輸出:
(1) 輸入說明:  一個正整數
(2) 輸出說明:  判斷是否為閏年或平年
(3) 範例輸入:  1992   (範例輸出: 不Key了)

(4) 範例輸入:  2010   (範例輸出: 不Key了)
'''
year = int(input())

if year%400==0 or (year%4==0 and year%100!=0):
  print('year, is a leap year.')
else:
  print(year, 'is not a leap year')

#綜合範例 04
'''算術運算
1. 題目說明:
請開啟 PYD02.py檔案,依下列題意進行作答,依輸入值進行算術運算,使輸
出值符合題意要求。請另存新檔為 PYA02.py,作答完成請儲存所有檔案至 C:\ANS.CSF原資料夾內。
2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入兩個整數a、b,然後再輸入一
算術運算子(+、-、*、/、// 、%),輸出這兩個數以及其經過運算後的結果 。

3. 輸入輸出:
(1) 輸入說明: 兩個整數a、b,及一個算術運算子(+、-、*、/、// 、%)
(2) 輸出說明: 運算結果(無須做格式化)
(3) 範例輸入：
30
60
*
1800
'''
a = eval(input())
b = eval(input())
opr = input()
ans = 0

if opr == '+': ans = a + b
elif opr == '-': ans = a - b
elif opr == '*': ans = a * b
elif opr == '/': ans = a / b
elif opr == '//': ans = a // b
elif opr == '%': ans = a % b

print(ans)

if opr == '+': 
    ans = a + b
elif opr == '-': 
    ans = a - b
elif opr == '*': 
    ans = a * b
elif opr == '/': 
    ans = a / b
elif opr == '//': 
    ans = a // b
elif opr == '%': 
    ans = a % b

print(ans)

if opr == '+': ans = a + b
elif opr == '-': ans = a - b
elif opr == '*': ans = a * b
elif opr == '/': ans = a / b
elif opr == '//': ans = a // b
else: ans = a % b

print(ans)

#綜合範例 05
'''字元判斷

1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,判斷輸入值的字元,使輸出值
符合題意要求。請另存新檔為 PYA02.py,作答完成請儲存所有檔案至 C:\ANS. CSF 原資料夾內。

2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入一個字元,判斷它是包括
大、 小寫的英文字母(alphabet)、數字(number)、或者其它字元(symbol)。
例如: a為英文字母、9為數字、$為其它字元。

3. 輸入輸出:
(1) 輸入說明: 一個字元
(2) 輸出說明: 判斷是英文字母(包括大、小寫)、數字、或者其它字元,
(3) 範例輸入:  P    (範例輸出: 不Key了)
(4) 範例輸入: @   (範例輸出: 不Key了)
(5) 範例輸入:  7    (範例輸出: 不Key了)
'''
c = input("輸入一個字元")

if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
  print(c, 'is an alphabet')
elif ('0' <= c <= '9'):
  print (c, 'is a number.')
else:
  print(c, 'is a symbol.')
  
####  
c = input("輸入一個字元")
if ('a' <= c <= 'z') :
  print(c, 'is an 小 alphabet')
elif ('A' <= c <= 'Z'):
  print (c, 'is an 大 alphabet')
elif ('0' <= c <= '9'):
  print (c, 'is a number.')
else:
  print(c, 'is a symbol.')

#綜合範例 06
'''等級判斷
1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,判斷輸入值所對應的等級,使輸出值符合題意要求。
請另存新檔為PYA02.py,作答完成請儲存所有檔案至
C:\ANS.CSF原資料夾內。

2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,根據使用者輸入的分數顯示對應的等級。
(2) 標準如下表所示:
  分數         等級
80 ~ 100        A
70 ~ 79         B
60 ~ 69         C
<= 59           F
3. 輸入輸出:
(1) 輸入說明:  一個整數
(2) 輸出說明: 判斷輸入值所對應的等級
(3) 範例輸入:  79   (範例輸出: 不Key了)
'''
score = eval(input())

if 80 <= score <= 100:
  grade = 'A'
elif 70 <= score <= 79:
  grade = 'B'
elif 60 <= score <= 69:
  grade = 'C'
elif score <= 59:
  grade = 'F'

print(grade)

#綜合範例 07
'''折扣方案

1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,判斷輸入值之折扣並計算實付 金額,使輸出值符合題意要求。請另存新檔為PYA02.py,作答完成請儲存所
有檔案至C:\ANS.CSF 原資料夾內。

2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,要求使用者輸入購物金額,購物金額需大於
8,000(含)以上,並顯示折扣優惠後的實付金額。
(2) 購物金額折扣方案如下表所示:
金額              折扣
8,000   (含)以上        9.5折
18,000 (含)以上        9折
28,000 (含)以上        8折
38,000 (含)以上        7折

3. 輸入輸出:
(1) 輸入說明:  一個數值,需大於8,000 (含)以上
(2) 輸出說明:  顯示折扣優惠後的實付金額(輸出不需指定小數點位數)
(3) 範例輸入:  12000   (範例輸出: 不Key了)
'''
cost = eval(input())

if cost >= 38000:
  pay = cost * 0.7
elif cost >= 28000:
  pay = cost * 0.8
elif cost >= 18000:
  pay = cost * 0.9
elif cost >= 8000:
    pay = cost *0.95

print(pay)

#綜合範例 08
'''十進位換算
1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,依輸入值進行進位轉換,使輸出值符合題意要求。
請另存新檔為 PYA02.py,作答完成請儲存所有檔案至 C:\ANS.CSF 原資料夾內。

2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入一個十進位整數
num ( 0 ≤  num  ≤15 ),將 num 轉換成十六進位值。

* 提示: 轉換規則 = 十進位0~9的十六進位值為其本身,十進位 10~15 的
十六進位值為A~F。
3. 輸入輸出:
(1) 輸入說明:  一個數值
(2) 輸出說明:  將此數值轉換成十六進位值
(3) 範例輸入: 13   (範例輸出: 不Key了)
(4) 範例輸入:  8    (範例輸出: 不Key了)
'''
num = eval(input())

if 0 <= num <= 9: hex_num = num
elif num == 10:   hex_num = 'A'
elif num == 11:   hex_num = 'B'
elif num == 12:   hex_num = 'C'
elif num == 13:   hex_num = 'D'
elif num == 14:   hex_num = 'E'
elif num == 15:   hex_num = 'F'

print(hex_num)

#綜合範例 09
#計算x,y座標與座標(5,6)之距離是否小於或等於15
'''距離判斷

1 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,計算輸入值之座標,使輸出值
符合題意要求。請另存新檔為 PYA02.py,作答完成請儲存所有檔案至
C:\ANS. CSF原資料夾内。

2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入一個點的平面座標x和y值,
判斷此點是否與點(5,6)的距離小於或等於15,如距離小於或等於15 顯示
【Inside】, 反之顯示【Outside】。
* 提示: 計算平面上兩點距離的公式
3. 輸入輸出:
(1) 輸入說明: 兩個數值x、y
(2) 輸出說明: 小於或等於15 輸出 Inside ; 大於15 輸出 Outside
(3) 範例輸入:  7 、20    (範例輸出: 不Key了)
(4) 範例輸入: 30 、35   (範例輸出: 不Key了)
'''
x = eval(input('第一個數值x'))
y = eval(input('第二個數值y'))
dist = ((x-5)**2 + (y-6)**2) ** 0.5

if dist <= 15:
  print('Inside')
else:
  print('Outside')

#綜合範例10
#輸入三角形邊長，檢查是否能形成三角形並輸出周長
'''三角形判斷

1. 題目說明:
請開啟 PYD02.py 檔案,依下列題意進行作答,檢查輸入值是否可組成三角形, 使輸出值符合題意要求。請另存新檔為PYA02.py,作答完成請儲存所有檔案 至C:\ANS. CSF原資料夾內。
2. 設計說明:
(1) 請使用選擇敘述撰寫一程式,讓使用者輸入三個邊長,檢查這三個邊長
是否可以組成一個三角形。若可以,則輸出該三角形之周長;否則顯示 【Invalid】。
* 提示: 檢查方法 = 任意兩個邊長之總和大於第三邊長。
3. 輸入輸出:
(1) 輸入說明: 三個正整數
(2) 輸出說明: 可以組成三角形則輸出周長;否則顯示 Invalid
(3) 範例輸入:  5、6、13   (範例輸出: 不Key了)
(4) 範例輸入:  1、1、1     (範例輸出: 不Key了)
'''
side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

if side1+side2 > side3 \
  and side2+side3 > side1 \
  and side1+side3 > side2:
    print(side1+side2+side3)
else:
  print('Invalid')
  
if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2:
    print(side1+side2+side3)
else:
  print('Invalid')
  
if side1+side2 > side3 \
   and side2+side3 > side1 \
   and side1+side3 > side2:
    print(side1+side2+side3)
else:
  print('Invalid')

#y綜合範例11
#點座標與矩形中心點水平距離小於或等於8/2，而且垂直距離小於或等於6/2，則點在矩形內否則外
'''請使用選擇敘述撰寫一程式,由使用者輸入整數的點座標(x,y),然後檢視該點是 否位於中心點為(0, 0), 長為8, 高為6的矩形内。

* 提示: 如果此點與矩形中心點之水平距離小於或等於8 / 2, 而且垂直距離
小於或等於6 / 2,則此點位於矩形内,否則位於矩形外。

1. 輸入輸出1:
(1) 範例輸入:  4 , 4   (範例輸出: 不Key了)

2. 輸入輸出2: ,
(1) 範例輸入:  4 , 3   (範例輸出: 不Key了)
'''
x1, y1 = eval(input())
if abs(x1) <= 8/2 and abs(y1) <= 6/2:
  print('(%d, %d) is inside of the rectangle' %(x1, y1))
else:
  print('(%d, %d)is outside of the rectangle' %(x1, y1))

#綜合範例 12
'''請使用選擇敘述撰寫一程式,利用亂數產生器產生介於1~100 之間的亂數,
然後檢視這個亂數是偶數或是奇數。
* 提示: 如果此亂數除以2,餘數為0時,則為偶數,否則為奇數。

1. 輸入輸出1:
(1) 範例輸入:  無   (範例輸出: 不Key了)

2. 輸入輸出2:
(1) 範例輸入:  無   (範例輸出: 不Key了)
'''
import random
num = random.randint(1, 100)
if num % 2 == 0:
  print('%d is even number.' %(num))
else:
  print('%d is odd number.' %(num))

#綜合範例 13
#二元一次方程式
'''請使用選擇敘述撰寫一程式,利用克拉瑪(Cramer's rule)公式解二元一次方程式。
假設有二個二元一次方程式,如下所示:
ax + by = c
dx + ey = f
其中a, b, c, d, e, f皆為整數, x與y的解如下:
x = (ce - bf) / (ae - bd)
y = (af - cd) / (ae - bd)

* 提示: 如果(ae - bd)為0,則表示有無限多組解或無解。

1. 輸入輸出1:
(1) 範例輸入: Enter a, b, c: 1, 2, 4
Enter d, e, f: 2, 4, 5        (範例輸出: 不Key了)

2. 輸入輸出2:
(1) 範例輸入: Enter a, b, c: 9,  4 , -6
Enter d, e, f: 3,  -5, -21   (範例輸出: 不Key了)
'''
a, b, c = eval(input('Enter a, b, c: '))
d, e, f = eval(input('Enter d, e, f: '))

if a*e - b*d == 0:
  if c*e - b*f == 0 and a*f - c*d == 0:
    print('有無限多個解')
  else:
    print('無解')
else:
  x = (c*e - b*f) / (a*e - b*d)
  y = (a*f - c*d) / (a*e - b*d)
  print('x is %.2f, y = %.2f'  %(x,y))

#綜合範例 14
#輸入三位數是否為迴文數
'''請使用選擇敘述撰寫一程式,讓使用者輸入的三位數的整數,檢視它是否為
迴文數 (palindrome number)。

1. 輸入輸出1:
(1) 範例輸入:  131   (範例輸出: 不Key了)

2. 輸入輸出2:
(1) 範例輸入:  122   (範例輸出: 不Key了)
'''
number = eval(input('Enter a three-digit integer: '))
reversedNumber = (number % 10) * 100 + (number // 10 % 10) * 10 +(number // 100)

if number == reversedNumber:
  print(number, 'is a palindrome number.')
else:
  print(number, 'is not a palindrome number.')

#綜合範例 15
#sort排序三個整數
'''請使用選擇敘述撰寫一程式,輸入三個整數,並由小至大加以排序後印出。

1. 輸入輸出:
(1) 範例輸入:  Enter three integers:  8,  6,  1   (範例輸出: 不Key了)
'''
num1, num2, num3 = eval(input('Enter three integrs: '))
if num1 > num2:
  (num1, num2) = (num2, num1)
if num2 > num3:
  (num2, num3) = (num3, num2)
if num1 > num2:
 ( num1, num2) = (num2, num1)

print('The sorted numbers are', num1, num2, num3)
