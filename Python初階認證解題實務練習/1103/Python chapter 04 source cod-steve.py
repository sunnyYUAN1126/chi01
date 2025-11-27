'''Chapter 4 進階控制流程 ===========================================

此章的進階控制流程其實就是前面二章的應用,
也就是將選擇敘述與迴圈敘述混搭來完成你的工作。
利用迴圈敘述加上選擇敘述,好比如虎添翼般的更具有威力, 請參閱以下的範例程式。

## 4-1 亂數產生器 ===================================================
試撰寫一程式產生10個亂數,程式如下所示:
範例 01
輸出： 4   63   33    6   99    3   18   19   24   84
'''
import random
for i in range(1, 11):
      randNum = random.randint(1, 100)
      print( '%4d' %(randNum), end = ' ' )

# 補充說明     
import random
# 產生 1 到 100 的一個整數型隨機數
print( random.randint(1,1000) ) 
# 產生 0 到 1 之間的隨機浮點數
print( random.random() ) 

# 產生 1.1 到 5.4 之間的隨機浮點數，區間可以不是整數
print( random.uniform(1.1,5.4) ) 

# 從序列中隨機選取一個元素
print( random.choice('tomorrow') ) 

a=[1,3,5,6,7] # 將序列a中的元素順序打亂
random.shuffle(a)
print(a)
         
      
'''若要檢視所產生的10亂數中有多少個是偶數或是奇數,此時就必需藉助選擇敘述來判斷。
如下範例程式所示:
範例 01    '''

import random
even = 0
odd = 0
for i in range(1, 11):
      randNum = random.randint(1, 100)
      print(randNum, end = ' ')
      if randNum % 2 == 0:
           even += 1
      else:
           odd += 1
print( ' \neven = %d, odd = %d' %(even, odd))

#此程式較上一程式多了以下的敘述:
#範例程式:
'''
randNum = random.randint(1, 100)
if randNum % 2 == 0:
       even += 1
else:
       odd += 1

以及用來印出偶數和奇數個數的 print 敘述:
print('\neven = %d, odd = %d'%(even, odd))

輸出：
38 54 66 26 95 66 19 85 91 8
even = 6, odd = 4
'''
# 範例 02 產生100個亂數
import random
even = 0
odd = 0
for i in range(1, 101):
      randNum = random.randint(1, 100)
      print(randNum, end = ' ')
      if randNum % 2 == 0:
           even += 1
      else:
           odd += 1
print( ' \neven = %d, odd = %d' %(even, odd))

''' 範例 03
再產生多一點的亂數,今利用亂數產生器產生100 個亂數,
然後判斷這些亂數有多少個是 3 的倍數, 5 的倍數, 7 的倍數,
和 不為3或5或7倍數 的個數?   

>>> ? 幾種判斷?  還有 迴圈 FOR
>>> 有起始值嗎?
>>> 旗標 flag 的目的?

則程式如下所示:

'''
# Version 01
import random
# random.seed(100)  # 初始化亂數種子

times3 = 0
times5 = 0
times7 = 0
others = 0
for i in range(1, 101):
     flag = False      # why?  >>> else ok?
     randNum = random.randint(1, 100)
     print(randNum, end = '*')
     if randNum % 3 == 0:
          times3 += 1
          flag = True
     if randNum % 5 == 0:
          times5 += 1
          flag = True
     if randNum % 7 == 0:
            times7 +=1
            flag = True
     if flag == False:
            others += 1
print('\ntimes3 = %d, times5 = %d , times7 = %d'%(times3,
         times5, times7))
print('others = %d'%(others))
'''
輸出：66 4 88 55 1 54 60 99 65 39 32 39 51 7 42 62 89 48 97 39 17 78 37 77 38 25 68 56 3 49 88 17 88 7 98 81 53 3 54 79 15 54 89 46 19 57 66 43 39 25 16 1 44 35 79 36 62 77 71 34 62 46 22 57 98 64 16 16 6 31 36 41 70 41 94 92 58 22 48 40 8 60 65 51 62 8 86 28 100 62 74 8 29 49 34 56 84 63 27 34
times3 = 30, times5 = 12 , times7 = 16
others = 50
'''

import random
# random.seed(100)  # 初始化亂數種子

