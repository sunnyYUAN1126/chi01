# In[1]
'''
有一個陣列為: arr=[99, 6, 7, 3, 78, 56, 72, 12]
請使用氣泡排序法由小到大排列
'''
arr=[99, 6, 7, 3, 78, 56, 72, 12]
n=len(arr)
while n > 1:
        n-=1
        for i in range(n):        
            if arr[i] > arr[i+1]:  
                arr[i], arr[i+1] = arr[i+1], arr[i]
for i in arr:
    print(i,end=" ")
    
    
# In[2]
'''
按逗號分隔列表: L = [1,2,3,4,5]
'''
L = [1,2,3,4,5]
str_L=(str(i) for i in L)
print(','.join(str_L))
#join 方法只接受一個全部都包含 string 的 list 數據類型，然而上面的 ids 變量裡包含了 int 型數字，那辦法就是將這些 int 轉換成 string。


# In[3]
'''
求一個3*3矩陣主對角線元素之和
'''
arr=[[1,2,3],[4,5,6],[7,8,9]]
b=arr[0][0]+arr[1][1]+arr[2][2]
for i in arr:
    print(i)
print("和=",b)
        

# In[4]
'''
有一個已經排好序的陣列。現輸入一個數，要求按原來的規律將它插入陣列中
'''
arr=[1,2,3,4,5,6,7,8,9,10]
a=eval(input("input:"))
arr.insert(a-1,a)
print(arr)
# In[5]
'''
輸入陣列，最大的與第一個元素交換，最小的與最後一個元素交換，輸出陣列
'''
arr=[]
for i in range(10):
    a=eval(input("input:"))
    arr.append(a)
print("befor:",arr)
m=max(arr)
n=min(arr)
m1=arr.index(m)
n1=arr.index(n)

print(m1)
print(n1)
arr[0],arr[m1]=arr[m1],arr[0]
arr[9],arr[n1]=arr[n1],arr[9]
print("after:",arr)

# In[6]
'''
某個公司採用公用電話傳遞資料，資料是四位的整數，在
傳遞過程中是加密的，加密規則如下：每位數字都加上5,
然後用和除以10的餘數代替該數字，再將第一位和第四位
交換，第二位和第三位交換
'''
a,b,c,d=eval(input("input 4:"))
a=(a+5)%10
b=(b+5)%10
c=(c+5)%10
d=(d+5)%10
print(d*1000+c*100+b*10+a)


# In[7]
'''
將一個陣列由大到小輸出lis=[1,10,100,1000,10000,100000]
'''
arr=[]
for i in range(6):
    if i==0:
        arr.append(1)
    else:
        a=arr[i-1]*10
        arr.append(a)
print(arr)


# In[8]
'''
請撰寫一程式，讓使用者輸入四週各三天的溫度，
接著計算並輸出這四週的平均溫度及最高、最低溫度。

提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

輸入與輸出會交雜如下: 
Week 1:
Day 1:23.1
Day 2:24
Day 3:23.5
Week 2:
Day 1:32
Day 2:33
Day 3:35.5
Week 3:
Day 1:29
Day 2:30
Day 3:26
Week 4:
Day 1:27.6
Day 2:25
Day 3:28.8
Average: 28.13
Highest: 35.5
Lowest: 23.1

'''
week=[]
b=0
for i in range(4):
    print("week",i+1)
    for j in range(1,4):
        a=eval(input("Day %d:"%j))
        week.append(a)
    print()
    
m=max(week)
n=min(week)
print("Highest:",m)
print("Lowest:",n)

for i in week:
    b+=i
    print(a)
b/=12
print("Average:%.2f"%b)

# In[9]
'''
輸入3個數a,b,c，按大小順序輸出。
'''
arr=[]
a,b,c=eval(input("input 3:"))
arr.append(a)
arr.append(b)
arr.append(c)
arr.sort()
print(arr)

# In[10]
'''
有n個整數，使其前面各數順序向後移m個位置，最後m個數變成最前面的m個數
'''
arr=[]
brr=[]
n=eval(input("n:"))
m=eval(input("m:"))
for i in range(n):
    nn=eval(input("input:"))
    arr.append(nn)
print("有n個整數:",arr)
for i in range(m):
    mm=eval(input("input:"))
    brr.append(mm)
arr=brr+arr
print(arr)