'''檔案與異常處理 =================================================
前面談到的輸入基本上是從鍵盤得到資料,而輸出則顯示於螢幕上,
此稱之為標準的輸入與輸出(standard input/output)。
標準的輸入與輸出有一缺點是,每次的執行資料皆要重新的輸入,
這對於輸入的資料若是一很大的檔案時,
則此方式會很費時又讓人很煩的一件事
此時我們可以藉助檔案的輸入與輸出(file input/output)。
此時的輸入與輸出的對象皆是檔案。
基本上,在檔案的運作上可以先寫入資料於某一檔案,之後再從此檔案讀取資料。

9-1 檔案的運作流程 有關檔案的運作流程如下==============================:
1、利用 open 函式開啟檔案名稱和其模式。
2、利用寫入的函式將資料寫入檔案,或是利用讀取的函式從檔案讀取資料。
3、利用 close 函式將檔案關閉。

接下來,我們將一一的介紹上述的函式,首先是利用open打開一檔案,其語法如下:
    
variable_name = open('file_name', 'mode')

其中 variable name 表示使用自訂的變數名稱, 
file name 是使用者自訂檔案的名稱,
而 mode 是檔案運作的屬性,如表 9-1 所示:
    
表9-1 文字檔模式
運作屬性   說明
  w       寫入
  r       讀取
  a       附加
  
以上的檔案屬性是文字檔,若是二進位檔案,則要在屬性後面多加上b,如下表所示:
表9-2 二進位檔模式
運作屬性       說明
  wb          寫入
  rb          讀取
  ab          附加

因此,以下敘述
outfile = open('names.dat', 'w')

表示打開一名為 names.dat 的檔案,其運作的屬性是寫入,
並將其檔案指標指定给 outfile。
從此 outfile 便代表 names.dat 檔案。

上述敘述也可以换寫為 with open('names.dat','w') as outfile:
    
若使用模式a,則表示附加到檔案的後面,
    而模式r表示從檔案讀取資料。
一般在開啟檔案做為寫入模式,必需將其關閉,
之後再將其開啟做為讀取檔案資料 使用。
此處提供一個較方便的方式,
就是在模式後加上 + ,就可表示此檔案可做寫入和讀取的功能。請看後面的綜合範例。

19-2 檔案資料的寫入與讀取 ===========================================
接下來我們就要使用文字檔的存取函式來運作,其相關的函式如表9-3 所示:

    表9-3 文字檔案的存取函式
文字檔案的存取函式          說明
  write                   寫入
  read()                  讀取檔案所有内容
  readline()              從檔案中讀取一行
  readlines()             讀取檔案所有内容
  read(n)                 從檔案中讀取 n 個字元

接著我們以範例程式來說明上述的函式。
首先,利用open 函式打開一檔案,接著 write 將資料寫入於檔案。
請看以下範例程式:
'''
def main():
    outfile = open('fruits.dat', 'w')
    #write data to the file
    outfile.write('Banana\n')
    outfile.write('Grape\n')
    outfile.write('Orange')
    outfile.close()
main()

# F:/pythonData
def main():
    outfile = open('F:/pythonData/fruits.dat', 'w')
    #write data to the file
    outfile.write('Banana\n')
    outfile.write('Grape\n')
    outfile.write('Orange')
    outfile.close()
main()

# E:/Python語言入門及TQC證照班 - 姜自強 副教授/Python 3 x 程式語言特訓教材
def main():
    outfile = open('E:/Python語言入門及TQC證照班 - 姜自強 副教授/Python 3 x 程式語言特訓教材/fruits.dat', 'w')
    #write data to the file
    outfile.write('Banana\n')
    outfile.write('Grape\n')
    outfile.write('Orange')
    outfile.close()
main()