times3 = 0
times5 = 0
times7 = 0
others = 0
for i in range(1, 101):
     #flag = False      # why?  >>> else ok?
     randNum = random.randint(1, 100)
     print(randNum, end = ' ')
     if randNum % 3 == 0:
          times3 += 1
          #flag = True
     elif randNum % 5 == 0:
          times5 += 1
          #flag = True
     elif randNum % 7 == 0:
            times7 +=1
            #flag = True
     else: 
            others += 1
print('\ntimes3 = %d, times5 = %d , times7 = %d'%(times3,
         times5, times7))
print('others = %d'%(others))

''' 範例 04
此程式和上一程式差不多都使用選擇敘述來判斷所產生的亂數是3或5或7的倍數，和不為3或5或7倍數的個數。程式雖然可正確的執行，但其輸出結果並不怎麼美觀，
以下程式將針對此點做了一些改善，請參閱以下範例程式:

#### 程式中以count 變數來控制每一列要印出10個數。
當 count 可被 10 整除時,則要跳行,所以其對應的 print 敘述不必加 end =' ' 。

輸出：   18    52    85    93    20    19    86    81    66    92
   26    97    29    31    32    61     2     4    37     1
   50    76    24    12    90    27    95    89    77    86
   44    99    76    61    57    73    37    27     6    16
    9    74    90    17    55    56    95    53    54    47
   28     9    93    28    31    84    20    84    54    99
   98     8    94    17    16    96    59    66    72    27
   58    59    21    99    24     1    99    55    40    97
   40    93    38    97    12    74    50    10    67    56
   27    69    16    16    10    14    73    21    53    68

times3 = 34, times5 = 15 , times7 = 11
others = 48
'''
import random

times3 = 0
times5 = 0
times7 = 0
others = 0
count = 1

for i in range(1,101):
    flag = False
    randNum = random.randint(1,100)
    if count % 10 != 0:
        print('%5d'%(randNum), end = ' ')
    else:
        print('%5d'%(randNum))   # 這裡做換行 處理
    count += 1
    # Calculate times3, times5, and times7
    if randNum % 3 == 0:
        times3 += 1
        flag = True
    if randNum % 5 == 0:
        times5 += 1
        flag = True
    if randNum % 7 == 0:
        times7 +=1
        flag = True
    if flag == False:
        others += 1
print('\ntimes3 = %d, times5 = %d , times7 = %d' %(times3, times5, times7))
print('others = %d'%(others))

'''
## 4-2 定數迴圈與不定數迴圈 ====================================================
當迴圈有固定執行的次數時,我們稱之為定數迴圈。
而不定數迴圈,表示沒有固定的迴圈執行次數,使用者隨時可以以另一種方式來中止迴圈的執行。
例如,產生10次的1到49 的亂數,此為定數迴圈,因為我們固定它執行10次。 程式如下所示:
    此程式為多重迴圈,在外迴圈的 while 用來控制產生多少(10)次的亂數,以count 變數來輔助。
而在內迴圈的 for 則產生六個1~49的亂數。
範例 01
輸出：
 23  30  25   9  36  36
 42  21  11  29   2  28
  3  22  11  41  10  31
 15  42  22  46  43  47
  4  49  32  15   7  39
 23  19  25  47  46  47
 17   2  14   4   1  10
  2  28  13  21  20  31
 18  40  12   3  35  24
 18  33  33  29  13  43
Over
'''
import random
count = 1
while count <= 10:

    for i in range(1, 7):
        randNum = random.randint(1, 49)
        print('%3d'%(randNum), end =' ')
    print()
    count += 1 # count = count +1
print('Over')

'''
我們現在以不定數迴圈來實作之。

程式中以交談式的方式詢問使用者是否要再繼續產生六個1~49 的亂數。如以下範例程式所示:

程式中以 again 變數來控制程式是否繼續產生六個1~49 的亂數。
以交談式的方式引導使用者輸入一數值,並指定給 again 變數,
若輸入1,則表示繼續產生六個1~49 的亂數,
若為0,則結束迴圈的執行。
範例 02
輸出：
 47  32  14  49  14   9
continue:1 or quit:0   >1
 49  34  42  49  17  42
continue:1 or quit:0   >0
Over
'''
import random
again = 1
count = 1
while again == 1:
    for i in range(1, 7):
        randNum = random.randint(1, 49)
        print('%3d'%(randNum), end =' ')
    print()
    again = eval(input('continue:1 or quit:0   >'))  # 使用者做決定!
