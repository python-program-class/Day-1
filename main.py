# startbit youtube chanel
# import random
from random import randint

myVar = 'hello '
math = 2 + 2
result = str(math)  # int type variable ke string type variable convert korbo
# print(myVar+math)# string + int aksathe concatinate korte parbo na tai
print(myVar + result)

x, y = (3, 4)
print(x, y)
# x,y= (3,4,5) # je koiti variable hobe oi sonkhok value declare korte hobe

a = 10
a = 4
print(a)  # sob ses er value assign korbe mane change kora bujhai
var = [78, 2, 34, 5]  # list
print(var)
print(var[0])
print(var[2:])
print(var[-1])
"""i=0
while i<=3: #3 no index track
    print(var[i])
    i+=1"""

# while loop e problem ase list print korte chai list update korchi modify korchi tokhon index number track rakhte hoi
# akhan e 3 no index porjonto ase tai problem nai but list e 1000 ta ba lak ta data thakle dekha lage j ata koto no index
# index no ta track na rekhe e akta list er modhe intaracct korte pari
for x in var:
    print(x)
subjects = ['c', 'c++', 'java', 'android']  # in , not in
print('python' in subjects)
print(subjects + ['swift', 27])
print(subjects * 3)
print(len(subjects))  # var length

subjects.append('Flutter')  # add korar jonno
print(subjects)
subjects.insert(2, 'dart')  # ['c', 'c++', 'dart', 'java', 'android', 'Flutter']
print(subjects)
subjects.remove('c')
print(subjects)
subjects.sort()  # sorting mane kivhabe sajate hoit a,b,c,d, like dictonary
print(subjects)
subjects.reverse()
print(subjects)

subjects.pop()  # pichoner function tule nibe
subjects.pop()  # pichoner function tule nibe
print(subjects)
subjects2 = subjects.copy()
print(subjects2)
pos = subjects.index('dart')  # item er position dakte chaile
print(pos)
pos = subjects2.count('java')
print('java')
subjects.clear()  # list e value nai
print(subjects)

# prime number
x = int(input("enter a number"))
if x > 0:
    for i in range(2, x):
        if x % 2 == 0:
            print('not a prime number')
            break
        else:
            print('prime number')
            break
else:
    print("give a positive number")

# break continue
i = 1
while i <= 30:
    if i == 20:
        break
    print(i)
    i = i + 1
print('hello')
# continue abar loop e fire jawwa niche jabe na


# sum of n
count = 0
i = 1
while i <= 100:
    count = count + i
    i = i + 1
print(count)

# 2+4+...+n
n = int(input("Enter the last term:"))
sum = 0
i = 2
while i <= n:
    sum = sum + i
    i = i + 2
print(sum)

num = list(range(10))  # range er sonkha generate kora range 0 to 9 10ta sonkha
# akdhik element return korbe tai variable e rakha hoise
print(num)
print(num[2])
# starting point ending point 5 to 10 porjonto

num = list(range(5, 11))
print(num)
num = list(range(2, 101, 2))  # bebodhan koto porjonto last er digit 2
# 2 kore barbe
print(num)

# series
# 1+ 2+3+...+n to n sonkhok number
n = int(input("Enter the last number:"))
sum = 0  # + fol nirnoy korar jonno variable nilam
for x in range(1, n + 1, 1):
    sum = sum + x
print(sum)

# 2+ 4+6+...+n
# 1 +3 + 5+...+n
# 4 +8+12+..+n
# 1^2+2^2+3^2+...+n^2 #sum = sum +x*x
# 2^2+4^2+6^2+...+n^2
# 1+1/2+1/3+...+1/n #sum = sum +x/x

# 2* 4*6*...*n # gun er bela sum er man 0 rakle hobe na 1 rakhte hobe
# 1 *3 * 5*...*n
# 4 *8*12*..*n
# 1^2*2^2*3^2*...*n^2
# 2^2*4^2*6^2*...*n^2
# Factorial (n!) # 1 to n porjonto oi sonkhar gun fol
# prime number
# Gcd, Lcm


'''
pattern
n= 3
*
**
***
'''
6

'''
pattern
n= 3
(2*i-1)1 line , 2nd line i er value 1st line  e
*
***
*****
'''

n = 3
for j in range(n + 1):  # 0 to 2 poerjonto tai +1 disi
    print((2 * j - 1) * '*')
"""
1.start
2. input guessnumber
3. generate random number 
4. if guessnumber == random number
i yes, print won
ii no, print lost
5. end
"""
for x in range(1, 10):
    guessNumber = int(input("Enter your guess between 1 to 9:"))
    randomNumber = randint(1, 9)
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was:", randomNumber)  # LOST HOLE RANDOM NUMBER TA KOTO CHILO ATA JANAR JONNO
# jotobar icha ami ai game ta khalte pari tai loop

"""randomNumber = random.randint(1,9)  # random number genarate er jonno random import korte hobe
# random module/ package er modhe rand int use korte pari
# random number ganerate er jonno range choto thakle randint dewwa better
randomNumber = random.Random()*100 # boro range er hole random function use kora vhalo
#  random module e onek function ase sob use korte chachi na rand int use korter chachi
#tahole memory save hobe """