'''上述程式打開了一個名為 fruits.dat 的檔案,做為寫入的模式。
之後利用 write 函式 將三筆資料寫入檔案中。
當你要關閉檔案時,就可以使用close 函式切斷檔案指標與檔案的關係將檔案關閉。
此時 fruits.dat 應該有三筆資料。
注意,有些資料有轉義字元 \n。

要注意的是,當打開一已存在的檔案時,檔案舊有的資料將被洗掉,所以要特別小心。
'''
# F:/pythonData
def main():
    outfile = open('F:/pythonData/fruits.dat', 'w')
    #write data to the file
    outfile.write('Banana2\n')
    outfile.write('Grape2\n')
    outfile.write('Orange2')
    outfile.close()
main()

#Banana2
#Grape2
#Orange2
'''
也可以將資料附加於檔案的後面,這不會有洗掉原有内容的風險 ==================。
如下所示: '''
def main():
    outfile = open('fruits.dat', 'a')
    #append data to the file
    outfile.write('Kiwi')
    outfile.close()
main()

#Banana
#Grape
#OrangeKiwi

def main():
    outfile = open('fruits.dat', 'a')
    #append data to the file
    outfile.write('\nKiwi')
    outfile.close()
main()

#Banana
#Grape
#OrangeKiwi
#Kiwi


'''此時再附加 Kiwi 的資料於檔案的後面,所以現在 fruits.dat 應該有四筆資料。
由於 將資料寫入檔案,我們並不知道它是否成功的將資料寫入於檔案。

所以,接下來都 會使用讀取的函式來讀取檔案的資料,以驗證是否成功寫入資料。
當要從檔案讀取資料時,
則利用 readline 函式,每次從檔案讀取一行,
而 readlines 函式,則讀取所有檔案的内容。
若使用 read()函式,則和 readlines 函式功能相同,
而read(n),則表示從檔案讀取 n個字元。
請看以下範例程式: '''
def main():
    infile = open('fruits.dat', 'r')
    #read data from the file
    #using readline()
    print('\nUsing readline()')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline ()
    
    print (repr(line1))
    print(repr(line2))
    print (repr(line3))
    
    print((line1))
    print((line2))
    print((line3))
    infile.close()
main()
'''輸出結果

Using readline()
'Banana\n'
'Grape\n'
'OrangeKiwi'
Banana

Grape

OrangeKiwi

程式中的 repr 函式，表示若字串的資料有轉義字元，如\n等，不會經過轉義的動作就直接印出。
因此：
repr 函式
Return the canonical string representation of the object.
返回對象的規範字符串表示形式。
'''
#print(repr(line1))
#print(repr(line2))
#print(repr(line3))

'''輸出結果

Using readline()
'Banana\n'
'Grape\n'

若是將repr去掉，如下一範例程式：
'''
#print((line1))
#print((line2))
#print((line3))
'''
輸出結果
Banana

Grape

OrangeKiwi

以下程式將以read 和 readlines 函式加以讀取,請參閱以下程式 ================:
'''
def main():
    infile = open('fruits.dat', 'r')
    #using read()
    line1 = infile.read()
    print('Using read()')
    print(repr(line1))
    print((line1))
    infile.close()
    
    #using readlines ()
    infile = open('fruits.dat', 'r')
    print('\nUsing readlins()')
    line1 = infile.readlines ()
    print((line1))
    infile.close()
main()
'''
輸出結果
Using read()
'Banana\nGrape\nOrangeKiwi'
Banana
Grape
OrangeKiwi

Using readlins()
['Banana\n', 'Grape\n', 'OrangeKiwi']

以下程式將以read(n)函式從檔案中讀取n個字元，請參閱以下程式================：
'''
def main():
    infile = open('fruits.dat', 'r')
    #using read(n)
    print('Using read(3)')
    line1 = infile.read(3)
    print (repr(line1))

    print('Using read(8)')
    line2 = infile.read(8)
    print (repr(line2))
    
    infile.close()
