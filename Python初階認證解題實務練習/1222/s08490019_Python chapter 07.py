# In[1]
'''
字典內容如下:
dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
1).字典長度是多少?
2).修改’python’這個key對應的value值改成80
'''
dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
print('befor:',dic)
print('len:',len(dic))
dic['python']=80
print('after:',dic)

# In[2]
'''
小明的購物清單如下
牛奶:70
麵包:40
可樂:50
餅乾:30
1).請以字典型式保存以上的購物清單
2).可樂的金額輸入錯誤了，請改成49元，需透果程式碼進行修改
3).輸出如以下的顯示:
您總共購買了4件商品，共計189.000000元
'''
dic={
     '牛奶':70,
     '麵包':40,
     '可樂':50,
     '餅乾':30,
     }

dic['可樂']=49
print(dic)
dic_sum=sum(dic.values())
print('您總共購買了4件商品，共計%.6f元'%dic_sum)
# In[3]
'''
請生成100個帳號與密碼，其初始密碼設定’000000’
帳號由6位數組成，前3位數為610，後面的號碼依次為001,002,003…100
需使用字典保存帳號與密碼
部分輸出如下:
{610001: '000000', 610002: '000000', 610003: '000000',
 610004: '000000', 610005: '000000', 610006: '000000',
 610007: '000000', 610008: '000000', 610009: '000000',
 610010: '000000', 610011: '000000', 610012: '000000',
 610013: '000000', 610014: '000000', 610015: '000000'
 }
'''
dic={}
for i in range(1,101):
    a=610000+i
    dic.setdefault(a,'000000')  #新增
print(dic)

# In[4]
'''
現有一個列表li = [1,2,3,'a',4,'c'],有一個字典(此字典是動態生成的，
你並不知道他裡面有多少鍵值，所以用dic={}模擬字典；現在需要完成這樣的操作：
如果該字典沒有"k1"這個鍵，那就創建這個"k1"鍵和對應的值(該鍵對應的值為空列表)，
並將列表li中的索引位為奇數對應的元素，添加到
"k1"這個鍵對應的空列表中。如果該字典中有"k1"這個鍵，且k1對應的value是列表類型。
那就將該列表li中的索引位為奇數對應的元素，添加到"k1"，這個鍵對應的值中。
'''
def fun1(dic):
    li = [1,2,3,'a','b','4','c']
    k1 = 'k1'
    myeven = []
    myodd = []
    for i in range(len(li)):
        if i % 2 == 0:
            myeven.append(li[i])
            continue
        else:
            myodd.append(li[i])
    if k1 not in dic.keys():
        dic[k1] = []
        for args in myodd:
            dic[k1].append(args)
    else:
        for args in myeven:
            dic[k1].append(args)
    print('first:',dic)
dic1 = {1:'a',2:'b','k1':['c']}
fun1(dic1)
  
def fun(dic):
    li = [1, 2, 3,'a','b', 4,'c']
    even = []
    odd = []
    for i in range(len(li)):
        if i % 2 == 0:
            even.append(li[i])
        else:
            odd.append(li[i])
    if 'k1' not in dic.keys():
        dic['k1'] = []
        dic['k1'].extend(odd)
    else:
        dic['k1'].extend(even)
    print('second:',dic)
dic1 = {'k1': [2, 6]}
dic2 = {'k2':9}
fun(dic2)
 
 

 


# In[5]
'''
將列表中的‘tt’變成大寫
list = [[‘k‘, [‘qwe‘, 20, {‘k1‘: [‘tt‘, 3, ‘1‘]}, 89], ‘ab‘]]
'''

lis= [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
lis[0][1][2]['k1'][0] = lis[0][1][2]['k1'][0].upper()
print(lis)
 


# In[6]
'''
請將以下字典反轉其key值與value值，限一行程式碼解決此問題
fruits = {“西瓜”:34,”木瓜”:63,”文旦”:81,”蘋果”:102,”鳳梨”:60,”橘子”:73}
輸出如下:
原始數據:{'西瓜': 34, '木瓜': 63, '文旦': 81, '蘋果': 102, '鳳梨': 60, '橘子': 73}
反轉key value:{34: '西瓜', 63: '木瓜', 81: '文旦', 102: '蘋果', 60: '鳳梨', 73: '橘子'}
'''
fruits = {'西瓜':34,'木瓜':63,'文旦':81,'蘋果':102,'鳳梨':60,'橘子':73}
print(fruits)

fruits = {v: k for k, v in fruits.items()}
print(fruits)

# In[7]
'''
數字重複統計:
1). 隨機生成1000個整數;
2). 數字的範圍[20, 100],
3). 升序輸出所有不同的數字及其每個數字重複的次數
4). 需使用字典
'''
import random

b={}
for i in range(20,101):
    b.setdefault(i,0)

for i in range(1000):
    a=random.randrange(20,101)
    b[a]+=1
    
for i in b.keys():
    print(i,'有:',b[i])
    

# In[8]
'''
將同樣的value的key集合在list裡
m1={'a':1,'b':2,'c':1}
輸出如下:
{1:['a','c'],2:['b']}
'''
from collections import defaultdict

m1={'a':1,'b':2,'c':1}
m1_inverted = defaultdict(list)
{m1_inverted[v].append(k) for k, v in m1.items()}
result = dict(m1_inverted)
print(result)

# In[9]
'''
重複的單詞: 此處認為單詞之間以空格為分隔符號
1). 用戶輸入一句英文句子
2). 打印出每個單詞及其重複的次數
3). 需使用字典
'''
lan=input("input:")
lan_s=lan.split(' ')
word={}
for i in lan_s:
    if i==',' or i=='.':
        continue
    count=lan_s.count(i)
    word[i]=count
print(word)

# In[10]
'''
現有一個字典dict1 保存的是小寫字母a-z對應的ASCII碼
dict1 = {'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 96, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 117, 't': 116, 'w': 119, 'v': 118, 'y': 121, 'x': 120, 'z': 122}
1). 將該字典按照ASCII碼的值排序
2). 有一個字母的ASCII錯了，修改為正確的值，並重新排序
3). 需使用字典
'''
dict1 = {'a': 97,  'c': 99, 'b': 98, 'e': 101,
         'd': 100, 'g': 103, 'f': 102, 'i': 105,
         'h': 104, 'k': 107, 'j': 106, 'm': 109,
         'l': 108, 'o': 96, 'n': 110, 'q': 113,
         'p': 112, 's': 115, 'r': 114, 'u': 117,
         't': 116, 'w': 119, 'v': 118, 'y': 121,
         'x': 120, 'z': 122}

dict1['o']=111
print(sorted(dict1.items(),key=lambda item:item[1]))


