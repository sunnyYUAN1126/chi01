'''7-1 數組 ( ) =====================================================
Python 的數組(tuple)和串列很相似,但有下列幾項不同:
1、數組的元素值不可以改變。
2、在數組中無法刪除個別元素和取代數組中的資料,
   但可以删除整個數組的所有元素。
3、沒有提供類似串列加入的方法如 append 和 insert,
   但可以利用 + 來加入元素於數組或是利用 * 來複製元素。
'''

'''7-1-1建立數組 =============================================
數組是以 小括號 來建立的,元素之間以逗號隔開,如下所示：
'''
tuple1  = (2,4,1,3,9,5)
tuple1
# (2,4,1,3,9,5)
'''若小括號內沒有元素,則表示為空數組,如下所示: '''
tuple2 =()
tuple2
#()
'''也可以從 串列 中建立數組,如下所示: *******************************''' 
tuple3 = tuple([x for x in range(1, 6)])
tuple3
#(1,2,3,4,5)

tuple3333 = ([x for x in range(1, 6)]) #list
'''這表示建立了一數組 tuple3 ,元素計有(1,2,3,4,5)。

注意,要加上tuple這個也可以從 字串 建立數組,
其數組是這字串中字元所組成的。如下所示: 
'''
tuple33 = tuple(1,2,3,4,5)
# TypeError: tuple expected at most 1 arguments, got 5
tuple33 = tuple("12345")
tuple33
#  ('1', '2', '3', '4', '5')

tuple4 = tuple( 'Python')
tuple4
# ('P', 'y', 't', 'h', 'o', 'n')

'''如始可以使用 len、max、min、sum 等串列所使用的函式,
同時也可以 in、not in、*,以及 + 的運算子,
這些功能和串列相似。如以下範例所示: '''
tuple1 = (2,4,1,3,9, 5)
tuple1
# (2, 4, 1, 3, 9, 5)

len(tuple1)
#6
max(tuple1)
#9
min(tuple1)
#1
sum(tuple1)
#24
8 in tuple1
#False
9 in tuple1
#True
9 not in tuple1
#False

'''注意,只連結一個元素時,而要在其後面加上逗號。也可以一次連結二個元素於數組 。'''
tuple1 += (6)
# TypeError: can only concatenate tuple (not "int") to tuple

tuple1 += (6,)
tuple1
#(2,4,1,3,9,5,6)

tuple1 += (7,8,9, )
tuple1
# (2, 4, 1, 3, 9, 5, 6, 7, 8, 9)

tuple1 += (7,8)
tuple1
# (2, 4, 1, 3, 9, 5, 6, 7, 8, 9, 7, 8)

'''可以利用索引來摘取數組的某一元素。 '''
tuple1
# (2, 4, 1, 3, 9, 5, 6, 7, 8, 9, 7, 8)
tuple1[2]
# 1
tuple1[3:6]
#(3, 9, 5)

tuple2 = 2 * tuple1
tuple2
# (2, 4, 1, 3, 9, 5, 6, 7, 8, 9, 7, 8, 2, 4, 1, 3, 9, 5, 6, 7, 8, 9, 7, 8)

'''同時也可以 for迴圈敘述印出數組中所有的資料。************************** '''
for i in tuple1:
    print(i, end = ' ')
# 2 4 1 3 9 5 6 7 8 9 7 8

'''我們前面提到,數組不可以删除某一元素,也不能更改其元素值,
但可以利用del 刪除整個數組。
如下所示: '''
del tuple1
tuple1
# NameError: name 'tuple1' is not defined

'''當利用del 删除了tuple1 整個數組後,
再顯示tuple1,只會印出  NameError: 的訊息。 '''

'''7-2 集合 {   } =====================================================
7-2-1 建立集合
集合是以大括號 { } 來建立的,元素之間以逗號隔開,如下所示:
'''
set1 = {1, 3, 5}
set1
#{1, 3, 5}
'''若是建立空集合,則必需撰寫如下:'''
set2 = set()
set2
# set()
print(set2)
# set()

'''集合也可以從 串列 或 數組 建立資料,
   如以下是從 串列 建立集合的資料: '''
set3 = set([x for x in range(1, 6)])
set3
# {1, 2, 3, 4, 5}

'''下面是從 數組 加以建立集合的資料: '''
set4 = set((1,2,3))
set4
# {1,2,3}
'''集合不會包含重複的資料,所以 *************************************** '''
set5 = set((1,1,2,2,3))
set5
# {1,2,3}

