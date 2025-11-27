'''6-1 一維串列的運作
有關串列的運作,我們在 IDLE 的模式下,以立即的方式向大家介紹,然後再談其運用。
'''
>>>lstl = [] #建立一空串列
>>>lst2 = [1,2,3,4,5]
>>>lst3 = ['apple', 'orange','banana']
>>>lst4 = [1,2,34.56,'pineapple']

'''6-1-1 []與 [start.end]
利用[]再加索引可存取其對應的項目,而「start:end」只要從來索引 Start 起到end-1為止的串列項目。
注意,索引0是串列的第一個項目,索引1是串列的第一項目,以此類推。請參閱以下說明。
'''
>>> lst2
[1, 2, 3, 4, 5]
>>> lst2[0]#印出索引0的串列項目
1
>>> lst2[3]#印出索引3的串列項目
4
>>> lst2[1:3]#印出索引1到2的串列項目
[2, 3]
>>> lst2[0:5]#印出索引0到4的串列項目
[1, 2, 3, 4, 5]
>>>

'''6-1-2 len
利用 len 計算串列的長度。
'''
>>>len(lst2)
>>> 5
>>>

'''6-1-3 append 與 insert 方法
利用 append(value) 方法將 value 加入串列尾端,利用 insert(index, value)方法將 value 加入於串列的索引為 index 處。請參閱以下敘述。
'''
>>> lst1.append(1)
>>> lst1
[1]
>>> lst1.append(2)
>>> lst1
[1, 2]
>>> lst1.insert(1,4)
>>> lst1
[1, 4, 2]
'''上述的 insert(1,4)表示將數值4加在串列索引為1的地方。 '''

'''6-1-4 pop 與 remove 方法 利用pop()删除串列的最後一個項目,pop(index)表示删除串列索引為 index 的項目。
利用 remove(value)删除串列中值為 value 的項目,若有多個 value 項目,則只删除第一個出現的項目。請參閱以下敘述。 '''
>>> lst2
[1,2,3,4,5]
>>> lst2.pop()
5
>>> lst2
[1,2,3,4]
>>> lst2.pop(1)
2
>>> lst2
[1, 3, 4]
>>> lst2.remove(3)
>>> Ist2
[1, 4]

'''6-1-5 count 與 index 方法
利用count(value)可以計算value出現於串列的次數。Index(value)立回傳出現value於串列的索引。
請參閱以下敘述。'''
>>> lst3
['apple', 'orange', 'banana']
>>> lst3.append('apple')
>>> lst3
['apple', 'orange', 'banana', 'apple']
>>> lst3.count('apple')
2
>>> lst3.index('banana')
1
>>> lst3.index('orange')
1

'''6-1-6 sort與reverse方法
利用sort()將串列由小至大加以排序。而reverse()則用來將串列加以反轉。
請參閱以下敘述。'''
>>> lst1
[1, 4, 2]
>>> lst1.append(5)
>>> lst1
[1, 4, 2, 5]
>>> lst1.sort()
>>> lst1
[1,2,4,5]
>>> lst1.reverse()
>>> lst1
[5, 4, 2,1]

'''6-1-7 in 與 not in
我們可以利用 in 和 not in 來判斷某項目是否存在於串列中。請參閱以下敘述。
'''
>>> lst1
[5, 4,2,1]
>>> 5 in lst1
True
>>> 8 not in lst1
True

'''6-1-8 Sum、max,以及 min 函式
利用 sum函式加總串列元素和,利用 max 和 min 函式分別回傳串列中最大的項目 與最小的項目。請參閱以下敘述。
'''
>>> lst1
[5, 4,2,1]
>>> sum(lst1)
12
>>> max(lst1)
5
>>> min(lst1)
1

'''6-1-9 + 與*
此處的+是將兩串列連結在一起,而* 是複製多少幾個串列。請參閱以下敘述。
'''
>>> lst1
[5, 4,2,1]
>>> lst2
[1, 4]
>>> lstl + lst2
[5, 4,2,1,1,4]
>>> lst2 * 2
[1, 4, 1, 4]
>>> 2 * lst2
[1, 4,1,4]

'''6-1-10 再論[]與[startiend]
前面曾提及此主題,不過在此處我們將提及當索引為負時的情況。
索引0是串列元 素的第一個,索引1是串列元素的第二個,以此類推。
而索引 -1 為串列元素的最 後一個,可以想像為 -1 加上串列長度。
請參閱以下說明。
'''

