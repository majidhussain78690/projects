    #functions

#eg 1
# def sum_num(a , b):
#     sum = a + b
#     print(sum)
#     return sum

# sum_num(2,8)
# sum_num(16,25)
# sum_num(24,46)


#eg 2
# def average(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# average (20,35,40)


 #q1
# names = [1,2,3,4,5]

# def length():
#     list_len = len(names)
#     print(list_len)
#     return(list_len)

# length()

#q2

# def element():
#     print(names)

# element()

#q3
# n =5
# def fect(n):
#     fect = 1
#     for i in range(1,n+1):
#         fect *= i
#     print(fect)

# fect(5)

#q4
# n = int(input("enter a value to finds its INR TO USD value :"))
# def inr(n):
#     inr_val = n * 83
#     print(n, "USD =" , inr_val , "INR" )
#     return(inr_val)

# inr(n) 


    #recursion
# eg 1
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show (n - 1)
# show(5)

#q5
# def fact(n):
#     if (n == 0 or n ==1):
#         return 1
#     else:
#         return n * fact(n - 1)

# print(fact(4))

#q6
# def sum(n):
#     if (n == 0):
#         return 0
#     return sum(n-1) + n

# print_sun = sum (10)
# print(print_sun)
    
#q7
def print_list(list , idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx + 1)

fruits = ["apple" , "mang0" , "banana" , "kiwi"]

print_list(fruits)
