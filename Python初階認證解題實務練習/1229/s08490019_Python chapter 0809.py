# In[1]
'''
請撰寫一程式，要求使用者輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
　a. 必須至少八個字元。
　b. 只包含英文字母和數字。
　c. 至少要有一個大寫英文字母。
　d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】。
'''
a=input("input:")
if len(a)<8: #八字元
    print('【Invalid password】')
elif a.isalpha()==True or a.isdigit()==True or a.islower()==True: #字母、數字、大寫英文字母
    print('【Invalid password】')
else:
    print('【Valid password】')

# In[2]
'''
請利用sStr1之字串找出’e’在這字串中的哪個位置。
sStr1 = 'abcdefg'
'''
sStr1 = 'abcdefg'
print(sStr1.find('e'))

# In[3]
'''
檢查字串中是否有數字，並顯示數字為何
EX:
輸入: Hi my age is 32 I have 213
輸出: [32, 213]
'''
a=input("input:")
a=a.split()
for i in a:
    if i.isdigit() ==True:
        print(i,end=' ')


# In[4]
'''
str1 = "你好"
a. 請將str1字串轉換成base64並輸出
b. 請將str1字串轉換成base64並輸出
'''
import base64
str1 = '你好'
b = str1.encode('UTF-8')
bytes_encode = base64.b64encode(b)
print(bytes_encode)
# In[5]
'''
str = "this is string example....wow!!! this is really string"
a.	請將str中的’is’替換成’was’
b.	請將str中的’wow’替換成’www’
'''
str1 = "this is string example.... wow!!! this is really string"
str1 =str1.replace('is', 'was')
str1 =str1.replace('wow', 'www')
print(str1)
# In[6]
'''
str1 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
a.	請將str1以空白做字串切割
b.	請將str1以’\’做字串切割
'''
str1 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
str1=str1.split()
print(str1)
# In[7]
'''
請撰寫一程式，將使用者輸入的五筆資料寫入到write.txt（若不存在，則讓程式建立它），
每一筆資料為一行，包含學生名字和期末總分，以空白隔開。檔案寫入完成後要關閉。
'''

fp=open("write.txt", "w",encoding='UTF-8')
for i in range(5):
  fp.write(input(':'))
  fp.write('\n')
fp.close()

# In[8]
'''
請嘗試打開一個fiokd.csv的檔案並寫入”這是一個測試檔”，如果無法開啟請顯示:無此檔案
'''
import csv
#import os
with open('fiokd.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['這是一個測試檔'])

    

      
      
        
      
      
      
# In[9]
'''
請嘗試打開一個fiokd.txt的檔案並寫入” 这是一个测试文件，用于测试异常!!”，如果無法寫入請顯示:編碼錯誤
'''
fp=open("fiokd.txt", "w",encoding='UTF-8')
fp.write('这是一个测试文件，用于测试异常!!')
fp.close()

# In[10]
'''
寫一個計算減法的方法，當第一個數小於第二個數時，顯示“被減數不能小於減數"
'''
def jianfa(a,b):
    if a<b:
        raise BaseException('被減數不能小於減數')
    else:
        return a-b
jianfa(1, 3)