print('Over')

######
import random
#again = 1
count = 1

again = eval(input('continue:1 or quit:0   >')) 
while again == 1:
    for i in range(1, 7):
        randNum = random.randint(1, 49)
        print('%3d'%(randNum), end =' ')
    print()
    again = eval(input('continue:1 or quit:0   >'))  # 使用者做決定!
print('Over')

'''
### 4-3 break 與 continue 敘述 =============================================
Python 和C一樣也提供了break 和 continue 敘述。
break 表示終止執行包含此敘述的迴圈。

若將上一程式改以無窮迴圈的方式執行時, # 何謂 無窮迴圈 ?
則必需在程式中有一break 敘述用來終止它。

程式中的
while True:
    
表示它是一無窮迴圈,當程式提示使用者輸入again 時,若它為0,則以 break 來
結束迴圈,以結束與此 break 對應的 while 迴圈,注意,不是結束 for迴圈喔!
範例 01
輸出：
16 43 16 37 31 13
continue:1 or quit:0 ---->1
3 15 1 4 38 17
continue:1 or quit:0 ---->1
36 34 13 48 8 31
continue:1 or quit:0 ---->0
Over
'''
import random
while True:
    for i in range(1, 7):
        randNum = random.randint(1, 49)
        print(randNum, end =' ')
    print()
    again = eval(input('continue:1 or quit:0 ---->'))
    if again == 0:
        break
print('Over')

'''再舉一範例來說明 break 敘述,以亂數產生器產生兩個亂數,
分別指定給nl 和 n2, 然後由使用者輸入這兩個數字的和。
若答錯,則將繼續做答;若答對,則以 break 敘述結束迴圈的執行。如下所示:
範例 02
輸出：
57 + 80 = 137
Correct, you are very good.
Over

58 + 25 = 0
Wrong answer, try again.
58 + 25 = 83
Correct, you are very good.
Over
'''
import random
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
while True:
    solution = n1 + n2
    answer = eval(input( '%d + %d = '%(n1,n2)))
    if answer == solution:
        print('Correct, you are very good.')
        break
    else:
        print('Wrong answer, try again.')
print('Over')

'''程式中也是以  提供 continue 敘述
while True:
的無窮迴圈格式來執行程式。除了break 敘述外,
Python 也提供了continue 敘述, 它表示不繼續執行continue 以下的敘述,
而直接回到迴圈的條件運算式進行判斷。

此程式是在計算由 1 到 15 中,將 5 的倍數去除, 其餘的數字印出並加總。

所以 當 number 為5的倍數時, 則執行 number 加 1 與 continue,
不加以執行印出和加總的動作,

再回到while 的條件運算式檢視 number 是否小於等於15。
如下範例程式:
範例 03
輸出：
1   2   3   4   6   7   8   9  11  12  13  14
total = 90
答案很明顯,只有執行1加到14,當 number 為15時,就執行 break 敘述,導致整個迴圈終止。
'''
total = 0
number = 1
while number <= 15:
    if number % 5 == 0:
        number += 1
        continue
    print('%3d'%(number), end =' ')
    total += number
    number += 1
print('\ntotal = %d' %(total))

'''
continue  改為 break 敘述
答案很明顯,只有執行 1 加到 4,當 number 為 5 時,就執行 break 敘述,導致整個迴圈終止。
'''
total = 0
number = 1
while number <= 15:
    if number % 5 == 0:
        number += 1
        break
    print('%3d'%(number), end =' ')
    total += number
    number += 1
print('\ntotal = %d' %(total))
'''
  1   2   3   4 
total = 10
'''

'''
### 綜合範例1: =================================================
設計說明:
(1) 請撰寫一程式,由使用者輸入 十 個數字,然後找出其最小值,最後輸出最小值。

輸入輸出:
(1) 輸入說明: 十個數值
(2) 輸出說明: 十個數值中的最小值
(3) 範例輸入: 23 57 48 2 99 70 9 65 35 88
輸出：2
'''
total = 10

min_num = eval(input('使用者請依序輸入 十 個數字:')) # 第一個數字
for i in range(total-1):
      print(i)
      num = eval(input( ))
      if num < min_num:
           min_num = num
print(min_num)


