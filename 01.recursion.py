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