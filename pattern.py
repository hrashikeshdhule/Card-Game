# row=int(input('row:'))
# col=int(input('col:'))

# for i in range(row):
#     for j in range(col):
#         print(j+1,end=' ')
#     print()
#o/p:-row:4
# col:3
# 1 2 3 
# 1 2 3 
# 1 2 3 
# 1 2 3 


# val=row
# for i in range(row):
#    for j in range(col):
#         print(val,end=' ')
#         val+=1
#    print()

#o/p:row:4
# col:3
# 4 5 6 
# 7 8 9 
# 10 11 12 
# 13 14 15 
  
   
# val=1
# for i in range(row):
    
#     for j in range(col):
#         print(val,end=' ')
        
#     print()
#     val+=1
# o/p:=row:4
# col:3
# 1 1 1 
# 2 2 2 
# 3 3 3 
# 4 4 4 

# val=65
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=' ')
#         val+=1
#     print()
# row:4
# col:3
# A B C 
# D E F 
# G H I 
# J K L 
    

# val=65
# for i in range(row):
    
#     for j in range(col):
#         print(chr(val),end=' ')
       
#     print()
#     val+=1
# row:4 
# col:3
# A A A 
# B B B 
# C C C 
# D D D  


# for i in range(row):
#     val=65
#     for j in range(col):
#         print(chr(val),end=' ')
#     print()
#     val+=1
# o/p:-row:4
# col:4
# A A A A 
# A A A A 
# A A A A 
# A A A A  



# for i in range(row):
#     val=65
#     for j in range(col):
#         print(chr(val),end=' ')
#         val+=1
#     print()
# row:4
# col:3
# A B C 
# A B C 
# A B C 
# A B C 


# val=1
# for i in range(row):
#     for j in range(col):
#         if i%2==0:
#             print(val,end=' ')
#         else:
#             print('*',end=' ')
        
#     print()
#     if i%2==0:
#         val+=1
# o/p:-
# row:4
# col:3
# 1 1 1 
# * * * 
# 2 2 2 
# * * * 
   

# val=1
# for i in range(row):
#     for j in range(col):
#         if j%2==0:
#             print(val,end=' ')
#             val+=1
#         else:
#             print('*',end=' ')
        
#     print()
# o/p:-
# row:4
# col:5
# 1 * 2 * 3 
# 4 * 5 * 6 
# 7 * 8 * 9 
# 10 * 11 * 12 


# val=1
# p=True
# for i in range(row):
#     for j in range(col):
#         if p:
#             print(val,end=' ')
#             val+=1
#             if val>9:
#                 val=1
#         else:
#             print('*',end=' ')
#         p=not p
#     print()
# o/p:-
# row:4
# col:5
# 1 * 2 * 3 
# * 4 * 5 * 
# 6 * 7 * 8 
# * 9 * 1 * 

# n=int(input("n:"))

# for i in range(n):
#     val=65
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=' ')
            
#         else:
#             print(' ',end=' ')
#     print()
#     val+=1
# o/p:-
# n:4
# A       
# A A     
# A A A   
# A A A A 

# n=int(input("n:"))
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print('*',end=' ')
            
#         else:
#             print(' ',end=' ')
#     print()
# o/p:-n:4
#       * 
#     *   
#   *     
# *       

# n=int(input("n:"))
# spc=n-1
# str=1
# for i in range(n):
#     for j in range(spc):
#        print(' ',end=' ')
#     for k in range(str):    
#         print('*',end=' ')
        
#     print()
#     spc-=1
#     str+=2 #pyramid
   

# n=int(input("n:"))

# for i in range(n):
#     for j in range(n-1-i):
#         print(' ',end=' ')
#     for k in range(n*i+1):
#         print('*',end=' ')
#     print() #pyramid

# n=int(input("n:"))
# spc=0
# str=2*n-1
# for i in range(n):
#     for j in range(spc):
#        print(' ',end=' ')
#     for k in range(str):    
#         print('*',end=' ')

#     print()
#     spc+=1
#     str-=2
#o/p:- n:4
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 



# n=int(input("n:"))
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(n-i)-1):
#         print('*',end=' ')
#     print()
#o/p:- n:4
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

# n=int(input('n:'))
# for i in range(n-1,-n,-1):
#     for j in range(n-abs(i)):
#         print('*',end=' ')
#     print()
#o/p:- n:4
# * 
# * * 
# * * * 
# * * * * 
# * * * 
# * * 
# * 

# n=int(input('n:'))
# for i in range(-n,n):
#     for j in range(abs(i)):
#         print(' ',end=' ')
#     for k in range(n-abs(i)):
#         print('*',end=' ')    
#     print()
#o/p:- n:4
#       * 
#     * * 
#   * * * 
# * * * * 
#   * * * 
#     * * 
#       * 

# n=int(input('n:'))
# for i in range(-n,n):
#     for j in range(n-abs(i)):
#         print('*',end=' ')
#     for k in range(2*abs(i)):
#         print(' ',end=' ')
#     for l in range(n-abs(i)):
#         print('*',end=' ')
#     print()
# n:4
# *             * 
# * *         * * 
# * * *     * * * 
# * * * * * * * * 
# * * *     * * * 
# * *         * * 
# *             * 

# n=int(input('n:'))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1 or i ==n//2 or j==n//2:
#             print('*',end=' ')
            