'''7-2-2 集合的 加入與 刪除 =======================================
你可以使用 add(x)將 x 加入集合中,或使用 
         remove(x)  將x 從集合中刪除。'''
set10 = {1,3,6}
set10
# {1, 3, 6}
set10.add(20)
set10
{1, 3, 6, 20}
set10.remove(3)
set10
# {1,6,20}
'''也可以使用計算長度的 len()、
   計算總和的 sum()、以及求出
   最大和最小值的 max() 與 min()。 '''
set20 = {1,3,6,8,10}
len(set20) 
# 5
sum(set20)
# 28
max(set20)
# 10
min(set20)
# 1

'''同樣地,也可以 in 和 not in 用來檢視某一元素是否在集合。 '''
set20 = {1,3,6,8,10}
4 in set20
#False
8 in set20
#True


'''若要印出集合中的所有元素,則也可以使用 for 來完成,如下所示: '''
for x in set20:
    print(x, end = ' ')
#1 3 6 8 10

set20[2]
# TypeError: 'set' object does not support indexing

'''7-2-3 集合的聯集、交集、差集,以及對稱差集 ================================
在集合中,一般還會使用所謂的

聯集(union)、                      |
交集(intersection)、               &
差集(difference), 以及             -
對稱差集(symmetric difference)。   ^

我們可使用 union 或 | 表示聯集,
以 intersection 或 & 表示交集,
以 difference 或 - 表示差集,以 
symmetric_difference 或 ^ 表示對稱差集。

A、B兩集合的聯集,表示先將A集合的項目加入後, ===============================
再加入B集合中 A 集合沒 有的項目。請看以下的範例:  
'''
set20 = {1,6,8,10,20}
set25 = {1,3,8,10}

set20.union(set25)
# {1, 3, 6, 8, 10, 20}
set20
#  {1, 6, 8, 10, 20}
set25
#  {1, 3, 8, 10}
'''以上與 set20 | set25 是相同的。'''
set20 = {1,6,8,10,20}
set25 = {1,3,8,10}

set20 | set25
# {1, 3, 6, 8, 10, 20}

'''A、B兩集合的交集,表示A 集合和B集合共有的項目,如下範例所示: =================='''
set20.intersection(set25)
# {1, 8, 10}
set20
# {1, 6, 8, 10, 20}
set25
# {1, 3, 8, 10}

'''以上與 set20 & set25 的運作是相同的。'''
set20 & set25
# {1, 8, 10}

''''A、B兩集合的差集,表示將A集合去掉與B集合共有的項目, ==========================
    如下範例所示: '''
set20.difference(set25)
# {6, 20}

'''以上與 set20 - set25 是相同的。'''
set20 - set25
#  {6, 20}

'''A、B兩集合的對稱差集,表示去掉A集合與B集合共有的項目, =========================
   如下範例所示: '''
set20.symmetric_difference(set25)
# {3, 6, 20}

'''以上與 set20 ^ set25 是相同的。'''
set20 ^ set25
# {3, 6, 20}


'''7-2-4 子集合、超集合,以及 == 和 !=    ===================================
除了上述有關集合的運作外,
還有子集合(subset)或超集合(superset)。
子集合 表示若A集合的所有項目是B集合的部份集合,則稱A是B的部份集合,
而B 是 A的超集合。如下範例所示: '''
set15 = {1,3,8, 10}
set20 = {1,3,8}
set20.issubset(set15)
True
set15.issuperset(set20)
True
'''最後,集合也可以利用 == 和 != 來檢視兩個集合是否相等或不相等,如下範例所
示: '''
set30 = {1,8,3}
set20 == set30
True
set30 != set30
False
set20 == set15
False

'''7-3 詞典 {  }  ===============================================================
  詞典(dictionary)由一 鍵值(key)和 數值(value)所組成的數對。

7-3-1 建立一詞典
我們可經由一對大括號建立詞典,若括號內是空的,如下所示:
其表示建立一空的 dic10 詞典。'''
dic10 = {}
dic10

dic10 = {'Taipei': '101', 'Paris':'Tour Eiffel', 'London': 'Big Ben'}
dic10
{'Taipei': '101', 'Paris': 'Tour Eiffel', 'London': 'Big Ben'}

'''7-3-2 詞典的運作 ======================================================
若要加入一詞典的項目,則如下範例所示: '''
dic10['Berlin'] = 'Wall' 
'''表示將鍵值'Berlin'與對應的數值 'Wall' 加入於 dict10 的詞典中。 '''

dic10 
'''
{'Taipei': '101',
 'Paris': 'Tour Eiffel',
 'London': 'Big Ben',
 'Berlin': 'Wall'}
'''