main()
'''
輸出結果
Using read(3)
'Ban'
Using read(8)
'ana\nGrap'

要印出檔案内的所有内容,也可以利用下列迴圈敘述加以印出,如下所示 ============:
'''
def main():
    infile = open('fruits.dat', 'r')
    line = infile.readline()
    while line != '':
        print(line)
        line = infile.readline()
    infile.close()
main()
'''
輸出結果
Banana

Grape

OrangeKiwi

當程式讀到檔尾時就會結束。亦即讀到的行資料是空的。
一般我們習慣先打開一檔案做寫入的運作後,將此檔案關閉,
之後再打開此檔案做為讀取的運作,結束後再將檔案關閉。
如以下程式所示:
'''
def main():
    outfile = open('cities.dat', 'w')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')
    
    outfile.close() #寫入的運作後 檔案關閉
    
    infile = open('cities.dat', 'r')
    data = infile.read()
    print(data)
    
    infile.close() #讀取的運作後 檔案關閉
main()
'''
輸出結果
Taipei
London
Coventry


開檔、關檔、開檔再關檔這是很花時間的動作,
是否只要開一檔案就可以處理 寫入和 讀取的動作 ==============================，
有的，只要在檔案的模式中加入 + 的符號即可。
如下敘述所示:
'''
def main():
    outfile = open('cities.dat', 'w+')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')

    outfile.seek(0, 0)
    data = outfile.read()
    print(data)
main()
'''
輸出結果
Taipei
London
Coventry

以上程式打開了一cities.dat 檔案,其模式為 W+,
表示此檔案可以處理為 寫入和讀取 的動作。

但要注意的是, 結束寫入檔案的動作後, 由於檔案指標是指向檔尾,

所以必需利用 seek(0, 0)將檔案的指標移到檔頭 =======================。
有關 seek 函式的語法如下:
'''
#seek(offset, where)
'''其中 offset 是位移多少 bytes,
 where 表示從哪裏位移,0表示檔頭, 1表示目前的位置, 2表示檔尾。
所以 seek(0, 0)
表示從擋頭位移 0個byte。
'''
def main():
    outfile = open('cities.dat', 'w+')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')

    #outfile.seek(0, 0)
    data = outfile.read()
    print(data)
main()

# 讀不到資料????

'''
9-3 二進位檔案的寫入與讀取 =======================================
以上討論檔案的屬性是文字檔,在Python 也提供二進位檔案的存取屬性。
若檔案 儲存的資料大都是數值的話,以二進位檔案來處理存取是較有效率的。
在二進位檔案的存取上必需引入 pickle 模組,
再利用 dump 函式來將資料寫入於檔案,
並利用 load 函式從檔案讀取資料。
如下表所示:
表9-4 二進位檔案的存取函式
二進位檔案的存取函式      說明
dump                    寫入
load                    讀取
'''
import pickle
def main():
    outbinfile = open('binaryFile.dat','wb')
    pickle.dump(123, outbinfile)
    pickle.dump (77.7, outbinfile)
    pickle.dump('Python is fun', outbinfile)
    pickle.dump ([11, 22, 33], outbinfile)
    outbinfile.close()
    
    inbinfile = open('binaryFile.dat', 'rb')
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    inbinfile.close()
main()
'''
輸出結果
123
77.7
Python is fun
[11, 22, 33]

以下範例程式是打開一個二進位的檔案,由使用者輸入資料,當輸入0時,
才結束資料寫入檔案和讀取資料的動作。

由於是二進位檔案,所以利用dump 函式將資料寫入於檔案。
接下來利用 load 函式從檔案讀取資料,當讀到檔尾時,
系統會丟出 “EOFError 的訊息,
此時在 except EOFError 下將 end_of_file 設定為True。
如下所示:
'''
import pickle
def main():
    outfile = open('scores.dat', 'wb')
    data = eval(input('Enter an integer, 0 to stop: '))
    while data != 0:
        pickle.dump (data, outfile)
        data = eval(input('Enter an integer, 0 to stop: '))
    outfile.close()

    infile = open('scores.dat', 'rb')
    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(infile), end = ' ')
        except EOFError:
            end_of_file = True
    infile.close()
    print("\nAll data are read")
