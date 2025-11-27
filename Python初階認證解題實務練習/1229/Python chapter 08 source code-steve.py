'''字串 ================================================================
  在字串(string)這個主題,Python 比較特殊,因為可以使用雙引號或單引號來括住字串,如'Python is fun!"或是"Python is fun!"皆可,由於Python 沒有字串和字
元(character)之分。
但在其它程式語言如C、C++、Java 就不同了,字串是以雙引號括起來的,而字元是以單引號括起來的。 '''

'''8-1 建立空字串 ========================================================
  我們可使用以下兩種方式建立空字串,
  一是以 str(),
  二是以 ''表示之。 '''
s1 = str()
s1
''
s2 = ' '
s2
''

'''8-2 字串的運作 =======================================================
你可以初始化的方式來建立一字串,如下所示: '''

s3 = 'Learning Python now!'
s3
'Learning Python now!'
s4 = str('若要計算字串的長度c')
s4
'Learning Python now!'

'''若要計算字串的長度可使用 len 函式,
利用 max 與 min 函式分別計算字串的最大與最小值。
len(s3) '''

s3
# 'Learning Python now!'
len(s4)
#20
max(s4)
'y'
min(s3)
' '

'''利用索引運算子[]]用來擷取字串的某一字元。如下所示: ========================'''
s3[3:5]
'r'

'''若索引值是負值,則需將此值加上字串長度。 ============================='''
s4 = 'Python'
s4[4]
'n'

'''由於 s4 的長度為 6,所以 s4[-1] 的真正索引值為5 。亦即摘取 s4[5]。========= '''
len(s4)
# 6
s4[-3]
'h'
s4[len(s4)-3]
# 'h'

'''以此類推,s4[-3] 即為s4[3]。 
也可以使用分割運算子[start:end] 表示擷取從 start 到 end-1。'''
s4
# 'Python'
s4[1:4]
'yth'
s4[:4]
'Pyth'
s4[1:]
'ython'
s4[1:-1]
'ytho'

'''其中 s4[1:-1] 表示從 s4[1:-1+len(s4)],亦即 s3[1:5]。
   和串列一樣, 
   + 表示連結,而 
   * 表示複製。
   如下範例所示: '''
s5 = 'Bright'
s6 = 'Tsai'

s5+s6
'BrightTsai'

s6*2
'BrightBright'

(s5+s6)*2
# 'BrightTsaiBrightTsai'

'''要注意的是,要檢視某一字串是否在另一字串,
   可使用 in 或 not in。
   如下範例所 '''
s5
# 'Bsight'
'b' in s5
True

s6
# 'Bsai'
'T' not in s6
False

'Bro' in s5
True
'T' not in s6
False

len(s5) < len(s6)
False
B = "B"
B in s5 
# Traceback (most recent call last):
# File "<pyshell#287", line 1, in <module>
# B in s5 NameError: name 'B' is not defined

'''由於是判斷字串是否出現於某一字串中,所以必需要加上引號。
   由於上述的敘述沒 加上引號,所以出現錯誤的訊息。

同理,也可以利用 for 敘述列印字串的所有元素值。
   如下所示:'''
   
#for i in s5: 
# SyntaxError: invalid syntax

for i in s5:
    print(i, end='*')
    
# B r i g h t

'''8.3 測試字串 ========================================================
Python中的 str 類別提供許字串運作的方法。
   包括測試字串、
   子字串處理、
   轉換字串、
   如何從字串去掉空白,
   以及如何將字串加以格式化。
   我們將一一的說明之。

測試字串旨在測試字串是否屬於英文字母數字、字母、數字、以及其它種類,
如以下表格所示:

    表 8-1 測試字串的方法:
方法              說明
isalnum()         若字串的字元是字母和數字所組成,則回傳True
isalpha()         若字串的字元是字母所組成,則回傳 True
isdigit()         若字串的字元是數字所組成,則回傳 True
isidentifier()    若字串是符合識別字的名稱,則回傳 True
islower()         若字串的英文字元皆是由小寫字母所組成,則回傳 True
isupper()         若字串的英文字元皆是由大寫字母所組成,則回傳 True
isspace()         若字串的字元皆是由白色空白所組成,則回傳 True

請看以下所執行的範例:
'''
s5
# 'Bright'