'''也利用 for迴圈印出 dic10 詞典上的鍵值:數值對'''
for key in dic10:
    print('%s:%s'%(key, dic10[key]))
'''    
Taipei:101
Paris: Tour Eiffel
London: Big Ben
Berlin:Wall
'''

'''可以利用 index [] 運算子,得到某一鍵值所對應的數值,如下範例所示: '''
dic10['Taipei']
'101'
dic10['Paris']
dic10['London']
dic10['Berlin']

dic10['Taiwan']
# KeyError: 'Taiwan'

'''詞典也可以使用 len 來計算詞典有多少項目,
   利用 in 和 not in 判斷某一鍵值是否 存在於詞典中,
   利用 == 和 != 檢視兩個詞典的項目是否相等或不相等,
   無關其項目的順序。如下範例所示: '''
len(dic10)
#4
' Taipei' in dic10
#True
'Tainan' in dic10
#False
'Tainan' not in dic10
#True

# 無關其項目的順序。如下範例所示: 
dic12 ={10:'John', 30: 'Peter', 20: 'Mary'}
dic22 ={10:'John', 20:'Mary', 30:'Peter'}

dic12 == dic22
# True
dic12 != dic22
# False

'''若要刪除詞典中的某一項目,則可利用 del 來完成,如下所示: '''
dic10
'''
{'Taipei': '101',
 'Paris': 'Tour Eiffel',
 'London': 'Big Ben',
 'Berlin': 'Wall'}
'''
del dic10['Taipei']
dic10 
{'Paris': 'Tour Eiffel', 'London': 'Big Ben', 'Berlin': 'Wall'}

del dic10['Tour Eiffel']
# KeyError: 'Tour Eiffel'

'''除了以上的功能外,還提供以下的有關詞典方法,方便使用者使用。
   1. 利用keys()可以得到詞典中項目的鍵值,'''
dic10.keys()

# dict_keys(['Paris', 'London', 'Berlin'])

''' 2. valunes)可以得到詞典中項目的數值, '''
dic10.values()
#dict_values(['Tour Eiffel', 'Big Ben', 'Wall'])

'''3. items()表示詞典的項目 ================================================'''
dic10.items()
#dict_items([('Paris', 'Tour Eiffel'), ('London', 'Big Ben'), ('Berlin','wall')])

'''不過上述的輸出結果都會加上dict 與其欲知的資訊。
   我們可以在方法前加上 tuple,則其結果會較簡潔。
   如下所示'''
tuple(dic10. keys())
#('Paris', 'London', 'Berlin')
tuple(dic10.values())
#('Tour Eiffel', 'Big Ben', 'Wall')
tuple(dic10.items())
#(('Paris', 'Tour Eiffel'), ('London', 'Big Ben'), ('Berlin', 'Wall'))

dic10.get('London')
# 'Big Ben'
print(dic10.get('London'))
# Big Ben

'''除了利用 del 删除詞典中某一項目外,也可以
   使用 pop() 删除某一鍵值的項目, 
   popitem()表示删除最後的一個項目,
   而clear()則刪除詞典中的所有項目,
    如下範例所示:'''

dic10 
#{'Paris': 'Tour Eiffel', 'London': 'Big Ben', 'Berlin': 'Wall'}
dic10.pop('Paris')
#'Tour Eiffel'
dic10
#{'London':'Big Ben', 'Berlin':'Wall'}

dic10['Taipei'] = '101'
dic10
#{'London': 'Big Ben','Berlin':'Wall','Taipei':'101'}

dic10.popitem()
#('Taipei', '11')

dic10.popitem()
# ('Berlin', 'Wall')

dic10 
#{'London': 'Big Ben'}

dic10['Berlin'] = 'Berlin Wall'
dic10['Taipei'] = '101'
dic10 
#{'London': 'Big Ben', 'Berlin': 'Berlin Wall', 'Taipei': '101'}
dic10.clear()
dic10
#{}

'''有關詞典的函式還有兩個蠻好用的。
    那就是copy() 和 update()。
copy()是將某一 詞典複製到另一詞典,而 
update()是將兩個詞典合併的意思,'''

dict1 = {1:'Red',2:'Yellow', 3:'Green'}
dict1
#{1:'Red', 2:'Yellow', 3: 'Green'}

dict2 = {4: 'Black', 1:'Red'}
dict2
#{4: 'Black', 1: 'Red'}

'''以下是將dictl 詞典複製給 dict3。 '''
dict3 = dict1.copy()
dict3
#{1:'Red', 2:'Yellow', 3:'Green'}

