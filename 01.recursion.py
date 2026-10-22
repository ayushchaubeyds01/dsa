# # print name 5 times
# def main():
#     n=int(input("enter n:"))
#     i=1
#     fn(i,n)
# def fn(j,x):
#     if j>x:
#         return 
#     print("ayush")
#     fn(j+1,x)
# main()



# # print 1 to n
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



# # print n to 1
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



# # print 1 to n by backtracking 
# def main():
#     n=int(input("enter n:"))
#     i=n
#     fn(i,n)
# def fn(j,x):
#     if j<1:
#         return
#     fn(j-1,x)
#     print(j)
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


# parameterized recursion 

# # print sum of 1 to n 
# def main():
#     n=int(input("enter n:"))
#     fn(n)
# def fn(x,sum=0):
#     if x<1:
#         print(sum)
#         return
#     fn(x-1,sum+x)
# main()




# functional recursion
# we do not print the value we just handback the value 
# def main():
#     n=int(input("enter n :"))
#     print(fn(n))
# def fn(x):
#     if x==0:
#         return 0
#     return x+fn(x-1)
# main()



# # facctorial
# def main():
#     n=int(input("enter n:"))
#     print(fn(n))
# def fn(x):
#     if x==0 or x==1:
#         return 1
#     return x*fn(x-1)
# main()



# # reverse an array using 2 pointer method 
# def main():
#     n=[1,2,3,4,5]
#     start=0
#     end=len(n)-1
#     print(fn(n,start,end))
# def fn(x,y,z):
#     if y>=z:
#         return x
#     x[y],x[z]=x[z],x[y] 
#     return fn(x,y+1,z-1)
# main()




# # reverse the array using single pointer method
# def main():
#     n=[1,2,3,4,5]
#     i=0
#     fn(i,n)
#     print(n)
# def fn(x,y):
#     mid=len(y)//2
#     if x>=mid:
#         return
#     y[x],y[len(y)-x-1]=y[len(y)-x-1],y[x]
#     fn(x+1,y)
# main()




# # revrese a string and check for palindrome
# def main():
#     i=0
#     n=input("Emter n:")
#     print(fn(i,n))
# def fn(x,y):
#     mid=len(y)//2
#     if x>=mid:
#         return True
#     if y[x]!=y[len(y)-x-1]:
#         return False
#     return fn(x+1,y)
# main() 



# fibonacci series
# def main():
#     n=int(input("enter n:"))
#     print(fn(n))
# def fn(x):
#     if x<=1:
#         return x
#     return fn(x-1)+fn(x-2)
# main()