s5.isalnum()
True

s5.isalpha()
True

s8 = '?'
s8.isalnum()
True

s8.isalpha()
True

s8.isdigit()
False

s8.isidentifier()
True

s8.isupper()
False

s8.islower()
False

s8.isspace()
False

s9 = 'abcde'
s9.islower()
True

'''8-4 子字串的運作 ======================================================
有時我們對子字串比較有興趣,有關子字串的運作方法如下表所示:

    表8-2 子字串的運作方法
方法             說明
endswith(s1)    若字串的尾端是 s1 子字串時,則回傳True
startswith(s1)  若字串的開頭是 s1 子字串時,則回傳 True
find(s1)        找尋字串中出現 sl 子字串的最小索引值,並加以回傳
rfind(sl)       找尋字串中出現 s1 子字串的最大索引值,並加以回傳
count(s1)       計算字串中出現 s1 子字串的個數。

請看以下所執行的範例:
'''
s8 = '請看以下所執行的範例'
s8.endswith('範例')
True

s8.startswith('li')
True

s8.find('d')
#3

s8.find('B')
#-1

s10 = 'abcdeabcde'
s10.find('e')
#9

s10.count('e')
#2

'''8-5 轉換字串 ================================================
也提供了一些用來轉換字串的方法,如下表所示:

    8-3 轉換字串的方法
方法                 說明
capitalize()        將字串中第一個字元轉換為大寫,其餘字元轉換為小寫後加 以回傳
lower()             將字串中的所有字元轉換為小寫後加以回傳
upper()             將字串中的所有字元轉換為大寫後加以回傳
title()             將字串中每一單字的第一個字元轉換為大寫,其餘字元轉換為小寫後加以回傳
swapcase()          將字串中大寫字元轉換為小寫字元,將小寫字元轉換為大寫字元後加以回傳
replace(old, new)   將 old 字串以 new字串取代之

請看以下所執行的範例:
'''
s11 = 'welcome to Taipei'
s11

s11.capitalize()
'Welcome to taipei'

s11.lower()
'welcome to taipei'

s11.upper()
'WELCOME TO TAIPEI'

s11.swapcase()
'WELCOME TO tAIPEI'

s11.title()
'Welcome To Taipei'


s11.replace('Taipei', 'Tainan')
'welcome to Tainan'

'''8-6 如何從字串中去掉頭尾空白 =======================================
有下列幾種方法可以將字串中的頭尾空白去掉,如表8-4 所示:
表8-4 從字串中去掉頭尾空白的方法
方法      說明
lstrip() 刪除字串左側的空白後加以回傳。
rstrip() 刪除字串右側的空白後加以回傳。
strip()  刪除字串兩側的空白後加以回傳。

請看以下所執行的範例:
'''
s12 = ' Learning Python now! '
s12 
' Learning Python now! '

s12.lstrip()
'Learning Python now! '

s12
'Learning Python now!'

s12.rstrip()
' Learning Python now!'

s12.strip()
'Learning Python now!'

s12
' Learning Python now! '

'''8-7 如何將字串加以格式化 =========================================
將字串加以格式化的方法,如下表所示:

    表8-5 將字串加以格式化的方法
方法          說明
center(width) 在給予 width 的欄位寬下 向中靠齊,並加以回傳。
ljust(width)  在給予 width 的欄位寬下 向左靠齊,並加以回傳。
rjust(width)  在給予 width 的欄位寬下 向右靠齊,並加以回傳。

請看以下所執行的範例:
'''
s13 = 'Bright Tsai'
s13.center(20)
'    Brigjt Tsai     '

s13
'Bright Tsai'

s13.ljust(20)
'Bright Tsai         '

s13
'Bright Tsail '

s13.rjust(20)
'         Bright Tsai'

'''還有一個方法是 split 方法,將字串解析到串列中,如: ===================='''

s100 = 'Apple Orange Banana Kiwi'
s100
'Apple Orange Banana Kiwi'
lst = s100.split()
lst
['Apple', 'Orange', 'Banana', 'Kiwi']

