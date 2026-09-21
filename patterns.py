'''****
   ****
   ****
   ****

def main():
    n=int(input("enter n"))
    (square_pattern(n))
def square_pattern(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            print("*",end="")
        print()
main()






*
**
***
****
*****

def main():
    n=int(input("enter n:"))
    right_triangle(n)
def right_triangle(x):
    for i in range(1,x+1):
        print("*"*i)
main()










1
12
123
1234
12345
def main():
    n=int(input("enter n:"))
    num_pattern(n)
def num_pattern(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
main()












1
22
333
4444
55555
def main():
    n=int(input("enter n:"))
    num_pattern2(n)
def num_pattern2(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(i,end="")
        print()
main()














*****
****
***
**
*

def main():
    n=int(input("enter n:"))
    inv_right_pattern(n)
def inv_right_pattern(x):
    for i in range(x,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()
main()












12345
1234
123
12
1
def main():
    n=int(input("enter n:"))
    inv_num_pattern(n)
def inv_num_pattern(x):
    for i in range(x,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()
main()











   *
  ***
 *****
*******
def main():
    n=int(input("enter n:"))
    pyramid(n)
def pyramid(x):
    for i in range(1,x+1):
        for _ in range(x-i):
            print(" ",end="")
        for _ in range(2*i-1):
            print("*",end="")
        print()
main()










*******
 *****
  ***
   *
def main():
    n=int(input("enter n:"))
    pyramid(n)
def pyramid(x):
    for i in range(x,0,-1):
        for _ in range(x-i):
            print(" ",end="")
        for _ in range(2*i-1):
            print("*",end="")
        print()
main()










    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
def main():
    n=int(input("enter x:"))
    daimond(n)
def daimond(x):
    for i in range(1,x+1):
        for _ in range(x-i):
            print(" ",end="")
        for _ in range(2*i-1):
            print("*",end="")
        print()
    for j in range(x,0,-1):
        for _ in range(x-j):
            print(" ",end="")
        for _ in range(2*j-1):
            print("*",end="")
        print()
main()









*
**
***
****
*****
*****
****
***
**
*
def main():
    n=int(input("enter n:"))
    half_butterfly(n)
def half_butterfly(x):
    for i in range(1,x+1):
        print("*"*i)
    for j in range(x,0,-1):
        print("*"*j)
main()










1
01
101
0101
10101
def main():
    n=int(input("enter n :"))
    binary_pattern(n)
def binary_pattern(x):
    for i in range(1,x+1):
        for j in range(i):
            print((i+j)%2,end="")
        print()
main()
















1        1
12      21
123    321
1234  4321
1234554321
def main():
    n=int(input("enter n:"))
    half_num_butterfly(n)
def half_num_butterfly(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(j,end="")
        for k in range(1,2*(x-i)+1):
            print(" ",end="")
        for l in range(i,0,-1):
            print(l,end="")
        print()
main()
            










1  
2  3  
4  5  6  
7  8  9  10  
11  12  13  14  15 
def main():
    n=int(input("enter n:"))
    num_r_a_t(n)
def num_r_a_t(x):
    num=1
    for i in range(1,x+1):
        for j in range(i):
            print(num," " ,end="")
            num+=1
        print()
main()









A
AB
ABC
ABCD
ABCDE
def main():
    n=int(input("enter n:"))
    alphabet_triangle(n)
def alphabet_triangle(x):
    for i in range(1,x+1):
        ch=65
        for j in range(1,i+1):
            print(chr(ch),end="")
            ch+=1
        print()
main()








ABCDE
ABCD
ABC
AB
A
def main():
    n=int(input("enter n:"))
    alphabet_triangle(n)
def alphabet_triangle(x):
    for i in range(x,0,-1):
        ch=65
        for j in range(1,i+1):
            print(chr(ch),end="")
            ch+=1
        print()
main()









A
BB
CCC
DDDD
EEEEE
def main():
    n=int(input("enter n:"))
    alphabet_tri2(n)
def alphabet_tri2(x):
    ch=65
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(chr(ch),end="")
        ch+=1
        print()
main()
'''


# n=int(input("enter n:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range((2*i)-1):
#         print("*",end="")
#     print()

def main():
    n=int(input("enter n:"))
    alphabet_pyramid(n)
def alphabet_pyramid(x):
    ch=65
    for i in range(1,x+1):
        for j in range(x-i):
            print(" ",end="")
        for k in range((2*i)-1):
            print(chr(ch),end="")
            ch+=1
        print()
main()