>>> lst1
[5, 4, 2,1]
>>> lst1[-1] #EP出索引-1的串列項目
-1
>> lst1[-3] #ED出索引-3的串列項目
4
>>> lst1[-3:-1] #出索引-3到-2的串列項目
[4,2]
>>> lst1[-4:4] #D出索引-4到3的串列項目
[5, 4, 2, 1]
>>>

'''6-1-11 利用for 印出串列所有的項目
利用 for.in range Ep出串列所有的項目,如下所示:'''
>>> lst3 = ['apple', 'orange', 'banana', 'kiwi']
>>> lst3
['apple', 'orange', 'banana', 'Kiwi']
>>> for i in range(len(lst3)):
        print('lst3[%d] = %s'%(i, lst3[i]))

lst3[0] = apple
lst3[1] = orange
lst3[2] = banana
lst3[3] = kiwi
'''python 又提供一種新的方式,讓我們可以印出串列的所有項目,如下所示: '''
>>> lst3
['apple', 'orange', 'banana', 'apple']
>>> lst3[3] = 'kiwi'
>>> lst3
['apple', 'orange', 'banana', 'kiwi']
'''利用 for in 即可。'''
>>> for i in lst3:
        print(i, end = '***')
apple***orange***banana***kiwi***
'''若要連項目所對應的位置也印出,則可以下列方式表示之。'''
>>> x = 0
>>> for i in lst3:
        print('lst3[%d] =%s'%(x,i))
lst3[0]=apple
lst3[0]=orange
lst3[0]=banana
lst3[0]=kiwi

'''以上所討論有關一維串列運作方法,摘要於表 6-1:
len() 計算串列長度
sum() 加總串列每一元素
max() 回傳串列最大值
min() 回傳串列最小值
有關串列運作之方法摘要於表 6-2 :
append(value)         附加value於串列的尾端
insert(indexp, value) 在索引indexp處加入value
pop()                 刪除串列最後一元素
pop(indexp)           刪除串列索引indexp的元素
remove(value)         刪除串列中的value，若有多個value，則只刪除第一個
count(value)          串列中出現value的個數
index(value)          value所在串列的索引
sort()                串列由小至大排序
reverse()             將串列元素反轉
有關串列運作之運算子摘要於表6-3 :
in      檢視某一元素是否在串列中
not in  檢視某一元素是否不在串列中
[]      印出串列中的某一元素
[star: end] 印出串列從 start 到end-1 的元素
*           複製多次的串列元素
+           連結兩個串列元素
'''


'''6-1
#範例01
以下我們大樂透電腦選號來探討有關串列程式的撰寫。
下一程式將以亂數產生器產生六個1~49 的亂數:
輸出結果：
The lottery numbers are:
  18   4   4  19  10  10
'''
import random
lotto = []
for i in range(1,7):
    randNum = random.randint(1, 49)
    lotto.append(randNum)
print('The lottery numbers are:')
for i in lotto:
    print("%4d"%(i), end ='')

'''範例02
程式中利用append 方法將所產生的亂數加入於串列。但我們發現有時可能會產生 重複的數字,這時應該要有一些機制來防止之。
我們的做法是可以利用一輔助串列0 checkNum[] 串列,首先將此串列的1到49
的元素值皆填為0,之後產生的亂數號碼當作 checkNum 串列的索引,檢視此索引 所對應的值,此時有兩種狀況,分別如下:
(1). 若是0,則將此亂數加入於 lotoc[] 串列,並將此索引所對應 checkNum[] 串 列的值改為1。
(2). 若是1,表示此亂數已加入於 lotto[] 串列中了。若未產生六個,則再產生一次亂數。
輸出結果：
The lottery numbers are:
3 20 21 35 15 11
'''
import random
lotto = []
checkNum = []
for i in range(0, 50):
    checkNum.append(0)
count = 1
while count <= 6:
    randNum = random.randint(1, 49)
    if checkNum[randNum] == 0:
        lotto.append(randNum)
        count += 1
    checkNum [randNum] = 1
print("The lottery numbers are: \n", end = '')
for i in lotto:
    print(i, end = ' ')
print()

