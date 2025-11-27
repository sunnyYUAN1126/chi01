'''
函式
函式(function)可以視為是一解決某一問題的片段程式,
函式它可以被重複使用, 同時也易於維護,因此可以節省開發與維護成本。
我們以一印出多個星號的程式來說明:

輸出:
********************
******************************
**************************************************
'''
for i in range(1,21,2):
    print('*', end = '')
print()

for i in range(1, 31):
    print('*', end = '')
print()

for i in range(1, 51):
    print('*', end = '')
print()
'''上述的程式分別印出 20、30,以及50 個星號(*)。
由此可看出,每次印多少星號皆要重新一次,這不是很沒效率嗎?
因為我們發現程式所做的事情是一樣的, 只是給予的星星數目不同而已,
所以可將它以函式的方式來共享之。'''

'''
### 5-1 範例01 函式的定義 ================================
輸出：
********************
******************************
**************************************************
'''
def printStar(n):
    for i in range(1, n+1,2):
        print('*', end = '')
    print()

printStar(20)
printStar(30)
printStar(150)

def main():
    printStar(20)
    printStar(30)
    printStar(50)

main()
'''此程式定義了一個 printStar() 函式,並帶有一個形式參數(formal argument)n。
同時也定義了另一個函式 main(),在此函式中呼叫 printStar(20),
其中的20 表示實際參數(actual argument)。
最後記得要呼叫 main()才能啟動 main()函式的運作, 請參閱第11行。
'''

'''### 5-2 範例01 沒有參數也沒有回傳值 ===========================
最陽春的函式定義,沒有形式參數,如要計算由1到100 的總和,其對應的程式
如下:

輸出:summation of 1 to 100: 5050
'''

sum = 0
for i in range(1, 101):
    sum += i
print('summation of 1 to 100:', sum)

def total():
    sum = 0
    for i in range(1, 11):
        sum += i
    print('summation of 1 to 100:', sum)

total()
#print('summation of 1 to 100:',sum)
def main():
    total()

main()
'''程式中定義了total()函式,此函式的任務從1加到100,順便印出其總和。
'''

'''### 5-3 函式回傳值 ====================================
執行完函式也可以有回傳值,若將上一範例程式改以回傳值的方式表示的話,如下所示:
輸出:summation of 1 to 100: 5050
'''
def total():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum

total()

sum01 = total()
print(sum01)
def main():
    t = total()
    print('summation of 1 to 100:', t )

main()
'''此程式和上一程式唯一不同的是,多了一個 return 敘述。
然後在呼叫函式 main() 中以一變數t接收此值,再利用 print 印出。 '''

'''### 5-4 帶有參數和回傳值 =========
範例01
函式的定義也可以接收參數和回傳值。
如我們要計算由使用者輸入兩個數值區間的總和。如以下程式所示:

輸出:
Enter start number: 2
Enter end number: 100
sumation of 2 to 100: 5049
Enter start number: 1
Enter end number: 101
sumation of 1 to 101: 5151
'''

sum = 0
for i in range(1, 101):
    sum += i
print('summation of 1 to 100:', sum )

def total(a, b):
    #a = int()
    sum = 0
    for i in range(a, b+1):
        sum += i
        return sum
#print('summation of 1 to 100:', sum )

