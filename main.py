##################################################
'''
Q1:
a: True
b: False
c:  True
d: false
e: True
f: False
g: True
h: True
i: True
'''

##################################################
'''
Q2:
a: y > 0
b: z != 0  
c: y > z
d: z >= 0
e: y-x < y-z
f: z % 2 !== 0
g: x % 2 == 0
h: y % z == 0
i: y >= 0 and y < 10
j: (x > 0 and z < 0) or (x < 0 and z > 0)
k: (x % 2 == 0 and y % 2 != 0) or  (y % 2 == 0 and x % 2 != 0)
'''

##################################################
'''
Q3:
'''


number = int(input('Give me a number: '))

if number % 2 == 0:
     print("Even number")
     if number % 3 == 0:
        print("Divisible by 6.")
else:
    print("Odd number.")





    
number = int(input('Give me a number: '))

if number % 2 != 0:
     print("Odd number")
     if number % 7 == 0:
        print("Divisible by 7.")
else:
    print("Even number.")
    if number % 7 == 0:
        print("Divisible by 7.")
##################################################