'''範例02
上一程式也可以直接使用串列所提供的 not in 的運算子,這樣子就不必使用另一 個輔助串列。
也不比較其值是否為0,如下範例程式所示:
輸出結果：
The lottery numbers are:
  23   46   15   37   27    8
'''
import random
lotto = []
n = 1
while n <= 6:
    randNum = random.randint(1, 49)
    if randNum not in lotto:
        lotto.append(randNum)
        n += 1

print("The lottery numbers are: \n", end = '')
for i in lotto:
    print('%4d'%(i), end = ' ')
print()

'''範例03
若要將串列的元素由小至大排序好再印出，則可呼叫sort()方法。如下範例程式所示:
輸出結果：
The lottery numbers are:
  40   29    6   18   41   35
After sorting:
   6    18    29    35    40    41
'''
import random
lotto = []
n = 1
while n <= 6:
    randNum = random.randint(1, 49)
    if randNum not in lotto:
        lotto.append(randNum)
        n += 1

print("The lottery numbers are: \n", end = '')
for i in lotto:
    print('%4d'%(i), end = ' ')
print()

lotto.sort()
print('After sorting:')
for i in lotto:
    print('%4d'%(i), end = '  ')
print()

'''6-2
範例01
二維串列的運作與一維串列的運作很相似。若對一維串列有所認知的話,基本上就 會迎刃而解。
6-2-1 如何得知二維串列的列數與行數
我們先來探討如何印出二維串列有多少列和多少行。
輸出結果：
[[1, 2, 3], [4, 5, 6]]
[1, 2, 3]
2
3
'''
lst2 = [[1,2,3], [4,5,6]]
print(lst2)
print(lst2[0])
print(len(lst2))
print(len(lst2[0]))

'''範例02
上述的程式中,lst2 表示為二維串列,所以印出時是 [[1, 2, 3], [4,5,6],而Ist2[0]二維串列的的第一列,所以印出時是「1.2.3] 。
同時 len(lst2) 表示 lst2一維串列的列數
數。而len(lst2[0])表示 lst2 第一列有多少個元素。
6-2-2 如何加入一元素於二維串列
有了這基本的概念後,我們由使用者輸入二維串列的列與行的個數,而串列的每一個元素值由亂數產生器產生的亂數填入。
輸出結果：
Enter the number of row: 5
Enter the number of column:3
[[18, 5, 27], [2, 6, 20], [5, 26, 24], [15, 20, 38], [39, 31, 4]]
'''
import random
rows = eval(input('Enter the number of row: '))
columns = eval(input('Enter the number of column:'))
lst2 = []
for i in range(rows):
    lst2.append([])
    for j in range(columns):
        lst2[i].append(random.randint(1, 50))
print(lst2)

'''範例03
接續上一個程式，以下範例程式是將二維串列的每一元素一一地印出，如下所示:
輸出結果：
Enter the number of row: 5
Enter the number of column:3
[[49, 12, 31], [50, 7, 36], [15, 44, 42], [5, 13, 3], [28, 29, 22]]

ist2[0][0] =    49
ist2[0][1] =    12
ist2[0][2] =    31

ist2[1][0] =    50
ist2[1][1] =     7
ist2[1][2] =    36

ist2[2][0] =    15
ist2[2][1] =    44
ist2[2][2] =    42

ist2[3][0] =     5
ist2[3][1] =    13
ist2[3][2] =     3

ist2[4][0] =    28
ist2[4][1] =    29
ist2[4][2] =    22
'''
print()
for i in range(len (lst2)):
    for j in range(len(lst2[0])):
        print('lst2[%d][%d] = %5d'%(i,j, lst2[i][j]))
    print()

'''範例04
此程式旨意在讓讀者了解二維串列每一索引的元素為何。除了上述的方法以外,也
由可以更簡潔的 for 敘述來印出二維串列的所有的元素,如下所示:
輸出結果：
   26   14   18
   36   30   48
    5    6   16
    4   41    1
   34   16   46
'''
for row in lst2:
    for value in row:
        print('%5d'%(value), end='')
    print()

'''範例05
程式中的 for 敘述沒有range,只有 for..in。若改為 for..in range,則程式如下所示:
輸出結果：
   31   27   32
   25   27   27
   22   16   14
   20   22   24
   19   43   29
'''
#another print
for i in range(len(lst2)):
    for j in range(len(lst2[0])):
        print('%5d'%(lst2[i][j]), end = '')
    print()