n = input("Enter a text of numbers:")
list = n.split()  # split function je number dibo list alada alada kora jonno use hoi
sum = 0  # jogfol nirnoy kore rakhar jonnno sum # sum int # num hol string
for num in list:
    sum = sum + int(num)
print(sum)

nOW = 0  # word
nOL = 0  # letter
nOD = 0  # digit ase koto
t = input("Number:")  # my name is 123
for x in t:  # t er prottek value x er modhe raktesi
    x = x.lower()  # upper ba lower letter hole
    if x >= 'a' and x <= 'z':
        nOL = nOL + 1  # letter er songkha barbe
    elif x >= '0' and x <= '9':
        nOD = nOD + 1
    elif x == ' ':
        nOW = nOW + 1
print(nOL)
print(nOD)
print(nOW + 1)

# 2 dimentional list / array
matrix = [
    [1, 2, 3],
    [4, 5, 6],  # index

]
matrix[0][2] = 10  # 0 row 2 no column
print(matrix[0][2])  # list er modhe arekta list
for row in matrix:
    for column in row:
        print(column)  # nested for loop
# 2 ta row 3 ta column


""" # dictionaries data stracture
group of obj 
#dict-name  = {key:value} # je format e key value dewwa hobe oi vhabe e 
# dekhabe fixed 
#indexing & slicing not work
# insertation order is preserved
# update , insert, add kora jai 
# mutable in nature
# key unique, but duplicate value are allowed
 # empty dic var = {}, dict() print (type(var))

 key-> Value pair
 name -> 'osama'
 Email-> osama@fjdg
 age-> 25
 kjey use korben er por value store korben key er madhome value gulo access korben
 """
sI = {
    '101': 'Osama',
    '102': 'Jannat',
    '103': 'Jardani',
    '104': 'Oni',
    '105': 'Ashique',

}  # key , value
# access key value
print(sI.get('101'))
print(sI.get('106', 'Note a valid key'))  # nai error dekhabe # get function dile none dekhabe

var = {"name": "Ankit", "age": 21, "name": "ankit", "password": "ankit1234"}
print(var)
print(var["name"])
print(var.keys())
print(var.values())
print(var.items())
var["age"] = 50
print(var)

for key, values in var.items():
    print(key, values, sep="-")
# separator sep
# list er moto tuples o data structure partokko holo list e 
# value change kora jai tuples er value change kora jai na
# karon tuple immuteble
student1 = (
    ('osama', 27, 3.35), 'jannat', 'oni',
)  # tuple er vitor e o tuple rakha jabe
# student1[0]= 'Khan'
print(student1[0])
print(student1[1:])  # tuple er o slice kora jai list er moto
# tuple er subidha holo fast onek list er theke o nek fast


# set = unoderd collection of item # order thake na
# same item theke na unique value thake
# curly braces {}
# element jodi {10,20} thake tahole hoite pare 20 age print hoi 10 pore
# indexing or slicing kora jai na
# pore change kora jai value / mutable
# je kono type er value rakha jai
# index num er madhome value/ item access k0ora jai na
# duplicate value rakha jabe na
# create = {}, set.function()
num1 = {1, 2, 3, 4, 5, 6}
num2 = set([4, 5])  # list value # convert set
num2.add(7)
num.remove(7)
print(7 in num2)
# var = {10,'ankit', 56.7,true}
# empty set var = set{}
# print(type(var))
# var.add('osama',10)
# var.update('osama',10)
# update method e 


# num1 | num2 # union mane sob dekhabe  n1 $ n2 # intersection mane comon value #differnt num1- num2

# define size n = even only
n = 8

# so this heart can be made n//2 part left,
# n//2 part right, and one middle line
# i.e; columns m = n + 1
m = n + 1

# loops for upper part
for i in range(n // 2 - 1):
    for j in range(m):

        # condition for printing stars to GFG upper line
        if i == n // 2 - 2 and (j == 0 or j == m - 1):
            print("*", end=" ")

        # condition for printing stars to left upper
        elif j <= m // 2 and ((i + j == n // 2 - 3 and j <= m // 4) \
                              or (j - i == m // 2 - n // 2 + 3 and j > m // 4)):
            print("*", end=" ")

        # condition for printing stars to right upper
        elif j > m // 2 and ((i + j == n // 2 - 3 + m // 2 and j < 3 * m // 4) \
                             or (j - i == m // 2 - n // 2 + 3 + m // 2 and j >= 3 * m // 4)):
            print("*", end=" ")

        # condition for printing spaces
        else:
            print(" ", end=" ")
    print()

# loops for lower part
for i in range(n // 2 - 1, n):
    for j in range(m):

        # condition for printing stars
        if (i - j == n // 2 - 1) or (i + j == n - 1 + m // 2):
            print('*', end=" ")

        # condition for printing GFG
        elif i == n // 2 - 1:

            if j == m // 2 - 1 or j == m // 2 + 1:
                print('G', end=" ")
            elif j == m // 2:
                print('F', end=" ")
            else:
                print(' ', end=" ")

        # condition for printing spaces
        else:
            print(' ', end=" ")

    print()