def total(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

x = eval(input('Enter start number: '))
y = eval(input('Enter end number: '))
t = total(x, y)
print('sumation of %d to %s: %d' %(x, y, t))
print('sumation of %d to %s: %d' %(x, y, total(x, y)))

#total = (x, y)

def main():
    x = eval(input('Enter start number: '))
    y = eval(input('Enter end number: '))
    t = total(x, y)
    print('sumation of %d to %s: %d' %(x, y, t))

main()
'''上述程式若輸入兩個數值2和100,表示計算2到100 的總和。若輸入是1和101, 表示計算1到101的總和。
程式中的total 函式接收了兩個形式參數a和b,最後以return 回傳 sum 給 main()函式的t。'''

'''### 5-5 回傳多個值 =====================
範例01
一般而言, 如C、C++、Java等等程式語言,基本上,函式只能回傳一個值。但在 Python提供可從函式回傳多個值。若要將某一函式所計算的總和與平均數回傳, 其程式如下所示:

輸出:sum = 5050, average = 50.500000
'''
def sumAndAverage(n1, n2):
    total = 0
    average = 0.0
    for i in range(n1, n2+1):
        total += i
    average = total/(n2-n1+1)
    return total, average, i

s, a, e = sumAndAverage(1, 100)
s1 = sumAndAverage(1, 100)  # 數組 tuple

def main():
    s, a = sumAndAverage(1, 100)
    print('sum = %d, average = %2f'%(s, a))

main()

def sumAndAverage02(n1, n2, step):
    total = 0
    average = 0.0
    for i in range(n1, n2+1, step):
        total += i
    average = total/(n2-n1+1)
    average02 = average *2
    return total, average, average02

t , a, a2 = sumAndAverage02(1, 100, 2)

'''此程式在main()函式中,呼叫 sumAndAverage()函式,
此時傳送了1和100 當做 參數給 sumAndAverage()函式的形式參數nl與n2。
最後,回傳 total 與 average
給 main()函式的s和a。
'''

'''5-5範例02
上一程式可以改為更加的友善性,計算的區間若不是固定在1到100,而是由使用者來決定。
如下範例程式所示:

輸出:
Enter start and end number: 1,100
sum = 100, average = 1
Enter start and end number: 2,100
sum = 99, average = 1
'''
def sumAndAverage(n1, n2):
    total = 0
    average = 0.0
    for i in range(n1, n2+1):
        total += i
    average = total/(n2-n1+1)
    return total, average

def main():
    x, y = eval(input('Enter start and end number: '))
    s, a = sumAndAverage(x, y)
    print('sum = %d, average = %d'%(s, a))

main()

s, a = sumAndAverage(1)
# TypeError: sumAndAverage() missing 1 required positional argument: 'n2'

# 變數範圍
print('sum = %d, average = %d'%(s, a))
# NameError: name 's' is not defined

s = 100
a = 5050
print('sum = %d, average = %d'%(s, a))

x, y = eval(input('Enter start and end number: '))
s, a = sumAndAverage(x, y)
print('sum = %d, average = %d'%(s, a))

s +=1

'''如此,要計算的區間由你來做主,有沒有感覺較有fu 呢?
在呼叫函式時,有時應給兩個參數值,但你卻只給一個,此時該怎麼辦?這可以使
用預設的參數值來處理之。如下節所示。
'''

'''### 5-6 函式預設參數值 =========================================
範例01
我們以上一範例程式來說明,若呼叫 sumAndAverage()函式時,你只給n1 的形式參數值 ,
而漏掉了n2,此時補救的方式就是在 sumAndAverage()函式中定義 n2 為預設的參數值,
亦即當沒有指定 n2 參數值時,就使用此預設值,如下所示:

輸出:
sum = 5050, average = 50
sum = 55, average = 5
'''
def sumAndAverage(n1=1, n2=100):
    total = 0
    average = 0.0
    for i in range(n1, n2+1):
        total += i
    average = total/(n2-n1+1)
    return total, average

s, a = sumAndAverage(1)
s, a = sumAndAverage()
s, a = sumAndAverage(2, 5) 


def main():
    s, a = sumAndAverage(1)
    print('sum = %d, average = %d'%(s, a))
    s, a = sumAndAverage(1, 10)
    print('sum = %d, average = %d'%(s, a))

main()
'''此程式中,當呼叫 sumAndAverage(1)
由於呼叫此函式本應該有兩個實際參數,但此函式只有一個實際參數,
其表示將實際參數1傳給形式參數nl,而形式參數 n2 將以100 表示之。
若有給兩個實際參數的話,則不會使用預設參數。但要注意的是,

## 預設參數值不可以置於沒有預設參數的前面,
如 def sumAndAverage(n1=100, n2):
是錯誤的寫法。
'''

'''### 5-6範例02 =========================================
若在呼叫函式時,都沒有給予實際參數值呢?
該如何處理,其實很簡單只要把所有的形式參數都設為預設參數值就可以了。
如下範例所示:
輸出:
sum = 5050, average = 50
sum = 5049, average = 51
sum = 55, average = 5
'''
def sumAndAverage(n1=1, n2=100):
    total = 0
    average = 0.0
    for i in range(n1, n2+1):
        total += i
    average = total/(n2-n1+1)
    return total, average

def main():
    s, a = sumAndAverage()
    print('sum = %d, average = %d'%(s, a))
    s, a = sumAndAverage(2)
    print('sum = %d, average = %d'%(s, a))
    s, a = sumAndAverage(1, 10)
    print('sum = %d, average = %d'%(s, a))

main()

'''### 綜合範例01 ===========================================
2. 設計說明:
(1) 請撰寫一程式,呼叫函式 compute(),該函式功能為讓使用者輸入系別
(Department)、學號(Student ID)和姓名(Name)並顯示這些訊息。

3. 輸入輸出:
(1) 輸入說明: 三個字串
(2) 輸出說明: 系別(Department)  學號(Student ID)  姓名(Name)
(3) 範例輸入:  Information Management  123456789   Tina. Chen


輸出:
Information Management
123456789
Jason Todd
Department: Information Management
Student ID: 123456789
Name: Jason Todd
'''

# 原始:
stu_dept = input('輸入系別(Department):')
stu_id = input('輸入學號(Student ID):')
stu_name = input('輸入姓名(Name):')

print('Department:', stu_dept)
print('Student ID:', stu_id)
print('Name:', stu_name)


def compute():
    stu_dept = input('輸入系別(Department):')
    stu_id = input('輸入學號(Student ID):')
    stu_name = input('輸入姓名(Name):')

    print('Department:', stu_dept)
    print('Student ID:', stu_id)
    print('Name:', stu_name)

compute()

'''### 綜合範例02 =============================================
2. 設計說明:
(1) 請撰寫一程式,將使用者輸入的兩個數字作為參數傳遞給一個名為
compute(x,y)的函式,此函式將回傳 x 和y的乘積。

3. 輸入輸出:
(1) 輸入說明: 兩個數值
(2) 輸出說明: 兩個數值相乘之乘積
(3) 範例輸入: 56 11

輸出:
56
11
616
'''
def compute(a, b):
    return a * b

num1 = eval(input('使用者輸入第一個數字：'))
num2 = eval(input('使用者輸入第二個數字：'))

print(compute(num1, num2))

def compute(a, b):
    p = a * b
    add = a + b
    return p, add

'''### 綜合範例03 =============================================
2. 設計說明:
(1) 請撰寫一程式,讓使用者輸入兩個整數,接著呼叫函式compute(),此函式
接收兩個參數a、b,並回傳從a連加到b的和。
3. 輸入輸出:
(1) 輸入說明: 兩個整數
(2) 輸出說明: 從a 連加到b的和
(3) 範例輸入: 33 66

輸出:
33
66
1683
'''
def compute(a, b):
    return int((a+b)*(b-a+1)/2)

a = eval(input('使用者輸入第一個數字：'))
b = eval(input('使用者輸入第二個數字：'))

print(compute(a, b))

def compute(a, b):
    sum = int((a+b)*(b-a+1)/2)
    return sum

'''### 綜合範例04 ============================================
2. 設計說明:
(1)請撰寫一程式,讓使用者輸入兩個整數,接著呼叫函式 compute(),此函式
接收兩個參數a、b,並回傳 a^b 的值。

3. 輸入輸出:
(1) 輸入說明:  兩個整數
(2) 輸出說明:  a^b 的值
(3) 範例輸入:  14  3

輸出:
14
3
2744
'''
def compute(a, b):
    return a**b

a = eval(input('使用者輸入第一個數字：'))
b = eval(input('使用者輸入第二個數字：'))

print(compute(a, b))

'''### 綜合範例05 ================================================
2. 設計說明:
(1) 請撰寫一程式,將使用者輸入的三個參數,變數名稱分別為
a(代表字元character)、
x(代表個數)、
y(代表列數),
作為參數傳遞給一個名為 compute()的
函式,該函式功能為:一列印出x個a字元,總共印出y列。

* 提示: 輸出的每一個字元後方有一空格。

3. 輸入輸出:
(1) 輸入說明: 三個參數,分別為a(代表字元 character)、x(代表個數)、y(代表 列數)
(2) 輸出說明: 一列印出x 個a字元,總共印出y列
(3) 範例輸入: e  5  4


輸出:
e
5
4
e e e e e
e e e e e
e e e e e
e e e e e
'''
def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print(a, end = ' ')
        print()

a = input('使用者輸入a(代表字元 character):')
x = int(input('使用者輸入x(代表個數):'))
y = int(input('使用者輸入y(代表 列數):'))

compute(a, x, y)

'''### 綜合範例06 =====================================================
2. 設計說明:
(1) 請撰寫一程式,將使用者輸入的三個數字(代表一元二次方程式 ax^2 + bx
+c = 0的三個係數a、b、c)作為參數傳遞給一個名為 compute()的函式,
 該函式回傳方程式的解,如無解則輸出【Your equation has no root.】。
* 提示: 輸出有順序性。

3. 輸入輸出:
(1) 輸入說明: 三個數字,分別為a、b、c
(2) 輸出說明: 代入一元二次方程式,回傳方程式解;如無解則輸出
           【Your equation has no root.】
(3) 範例輸入: 2  -3  1
(4) 範例輸入: 9   9  8

輸出:
2
-3
1
1.0, 0.5
9
9
8
Your equation has no root.
'''
def compute(a, b, c):
       delta = b**2 - 4 * a * c

       if delta < 0 :
            return None
       elif delta == 0:
              return -b /(2* a)
       else:
              res1 = (-b + delta **0.5)/(2 * a)
              res2 = (-b - delta**0.5)/(2 * a)
              return str(res1) + ", " + str(res2)


a = eval(input('使用者輸入係數 a:'))
b = eval(input('使用者輸入係數 b:'))
c = eval(input('使用者輸入係數 c:'))
result = compute(a, b, c)
if result == None:
     print("Your equation has no root.")
else:
     print(result)

'''### 綜合範例07 ===========================================================
2. 設計說明:
(1) 請撰寫一程式,讓使用者輸入一個整數x ,並將x傳遞給名為 compute()的函式,
此函式將回傳x是否為質數(Prime number)的布林值,接著再將判斷結果輸出。
如輸入值為質數顯示【Prime】,否則顯示【Not Prime】。

3. 輸入輸出:
(1) 輸入說明: 一個整數
(2) 輸出說明: 判斷是否為質數,若為質數顯示【Prime】,否則顯示【Not Prime】
(3) 範例輸入: 3
(4) 範例輸入: 6
(5) 範例輸入: 1
(6) 範例輸入: 0
(7) 範例輸入: -5
輸出：
3
Prime
4
Not prime
'''
import math

def compute(num) :
    s_num = math.floor(num ** 0.5)
    for i in range (2, num+1) :
        if (num % i) == 0:
            return False
    return True

x= int (input('使用者輸入一個整數 x :'))

if x > 1:
    if compute(x):
        print('Prime')
    else:
        print('Not Prime')
else:
    print('Not Prime')
    
###
import math

def compute(num) :
    #s_num = math.floor(num ** 0.5)
    for i in range (2, num ) :
        if (num % i) == 0:
            return False
    return True

x= int (input('使用者輸入一個整數 x :'))

if x > 1:
    if compute(x):
        print('Prime')
    else:
        print('Not Prime')
else:
    print('Not Prime')

###
def compute(num) :
    s_num = num // 2
    for i in range (2, (s_num + 1)) :
        if (num % i) == 0:
            return False
    return True

x= int (input('使用者輸入一個整數 x :'))

if x > 1:
    if compute(x):
        print('Prime')
    else:
        print('Not Prime')
else:
    print('Not Prime')
    
'''
：若正數a有≦√a之因數，則a為非質數。若沒有，則a為質數http://www.mathland.idv.tw/forum/memo.asp?srcid=16320&bname=ASP'''

'''### 綜合範例08 =========================================================
2. 設計說明:
(1) 請撰寫一程式,讓使用者輸入兩個正整數x、y,並將 x 與 y 傳遞給名為
compute() 的函式,此函式回傳 x 和 y 的最大公因數 gcd 。
3. 輸入輸出:
(1) 輸入說明: 兩個正整數(以半形逗號分隔)   x,y
(2) 輸出說明: 最大公因數
(3) 範例輸入:  12,8
(4) 範例輸入:    4,6

輸出：
12,8
4
4,6
2
'''
def compute(a, b):
    gcd = 1
    k = 2
    if a > 0 and b > 0:
        while k <= a and k <= b:
            if a % k == 0 and b % k == 0:
                gcd = k
            k += 1
        return gcd

x, y = eval(input('使用者輸入兩個正整數x、y:'))
gcd = compute(x, y)
print('最大公因數 gcd = ', gcd)

'''### 綜合範例09 ==================================================

2. 設計說明:
(1) 請撰寫一程式,讓使用者輸入二個分數,分別是 x/y 和 m/n(其中x,y,n,n皆為正整數),
計算這兩個分數的和為p/q,接著將p與q傳遞給名為compute() 函式,
此函式回傳p和q的最大公因數(Greatest Common Divisor, GCD)。 
再將 p 和 q 各除以其最大公因數,最後輸出的結果就是以最簡分數表示。

3. 輸入輸出:
(1) 輸入說明: 四個正整數(以半形逗號分隔) x,y  m,n
(2) 輸出說明: 兩個分數和的最簡分數
(3) 範例輸入:  1,2   1,6
(4) 範例輸入:  12, 16   18, 32
輸出：
12,2
1,6
12/2 + 1/6 = 37/6
12,16
18,32
12/16 + 18/32 = 21/16
'''
def compute(a, b):
    gcd = 1
    k = 1
    if a > 0 and b > 0:
        while k <= a and k <= b:
            if a % k == 0 and b % k == 0:
                gcd = k
            k += 1
        return gcd

x, y  = eval(input('使用者輸入二個分數,分別是 x/y , x , y:'))
m, n =  eval(input('使用者輸入二個分數,分別是 m/n , m , n:'))
p = x*n + m*y
q = y*n
gcd = compute(p,q)
print('%d/%d + %d/%d = %d/%d' % (x,y,m,n, p/gcd, q /gcd))

#### 變形
def compute(x, y, m, n):
    a = x*n + m*y
    b= y*n
    gcd = 1
    k = 1
    if a > 0 and b > 0:
        while k <= a and k <= b:
            if a % k == 0 and b % k == 0:
                gcd = k
            k += 1
        return a/gcd , b/gcd

x, y  = eval(input('使用者輸入二個分數,分別是 x/y , x , y:'))
m, n =  eval(input('使用者輸入二個分數,分別是 m/n , m , n:'))
#p = x*n + m*y
#q = y*n
p, q = compute(x, y, m, n)
print('%d/%d + %d/%d = %d/%d' % (x,y,m,n, p, q))

'''### 綜合範例10 ==========================================================
2. 設計說明:
(1) 請撰寫一程式,計算費氏數列(Fibonacci numbers),使用者輸入一正整數
num(num>=2),並將它傳遞給名為compute()的函式,
此函式將輸出費氏數列前 num 個的數值。

* 提示: 費氏數列的某一項數字是其前兩項的和,而且第0項為0,第一項為1,
表示方式如下:

Fo = 0
F1 = 1
Fn = F(n-1) + F(n-2)

3. 輸入輸出:
(1)輸入說明:  一個正整數num(num>=2)
(2)輸出說明:  依輸入值 num,印出費氏數列前 num 個的數值
                        (每個數值後方為一個半形空格)
(3) 範例輸入: 10
(4) 範例輸入: 20
輸出：
10
0 1 1 2 3 5 8 13 21 34
20
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
'''

# 原始
num = eval(input('計算費氏數列(Fibonacci numbers),使用者輸入一正整數:'))
n1 = 0
n2 = 1
print('%d %d' % (n1,n2), end=' ')
for i in range(3, num+1):
    n3 = n1 + n2
    print('%d' % (n3), end=' ')
    n1 = n2
    n2 = n3
        
####         
def compute(n):
    n1 = 0
    n2 = 1
    print('%d %d' % (n1,n2), end=' ')
    for i in range(3, n+1):
        n3 = n1 + n2
        print('%d' % (n3), end=' ')
        n1 = n2
        n2 = n3

num = eval(input('計算費氏數列(Fibonacci numbers),使用者輸入一正整數:'))
compute(num)

'''### 綜合範例11 ================================================
試撰寫一程式,在main()函式輸入一整數n,將此整數傳給 randNum() 函式,用
以顯示n個介於1到100 的亂數。若n大於10,則每一列印出十個亂數。

1. 輸入輸出1:
(1) 範例輸入: 30
2. 輸入輸出2:
(1) 範例輸入: 100

輸出：
30
  43  64  42  78   6  26  84  33  17  28
  14  96  36  64  22  90  80  64  47  82
  70  75  97  50  54   3  93  62  11  67
 2
  87  13
'''
import random
def randNum(num):
    for i in range(1, num+1):
        rn = random.randint(1, 100)
        if i % 10 == 0:
            print('%4d'%(rn))
        else:
            print('%4d'%(rn), end = '')

def main():
    n = eval(input('輸入一整數 n :'))
    randNum(n)
main()

###
import random
def randNum(num, c):
    for i in range(1, num+1):
        rn = random.randint(1, 100)
        if i % c == 0:
            print('%4d'%(rn))
        else:
            print('%4d'%(rn), end = '')

def main():
    n, c = eval(input('輸入一整數 n 與 c :'))
    randNum(n, c)
main()


'''### 綜合範例12 ========================================
試撰寫一程式,在main() 函式輸入一年份 year,
將此整數傳 isLeap()函式,用以顯示 year 是否為閏年。

1. 輸入輸出1:
(1) 範例輸入: 2018
2. 輸入輸出2:
(1) 範例輸入: 2020
輸出：
2018
2018 is not a leap year.
2020
2020 is a leap year.
'''
def isLeap(y):
    if y % 400 ==  0 or (y % 4 == 0 and y % 100 != 0) :
        print('%d is a leap year. '%(y))
    else:
        print('%d is not a leap year.'%(y))

def main():
    year = eval(input('輸入一年份 year:'))
    isLeap(year)
main()

'''### 綜合範例13 ============================================
試撰寫一程式,在main() 函式利用不定數迴圈輸入一年份 year,
將此整數傳 isLeap()函式,用以顯示 year 是否為閏年。
當輸入的年份是-9999 時,則結束輸入的動作。

1. 輸入輸出1:
(1) 輸入與輸出會交雜如下,輸出之項目以粗體字表示
輸出：
2018
2018 is not a leap year.
2030
2030 is not a leap year.
2040
2040 is a leap year.
-9999
'''
def isLeap(y):
    if  y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        print('%d is a leap year. '%(y))
    else:
        print('%d is not a leap year.'%(y))

def  main():
    while True:
        year = eval(input('輸入一年份 year:'))
        if year != -9999:
            isLeap(year)
        else:
            print('程式碼結束！ Bye!')
            break
main()

'''### 綜合範例 14: =====================================================
試撰寫一程式,在main()函式輸入一正整數n,將此整數傳給 factor()函式,用以
顯示1~n的階層。
1. 輸入輸出1:
(1) 範例輸入: 20
輸出：
20
 1! = 1
 2! = 2
 3! = 6
 4! = 24
 5! = 120
 6! = 720
 7! = 5040
 8! = 40320
 9! = 362880
10! = 3628800
11! = 39916800
12! = 479001600
13! = 6227020800
14! = 87178291200
15! = 1307674368000
16! = 20922789888000
17! = 355687428096000
18! = 6402373705728000
19! = 121645100408832000
20! = 2432902008176640000
'''
def factor(k):
    for i in range(1, k+1):
        factor = 1
        print('%2d! = ' %(i), end = '')
        for j in range(1, i+1):
            factor *= j   # factor =factor * j
        print(factor)

def main():
    n = eval(input('輸入一正整數n:'))
    factor(n)
main()

### 
def factor(k, end01):
    for i in range(1, k+1):
        factor = 1
        print('%2d! = ' %(i), end = '')
        for j in range(1, i+1):
            factor *= j   # factor =factor * j
            if factor >= end01:
                break
        print(factor)

def main():
    n, end01 = eval(input('輸入一正整數n and end:'))
    factor(n, end01)
main()

'''### 綜合範例 15: ========================================================
試撰寫一程式,在main()函式輸入n,表示有幾個邊,
再輸入g,表示邊長,將這兩個整數傳給 nEdge() 函式,
用以計算n邊形面積。最後將其顯示之。

* 提示: n 邊形的面積計算公式如下:
area = (n*g^2)/(4 *tan (π/n))

1. 輸入輸出:
(1) 範例輸入: 5  6.5
輸出：
5
6.5
area = 72.69
'''
import math
def nEdge(n, g):
    area = (n * g**2)/(4 * math.tan(math.pi/n))
    print('area = %.2f' %(area))

def main():
    n = eval(input('輸入n,表示有幾個邊:'))
    g = eval(input('再輸入g,表示邊長:'))
    nEdge(n, g)
main()