main()
'''
輸出結果
Enter an integer, 0 to stop: 90
Enter an integer, 0 to stop: 12
Enter an integer, 0 to stop: 34
Enter an integer, 0 to stop: 55
Enter an integer, 0 to stop: 67
Enter an integer, 0 to stop: 0
90 12 34 55 67
All data are read

9-4異常處理 ==========================================================
應用程式最怕當機,這會給使用者非常驚恐,導致程式是不友善的,
所以優良的程式設計師會有異常處理機制。
例如兩數相除，分母不可為0，則不處理將會產生錯誤而結束程式執行，
還有若開啟一寫入的檔案，
但該檔案已設為唯讀的屬性時，也將產生錯誤的訊息。

以上這些需要有異常處理的機制。
Python的異常處理機制是利用以下的方式處理之,如下所示

try: 敘述主體
except <異常型態>
處理方式
上一範例中的片段程式
'''
try:
    print(pickle.load(infile), end = '')
except EOFError:
    end_of_file = True
    
'''表示敘述主體是當讀取檔案資料到達橙尾時,將會有 EOFError 的異常情形發生,
這時的處理方式就是將 end of file 設為 True。
當程式可能有多種異常情形時,則以下列的異常處理機制來執行,如下所示:

try:
    敘述主體
except <異常型態 1>
    處理方式
except <異常型態N>
    處理方式
except:
    上述都沒有匹配時的處理方式
else:
    若沒有異常時所執行的敘述
finally:
    最後一定會處理的方式

'''
def main():
    try:
        n1, n2 = eval(input('Enter two numbers, separated by a comma：'))
        ans = n1 / n2
        print('%d/%d = %d'%(n1, n2, ans))
    except ZeroDivisionError:
        print('Division by zero!')
    except SyntaxError:
        print('A comma may be missing in the input')
    except:
        print('Something wrong in the input')
    else:
        print('No exception')
    finally:
        print('The finally clause is executed')

main()
'''
輸出結果
一、
Enter two numbers, separated by a comma：10,0
Division by zero!
The finally clause is executed

二、
Enter two numbers, separated by a comma：12 3
A comma may be missing in the input
The finally clause is executed

三、
Enter two numbers, separated by a comma：a,u
Something wrong in the input
The finally clause is executed

四、
Enter two numbers, separated by a comma：12, 3
12/3 = 4
No exception
The finally clause is executed

程式中共有三個異常處理的機制,一為當分母為0會產生ZeroDivisionError;
二 為輸入兩個資料時,中間沒有逗號時會產生 SyntaxError;三是其它的問題時曾生
生的錯誤訊息。
程式中的 finally子句,到最後一定會執行的。

'''
# Python Exceptions: An Introduction
# https://realpython.com/python-exceptions/
# Python 異常處理
# https://www.runoob.com/python/python-exceptions.html

'''
綜合範例1: =============================================================
設計說明:
(1) 請撰寫一程式,將使用者輸入的五筆資料寫入到 write.txt (若不存在,則讓程式建立它),
每一筆資料為一行,包含學生名字和期末總分,以空白隔開。檔案寫入完成後要關閉。
3. 輸入輸出:
(1) 輸入說明
五筆資料(每一筆資料為一行,包含學生名字和分數,以空白隔開)
(2) 輸出說明
| 將輸入的五筆資料寫入檔案中,不另外輸出於頁面
(3) 範例輸入
Leon 87
Ben 90
Sam 77
Karen 92
Kelena 92

範例輸出
在write.txt寫入一模一樣的字串
'''
file = open("write.txt", "w")

for i in range(5):
    data = input('輸入學生名字和分數,以空白隔開:')
    file.write(data + '\n')
file.close()

#Leon 87
#Ben 90
#Sam 77
#Karen 92
#Kelena 92

