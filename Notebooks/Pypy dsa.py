#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np




# In[ ]:


bits = np.random.randint(0,2,12)


# In[ ]:


list(enumerate(bits))


# In[ ]:


reduce(lambda x, y: x^y, [ i for i,bit in enumerate(bits) if bit])


# In[ ]:


from functools import reduce
import operator as op


# In[ ]:


bin(13)


# In[ ]:


bits[1] = not bits[1] 


# In[ ]:


bits[4] = not bits[4]
bits[8] = not bits[8]


# In[ ]:


reduce(lambda x, y: x^y, [ i for i,bit in enumerate(bits) if bit])


# In[ ]:


bits


# In[ ]:


bits = np.random.randint(0,2,256)


# In[ ]:


bits


# In[ ]:


reduce(lambda x, y: x^y, [ i for i,bit in enumerate(bits) if bit])


# In[ ]:


bin(233)


# In[ ]:


bits[1] = not bits[1]
bits[8] = not bits[8]
bits[32] = not bits[32]
bits[64] = not bits[64]
bits[128] = not bits[128]


# In[ ]:


reduce(lambda x, y: x^y, [ i for i,bit in enumerate(bits) if bit])


# In[ ]:


bits


# In[ ]:


bits[41] = not bits[41]


# In[ ]:


reduce(lambda x, y: x^y, [ i for i,bit in enumerate(bits) if bit])


# In[ ]:


bin(41)


# In[ ]:


a = int(input())
if a == 2:
    print("NO")
elif a%2==0:
    print("YES")
else:
    print("NO")


# In[ ]:


b = int(input())
arr = []
for i in range(0,b):
    temp = input()
    arr.append(temp)
for a in range(0,len(arr)):
    if len(arr[a]) > 10:
        temp2 = arr[a]
        start = temp2[0]
        end = temp2[-1]
        print(start + str(int(len(temp2)) - 2) + end)
    else:
        print(arr[a])


# In[ ]:


len(temp2)


# In[ ]:


b = int(input())
arr = []
for i in range(0,b):
    temp = input()
    temp2 = temp.split()
    arr.append(temp2)
yes = 0
sums = 0

for j in arr:
    for k in j:
        sums = sums + int(k)
    if sums >= 2:
        yes = yes + 1
    sums = 0
print(yes)    


# In[ ]:


d = input()
d = d.split()
b = int(d[0])
c = int(d[1])

e = input()
arr = e.split()

success = []
for j in arr:
    if int(j) >= int(arr[c-1]) and int(j)>0:
        success.append(j)
print(len(success))


# In[ ]:


b = int(input())
arr = []
x =0
for i in range(0,b):
    temp = input()
    arr.append(temp)
for j in arr:
    if "++" in j:
        x = x +1
    if "--" in j:
        x = x - 1
print(x)


# In[ ]:


x


# In[ ]:


one = input()
two = input()

if one.lower() > two.lower():
    print("1")
if one.lower() < two.lower():
    print("-1")
if one.lower() == two.lower():
    print("0")


# In[ ]:


b = input()
c = b[0].capitalize()
d = b[1:]
print(c + d)


# In[ ]:


count = int(input())
step = 0
sub = 5
while count >= 0 and sub > 0:
    while count - sub >= 0 and sub > 0:
        count = count - sub
        step = step + 1
    sub = sub - 1
        
print(step)        


# In[ ]:


usls = input()
usls = usls.split()
l = int(usls[1])
n = int(usls[0])

values = input()
values = values.split() 


values_int = []
for i in range(0,n):
    values_int.append(int(values[i])) 

values_int.sort()
maxi = 0
for j in range(0,len(values_int)-1):
    temp = values_int[j+1] - values_int[j]
    if temp > maxi:
        maxi = temp
x = max(maxi/2,(values_int[0]-0), (l- values_int[n-1]))
print(x)


# In[ ]:


b = int(input())
arr = []
for i in range(0,b):
    temp = input()
    arr.append(temp)


for i in range(0,len(arr)):
    a = arr[i].split()
    n = int(a[0])
    k = int(a[1])
    c = k
    d = k//n
    
    while k >= -1:
        if c/n != 0:
            k = k - 1- d 
        c = c + 1
    print(c)


    
    