s200 = '01-13-2018'
lst2 = s200.split('-')
lst2
['01', '13', '2018']

lst22 = s200.split()
lst22
# ['01-13-2018']

'''其中 lciest = s100.split()
表示將字串 s100 以空白為分隔字符,將字串s100 加以分割, 然後存放於串列 Ist
中。從輸出結果['Apple', 'Orange', 'Banana', 'Kiwi'] 可得知它是存放於串列中。
下一個敘述
lst2 = s200.split('-') 是以'-'(dash 字符)為分隔字符,
將字串s200 分割後存放於串列 lst2。  '''

'''綜合範例1: ====================================================
2. 設計說明:
(1) 請撰寫一程式,要求使用者輸入一字串,顯示該字串每個字元的 索引。
3. 輸入輸出:
(1) 輸入說明
一個字串 (2)輸出說明
字串每個字元的索引
(3) 範例輸入
Sandwich

範例輸出
Index of 'S': 0
Index of 'a': 1
Index of 'n': 2
Index of 'd': 3
Index of 'w': 4
Index of 'i': 5
Index of 'c': 6
Index of 'h': 7
'''
string = input('輸入一字串:')
for i in range(len(string)):
    print("Index of '%c': %d" % (string[i], i))

'''綜合範例2: ===================================================
2. 設計說明:
(1) 請撰寫一程式,要求使用者輸入一字串,
    顯示該字串每個字元的對應 ASCII碼及其總和。
3. 輸入輸出:
(1) 輸入說明
一個字串
(2)輸出說明
依序輸出字串中每個字元對應的 ASCII碼
每個字元 ASCII碼的總和 (3)範例輸入
Kingdom
範例輸出
ASCII code for 'K' is 75
ASCII code for 'i' is 105
ASCII code for 'n' is 110
ASCII code for 'g' is 103
ASCII code for 'd' is 100
ASCII code for 'o' is 111
ASCII code for 'm' is 109
713
'''
total = 0
string = input()
for i in range(0, len(string)):
    num = ord(string[i])
    print("ASCII code for '%s' is %d" % (string[i], num))
    total += num
print(total)

'''綜合範例3: ==================================================
2. 設計說明:
(1) 請撰寫程式,讓使用者輸入一個句子(至少有五個詞,以空白隔開),
    並輸出該句子倒數三個詞。
3. 輸入輸出:
(1) 輸入說明
一個句子(至少五個詞,以空白隔開)
(2) 輸出說明
該句子倒數三個詞 (3) 範例輸入
Many foreign students study in TAIWAN
範例輸出
study in TAIWAN
'''
s = input('使用者輸入一個句子(至少有五個詞,以空白隔開):')

s_list = s.split(' ')

print(' '.join(s_list[-3:]))

print(' '.join(s_list[-4:]))

'''綜合範例4: ====================================================
設計說明:
(1) 請撰寫一程式,讓使用者輸入一字串,
    分別將該字串轉換成全部大寫以及
     每個字的第一個字母大寫。
3. 輸入輸出:
(1) 輸入說明
一個字串
(2)輸出說明 全部大寫
每個字的第一個字母大寫 
(3) 範例輸入
learning python is funny
範例輸出
LEARNING PYTHON IS FUNNY
Learning Python Is Funny
'''
st = input('使用者輸入一字串:')

str1 = st.upper()
print('字串轉換成全部大寫:',str1)
str2 = st.title()
print('每個字的第一個字母大寫:', str2)

'''綜合範例5: ======================================================
(1) 請撰寫一程式,要求使用者輸入一個長度為 6 的字串,
    將此字串分別置於 10 個欄位的寬度的
    左邊、 中間 和 右邊,
    並顯示這三個結果,左右皆以直線|(Vertical bar)作為邊界。
    
3. 輸入輸出:
(1) 輸入說明
一個長度為6的字串
(2) 輸出說明
格式化輸出 (3) 範例輸入
python
範例輸出
python
|python    |
|  python  |
|    python|
'''
string = input('使用者輸入一個長度為 6 的字串:')
if len(string) == 6:
    print("|%-10s|" %(string))
    print("|%s|" % string.center(10))
    print("|%10s|" % (string))