dict3 == dict1
# True

'''以下是將dict2 詞典合併到 dict3。'''
dict2
# {4: 'Black', 1: 'Red'}
dict3
# {1: 'Red', 2: 'Yellow', 3: 'Green'}

dict3.update(dict2)    # update()是將兩個詞典合併的意思
dict3
{1:'Red', 2:'Yellow', 3:'Green', 4: 'Black'}
# 有相同的 key 只取一個 key

'''
綜合範例1: =============================================================
設計說明:
(1) 請撰寫一程式,輸入數個整數並儲存至串列 [] 中,
    以輸入-9999 為結束點(列中不包含-9999),
    再將此 串列 轉換成 數組,最後顯示該 數組以及
    其長度 (Length)、最大值(Max)、最小值(Min)、總和(Sum)。
3. 輸入輸出:
(1) 輸入說明
    n個整數,直至-9999 結束輸入
輸出：
-4
0
37
19
26
-9999
(-4, 0, 37, 19, 26)
Length: 5
Max: 37
Min: -4
Sum: 78
'''

# 輸入數個整數並儲存至串列 [] 中
num = []
count = 1
while True:
    n = int(input('輸入第 %d 個整數,如果輸入-9999 為結束輸入:' %count))
    if n == -9999:
        break
    num.append(n)
    count +=1

type(num)

# 將此 串列 轉換成 數組
num_tuple = tuple(num)
type(num_tuple)

print(num_tuple)

# 顯示該 數組以及其長度 (Length)、最大值(Max)、最小值(Min)、總和(Sum)。
print("Length:", len(num_tuple))
print("Max:", max(num_tuple))
print("Min:", min(num_tuple))
print("Sum:", sum(num_tuple))

'''
綜合範例2: =============================================================
設計說明:
(1)請撰寫一程式,輸入並建立兩組 數組,各以-9999 為結束點(數組中不包含 -9999)。         
   將此兩數組合併並從 小到大排序之, 顯示排序前的數組 和 排序後的串列。
3. 輸入輸出:
(1) 輸入說明
    兩個數組,直至-9999 結束輸入
(2) 輸出說明
排序前的數組
排序後的串列
輸出：
Create tuple1:
9
0
-1
3
8
-9999
Create tuple2:
28
16
39
56
78
88
-9999
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]
'''

# 建立兩組空數組
tup1 = ()
tup2 = ()

# 輸入建立兩組數組
print("Create tuple1:")
count = 1
while True:
    num = eval(input('輸入第 %d 個整數,如果輸入-9999 為結束輸入:' %count))
    if num == -9999:
        break
    tup1 += (num,)
    count +=1

print("Create tuple2:")
count = 1
while True:
    num = eval(input('輸入第 %d 個整數,如果輸入-9999 為結束輸入:' %count))
    if num == -9999:
        break
    tup2 += (num, )
    count +=1

# 將此兩數組合併
tup_comb = tup1 + tup2
print("數組 1:", tup1)
# 數組 1: (9, 0, -1, 3, 8)
print("數組 2:", tup2)
# 數組 2: (28, 16, 39, 56, 78, 88)

print("Combined tuple before sorting:", tup_comb)
# Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)

# 排序後的串列
lst_comb = list(tup_comb)
print("Combined list after sorting:", sorted(lst_comb))
# Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]

# 排序後的串列
lst_comb.reverse()
print("Combined list after sorting:", lst_comb)
# Combined list after sorting: [88, 78, 56, 39, 16, 28, 8, 3, -1, 0, 9]


'''綜合範例3: ===================================================
設計說明:
(1) 請撰寫一程式,輸入一些 字串至數組(至少輸入五個字串), 
    以字串"end"為結束點(數組中不包含字串"end")。
    接著輸出該數組,再分別
    顯示該數組的第一個元素到第三個元素和 倒數三個元素。
3. 輸入輸出:
(1) 輸入說明
至少輸入五個字字串至數組,直至end 結束輸入
(2) 輸出說明
數組 該數組的前三個元素 該數組最後三個元素
(3) 範例輸入
president
dean
chair
staff
teacher
student
end
輸出：
('president ', 'dean ', 'chair ', 'staff ', 'teacher ', 'student ')
('president ', 'dean ', 'chair ')
('staff ', 'teacher ', 'student ')
'''
tup = ()
count = 1
while True:
    word = input('輸入第 %d 個字串,如果輸入字串"end"為結束輸入:'%count)
    if word == "end":
        break
    tup += (word, )
    count +=1
    