### 程式碼改善! why?
total = 10
count = 1
min_num = eval(input('使用者請依序輸入 十 個數字: 第一個數字:')) # 第一個數字
for i in range(total-1):
      print('i 目前為 %d' % i)
      count += 1
      num = eval(input( '使用者請依序輸入 十 個數字: 第 %d 個數字:' %count))
      if num < min_num:
           min_num = num
print('最小數字為 %d' %min_num)

###
total = 10
count = 1
sum = 0
max_num = eval(input('使用者請依序輸入 十 個數字: 第一個數字:')) # 第一個數字
sum = sum + max_num
for i in range(total-1):
      print('i 目前為 %d' % i)
      count += 1
      num = eval(input( '使用者請依序輸入 十 個數字: 第 %d 個數字:' %count))
      sum = sum + num
      if num > max_num:
           max_num = num
print('最小數字為 %d' %max_num)
print('sum=  %d' %sum)


'''綜合範例2: =============================================================
設計說明:
(1) 請撰寫一程式,讓使用者輸入數字,輸入的動作直到輸入值為9999 才結
來,然後找出其最小值,並輸出最小值。

3. 輸入輸出:
(1) 輸入說明: n個數值,直至9999 結束輸入
(2) 輸出說明: n個數值中的最小值
(3) 範例輸入: 29 100 948 377 -28 0 -388 9999
輸出：-388
'''
num = eval(input('請使用者輸入一個數字, 若是輸入值為9999 停止: ' ))
min_num = num

while num != 9999:
    num = eval(input('請使用者輸入一個數字, 若是輸入值為9999 停止: ' ))
    if num < min_num:
        min_num = num

print('數值中的最小值: %d' %min_num)

### 程式碼改善! 找最大值呢?
num = eval(input('請使用者輸入一個數字, 若是輸入值為9999 停止: ' ))
min_num = num

while num != 9999:
    num = eval(input('請使用者輸入一個數字, 若是輸入值為9999 停止: ' ))
    if num > min_num :
        min_num = num

print('數值中的最大值: %d' %min_num)

#### 正確程式碼:
num = eval(input('請使用者輸入一個數字, 若是輸入值為9999 停止: ' ))
min_num = num

while num != 9999:
    num = eval(input('請使用者輸入一個數字, 若是輸入值為9999 停止: ' ))
    if num > min_num and num != 9999 :
        min_num = num

print('數值中的最大值: %d' %min_num)

'''綜合範例3: ============================================================
設計說明:
(1) 請撰寫一程式,讓使用者輸入兩個正整數a、b (a<=b),
輸出從a到b (包含a和b)之間4或9之倍數(一列輸出十個數字、欄寬為4、靠左對齊) 
以及倍數之個數、總和。

輸入輸出:
(1) 輸入說明: 兩個正整數a、b (a<=b)
(2) 輸出說明: 格式化輸出兩個正整數之間4或9之倍數(包含a和b)
倍數個數、倍數總合
(3) 範例輸入:  5  55
輸出：
8    9    12   16   18   20   24   27   28   32
36   40   44   45   48   52   54
17 #個數
513 #總和
'''
a = int(input('輸入兩個正整數a、b (a<=b), a = '  )) 
b = int(input('輸入兩個正整數a、b (a<=b), b = ' )) 
count = total_sum = 0 
time = 10 
for i in range(a, b + 1): 
      if i % 4 == 0 or i % 9 == 0: 
           print( '%-4d' %i, end=' ' ) 
           total_sum += i 
           count += 1 
           if count % time == 0:   # 一列輸出十個數字
                print( ) 
if count > 0 and count % 10 != 0 : 
       print( ) 
print( '%d'%(count)) 
print(total_sum) 

### 程式碼改善! 如果輸入錯誤呢?
a = int(input('輸入兩個正整數a、b (a<=b), a = '  )) 
b = int(input('輸入兩個正整數a、b (a<=b), b = ' )) 

if a > b:
    a,b = b,a #python交換兩個值得方法非常簡單，即a,b = b,a，一步操作就交換了兩個值

count = total_sum = 0 
time = 10 
for i in range(a, b + 1): 
      if i % 4 == 0 or i % 9 == 0: 
           print( '%-4d' %i, end=' ' ) 
           total_sum += i 
           count += 1 
           if count % time == 0:   # 一列輸出十個數字
                print( ) 