# In[ ]:


temp


# In[ ]:


def sumOfTwoPerfectCubes(N) :
    cubes = {}
    i = 1
    while i*i*i <= N :
        cubes[i*i*i] = i
        i += 1
  
    for itr in cubes :
  
        firstNumber = itr
  
        secondNumber = N - itr
  
        if secondNumber in cubes :
            print("YES", end = "")
            return
  
    print("NO", end = "")

b = int(input())
arr = []
for i in range(0,b):
    temp = input()
    arr.append(temp)

values = []
for j in arr:
    values.append(int(j))

for k in values:
    sumOfTwoPerfectCubes(k)


# In[ ]:


b = int(input())
arr = []
for i in range(0,b):
    temp = input()
    arr.append(temp)

for j in range(0,b):
    values = arr[j].split()
    h = int(values[0])
    c = int(values[1])
    t = int(values[2])
    tub = 0
    count = 0
    while True:
        tub += h
        count += 1
        if tub == t:
            print(count)
            break
        tub -= c
        count += 1
        if tub == t:
            print(count)
            break

        
    


# In[ ]:


#lutherleo
for _ in range(int(input())):
    h,c,t=map(int,input().split())
    if t<=(h+c)/2:
        print(2)
    else:
        k=(h-t)//(2*t-h-c)
        if abs((2*k+3)*t-k*h-2*h-k*c-c)*(2*k+1)<abs((2*k+1)*t-k*h-h-k*c)*(2*k+3):
            print(2*k+3)
        else:
            print(2*k+1)


# In[ ]:


test_str = "0111"  #write the input statement here

res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]
  
#output = []
#for x in res:
#    if x not in output:
#        output.append(x)
print(res)


# In[ ]:


b = int(input())
shops = input()
shops = shops.split()
int_shops = []
for shop in shops:
    int_shops.append(int(shop))

f_count = []
days = int(input())
for i in range(0,days):
    coins = int(input())
    coinss.append(coins)
    count =0
    for shop in int_shops:
        if coins>= shop:
            count += 1
    f_count.append(count)

for lol in f_count:
    print(lol)


# In[ ]:


print(eval(input().replace(' ','*'))//2)


# In[ ]:


import bisect
 
input()
x = sorted(map(int, input().split()))
 
for i in range(int(input())):
	print(bisect.bisect_right(x, int(input())))


# In[ ]:


m , n = map(int, input().split())
c = (m*n)//2
print(c)


# In[ ]:


class LikedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
    
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
     
    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
    
    def get_element(self,position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


# In[ ]:


class Node():
    def __init__(self,value):
        self.data = value
        self.next = None
n1 = Node(3)


# In[ ]:


list2 = LikedList()
list2.append(2)
list2.append(None)


# In[ ]:


list2.head.data


# In[ ]:


class User:
    def __init__(self,username, name, email):
        self.username = username
        self.name = name
        self.email = email

    
    def intro(self, guest_name):
        print("hi {}, I'm {}! Contact me at {}.".format(guest_name, self.name, self.email))
        
    def __repr__(self):
        return "User(username = '{}', name ='{}', email = '{}')".format(self.username, self.name, self.email)


# In[ ]:


user2 = User("lol", "name", 'email.com')


# In[ ]:


user2.intro("hey")


# In[ ]:


user2


# In[ ]:


class UserDatabase:
    def __init__(self):
        self.users = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i,user)
        
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
            
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user,email
        
    def list_all(self):
        return self.users


# In[ ]:


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


# In[ ]:


users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]


# In[ ]:


database = UserDatabase()


# In[ ]:


database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)


# In[ ]:


database.find('siddhant')


# In[ ]:


database.list_all()


# In[ ]:


class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


# In[ ]:


tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))


# In[ ]:


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
        


# In[ ]:


tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))


# In[ ]:


tree2.left.key


# In[ ]:


def display_keys(node, space='\t',level = 0):
    
    if node is None:
        print(2*space*level + 'N')
        return
    if node.left is None and node.right is None:
        print(2*space*level + str(node.key))
        return
    display_keys(node.right, space, level+1)
    print(2*space*level + str(node.key))
    display_keys(node.left, space, level+1)