'''範例06
計算行與列的和
計算二維串列每一行的和,有一重點就是外迴圈以行的區間為主,而内迴圈以列的區間為主。程式如下所示:
輸出結果：
sum for column 0 is 117
sum for column 1 is 157
sum for column 2 is 117
'''
for column in range(len(lst2[0])):
    total = 0
    for row in range(len(lst2)):
        total += lst2[row][column]
    print('sum for column %d is %d'%(column, total))

'''範例07
反之,若要求二維串列每一列的和,則外迴圈以列的區間為主,而内迴圈則以行的
區間為主。程式如下所示:
輸出結果：
sum for row 0 is 65
sum for row 1 is 128
sum for row 2 is 65
sum for row 3 is 69
sum for row 4 is 102
'''
for row in range(len(lst2)):
    total = 0
    for column in range(len(lst2[0])):
        total += lst2[row][column]
    print('sum for row %d is %d'%(row, total))

'''範例08
其實在計算二維串列的每一列的和,可以直接使用sum 完成。程式如下所示:
輸出結果：
sum for row 0 is 127
sum for row 1 is 60
sum for row 2 is 97
sum for row 3 is 57
sum for row 4 is 66
'''
for row in range (len(lst2)):
    total = 0
    total += sum(lst2[row])
    print('sum for row %d is %d'%(row, total))

'''綜合範例01
偶數索引值加總
1. 題目說明:
請開啟 PYD06.py 檔案,依下列題意進行作答,處理偶數索引的值,使輸出值符合題意要求。請另存新檔為 PYA06.py,作答完成請儲存所有檔案至 C:\ANS. CSF 原資料夾内。
2. 設計說明:
(1) 請撰寫一程式,利用一維串列存放使用者輸入的12個正整數(範圍1~99)。
顯示這些數字,接著將串列索引為偶數的數字相加並輸出結果。
* 提示:輸出每一個數字欄寬設定為3,每3個一列,靠右對齊。
3. 輸入輸出:
(1) 輸入說明
12 個正整數(範圍 1~99)
(2) 輸出說明
格式化輸出12個正整數
12個數字中,索引為偶數的數字相加總合
(3) 範例輸入
範例輸入：
1
2
3
4
....12
輸出結果：
  1  2  3
  4  5  6
  7  8  9
 10 11 12
36
'''
size = 12
sum_of_even_index = 0
count = 0
aList = []
for i in range(size):
    aList.append(eval(input()))
for i in range(size):
    count += 1
    print('%3d' % aList[i], end = '\n' if count % 3 == 0 else'')
    if i % 2 == 0:
        sum_of_even_index += aList[i]
print(sum_of_even_index)

'''綜合範例02
(1) 請撰寫一程式,讓使用者輸入 52 張牌中的5張,計算並輸出其總和。
* 提示:J、Q、K以及A分別代表 11、12、13 以及1。
3. 輸入輸出:
(1) 輸入說明
5張牌數
(2)輸出說明
5張牌的數值總和
範例輸入：
5
10
K
3
A
輸出結果：
32
'''
cards = []
result = 0
for i in range(5):
    cards.append(input())
for i in range(5):
    if cards[i] == 'A': result += 1
    elif cards[i] == 'i': result += 11
    elif cards[i] == 'a': result += 12
    elif cards[i] == 'K': result += 13
    elif cards[i] == '10': result += 10
    else:
        result += eval(cards[i])
print(result)

'''綜合範例03
(1) 請撰寫一程式,要求使用者輸入十個數字並存放在串列中。
接著由大到小的順序顯示最大的3個數字。
輸入輸出:
(1) 輸入說明
十個數字
(2)輸出說明
由大到小排序,顯示最大的3個數字
範例輸入：
1
2
3
4
....10
輸出結果：
10 9 8
'''
lst = []
for i in range(10):
    lst.append(eval(input()))
lst.sort()
print(lst[-1], lst[-2], lst[-3])

'''綜合範例04
(1) 請撰寫一程式,讓使用者輸入十個整數作為樣本數,輸出眾數(樣本中出 現最多次的數字)及其出現的次數。
* 提示:假設樣本中只有一個眾數。
3. 輸入輸出:
(1) 輸入說明
十個整數
(2)輸出說明
眾數
眾數出現的次數
範例輸入：
1
1
1
3
4
5
6
7
8
10
輸出結果：
1
3
'''
size = 10
sample = []
count = [0]*size

for i in range(size):
    num = int(input())
    sample.append(num)
    count[sample.index(num)] += 1