'''綜合範例6: ======================================================
(1) 請撰寫一程式,讓使用者輸入一字串和一字元,
    並將此字串及字元作為參數傳遞給名為 compute()的函式,
    此函式將回傳並輸出該字串中指定字元 出現的次數,接著再輸出結果。
3.輸入輸出:
(1) 輸入說明
一個字串和一個字元
(2)輸出說明
字串中指定字元出現的次數
(3) 範例輸入
Our country is beautiful
u

範例輸出
u
u occurs 4 time(s)
'''
def compute(sentence, w):
    return sentence.count(w)

sentence = input('使用者輸入一字串:')
word = input('使用者輸入一字元:')

print(word, "occurs", compute(sentence, word), "time(s)")

'''綜合範例7: ====================================================
(1) 請撰寫一程式,要求使用者輸入一字串,該字串為 五 個數字,以空白隔開。
    請將此五個數字 加總(Total)並計算 平均(Average)。
3. 輸入輸出:
(1) 輸入說明
一個字串(五個數字,以空白隔開)
(2) 輸出說明
總和
平均
(3) 範例輸入
-2 34 18 29 -56
範例輸出
Total = 23
Average = 4.6
'''
s = input('使用者輸入一字串,該字串為 五 個數字,以空白隔開:')

slist = [int(x) for x in s.split(' ')]

print("Total =", sum(slist))
print("Average =", sum(slist)/len(slist))

'''綜合範例8: ====================================================
設計說明:
(1)請撰寫一程式,提示使用者輸入一個社會安全碼 SSN,格式為 ddd-dd-dddd ,
   d表示數字。
   若格式完全符合(正確的SSN)則顯示(Valid SSN),
   否則 顯示(Invalid SSN)。
3.輸入輸出:
(1) 輸入說明
一個字串(格式為 ddd-dd - dddd,d表示數字)
(2) 輸出說明
判斷是否符合 SSN 格式

(3) 範例輸入

323-48-4977
範例輸出
Valid SSN

(4) 範例輸入
837-a3-3000
範例輸出
Invalid SSN
'''
s = input('輸入一個社會安全碼 SSN:')
isSSN = (len(s) == 11)
if isSSN:
    for i in range(len(s)):
        if i == 3 or i == 6:
            if s[i] != '-':
                isSSN = False
                break
        elif not s[i].isdigit():
            isSSN = False
            break

if isSSN:
    print(s, 'is a Valid SSN')
else:
    print(s, 'is an Invalid SSN')

'''綜合範例9: ==================================================
設計說明:
(1)請撰寫一程式,要求使用者輸入一個密碼(字串),
   檢查此密碼是否符合規則。
   密碼規則如下:
   a.必須至少八個字元。 
   b. 只包含英文字母和數字。 
   c. 至少要有一個大寫英文字母。
   
若符合上述三項規則,程式將顯示檢查結果為(Valid password),
否則 顯示(Invalid password)。

3. 輸入輸出:
(1) 輸入說明
一個字串
(2) 輸出說明
判斷是否符合密碼規則
(3) 範例輸入
39Gfjkd98
範例輸出
Valid password
'''

pw = input('使用者輸入一個密碼:')
validPw = True
if len(pw) <= 7 or pw.isalpha() or pw.isdigit() or pw.islower():
    validPw = False
else:
    for i in range(0, len(pw)):
        if not pw[i].isalpha() and not pw[i].isdigit():
            validPw = False
            break

if validPw:
    print("Valid password")
else:
    print("Invalid password")