# In[ ]:


display_keys(tree2, ' ')


# In[ ]:


def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left)+[node.key] + traverse_in_order(node.right))


# In[ ]:


def traverse_pre_order(node):
    if node is None:
        return []
    return([node.key]+traverse_pre_order(node.left) + traverse_pre_order(node.right))


# In[ ]:


def traverse_post_order(node):
    if node is None:
        return []
    return(traverse_post_order(node.left) + traverse_post_order(node.right) + [node.key])


# In[ ]:


traverse_post_order(tree2)


# In[49]:


class BSTNode():
    def __init__(self, key, value =None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None 
        self.parent = None


# In[ ]:


def insert(node, key, value):
    if node is None:
        node = BSTNode(key,value)
    elif key < node.key:
        node.left = insert(node.left,key,value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right,key,value)
        node.right.parent = node
    return node


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Watch House Party

# In[ ]:


def minSwapsToSort(arr, n):
 
    # Create an array of pairs
    # where first element is
    # array element and second
    # element is position of
    # first element
    arrPos = [[0 for x in range(2)]
                 for y in range(n)]
     
    for i in range(n):   
        arrPos[i][0] = arr[i]
        arrPos[i][1] = i
 
    # Sort the array by array
    # element values to get right
    # position of every element
    # as second element of pair.
    arrPos.sort()
 
    # To keep track of visited
    # elements. Initialize all
    # elements as not visited
    # or false.
    vis = [False] * (n)
 
    # Initialize result
    ans = 0
 
    # Traverse array elements
    for i in range(n):
     
        # Already swapped and corrected or
        # already present at correct pos
        if (vis[i] or arrPos[i][1] == i):
            continue
 
        # Find out the number of  node in
        # this cycle and add in ans
        cycle_size = 0
        j = i
         
        while (not vis[j]):       
            vis[j] = 1
 
            # Move to next node
            j = arrPos[j][1]
            cycle_size+= 1
        
        # Update answer by
        # adding current cycle.
        ans += (cycle_size - 1) 
 
    # Return result
    return ans
 
# Method returns minimum
# number of swap to mak
# array B same as array A
def minSwapToMakeArraySame(a, b, n):
         
    # map to store position
    # of elements in array B
    # we basically store
    # element to index mapping.
    mp = {}
    for i in range(n):
        mp[b[i]] = i
 
    # now we're storing position
    # of array A elements
    # in array B.
    for i in range(n):
        b[i] = mp[a[i]]
 
    # Returing minimum swap
    # for sorting in modified
    # array B as final answer
    return minSwapsToSort(b, n)
 
# Driver code
if __name__ == "__main__":
 
    a = [3, 6, 4, 8]
    b = [4, 6, 8, 3]
    n = len(a)
    print(minSwapToMakeArraySame(a, b, n))


# array, strings, dp, binary search,matrix,sorting,hashmap, greedy, LinkedList
# Stack,Que and Deque
# Tree, Binary search Tree

# In[ ]:


a1 = input()
a2 = input()
a3 = input()
a4 = input()
a5 = input()
count = 0
if "1" in a1:
    count += 2
    a1 = a1.split()
    ind = a1.index('1')
    count += abs(ind - 2)
if "1" in a2:
    count += 1
    a2 = a2.split()
    ind = a2.index('1')
    count += abs(ind - 2)
if "1" in a3:
    count += 0
    a3 = a3.split()
    ind = a3.index('1')
    count += abs(ind - 2)
if "1" in a4:
    count += 1
    a4 = a4.split()
    ind = a4.index('1')
    count += abs(ind - 2)
if "1" in a5:
    count += 2
    a5 = a5.split()
    ind = a5.index('1')
    count += abs(ind - 2)

print(count)
            


# In[ ]:


n = int(input())
strings = input()
count = 0
for i in range(1,n):
    temp = strings[i]
    if strings[i] is strings[i-1]:
        count = count +1
print(count)  



# In[ ]:


k,n,w = map(int,input().split())
print(max(0,(w*(w+1)//2*k-n)))


# In[ ]:


a = input()
a = a.lower()
b = list(a)
vowels = ["a","o","y","e","u","i"]
for letter in b[::-1]:
    if letter in vowels:
        b.remove(letter)
for c in b:
    print("." + c, end="")


# In[ ]:


a = int(input())
x,y,z = 0,0,0
for _ in range(0,a):
    x1,y1,z1 = map(int,input().split())
    x += x1
    y += y1
    z += z1
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")


# In[ ]:


stl = input().split("+")
stl.sort()
print(*stl, sep="+")


# In[ ]:


a, b = map(int, input().split())
count = 0
while a <= b:
    a = a*3
    b = b*2
    count += 1
print(count)


# In[ ]:


n,k = map(int, input().split())
for _ in range(0,k):
    if str(n)[-1] == "0":
        n = n//10
    else:
        n = n-1
print(n)


# In[ ]:


wrd = input()
countl = 0
countu = 0
for letter in wrd:
    if(letter.islower()):
        countl += 1
    if(letter.isupper()):
        countu += 1
if countl >= countu:
    print(wrd.lower())
else:
    print(wrd.upper())


# In[ ]:


n = int(input())
passengers = 0
max =0
for _ in range(0,n):
    a,b = map(int, input().split())
    passengers = passengers + b - a
    if passengers > max:
        max = passengers
print(max)


# In[ ]:


n = iter(input())
if all(c in n for c in 'hello'):
    print("YES")
else:
    print("NO")
#66,811


# In[ ]:


n = int(input())
thing = 1
ath = ['4', '7']
for i in range(0, len(str(n))):
    if str(n)[i] not in ath:
        thing = 0
if n%4 == 0 or n%7 == 0:
    thing = 1
if thing == 1:
    print("YES")
elif thing == 0:
    print("NO")


# In[ ]:


s = input()
t = input()
if s[::-1] == t:
    print("YES")
else:
    print("NO")
    


# In[ ]:


n=int(input());print(["YES","NO"][all(n%i for i in[4,7,47,477])])


# In[ ]:


a = int(input())
con = input().split()
con2 = []
for l in con:
    con2.append(int(l))
con2.sort()
con2.reverse()
sum2 = sum(con2)
sum1 = 0
i = 0
while sum1 <= sum2//2:
    sum1 += con2[i]
    i += 1
print(i)


# In[ ]:


con2


# In[ ]:


_ = input()
b = input()
Anton, Derik = 0, 0
for l in b:
    if l == "A":
        Anton += 1
    if l == "D":
        Derik += 1
if Derik > Anton:
    print("Danik")
elif Anton > Derik:
    print("Anton")
elif Derik == Anton:
    print("Friendship")
#61818


# In[ ]:


a = int(input())
b = a + 1
th = 0
while b > a and th == 1:
    j = 0
    while j< len(str(b))-1:
        if str(b)[j] == str(b)[j+1]:
            
    
#check if all are differnet numbers


# In[ ]:


n,h = map(int, input().split())
count = 0
thing = input().split()
for temp in thing:
    if int(temp) > h:
        count += 2
    else:
        count += 1
print(count)


# In[ ]:


a = input()
yes = 0
for letter in a:
    if letter in ["H","Q","9"]:
        print("YES")
        yes = 1
        break
if yes == 0:
    print("NO")


# In[ ]:


a = int(input())
count = 0
for _ in range(0,a):
    p,q = map(int,input().split())
    if q-p >0:
        count += 1
print(count)


# In[ ]:


b = int(input())
a = input().split()
list2 = [0]*b
i = 0
while i < len(a):
    temp = int(a[i]) -1
    list2[temp] = i + 1
    i += 1
print(*list2, sep = " ")  
#take a value and index of a thing from a
#then reverse them and add them into list2


# In[ ]:


m = int(input())
n = 0
a= input()
for i in range(m-1):
    b= input()
    if a!= b:
        n+=1
        a=b
print(n+1)


# In[ ]:


_ = input()
if "1" in input():
    print("HARD")
else:
    print("EASY")


# In[ ]:


n,k=map(int,input().split())
n += 1
n = n//2
print(2*k-1 if k<=n else(k-n)*2)


# In[ ]:


a = int(input())
a = input().split()
count = 0
count1,count2, count3,count4 = 0,0,0,0
for i in a:
    if i == "4":
        count4 += 1
    elif i == '3':
        count3 += 1
    elif i == '2':
        count2 += 1    
    elif i == '1':
        count1 += 1

vacay = 1*count3 + count2%4
if vacay > count1:
    count = count4 + count3 -(-count2//2)
elif vacay <= count1:
    count = count4 + count3 + count2//2 + -(-count1+ vacay)//4
print(count)
        

#check if sum exceeds 4 then dont do the add


# In[ ]:


input()
a,b,c,d = map(input().count,('1','2','3','4'))
print(d+c+(b*2+max(0,a-c)+3)//4)


# In[ ]:


a = int(input())
o1 = "I hate it"
e1 = "I hate that I love it"
o2 = "I hate that I love that "
if a%2 == 0:
    print(o2*((a-2)//2) + e1)
else:
    print(o2*((a-1)//2) + o1)


# In[ ]:


n = int(input())
o = (n + 1)//2
e = n//2
sume = e*(e+1)
sumo = o*o
    
print(sume - sumo)


# In[3]:


a = int(input())
b = input().split()
count = 1
maxi = 1
for i in range(0,len(b)-1):
    if int(b[i]) <= int(b[i+1]):
        count += 1
        if count > maxi:
            maxi = count
    else:
        count = 1
print(maxi)


# In[5]:


a = input()
b = input()
c = []
for num in range(len(b)):
    if a[num] == b[num]:
        c.append("0")
    else:
        c.append("1")
print(*c, sep ="")


# In[26]:


a = input()
b = []
if a[1:].isupper() or len(a)==1:
    if a[0].isupper():
        b.append(str(a[0].lower()))
    elif a[0].islower():
        b.append(a[0].upper())
    b.append(str(a[1:].lower()))
    print(*b,sep='')

else:
    print(a)


# In[19]:


a[1:].lower


# In[30]:


a = int(input())
b = int(input())
c = int(input())
print(max((a+b)*c,a*(b+c),a*b*c,a+b+c,a*b+c,a+c*b))


# In[35]:


input()
a = input().split()
c =[]
for b in a:
    c.append(int(b))
c.sort()
print(*c, sep = " ")


# In[46]:


n = int(input())
x = input().split()
y = input().split()
z = x+y
count = 0
for i in range(1,n+1):
    if str(i) in z:
        count += 1
    else:
        count = 0
if count == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")    


# In[48]:


print("I become the guy.") if(int(input()) == len(set(input().split()[1:]+input().split()[1:]))) else print("Oh, my keyboard!")


# In[51]:


print(4-len(set(input().split())))


# In[62]:


k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

print((d//k + d//l + d//m + d//n - d//(k*l)- d//(k*m)- d//(k*n) - d//(m*l)- d//(n*l)- d//(m*n) + d//(k*l*m) + d//(k*m*n) + d//(k*l*n) + d//(l*n*m) - d//(k*l*m*n)))


# In[70]:


a = input()
a = a.replace("WUB", " ")
print(a)


# In[90]:


n,m = map(int, input().split())
b = input().split()
a = []
for c in b:
    a.append(int(c))
a.sort()
mini = 1000000
if m > n:
    for i in range(m-n):
        diff = int(a[i+n-1]) - int(a[i])
        if diff < mini:
            mini = diff
else:
    mini = 0
print(mini)
    


# In[86]:


I=lambda:map(int,input().split())
n,m=I()
a=sorted(I())
print(min(j-i for i,j in zip(a,a[n-1:])))


# In[93]:


a,a[n-1:]


# In[101]:


I = lambda:map(int,input().split())
a = I()
b = I()
b = list(b)
mini = b.index(min(b)) + 1
maxi = b.index(max(b)) + 1
print(len(b) + maxi - mini )


# In[106]:


I = lambda:map(int,input().split())

c = int(input())
for _ in range(c):
    a,b = I()
    print(a%b) if a%b ==0 else print(b-a%b)


# In[124]:


a = input();print(len(set(a[1:len(a)-1].split(", ")))) if a != '{}' else print(0)


# In[123]:


a


# In[ ]:




