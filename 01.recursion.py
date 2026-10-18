# # factorial of a number 
# n=int(input("enter n:"))
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))



# # count n to 1

# def main():
#     n=int(input("enter n:"))
#     (count(n))
# def count(x):
#     if x==0:
#         return
#     else:
#         print(x)
#         return (count(x-1))
# main()



# # count 1 to n
# def main():
#     n=int(input("enter n:"))
#     count(1,n)
# def count(x,n):
#     if x>n:
#         return
#     else:
#         print(x)
#         return count(x+1,n)
# main()






# # sum of n natural number 
# def main():
#     n=int(input("enter n:"))
#     print(total(n))
# def total(x):
#     if x==0 :
#         return 0
#     else:
#         return x + total(x-1)
# main()










# # factorial
# def main():
#     n=int(input("enter n:"))
#     print(fact(n))
# def fact(x):
#     if x==0 or x==1:
#         return 1 
#     else:
#         return x * fact(x-1)
# main()





# power of the number
# def main():
#     n=int(input("enter n:"))
#     power=int(input("Enter n:"))
#     print(get_power(n,power))
# def get_power(x,y):
#     if y==0:
#         return 1
#     else:
#         return x*get_power(x,y-1)
# main()






# # count digit
# def main():
#     n=int(input("Enter n:"))
#     count(n)
# def count(x):
#     if x>0 and x<=9:
#         return 1
#     else:
#         count=0
#         digit=x%10
#         return count
#         x//=10
        

     

# def main():
#     count=0
#     fn(count)
# def fn(x):
#     if x==5:
#         return
#     print(x)
#     return fn(x+1)
# main()


# # to print names 5 time
# def main():
#     n=5
#     i=1
#     fn(i,n)
# def fn(j,x):
#     if j>x:
#         return
#     print("ayush")
#     return fn(j+1,x)
# main()   
    


# # print numbers 1 to n 
# def main():
#     n=int(input("enter n:"))
#     i=1
#     fn(i,n)
# def fn(j,x):
#     if j>x:
#         return 
#     print(j)
#     return fn(j+1,x)
# main()




# # # print numbers  n to 1
# def main():
#     n=int(input("enter n:"))
#     i=n
#     fn(i,n)
# def fn(j,x):
#     if j==0:
#         return
#     print(j)
#     return fn(j-1,x)
# main()



# # print 1 to n using backtracking 
# def main():
#     n=int(input("enter n:"))
#     fn(n)
# def fn(x):
#     if x<1:
#         return
#     fn(x-1)
#     print(x)
# main()


# # print n to 1 using backtracking 
# def main():
#     n=int(input("enter n:"))
#     i=1
#     fn(i,n)
# def fn(j,x):
#     if j>x:
#         return
#     fn(j+1,x)
#     print(j)
# main()


# def main():
#     n=int(input("enter n:"))
#     i=1
#     fn(i,n)
# def fn(j,x):
#     if j>x:
#         return
#     print(j)
#     fn(j+1,x)
# main()

# def main():
#     n=int(input("enter n:"))
#     i=n
#     fn(i,n)
# def fn(j,x):
#     if j<1:
#         return
#     print(j)
#     fn(j-1,x)
# main()




# # Print even numbers from N to 1 
# def main():
#     n=int(input("enter n:"))
#     i=n
#     fn(i,n)
# def fn(j,x):
#     if j<1:
#         return
#     if j%2==0:
#         print(j)
#     fn(j-1,x)
# main()



# # Find the sum of numbers from 1 to N using a recursive parameter
# def main():
#     i=1
#     n=int(input("enter n:"))
#     fn(i,n)
# def fn(j,x,sum=0):
#     if j>x:
#         print(sum)
#         return
#     fn(j+1,x,sum+j)
# main()




# # Find the sum of numbers from 1 to N using back tracking 
def main():
    n=int(input("enter n:"))
    print(fn(n))
def fn(x):
    if x==0:
        return 0
    result=fn(x-1)
    result=result+x
    return result
main()