if count > 0 and count % 10 != 0 : 
       print( ) 
print( '%d'%(count)) 
print(total_sum) 

'''綜合範例4: ===========================================================
2. 設計說明:
(1) 請撰寫一程式,讓使用者輸入一個正整數,將此正整數以反轉的順序輸出,
並判斷斷如輸入為0,則輸出為0。
3. 輸入輸出:
(1) 輸入說明: 一個正整數或 0
(2) 輸出說明: 正整數反轉輸出。如輸入數值為0,輸出為0
(3) 範例輸入: 31283
(4) 範例輸入: 0
(5) 範例輸入: 135790
輸出：
31283
3 8 2 1 3
0
0
135790
0 9 7 5 3 1
'''
number = eval(input('輸入一個正整數:' ))

if number == 0:
    print(number)
else:
    while number != 0 :
        print(number % 10, end=' ')
        number //= 10
        print('number = ', number)

### 程式碼改善! 如果輸入錯誤 成 小數 12345.6 呢? 
# python 判斷 整數 type(x) == int
number = eval(input('輸入一個正整數:' ))
print('number=', number)
if type(number) != int:   
    number = int(number)
    print('你輸入數值為小數 已經為您 轉成整數=', number)

if number == 0:
    print(number)
else:
    while number != 0 :
        print(number % 10, end=' ')
        number //= 10   # number = number // 10

'''綜合範例5: ============================================================
2. 設計說明:
(1) 請撰寫一程式,以不定數迴圈的方式輸入一個正整數(代表分數),之後根據以下分數與 GPA的對照表,
印出其所對應的GPA。假設此不定數迴圈輸入-9999則會結束此迴圈。
(2) 標準如下表所示:
分數           GPA
90 ~ 100        A
80 ~ 89         B
70 ~ 79         C
60 ~ 69         D
0 ~ 59          E

3. 輸入輸出:
(1) 輸入說明: 一個正整數,直至-9999 結束輸入
(2) 輸出說明: 依輸入值,輸出對應的GPA
(3) 輸入與輸出會交雜如下,輸出之項目以粗體字表示
輸出：
80
B
60
D
70
C
100
A
-9999
'''
grade = ""
score = int(input('輸入成績:-9999 結束輸入:'))
while score != -9999:
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score <= 89:
        grade = 'B'
    elif score >= 70 and score <= 79:
        grade = "C"
    elif score >= 60 and score <= 69:
        grade = "D"
    else:
        grade = "E"
    #print('輸入成績 %d GPA 為 %s:' %score %grade)
    print('輸入成績 %d GPA 為 %s:' %(score, grade))

    score = eval(input('輸入成績:-9999 結束輸入:'))
    
###  如何修改錯誤?
#輸入成績:120
#輸入成績 120 GPA 為 E:

'''綜合範例6: =========================================================
2. 設計說明:
(1) 請撰寫一程式,以不定數迴圈的方式輸入身高與體重,計算出 BMI 之後再
根據以下對照表,印出 BMI 及相對應的 BMI 代表意義(State)。
假設此不定數迴圈輸入-9999則會結束此迴圈。

*提示: BMI = 體重(kg)/身高^2(m),輸出浮點數到小數點後第二位。
           不需考慮男性或女性標準。
(2) 標準如下表所示:
BMI 值                         代表意義
BMI < 18.5                  under weight
18.5 <= BMI < 25        normal
25.0 <= BMI < 30          over weight
30 <= BMI                   fat

3. 輸入輸出:
(1) 輸入說明: 兩個正數(身高cm、體重kg),直至-9999 結束輸入
(2) 輸出說明: 輸出 BMI 值, BMI值代表意義
(3) 輸入與輸出會交雜如下,輸出之項目以粗體字表示
輸出：
175
90
BMI: 29.39
-9999
'''
state = ""
height = eval(input('你的身高cm -9999 結束輸入:'))
while height != -9999:
    weight = eval(input('你的體重kg:' ))
    bmi = weight / (height / 100 * height / 100)
    if weight == -9999:
        break
    elif bmi >= 30:
        state = "fat"
    elif bmi >= 25 and bmi < 29.9:
        state = "over weight"
    elif bmi >= 18.5 and bmi <= 24.9:
        state = "normal"
    elif bmi < 18.5:
        state = "under weight"
    print("BMI: %.2f " % bmi)
    print("state: %s " % state)
    height = eval(input('你的身高cm -9999 結束輸入:'))