'''綜合範例2: ========================================================
2. 設計說明:
(1) 請撰寫一程式,讀取 read.txt 的內容(内容為數字,以空白分隔)
    並將這些數字加總後输出。檔案讀取完成後要關閉。
3. 輸入輸出:
(1) 輸入說明
讀取 read.txt 的内容(内容為數字,以空白分隔)
(2)輸出說明
總和
(3) 範例輸入
範例輸出
660
'''
file = open("read.txt", "w")
file.write("11 22 33 22 33 44 33 44 55 44 55 66 55 66 77" + '\n')
file.close()

f = open("read.txt", 'r')
data = f.read()   # data type?
print(data)
# 11 22 33 22 33 44 33 44 55 44 55 66 55 66 77
type(data)
# str
f.close()

num = data.split(' ')  # num type?
print(num)
type(num)
#['11', '22', '33', '22', '33', '44', '33', '44', '55', '44', '55', '66', '55', '66', '77\n']
# list

total = 0
for i in range(0, len(num)):
    total += eval(num[i])
print(total)
# 660

'''綜合範例3: =====================================================
2. 設計說明:
(1) 請撰寫一程式,要求使用者輸入五個人的名字並加入到 data.txt 的尾端。
    之後再顯示此檔案的内容。
3. 輸入輸出:
(1)輸入說明
輸入五個人的名字
(2) 輸出說明
讀取檔案,輸出此檔案内容
(3) 範例輸入
Daisy
Kelvin
Tom
Joyce
Sarah
範例輸出
Append completed!
Content of "data.txt":

Daisy
Kelvin
Tom
Joyce
Sarah
'''
file = open("data.txt", "w")
file.write("Ben" + '\n')
file.write("Cathy" + '\n')
file.write("Tony" + '\n')
file.close()

file = open("data.txt", "a+")

for i in range(5):
    file.write('\n' + input())
print("Append completed!")
print('Content of "data.txt":')

print(file.read()) # why? 沒有任何資料

file.seek(0, 0)
print(file.read())

file.close()

'''綜合合範例4: =====================================================
2. 設計說明:
(1) 請撰寫一程式,讀取 read.txt(每一列的格式為 名字 和 身高、 體重,以空白分隔)
    並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者 。
* 提示:輸出浮點數到小數點後第二位。
3. 輸入輸出:
(1) 輸入說明
讀取 read.txt (每一列的格式為名字和身高、體重,以空白分隔)
(2) 輸出說明
輸出檔案中的内容
平均身高
平均體重
最高者
最重者

範例輸入
在read.txt手動輸入
Ben 175 65
Cathy 155 55
Tony 172 75

範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg
'''

'''
Python 的 with 語法使用教學：Context Manager 資源管理器
https://blog.gtwang.org/programming/python-with-context-manager-tutorial/
# 以 with 開啟檔案
with open(filename) as f:
  # ...
這裡在使用 with 開啟檔案時，會將開啟的檔案一樣放在 f 變數中，但是這個 f 只有在這個 with 的範圍內可以使用，而離開這個範圍時 f 就會自動被關閉，回收相關的資源。

'''
file = open("read.txt", "w")
file.write("Ben 175 65" + '\n')
file.write("Cathy 155 55" + '\n')
file.write("Tony 172 75" + '\n')
file.close()

data = []
with open("read.txt","r") as file:  #pp 9-3
    for line in file:
        print(line)
        tmp = line.strip ('\n').split(' ')
        tmp = [tmp[0], eval(tmp[1]), eval(tmp[2])]
        data.append(tmp)
data
'''
[['Ben', 175, 65], ['Cathy', 155, 55], ['Tony', 172, 75]]
'''
line
# 'Tony 172 75\n'
line.strip ('\n')
# 'Tony 172 75'
line.strip ('\n').split(' ')
# ['Tony', '172', '75']


name = [data[x] [0] for x in range(len (data))]
height = [data[x] [1] for x in range (len (data))]
weight = [data[x] [2] for x in range(len(data))]