num_occu = max(count)
print('\n%s' %sample[count.index(num_occu)])
print(num_occu)

'''綜合範例05
設計說明:
(1) 請撰寫一程式,讓使用者輸入十個成績,接下來將十個成績中最小和最大
值(最小、最大值不重複)以外的成績作加總及平均,並輸出結果。
* 提示:平均值輸出到小數點後第二位。
3. 輸入輸出:
(1) 輸入說明
十個數字
(2)輸出說明
總和 平均
範例輸入：
1
2
3
4
5
6
7
8
9
10
輸出結果：
44
5.50
'''
lst=[]

for i in range (10):
    lst.append(eval(input()))

total = sum(lst) - max(lst) - min(lst)

print('\n%s'%total)
print("%.2f" % (total/8))

'''綜合範例06
設計說明:
(1)請撰寫一程式,讓使用者輸入兩個正整數rows、cols,分別表示二維串列
lst 的「第一個維度大小」與「第二個維度大小」。串列元素[row][col]所儲存的數字,其規則為:row、col 的交點值 = 第二個維度的索引 col - 第一
個維度的索引 row。
(2) 接著以該串列作為參數呼叫函式compute()輸出串列。
* 提示:欄寬為4。
(1) 輸入說明
兩個正整數(rows、cols)
(2)輸出說明
格式化輸出 Pow、col 的交點值點
範例輸入：
5
10
輸出結果：
   0   1   2   3   4   5   6   7   8   9
  -1   0   1   2   3   4   5   6   7   8
  -2  -1   0   1   2   3   4   5   6   7
  -3  -2  -1   0   1   2   3   4   5   6
  -4  -3  -2  -1   0   1   2   3   4   5
'''
def compute(lst):
    for i in range (len(lst)):
        for j in range(len(lst[i])):
            print("%4d" % lst[i][j], end='')
        print()
row = eval(input())
column = eval(input())
lst = []
for i in range(row):
    lst.append([])
    for j in range(column):
        lst[i].append(j - i)

compute(lst)

'''綜合範例07
設計說明:
(1) 請撰寫一程式,讓使用者輸入三位學生各五筆成績,接著再計算並輸出每
位學生的總分及平均分數。
* 提示:平均分數輸出到小數點後第二位。
(1) 輸入說明
三位學生各五筆成績
(2)輸出說明
格式化輸出每位學生的總分及平均分數
(3) 輸入與輸出會交雜如下,輸出之項目以粗體字表示
範例輸入：
The 1st student:
99
100
88
75
10
The 2nd student:
45
65
18
90
100
The 3rd student:
55
66
23
14
85
輸出結果：
Student 1
#Sum 372
#Average 74.40
Student 2
#Sum 318
#Average 63.60
Student 3
#Sum 243
#Average 48.60
'''
score_lst = []
order_lst = ["1st", "2nd", "3rd"]

for i in range(3):
    print("The %s student:" % order_lst[i])
    score_lst.append([])
    for j in range (5):
        score_lst[i].append(eval(input()))
for i in range(3):
    print("Student %d" % (i + 1))
    print("#Sum %d" % (sum(score_lst[i])))
    print("#Average %.2f" % (sum(score_lst[i]) / 5))

'''綜合範例08
設計說明:
(1) 請撰寫一程式,讓使用者建立一個3*3的矩陣,其內容為從鍵盤輸入的整
數(不重複),接著輸出矩陣最大值與最小值的索引。
3. 輸入輸出:
(1) 輸入說明
九個整數
(2) 輸出說明
矩陣最大值及其索引 矩陣最小值及其索引
範例輸入：
1
2
3
4
5
6
7
8
9
輸出結果：
Index of the largest number 9 is: (2, 2)
Index of the smallest number 1 is: (0, 0)
'''
size = 3
mat = []

for i in range(size):
    mat.append([])
    for j in range(size):
        mat[i].append(eval(input()))
max_num = min_num = mat[0][0]
max_index = min_index = [0, 0]

for i in range(size):
    for j in range(size):
        if mat[i][j] > max_num:
            max_num = mat[i][j]
            max_index = [i, j]
        elif mat[i][j] < min_num:
            min_num = mat[i][j]
            min_index = [i, j]

print("Index of the largest number %d is: (%d, %d)"
        % (max_num, max_index[0], max_index[1]))