'''綜合範例7: ===============================================================
2. 設計說明:
(1) 請撰寫一程式,以不定數迴圈的方式讓使用者輸入西元年份,
然後判斷它是否為閏年(leap year)或平年。
其判斷規則為:每四年一閏,每百年不閏,但每四百年也一閏。
(2) 假設此不定數迴圈輸入-9999則會結束此迴圈。
3. 輸入輸出:
(1) 輸入說明: 一個正整數,直至-9999 結束輸入
(2) 輸出說明: 判斷是否為閏年或平年
(3) 輸入與輸出: 會交雜如下,輸出之項目以粗體字表示
輸出：
2020
2020 is a leap year.
2019
2019 is not a leap year.
-9999
'''
year = eval(input('請輸入西元年分:'))
while year != -9999:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
    year = eval(input('請輸入西元年分:'))

## 民國年分呢?

'''綜合範例8: ===============================================================
設計說明:
(1) 請撰寫一程式,讓使用者輸入十個整數,計算並輸出偶數和奇數的個數。

3. 輸入輸出:
(1) 輸入說明: 十個整數
(2) 輸出說明: 偶數的個數, 奇數的個數
(3) 範例輸入: 69 48 19 91 83 22 18 37 82 40
輸出：
69
48
19
91
83
22
18
37
82
40
Even numbers: 5
Odd numbers: 5
'''
even = odd = 0

for i in range(10):
     a = int(input( ))
     if a%2 == 0:
         even += 1
     else:
         odd += 1

print("Even numbers:", even)

print("Odd numbers:", odd)

###
even = odd = 0

for a in range(1000):
     #a = int(input( ))
     if a%2 == 0:
         even += 1
     else:
         odd += 1

print("Even numbers:", even)

print("Odd numbers:", odd)

'''綜合範例9: ================================================================
2. 設計說明:
(1) 某次選舉有兩位候選人,分別是 No.1: Nami、No.2: Chopper。
請撰寫一程式,輸入五張選票,輸入值如為1即表示針對1號候選人投票;
輸入值如為2即表示針對2號候選人投票,
如輸入其他值則視為廢票。
每次投完後 
需印出目前每位候選人的得票數,
最後印出最高票者為當選人;
如最終計算有相同的最高票數者或無法選出最高票者,
顯示【=>  No one won the election. 】

輸入輸出:
(1) 輸入說明: 五個正整數(1、2 或其他)
(2) 輸出說明: 每次投完後需印出目前每位候選人的得票數
五張選票投票完成,最後印出最高票者為當選人
(3) 輸入與輸出會交雜如下,輸出之項目以粗體字表示
輸出：
1
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  0
Total null votes =  0
1
Total votes of No.1: Nami =  2
Total votes of No.2: Chopper =  0
Total null votes =  0
2
Total votes of No.1: Nami =  2
Total votes of No.2: Chopper =  1
Total null votes =  0
1
Total votes of No.1: Nami =  3
Total votes of No.2: Chopper =  1
Total null votes =  0
1
Total votes of No.1: Nami =  4
Total votes of No.2: Chopper =  1
Total null votes =  0
=> No.1 Nami won the election.
'''
vote1 = vote2 = null_vote = 0

for i in range(5):
    n = eval(input())
    if  n == 1:
        vote1 += 1
    elif n == 2:
        vote2 += 1
    else:
        null_vote += 1

    print("Total votes of No.1: Nami = ", vote1)
    print("Total votes of No.2: Chopper = ", vote2)
    print("Total null votes = ", null_vote)
    
if  vote1 > vote2:
    print("=> No.1 Nami won the election.")
elif vote1 < vote2:
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")
    
### 修改 提示?

'''綜合範例 10: ==============================================================
2. 設計說明:
(1) 請撰寫一程式,依照使用者輸入的n,畫出對應的等腰三角形。

3. 輸入輸出:
(1) 輸入說明: 一個正整數
(2) 輸出說明: 以 * 畫出等腰三角形(每列最後一個*的右方無空白)
(3) 範例輸入:  7
輸出：
7
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *   # 7*2 -1 = 13
'''
n = eval(input('輸入一個正整數:'))