name
# ['Ben', 'Cathy', 'Tony']
height
# [175, 155, 172]
weight
# [65, 55, 75]

print("Average height: %.2f" % (sum(height)/len(height)))
print("Average weight: %.2f" % (sum (weight)/len(weight)))
max_h = max(height)
max_h
# 175
max_w = max(weight)
max_w
# 75

print("The tallest is %s with %.2fcm" % (name[height.index(max_h)], max_h))
print("The heaviest is %s with %.2fkg" % (name[weight.index(max_w)], max_w))

height.index(max_h)
# 0
name[height.index(max_h)]
# 'Ben'

'''綜合範例5: ============================================================
2. 設計說明:
(1) 請撰寫一程式,要求使用者輸入檔案名稱 data.txt 和一字串 s,
    顯示該檔案的内容。
    接著刪除檔案中的字串 s ,顯示刪除後的檔案内容並存檔。
3. 輸入輸出:
(1) 輸入說明
輸入data.txt 及一個字串
(2)輸出說明
先輸出原檔案內容,再輸入删除指定字串後的新檔案内容
(3) 範例輸入
data.txt
Tomato

範例輸出
=== Before the deletion
Apple Kiwi Banana
Tomato Pear Durian
=== After the deletion
Apple Kiwi Banana
 Pear Durian
'''
file = open("data.txt", "w")
file.write("Apple Kiwi Banana" + '\n')
file.write("Tomato Pear Durian" + '\n')
file.close()

f_name = input('輸入檔案名稱:')
string = input('輸入刪除檔案中的字串名稱:')

file = open(f_name, "r+")
data = file.read()
data
# 'Apple Kiwi Banana\nTomato Pear Durian\n'

print("=== Before the deletion")
print(data)
# Apple Kiwi Banana
# Tomato Pear Durian

print("=== After the deletion")
data = data.replace(string,'')
print(data)
'''
Apple Kiwi Banana
 Pear Durian
'''

file.seek(0)
file.truncate()  # # 截断剩下的字符串
file.write(data)
file.close()

'''
Python file.truncate()方法
http://tw.gitbook.net/python/file_truncate.html
truncate()方法截斷該文件的大小。如果可選的尺寸參數存在，該文件被截斷(最多)的大小。
'''

'''綜合範例6: ======================================================
2. 設計說明:
(1) 請撰寫一程式,要求使用者輸入檔名 data.txt、字串sl 和字串s2。
    程式將檔案中的字串sl以s2 取代之。
3. 輸入輸出:
(1) 輸入說明
輸入data.txt 及兩個字串(分別為S1、S2,字串 s1 被 s2 取代)
(2) 輸出說明
輸出檔案中的内容 輸出取代指定字串後的檔案內容
(3)範例輸入
data.txt
pen
sneakers
範例輸出
=== Before the replacement
watch shoes skirt
pen trunks pants
=== After the replacement
watch shoes skirt
sneakers trunks pants
'''
file = open("data.txt", "w")
file.write("watch shoes skirt" + '\n')
file.write("pen trunks pants" + '\n')
file.close()

f_name = input('輸入檔案名稱:')
str_old = input('輸入字串 s1, 字串 s1 被 s2 取代:')
str_new = input('輸入字串 s2, 字串 s1 被 s2 取代:')

infile = open(f_name, 'r')
data = infile.read()
data
# 'watch shoes skirt\npen trunks pants\n'
print(data)
#watch shoes skirt
#pen trunks pants

print("=== Before the replacement")
print(data)
infile.close()

print("=== After the replacement")
new_data = data.replace(str_old, str_new)
print(new_data)

outfile = open(f_name, 'w')
outfile.write(new_data)
outfile.close()

'''綜合範例7: =================================================
2. 設計說明:
(1) 請撰寫一程式,要求使用者輸入檔名 read.txt,
    顯示該檔案的行數、單字數
    (簡單起見,單字以空白隔開即可,忽略其它標點符號)以及
    字元數(不含空白)。
3. 輸入輸出:
(1) 輸入說明
讀取 read.txt，並在檔案裡輸入文章
(2)輸出說明
行數
單字數
字元數(不含空白)
(3) 範例輸入
read.txt
範例輸出
6 line(s)
102 word(s)
614 character(s)
'''

f_name = input('輸入檔案名稱:')

c_line = c_word = c_char = 0

with open(f_name, 'r') as file:
    for line in file:
        c_line += 1

        word = line.strip('\n').split(' ')
        c_word += len(word)

        c_char += sum([len(x) for x in word])

print("%d line(s)" %c_line)
print("%d word(s)" % c_word)
print("%d character(s)" % c_char)

'''綜合範例8： ==================================================
2. 設計說明: ****************
(1) 請撰寫一程式,要求使用者輸入檔名 read.txt,
    以及檔案中某單字出現的次數,輸出符合次數的單字,
    並依單字的第一個字母大小排序(單字的判斷以空白隔開即可)。
3. 輸入輸出:
(1) 輸入說明
讀取 read.txt 的内容,以及檔案中出現單字的次數
(2)輸出說明
輸出符合次數的單字,並依單字的第一個字母大小排序
(3) 範例輸入
read.txt
3
範例輸出
Python
a
is
programming
'''
f_name = input('輸入檔案名稱:')
n = int(input('出現單字的次數:'))
word_dict = dict()

with open(f_name, 'r') as file:
    for line in file:
        word = line.strip('\n').split(' ')

        for x in word:
            if x in word_dict:
                word_dict[x] += 1
            else:
                word_dict[x] = 1

word_list = word_dict.items()
wordQTY = [x for(x,y) in word_list if y == n]
sortedword = sorted(wordQTY)

for x in sortedword:
    print(x)

'''綜合範例9: =========================================================
聯絡人資料
2. 設計說明:
(1) 請撰寫一程式,將使用者輸入的五個人的資料寫入data.dat 檔,
    每一個人的資料為姓名和電話號碼,以空白分隔。
    再將檔案加以讀取,並顯示檔案内容。
3. 輸入輸出:
(1) 輸入說明
五個人的姓名和電話號碼,以空白分隔
(2) 輸出說明
讀取及寫入檔案後,再輸出讀入的檔案名稱及內容
(3)範例輸入
Karen  123456789
Bonnie 235689147
Simon 987612345
Louis 675489321
Andy 019238475

範例輸出
The content of "data.dat":
Karen 123456789

Bonnie 235689147

Simon 987612345

Louis 675489321

Andy 019238475

file = open("data.txt", "w")
file.write("Karen  123456789" + '\n')
file.write("Bonnie 235689147" + '\n')
file.write("Simon 987612345" + '\n')
file.write("Louis 675489321" + '\n')
file.write("Andy 019238475" + '\n')
file.close()
'''

f_name = "data.dat"
file = open(f_name, "wb")
for i in range (5):
    inp = input('輸入的五個人的資料姓-名和電話號碼,以空白分隔:')
    b_inp = bytearray(inp + '\n', 'utf-8')
    file.write(b_inp)
file.close()

print('The content of "%s":' % f_name)
with open(f_name, "rb") as file:
    for line in file:
        print(line.decode('utf-8'))

'''綜合範例 10: =====================================================
學生基本資料
2.設計說明:
(1) 請撰寫一程式,要求使用者讀入read.dat(以UTF-8 編碼格式讀取),
    第一列為欄位名稱, 第二列之後是個人記錄。
    請輸出檔案內容並顯示男生人數和女生人數(根據"性別"欄位,0為女性、1為男性)。
3. 輸入輸出:
(1) 輸入說明
    讀取 read.dat
(2)輸出說明
    讀取檔案内容,並格式化輸出男生人數和女生人數
(3)範例輸入
在read.txt裡輸入
範例輸出
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文
Number of males: 3
Number of females: 2
'''
f_name = "read.dat"
c_male = c_female = 0