print("Index of the smallest number %d is: (%d, %d)"
        % (min_num, min_index[0], min_index[1]))

'''綜合範例09
設計說明:
(1) 請撰寫一程式,讓使用者建立兩個2*2 的矩陣,其内容為從鍵盤輸入的整
數,接著輸出這兩個矩陣的内容以及它們相加的結果。
3. 輸入輸出:
(1) 輸入說明
兩個2*2 矩陣,皆輸入整數
(2) 輸出說明
矩陣1的内容
矩陣2的内容
矩陣1及矩陣2相加的結果
範例輸入：
Enter matrix 1:
[1, 1]: 3
[1, 2]: 5
[2, 1]: 7
[2, 2]: 5
Enter matrix 2:
[1, 1]: 6
[1, 2]: 9
[2, 1]: 8
[2, 2]: 3
輸出結果：
Matrix 1:
35
75
Matrix 2:
69
83
Sum of 2 matrices:
914
158
'''
def compute(mat, num_row, num_col):
    for i in range(num_row):
        for j in range(num_col):
            print("%d" % mat[i][j], end='')
        print()

ROWs = COLs = 2
mat1 = []
mat2 = []

print("Enter matrix 1:")
for i in range (ROWs):
    mat1.append([])
    for j in range (COLs):
        print("[%d, %d]: " % (i + 1, j + 1), end='')
        mat1[i].append(eval(input()))

print("Enter matrix 2:")
for i in range (ROWs):
    mat2.append([])
    for j in range (COLs):
        print("[%d, %d]: " % (i + 1, j + 1), end='')
        mat2[i].append(eval(input()))
print("Matrix 1:")
compute(mat1, ROWs, COLs)
print("Matrix 2:")
compute(mat2, ROWs, COLs)

print("Sum of 2 matrices:")
for i in range (ROWs):
    for j in range (COLs):
        print("%d" % (mat1[i][j] + mat2[i][j]), end='')
    print()

'''綜合範例10
設計說明:
(1) 請撰寫一程式,讓使用者輸入四週各三天的溫度,接著計算並輸出這四週
的平均溫度及最高、最低溫度。
* 提示1:平均溫度輸出到小數點後第二位。
* 提示2:最高溫度及最低溫度的輸出,如為31 時,則輸出31,如為
31.1 時,則輸出 31.1。
3. 輸入輸出:
(1) 輸入說明
四週各三天的溫度
(2) 輸出說明
平均溫度
最高溫度
最低溫度
範例輸入：
Week 1:
Day 1:23.1
Day 2:24
Day 3:23.5
Week 2:
Day 1:32
Day 2:33
Day 3:35.3
Week 3:
Day 1:29
Day 2:30
Day 3:26
Week 4:
Day 1:27.6
Day 2:25
Day 3:28.8
輸出結果：
Average: 28.11
Highest: 35.3
Lowest: 23.1
'''
num_week = 4
num_day = 3
temp = []

for i in range(num_week):
    temp.append([])
    print("Week %d:" % (i+1))
    for j in range(num_day):
        temp[i].append(eval(input("Day %d:" % (j+1))))
comb = []
for i in range (num_week):
    comb.extend(temp[i])

avg = sum( comb) / (num_week*num_day)
print("Average: %.2f" % avg)
print("Highest:", max(comb))
print("Lowest:", min(comb))

'''綜合範例11
設計說明:
請撰寫一程式,將一宣告好的整數串列(大小為5)傳遞給名為output(aList)的函式,
此函式將以使用者的輸入初始化後,再將之回傳到主程式並輸出該串列。
接著, 主程式將該串列傳遞給名為 max(aList)和 min(aList)函式,
並分別回傳後輸出 aList 的巨大植(Max)和最小值(Min)。請不要使用系統提供的函式。
範例輸入：

輸出結果：

'''
#程式教材有error
def output(aList):
    for i in range(len(aList)):
        aList[i] = eval(input())
    return aList

def max(aList):
    max_num = aList[0]
    for i in range(len(aList)):
        if aList[i] >max_num:
            max_num = aList[i]
    return max_num

def min(aList):
    min_num = aList[0]
    for i in range(len(aList)):
        if aList[i] <min_num:
            min_num = aList[i]
    return min_num

def main():
    lst = [0] * 5
    print(compute(lst))
    print("Max =", max(lst))
    print("Min =", min(lst))
main()