print(tup)
# ('president', 'dean', 'chair', 'staff', 'teacher', 'student')

# 數組的前三個元素
print(tup[0:3])
# ('president', 'dean', 'chair')

# 該數組最後三個元素
print(tup[-3:])
# ('staff', 'teacher', 'student')

'''綜合範例4: ===================================================
2. 設計說明:
(1) 請撰寫一程式,輸入數個整數並儲存至 集合,
    以輸入-9999 為結束點(集合中不包含-9999),
    最後顯示該
    集合的長度(Length)、最大值(Max)、 最小值(Min)、總和(Sum)。
3. 輸入輸出:
(1) 輸入說明
輸入n個整數至集合,直至-9999 結束輸入
(2) 輸出說明
集合的長度
集合中的最大值 集合中的最小值 集合内的整數總和
輸入：
9
6
7
4
5
-9999
輸出：
Length: 5
Max: 9
Min: 4
Sum: 31
'''
num = set()
count = 1
while True:
    inp = eval(input('輸入第 %d 個整數,如果輸入-9999 為結束輸入:'%count))
    if inp == -9999:
        break
    num.add(inp)
    count +=1

print("集合元素:", num)
# 集合元素: {4, 5, 6, 7, 9}

# 集合的長度(Length)、最大值(Max)、 最小值(Min)、總和(Sum)。   
print("Length:", len(num))
# Length: 5

print("Max:", max(num))
# Max: 9

print("Min:", min(num))
# Min: 4

print("Sum:", sum(num))
# Sum: 31

'''綜合範例5: ===========================================================
(1) 請撰寫一程式,依序輸入五個、三個、九個整數,
    並各自儲存到集合 setl、set2、set3中。
    接著回答:set2 是否為 set1 的子集合(subset) ?
    set3 是否 為 set1 的超集合(superset)?
3. 輸入輸出:
(1) 輸入說明
   依序分別輸入五個、三個、九個整數
(2)輸出說明
顯示回覆: set2 是否為 set1的子集合(subset)? set3 是否為 set1的超集合(superset)?
輸入：
Input to set1:
3
28
-2
7
39
Input to set2:
2
77
0
Input to set3:
3
28
12
99
39
7
-1
-2
65
輸出：
set2 is subset of set1: False
set3 is superset of set1: True
'''
set1 = set()
set2 = set()
set3 = set()

# 依序分別輸入五個、三個、九個整數
print("Input to set1 輸入五個整數:")
for i in range (5):
    num = int(input('輸入五個整數第 %d 個整數:'%(i+1)))
    set1.add(num)
print("set1:", set1)
# set1: {3, 39, 7, 28, -2}

print("Input to set2 輸入三個整數:")
for i in range(3):
    num = int(input('輸入三個整數第 %d 個整數:'%(i+1)))
    set2.add(num)
print("set2:", set2)
# set2: {0, 2, 77}

print("Input to set3 輸入九個整數:")
for i in range(9):
    num = int(input('輸入九個整數第 %d 個整數:'%(i+1)))
    set3.add(num)
print("set3:", set3)
# set3: {65, 99, 3, 39, 7, 12, -2, 28, -1}

print("set2 is subset of set1:", set2.issubset(set1))
print("set2:", set2)
print("set1:", set1)

print("set3 is superset of set1:", set3.issuperset(set1))
print("set3:", set3)
print("set1:", set1)

'''綜合範例6: ==========================================================
2. 設計說明:
(1) 全字母句(Pangram)是英文字母表所有的字母都出現至少一次
    (最好只出現一次)的句子。
    請撰寫一程式,要求使用者輸入一正整數 k(代表有 k 筆 測試資料),
    每一筆測試資料為一句子,程式判斷該句子是否為 Pangram, 
    並印出對應結果 True(若是)或 False(若不是)。
13. 輸入輸出:
(1) 輸入說明
    先輸入一個正整數表示測試資料筆數,再輸入測試資料 
(2) 輸出說明
輸入的資料是否為全字母句
輸出：
3
The quick brown jumps over the lazy dog
False
Learning pythob is funny
False
Pack my box with five dozen liquor jugs
True
'''
num_alph = 26

k = eval(input('使用者請輸入有幾筆測試資料?'))

for i in range(k):
    sentence = input('輸入 %d 個句子第 %d 個句子:'%(k, i+1))
    alphabet = set(sentence.lower())
    alphabet.remove(' ')
    print('alphabet = ',alphabet)
    print('alphabet = ',sorted(alphabet))
    print('alphabet有%d 字母'%(len(alphabet)))
    print('輸入的資料是否為全字母句(Pangram)?',len(alphabet) == num_alph)
    print(len(alphabet) == num_alph)