'''綜合範例10: ========================================================
設計說明:
(1)請撰寫一程式,首先要求使用者輸入正整數 k(1 <= k <= 100),
   代表有 k 筆測試資料。
   每一筆測試資料是一串數字,每個數字之間以空白區隔,
   請找出此串列數字中最大值和最小值之間的差。
   
* 提示:差值輸出到小數點後第二位。
3. 輸入輸出:
(1) 輸入說明
  先輸入測試資料的筆數,
  再輸入每一筆測試資料(一串數字,每個數字之間以空白區隔)
  
(2) 輸出說明
每個串列數字中,最大值和最小值之間的差
輸出：
2
94 52 9 3 14 77 46 91.00
-2 0 1000 34 -14 4 89 50
1014.00
'''
k = eval(input('有幾筆測試資料?'))
for i in range(k):
    str_num = input('每一筆測試資料是一串數字:')
    str_num_list = str_num.split(' ')
    str_num_list = [eval(x) for x in str_num_list]
    print("%.2f" % (max(str_num_list) - min(str_num_list)))

'''綜合範例11: ================================================
撰寫一程式,以一不定迴圈要求使用者輸入字串,
檢視若字串是以 B 字元開頭, 字串加入lst 串列中,最後將其印出。
當使用者輸入的 end 時將結束輸入的
就撰寫一程式, 則將此字串加入 動作。

1. 輸入輸出:
(1) 範例輸入
Block
Apple
Banana
Cathy
Boy
end

(2) 範例輸出
[ 'Block', 'Banana', 'Boy']
'''
lst = []
while True:
    str = input('輸入字串:')
    if str != 'end':
        if str.startswith('B'):
            lst.append(str)
    else:
        break
print(lst)

'''綜合範例12: ======================================================
試撰寫一程式,以一不定迴圈要求使用者輸入字串,將輸入的字串以空白為分隔字元,
並儲存於ist 串列中,最後將其印出。

1. 輸入與輸出樣本:
I am a teacher
['I', 'am', 'a', 'teacher']
He is a student
['He', 'is', 'a', 'student']
Hello, world
['Hello,', 'world']
end
'''
lst = []
while True:
    str = input('輸入字串:')
    if str != 'end':
        lst = str.split()
        print(lst)
    else:
        break

'''綜合範例13: =================================================
撰寫一程式,隨機產生10個介於 65~90 的亂數,
然後將其轉換為一對應於英文
就撰寫一程式, 字母的字串。
1. 輸入輸出1:
(1) 範例輸入
無
(2) 範例輸出
XGGCUDCLCZ
2. 輸入輸出2:
(1) 範例輸入
無
(2) 範例輸出
MHQWXUGPEY
'''
import random
str = ''
for i in range(1,11):
    randNum = random.randint(65, 90)
    str += (chr(randNum))
print(str)

'''綜合範例14: =================================================
   試撰寫一程式,輸入 九 個字串置放於一名為 lst 的字串,
   其長度不超過10個字元。 
   接下來,每一列印出三個字串, 並且向中靠齊。
* 提示:每個字串輸出欄位寬為15。
1. 輸入輸出:
(1) 範例輸入
apple
orange
kiwi
banana
grape
pineapple
guava
cherry
blueberry
(2) 範例輸出
|     apple     ||    orange     ||     kiwi      |
|    banana     ||     grape     ||   pineapple   |
|     guava     ||    cherry     ||   blueberry   |
'''
lst = []
for i in range(1, 10):
    str = input()
    lst.append(str)
for k in range(1, 10):
    if k % 3 != 0:
        print('|'+lst[k-1].center(15) + '|', end = '')
    else:
        print('|'+lst[k-1].center(15) + '|')

'''綜合範例15: ======================================================
撰寫一程式,輸入一名為 str 的字串與欲尋找的字串,
將找到的字串以'Bright'字中印代之。
若沒有欲找尋的字串,則印出'is not found' 的訊息。
1. 輸入輸出1:  
(1) 範例輸入
I make an appointment with Linda
Linda

範例輸出
I make an appointment with Bright

12. 輸入輸出2:
(1) 範例輸入
I make an appointment with Linda 
Nancy
(2) 範例輸出
Nancy is not found
'''
str = input('輸入一名為 str 的字串:')
fstr = input('欲尋找的字串:')
if str.find(fstr) != -1:
    endStr = str.replace(fstr, 'Bright')
    print('找到的字串%s以Bright字中印代之:%s'  %(fstr, endStr))
else:
    print(fstr + ' is not found')