'''綜合範例12
設計說明:
請撰寫一程式,使用者輸入十個數字(不重複)至串列,並將該串列傳遞給名為comput()函式
此函式接收一個串列 lst 和一個數字a(預設3),並回傅 1st中3個最大的數字最後再將回傳結果輸出。
範例輸入：

輸出結果：

'''
#程式教材有error
def compute(lst, a=3):
    lst.sort()
    ans = []
    for i in range(-1,-1*a-1,-1):
        ans.append(lst[i])
    return ans
def main():
    lst = []
    for i in range(10):
        num = eval(input())
        lst.append(num)
        print(lst)
        print(compute(lst))
main()

'''綜合範例13
設計說明:
試撰寫程式,以lotto()產生大樂透號碼,並以main()函式呼叫五次lotto()函式，
亦即產生五組大樂透號碼。請將的樂透號碼由小至大排序之。

範例輸入：
無
輸出結果：
[35]
[27, 35]
[27, 35, 43]
[25, 27, 35, 43]
[25, 26, 27, 35, 43]
[25, 26, 27, 35, 43, 46]
[25]
[25, 34]
[9, 25, 34]
[9, 25, 34, 43]
[9, 25, 34, 37, 43]
[9, 25, 29, 34, 37, 43]
[2]
[2, 28]
[2, 28, 47]
[2, 28, 42, 47]
[2, 28, 31, 42, 47]
[2, 26, 28, 31, 42, 47]
[26]
[26, 45]
[22, 26, 45]
[18, 22, 26, 45]
[18, 22, 26, 45, 49]
[12, 18, 22, 26, 45, 49]
[15]
[15, 43]
[15, 43, 49]
[15, 20, 43, 49]
[12, 15, 20, 43, 49]
[3, 12, 15, 20, 43, 49]
'''
import random
def lotto():
    lottoLst = []
    count = 0
    while count < 6:
        lottoNum = random.randint(1,49)
        if lottoNum not in lottoLst:
            lottoLst.append(lottoNum)
            count += 1
        lottoLst.sort()
        print(lottoLst)

def main():
    for i in range(1,6):
        lotto()
main()

'''綜合範例14
設計說明:
試撰寫一程式,以隨機亂數的方式產生100 個介於1~1000 的亂數,將它置放於randLst串列中
然後印出第二小的數和第二大的數。
範例輸入：
無
輸出結果：
   1   5  10  13  18  38  40  41  64  77
 104 107 113 137 166 186 188 193 207 220
 238 242 255 256 258 262 264 265 287 295
 326 351 353 353 360 364 369 372 409 415
 418 426 427 427 452 455 487 513 517 517
 534 554 563 564 573 592 605 624 625 664
 678 693 698 702 704 711 715 717 717 721
 750 795 797 811 820 840 844 851 854 862
 865 867 875 878 878 878 917 924 925 925
 927 928 937 939 960 970 976 990 991 998

5
991
'''
import random
randLst = []
for i in range(100):
    randNum = random.randint(1, 1000)
    randLst.append(randNum)

randLst.sort()
for j in range(1, 101):
    if j% 10 == 0:
        print('%4d'%(randLst[j-1]))
    else:
        print('%4d'%(randLst[j-1]), end = '')

print()
print(randLst[1])
print(randLst[len(randLst) - 2])

'''綜合範例15
設計說明:
承綜合範例14，這100個亂數不能重複
範例輸入：
無
輸出結果：
  10  11  13  25  62  64  79 113 117 122
 130 134 141 142 143 150 157 167 181 185
 194 201 203 207 216 225 253 258 259 277
 284 297 313 316 333 359 361 366 378 399
 401 403 456 465 482 486 490 502 510 522
 539 546 560 566 580 587 594 597 598 602
 610 612 628 638 641 650 651 656 663 687
 717 724 737 749 751 761 763 775 783 784
 790 848 864 879 880 890 905 912 915 919
 933 936 943 945 952 974 981 983 989 998

11
989
'''
import random
randLst = []
count = 1
while count <= 100:
    randNum = random.randint(1, 1000)
    if randNum not in randLst:
        randLst.append(randNum)
        count += 1
randLst.sort()
for j in range(1, 101):
    if j % 10 == 0:
        print('%4d'%(randLst[j-1]))
    else:
        print('%4d'%(randLst[j-1]), end = '')

print()
print(randLst[1])
print(randLst[len(randLst) - 2])