for  i  in range(0, n):
    for j in range( n-i,  1,  -1):
        print(' ', end=' ')
    for k in range( 0,  i * 2 + 1,  1):
        print('*', end=' ')
    print()

'''綜合範例 11: =======================================================
試撰寫一程式,試輸入二個年份 yearl 和 year2 (如 yearl <= year2),
然後顯示 year1 ~ year2(如 2000~2100)的所有閏年。
* 提示: 有關閏年的判斷,請參閱綜合範例7的說明。在此不再贅述。

1. 輸入輸出:
(1) 範例輸入:  2000, 2100
輸出：
2000,2100
2000   2004   2008   2012   2016   2020   2024   2028   2032   2036   2040   2044   2048   2052   2056   2060   2064   2068   2072   2076   2080   2084   2088   2092   2096
'''
year1, year2 = eval(input('試輸入二個年份 yearl 和 year2:'))
for i  in range (year1, year2+1):
    if  i%400 == 0 or( i%4==0 and i%100!=0 ):
        print( '%5d ' %(i),  end = ' ' )

'''綜合範例 12: =======================================================
承上題,將輸出每一列印十個。

1. 輸入輸出:
(1) 範例輸入: 2000,2100
輸出：
2000,2100
 2000   2004   2008   2012   2016   2020   2024   2028   2032   2036
 2040   2044   2048   2052   2056   2060   2064   2068   2072   2076
 2080   2084   2088   2092   2096
'''
count = 0
year1, year2 = eval(input('試輸入二個年份 yearl 和 year2:'))
for i in range (year1, year2+1):
    if i%400 ==0 or (i%4 ==0 and i%100!=0) :
        count += 1
        if count % 10 != 0:
            print('%5d '%(i), end = ' ')
        else:
            print('%5d'%(i))

'''綜合範例 13: ============================================================
試撰寫一程式,輸入三個正整數 a, b 以及c,然後求出這三個正整數的最大公因數。

1. 輸入輸出1:
(1) 範例輸入: 12 24 8

2. 輸入輸出2:
(1) 範例輸入: 12 18 20
輸出：
12
24
8
gcd (12, 24, 8) = 4

12
18
20
gcd (12, 18, 20) = 2

'''
a = eval(input('輸入三個正整數 a, b 以及c, a = '))
b = eval(input('輸入三個正整數 a, b 以及c, b = '))
c = eval(input('輸入三個正整數 a, b 以及c, c = '))
gcd = 1
k = 2
while k <= a and k <= b and k <= c:
    if a % k == 0 and b % k == 0 and c % k == 0:
        gcd = k
    k += 1
print('gcd (%d, %d, %d) = %d' %(a, b, c, gcd))

'''綜合範例 14: ==============================================================
試撰寫一程式,輸入一正整數a,然後判斷它是否為質數。

1. 輸入輸出1:
(1) 範例輸入: 13

2. 輸入輸出2:
(1) 範例輸入: 12
輸出：
13
13 is a prime number.
12
12 is not a prime number.
'''
a = eval(input('輸入一正整數a = '))
isPrime = 1
divisor = 2
while divisor <= a / 2 :
    print( '%d = divisor. '%(divisor))
    if a % divisor == 0:
        isPrime = 0
        break
    divisor += 1  # 2,3,4 ..... why?
if isPrime == 1:
    print( '%d is a prime number. '%(a))
else:
    print( '%d is not a prime number. '%(a))

'''綜合範例 15: ===============================================================
試撰寫一程式,輸入一正整數number, 然後印出前面 number 個的質數。

1. 輸入輸出1:
(1) 範例輸入: 50

2. 輸入輸出2:
(1) 範例輸入: 100
輸出：
輸入一正整數number = 50
The first 50 prime numbers are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229

輸入一正整數number = 100
The first 100 prime numbers are: 
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 
'''
number = eval(input('輸入一正整數number = '))
a = 2
count = 0

print('The first %d prime numbers are: '%(number))
while count < number:
    isPrime = 1
    divisor = 2#因數2為開始
    while divisor <= a / 2:   #找出number除以2之後的因數
        if a % divisor == 0:
            isPrime = 0
            break
        divisor += 1#一步一步往下找
    if isPrime == 1:
        count += 1
        print(a, end = ' ')
    a += 1#number一步一步往下找
    
## 每行印10個數值!
