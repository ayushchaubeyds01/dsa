# count digit
# n=int(input("enter n:"))
# count=0
# for i in range(1,len(str(n))+1):
#     digit=n%10
#     count+=1
#     n//=10
# print(count)





# # reverse a number 
# n=int(input("Enter n:"))
# rev=0
# for i in range(1,len(str(n))+1):
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)




# palindrome
# n=int(input("Enter n:"))
# rev=0;temp=n
# for i in range(1,len(str(n))+1):
#     digit=temp%10
#     rev=rev*10+digit
#     temp//=10
# if rev==n:
#     print("palindrome")
# else:
#     print("not")






# # armstrong number
# n=int(input("Enter n:"))
# sum=0;temp=n;b=len(str(n))
# for i in range(1,len(str(n))+1):
#     digit=temp%10
#     sum+=digit**b
#     temp//=10
# if sum==n:
#     print("armstrong")
# else:
#     print("not")




# # divisors
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)




# # prime number
# n=int(input("enter n:"))
# if n<=1:
#     print("npt prime")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")




# # gcd/ hcf
# n=int(input("enter n:"))
# n2=int(input("enter n:"))
# for i in range(min(n,n2),0,-1):
#     if n%i==0 and n2%i==0:
#         print(i)
#         break

# euclidean algo
n=int(input("enter n:"))
n2=int(input("enter n2:"))
for i in range((n-n2),n2):
    if n%i==0 and n2%i==0:
        print(i)
        break