with open(f_name, "rb") as file:
    for line in file:
        row = line.decode('utf-8')
        print(row)
        row = row.strip('\n').split(' ')

        if row [2] == '1':
            c_male += 1
        elif row [2] == '0':
            c_female += 1

print("Number of males:", c_male)
print("Number of females:", c_female)

'''綜合範例 11: ====================================================
   試撰寫一程式,以不定數迴圈輸入學生姓名、微積分與會計成績。
當輸入學生姓名為 none 時,則結束翰入的動作。
並將上述輸入的資料寫入名為 students.dat 的檔案
1. 輸入輸出:
(1) 範例输入
Peter
90
89
Mary
88
79
John
80
95
Nancy
87
76
Lulu
67
99
none
10
10
(2) 範例輸出
寫入到students.dat
'''
outfile = open('students.dat', 'w')
#write data to the file
while True:
    name = input('輸入學生姓名:')
    calculus = input('輸入學生微積分成績:')
    accounting = input('輸入學生會計成績:')
    if name == 'none':
        break
    else:
        outfile.write(name)
        outfile.write(' ')
        outfile.write(calculus)
        outfile.write(' ')
        outfile.write(accounting)
        outfile.write(' ')
        outfile.write('\n')

outfile.close()

'''綜合範例 12: ===========================================================
試撰寫一程式,將綜合範例 11 所建立的 students.dat 檔案加以讀取之。
1. 輸入輸出:
(1) 範例輸入
無
(2) 範例輸出
Peter 90 89

Mary 88 79

John 80 95

Nancy 87 76

Lulu 67 99
'''
infile = open('students.dat','r')

info = infile.readline()
while info != '':
    print(info)
    info = infile.readline()

infile.close()

'''綜合範例 13: =======================================================
    撰寫一程式,將綜合範例 11 所建立的 students.dat 檔案加以讀取之,
並計算每位均分數。
假設微積分的比重是60%,而會計的比重是40%。學生的平均分數。

1. 輸入輸出:
(1) 範例輸入
無
(2) 範例輸出
|     Peter: 54.00|
|      Mary: 52.80|
|      John: 48.00|
|     Nancy: 52.20|
|      Lulu: 40.20|
'''
infile = open('students.dat', 'r')
info = infile.readline()
while info != '':
    lst = info.split(' ')
    calculus = eval(lst[1])
    accounting = eval(lst[2])
    average = calculus * 0.6 + accounting * 0
    print('|%10s: %.2f|'%(lst[0], average))
    info = infile.readline()
infile.close()

'''綜合範例 14: =========================================================
   試撰寫一程式,將綜合範例 11 所建立的 students.dat 檔案加以讀取之,
   看哪位學生 的微積分最高。
1. 輸入輸出:
(1) 範例輸入
無
(2) 範例輸出
#1 calculus score is
     Peter:  90.
'''
infile = open('students.dat', 'r')
max = -1
info = infile.readline()
while info != '':
    lst = info.split(' ')
    calculus = eval(lst[1])
    if calculus > max:
        max = calculus
        name = lst[0]
    info = infile.readline()

print('#1 calculus score is \n%10s: %3d. '%(name, max))
infile.close()

'''綜合範例 15: =============================================================
   程式,將綜合範例 11 所建立的 students.dat 檔案加以讀取之,
看哪位學生的會計最低。

 1. 輸入輸出:
(1) 範例輸入
無
(2) 範例輸出
The lowest accounting score is
     Nancy:  76.
'''
infile = open('students.dat', 'r')
min = 101
info = infile.readline()
while info != '':
    lst = info.split(' ')
    accounting = eval(lst[2])
    if accounting < min:
        min = accounting
        name = lst[0]
    info = infile.readline()
print('The lowest accounting score is\n%10s: %3d.'%(name, min))
infile.close()