'''
輸入 3 個句子第 1 個句子:The quick brown jumps over the lazy dog
alphabet =  {'r', 'h', 'v', 'w', 'p', 'u', 'i', 'l', 'o', 'c', 'a', 'q', 'g', 'z', 'e', 'm', 'n', 'k', 'b', 't', 'd', 'j', 'y', 's'}
alphabet =  ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
alphabet有24 字母
輸入的資料是否為全字母句(Pangram)? False
False

輸入 3 個句子第 2 個句子:Learning pythob is funny
alphabet =  {'g', 'l', 'r', 'h', 'o', 'b', 't', 's', 'a', 'f', 'e', 'p', 'y', 'u', 'n', 'i'}
alphabet =  ['a', 'b', 'e', 'f', 'g', 'h', 'i', 'l', 'n', 'o', 'p', 'r', 's', 't', 'u', 'y']
alphabet有16 字母
輸入的資料是否為全字母句(Pangram)? False
False

輸入 3 個句子第 3 個句子:Pack my box with five dozen liquor jugs
alphabet =  {'r', 'h', 'v', 'w', 'p', 's', 'u', 'x', 'i', 'l', 'o', 'c', 'a', 'q', 'g', 'z', 'e', 'm', 'n', 'k', 'b', 't', 'd', 'j', 'f', 'y'}
alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet有26 字母
輸入的資料是否為全字母句(Pangram)? True
True
'''

'''綜合範例7： =========================================================
設計說明:
(1) 請撰寫一程式,輸入 X 組和 Y 組各自的科目至集合中,
    以字串"end"作為結束點(集合中不包含字串"end")。
    請依序分行顯示
    (1) X 組和 Y 組的所有科目、
    (2) X 組和 Y 組的共同科目、
    (3) Y 組有但 X 組沒有的科目,以及 
    (4) X 組和 Y 組彼此沒有的科目(不包含相同科目)。
     * 提示:科目須參考範例輸出樣本,依字母由小至大進行排序。
3. 輸入輸出:
(1) 輸入說明,
   輸入X組和Y組各自的科目至集合,直至 end 結束輸入
(2) 輸出說明
   X 組和 Y 組的所有科目 
   X 組和 Y 組的共同科目 
   Y 組有但 X 組沒有的科目 
   X 組和 Y 組彼此沒有的科目(不包含相同科目)
輸入：
Enter group X's subjects:
Math
Literature
English
History
Geography
end

Enter group Y's subjects:
Math
Literature
Chinese
physical
Chemistry
end

輸出：
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Literature', 'Math', 'physical']
['Literature', 'Math']
['Chemistry', 'Chinese', 'physical']
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'physical']
'''
X = set()
Y = set()

print("Enter group X's subjects:")
while True:
    subject = input()
    if subject == "end":
        break
    X.add(subject)
print("Group X's subjects:", X) 
# Group X's subjects: {'History', 'English', 'Geography', 'Math', 'Literature'}

print("Enter group Y's subjects:")
while True:
    subject = input()
    if subject == "end":
        break
    Y.add( subject)
print("Group Y's subjects:", Y)  
# Group Y's subjects: {'Chinese', 'Chemistry', 'physical', 'Math', 'Literature'}
 
print("Group X's subjects:", X)   
print("Group Y's subjects:", Y)     
    
print(sorted(X | Y))
print(sorted(X & Y))
print(sorted(Y - X))
print(sorted(X ^ Y))

print('X 組和 Y 組的所有科目' , sorted(X | Y))
# X 組和 Y 組的所有科目 ['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Literature', 'Math', 'physical']

print('X 組和 Y 組的共同科目' , sorted(X & Y))
# X 組和 Y 組的共同科目 ['Literature', 'Math']

print('Y 組有但 X 組沒有的科目' , sorted (Y - X))
# Y 組有但 X 組沒有的科目 ['Chemistry', 'Chinese', 'physical']

print('X 組和 Y 組彼此沒有的科目(不包含相同科目)' , sorted(X ^ Y))
# X 組和 Y 組彼此沒有的科目(不包含相同科目) ['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'physical']