#         else:
#             print(' ',end=' ')
#     print()

# n=int(input('n:'))
# for i in range (n):
#     for j in range(2*n-1):
#         if i==0 or i+j==2*n-2 or i==j :            #i+j==n-1 or j-i==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()# Triangle

# n= int(input('n:'))
# for i in range(n):
#     for j in range (n):
#         if i==0 or i==n-1 or i==n//2 or j==0 and i<n//2 or j==n-1 and i>n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print() # S


# n= int(input('n:'))
# for i in range(n):
#     for j in range (n):
#         if i>=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# o/p:
# n:5
# *         
# * *       
# * * *     
# * * * *   
# * * * * *
 
    
# n= int(input('n:'))
# for i in range(n):
#     for j in range(n):
#         if j<n-i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# o/p:
# n:5
# * * * * * 
# * * * *   
# * * *     
# * *       
# *     

# n= int(input('n:'))
# for i in range(n):
#     for j in range(n):
#         if j>=n-i-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#o/p- n:5
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# n= int(input('n:'))
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or i==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#o/p:-n:5
# *         
# * *       
# *   *     
# *     *   
# * * * * *

# n= int(input('n:'))
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()#H


# How to check prime numbers:- 

# n= int(input())
# b=0
# for i in range(1,n+1):
#     if n%i==0:
#         b+=1
# if b==2:
#     print(f'{n} is a prime number')
# else:
#     print(f'{n} is not a prime number')
# print(b)


#How to check sum numbers:-
# n=int(input('n:'))
# res=0
# while n>0:
#     res+=n%10
#     n//=10
# print(res)

#Another method
# n=int(input('n:'))
# res=0
# for i in str(n):
#     res-=int(i)
# print(res)

# Multiple methods of finding prime numbers
# from math import*
# n=int(input('n:'))
# for n in range(2,n+1):
#     c=0
#     for i in range(2,int(sqrt(n))+1):
#         if n%i==0:
#             c+=1
#             break
#     if c==0:
#         print(n,end=' ')  #n=10:=2,3,5,7

# from math import*
# n=int(input('n:'))
# count=0
# val=2
# while True :
#     c=0
#     for i in range(2,int(sqrt(val))+1):
#         if val%i==0:
#             c+=1
#             break
#     if c==0:
#         print(val,end=' ')
#         count+=1
#     if count==n:
#         break
#     val+=1  #n:10=2,3,5,7,11,13,17,19,23,29

#Counting how many numbers:-
# n=int(input('n:'))
# n=abs(n)
# c=0
# while n>0:
#     c+=1
#     n//=10
# print(c) #n:1233:4


# Palindrome:-

# n=int(input('n:'))
# print(str(n)[::-1])

# n=int(input('n:'))
# rev=0
# temp=n
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n//=10
# if rev==temp:
#     print('Plaindrome')
# else:
#     print('Not a Palindrome')


# Armstrong no:-
# n=int(input('n:'))
# res=0
# temp=n
# p=len(str(n))
# while n>0:
#     rem=n%10
#     res+=rem**p
#     n//=10
# if temp==res:
#     print('Armstorm no')
# else:
#     print('Not Armstorm no')

# # Strong no:-
# n=int(input('n:'))
# res=0
# temp=n
# while n>0:
#     rem=n%10
#     fact=1
#     for i in range(1,rem+1):
#         fact*=1
#     res=fact
#     n//=10
# if temp==res:
#     print('Strong no')
# else:
#     print('Not a strong no')

# Perfect no:-
# n=int(input('n:'))
# res=0
# for i in range(1,n//2+1):
#     if n%i==0:
#         res+=i
# if res==n:
#     print('Perfect no')
# else:
#     print('Not a Perfect no')

#Disarium Number:
# n=int(input('n:'))
# p=len(str(n))
# temp=n
# res=0
# while n > 0:
#     res += (n % 10)**p
#     n//=10
#     p-=1
# if temp == res:
#     print("Disarium Number")
# else:
#     print("Not a Disarium Number")

#Abundant Number:-
# n=int(input('n:'))
# res=0
# for i in range(1,n):
#     if n%i==0:
#         res=res+i
# if res>n:
#     print('Abundant Number')
# else:
#     print('Not a Abundant Number')

# HCF(Highest commom factor):-
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# hcf=0
# m=min(a,b)
# for i in range(1,m+1):
#     if a%i==0 and b%i==0:
#         hcf=i
# print('HCF=',hcf) #HCF
# print(a*b//hcf) #LCM


#LCM:-
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# lcm=None
# m=max(a,b)
# while True:
#     if m % a == 0 and m % b == 0:
#         lcm=m
#         break
#     m+=1

# print("LCM =", lcm)


# How to find  LCM and counting numbers how many time it will multilply:-
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# lc=0
# lcm=None
# m=max(a,b)
# while True:
#     lc+=1
#     if m % a == 0 and m % b == 0:
#         lcm=m
#         break
#     m+=max(a,b)

# print("LCM =", lcm,lc)

# How to find binary numbers:-
# n=int(input('n:'))
# print(bin(n)[2:])

# n = int(input("Enter a number: "))

# binary = ""

# while n > 0:
#     remainder = n % 2
#     binary = str(remainder) + binary
#     n = n // 2

# print("Binary =", binary)

binary = input("Enter a binary number: ")

decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print("Decimal =", decimal)