'''綜合範例8: ===================================================
2. 設計說明:
(1)請撰寫一程式,自行輸入兩個 詞典 
   (以輸入鍵值"end"作為輸入結束點,詞典中將不包含鍵值"end"),
   將此兩詞典合併,並根據 key 值字母由 小到大 排序輸出,
   如有重複 key值,後輸入的key值將覆蓋前一key值。
3. 輸入輸出:
(1) 輸入說明
    輸入兩個詞典,直至end 結束輸入
(2) 輸出說明
    合併兩詞典,並根據key 值字母由小到大排序輸出,
    如有重複key值,後 輸入的key 值將覆蓋前一key 個
輸入：
Create dict1:
Key: a
Value: apple
Key: b
Value: banana
Key: d
Value: durian
Key: end

Create dict2:
Key: c
Value: cat
Key: e
Value: elephant
Key: end

輸出：
a: apple
b: banana
c: cat
d: durian
e: elephant
'''

def compute():
    dic = {}
    while True:
        key = input("Key: ")
        if key == "end":
            return dic

        value = input("Value: ")
        dic[key] = value

print("Create dict1:")
dict1 = compute()
print("詞典1 dict1:", dict1)
# 詞典1 dict1: {'a': 'apple', 'b': 'banana', 'd': 'durian'}

print("Create dict2:")
dict2 = compute()
print("詞典2 dict2:", dict2)
# 詞典2 dict2: {'c': 'cat', 'e': 'elephant'}

merge_dict = dict1.copy()
merge_dict
# {'a': 'apple', 'b': 'banana', 'd': 'durian'}

# 兩詞典合併
merge_dict.update(dict2)
merge_dict
#  {'a': 'apple', 'b': 'banana', 'd': 'durian', 'c': 'cat', 'e': 'elephant'}

# 根據 key 值字母由 小到大 排序
sortedDict = sorted (merge_dict)
sortedDict
#  ['a', 'b', 'c', 'd', 'e']

for i in sortedDict:
    print('%s: %s' % (i, merge_dict[i]))
'''
a: apple
b: banana
c: cat
d: durian
e: elephant
'''

'''綜合範例9 =======================================
2. 設計說明:
   請撰寫一程式,輸入一顏色詞典 color dict
   (以輸入鍵值"end"作為輸入結 束點,詞典中將不包含鍵值"end"),
   再根據 key值的字母由小到大排序並輸出。
3. 輸入輸出:
(1) 輸入說明
    輸入一個詞典,直至end 結束輸入
(2)輸出說明
   根據key 值字母由小到大排序輸出
   
輸入:
Key: Green Yellow
Value: #ADFF2F
Key: snow
Value: #FFFAFA
Key: Red
Value: #FF0000
Key: end

輸出:
Green Yallow: #ADFF2F
Red: #FF0000
snow: #FFFAFA
'''
color_dict = {}

while True:
    key = input("Key: ")
    if key == "end":
        break
    value = input("Value: ")
    color_dict[key] = value
    sortedDict = sorted(color_dict)

sortedDict
# ['Green Yellow', 'Red', 'snow']

for i in sortedDict:
    print('%s: %s' % (i, color_dict[i]))
'''
Green Yellow: #ADFF2F
Red: #FF0000
snow: #FFFAFA
'''

'''綜合範例10 ================================================================
2. 設計說明:
(1) 請撰寫一程式,為一詞典輸入資料
    (以輸入鍵值"end"作為輸入結束點,詞 典中將不包含鍵值"end"),
    再輸入一鍵值並檢視此鍵值是否存在於該詞典
3. 輸入輸出:
(1) 輸入說明
   先輸入一個詞典,直至 end 結束輸入,再輸入一個鍵值進行搜尋是否存在
(2) 輸出說明
    鍵值是否存在詞典中
    
輸入：
Key: 123-4567-89
Value: Jennifer
Key: 987-6543-21
Value: Tommy
Key: 246-8246-82
Value: Kay
Key: end
輸出：
Search key: 246-8246-82
True
'''
my_dict = {}

while True:
    key = input("Key: ")
    if key == "end":
        break
    value = input("Value: ")
    my_dict[key] = value

search_key = input("Search key: ")
print(search_key in my_dict)
'''
Search key: 246-8246-82
True

Search key: 246-8246-85
False

'''

'''綜合範例11 ============================================================
   撰寫一程式,輸入五筆資料置放於名為 tup10 的數組,
   之後印出此數組的每一元,以及找出此數組最大值、最小值與總和。
輸入輸出:
(1) 範例輸入
10
20
5
38
8
(2) 範例輸出
(10, 20, 5,38, 8)
max of the tuple is 38
min of the tuple is 5
sum of the tuple is 81
'''
i = 1
tup10 = ()
while i <= 5:
    a = eval(input())
    tup10 += (a, )
    i += 1
print(tup10)
# (10, 20, 5, 38, 8)

print('max of the tuple is ', max(tup10))
# max of the tuple is  38

print('min of the tuple is ', min(tup10))
# min of the tuple is  5

print('sum of the tuple is ', sum(tup10))
# sum of the tuple is  81


'''綜合範例12 ===============================================================
   試撰寫一程式,使用不定數迴圈,當使用者輸入 -9999 時才結束迴圈。
   將資料置於 名為 tup20 的數組,之後印此數組的每一元素,
   以及此數組第一個元素和最後一個元素。
1. 輸入輸出:
(1) 範例輸入
9
67
22
36
98
2
45
-9999
(2) 範例輸出
(9, 67, 22, 36, 98, 2, 45)
length of the tuple is  7
the first element is  9
the last element is  45
'''
tup20 = ()

while True:
    a = eval(input())
    if a != -9999:
        tup20 += (a, )
    else:
        break
print(tup20)
# (9, 67, 22, 36, 98, 2, 45)

print('length of the tuple is ', len(tup20))
# length of the tuple is  7

print('the first element is ', tup20[0])
# the first element is  9

print('the last element is ', tup20[len(tup20)-1])
# the last element is  45

'''綜合範例13 ===========================================================
   撰寫一程式,使用不定數迴圈輸入集合的資料,當使用者輸入 -9999 時才結束輸入。
   將資料置於名為 set10 的集合,之後印出此集合的每一元素。
1. 輸入輸出:
(1) 範例輸入
1
2
3
4
5
6
-9999
(2) 範例輸出
{1,2,3,4,5,6}
'''
set10 = set()

while True:
    a = eval(input())
    if a != -9999:
        set10.add(a)
    else:
        break
print(set10)
# {1, 2, 3, 4, 5, 6}

'''綜合範例14 ==============================================================
   試撰寫一程式,在inputData 函式中使用不定數迴圈輸入集合資料,
   當使用者輸入 -9999 時才結束輸入。
   在main()函式中,呼叫兩次 inputData()函式以建立兩個集合 setl 和 set2。
   利用operation()函式檢視 setl 和 set2 這兩個集合的聯集、交集、 差集,以及對稱差集。
   程式最後印出 setl 和 set2 集合的元素值,及上述集合的基本運算
輸入：
Input set1 data:
1
2
3
4
5
6
-9999
Input set2 data:
2
4
6
-9999
輸出：
set1 {1, 2, 3, 4, 5, 6}
set2 {2, 4, 6}

set1 | set2 = {1, 2, 3, 4, 5, 6}
set1 & set2 = {2, 4, 6}
set1 - set2 = {1, 3, 5}
set1 ^ set2 = {1, 3, 5}
'''
def inputData(set10):
    while True:
        a = eval(input())
        if a != -9999:
            set10.add(a)
        else:
            break
    return set10

def operation(set11, set12):
    print()
    print('set1 | set2 =', set11 | set12)
    print('set1 & set2 =', set11 & set12)
    print('set1 - set2 =', set11 - set12)
    print('set1 ^ set2 =', set11 ^ set12)

def main():
    print('Input set1 data: ')
    set1 = set()
    inputData(set1)
    print('Input set2 data: ')
    set2 = set()
    inputData(set2)
    print('set1', set1)
    print('set2', set2)
    operation(set1, set2)

main()
'''
set1 {1, 2, 3, 4, 5, 6}
set2 {2, 4, 6}

set1 | set2 = {1, 2, 3, 4, 5, 6}
set1 & set2 = {2, 4, 6}
set1 - set2 = {1, 3, 5}
set1 ^ set2 = {1, 3, 5}
'''


'''綜合範例15 ================================================================
  試撰寫一程式,使用不定數迴圈輸入詞典的鍵值與其對應的資料,
  使用者輸入. 9999 時才結束輸入。將資料置於名為 dict10 的詞典,
  之後印出此詞典的每一個鍵 值與其對應的資料。
1. 輸入輸出:
(1) 範例輸入
Input key: 1122
Input value: Peter
Input key: 1128
Input value: Mary
Input key: 1135
Input value: John
Input key: -9999
Input value: -9999
(2) 範例輸出
{1122:'Peter', 1128: 'Mary', 1135:'John'}
'''
dict10 = {}

while True:
    print('Input key: ', end = '')
    k = eval(input())
    print('Input value: ', end = '')
    V = eval('input()')
    if k != -9999:
        dict10[k] = V
    else:
        break
print(dict10)
# {1122: 'Peter', 1128: 'Mary', 1135: 'John'}
