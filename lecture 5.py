            # while loops

#q1
# i = 1
# while i <=100:
#     print(i)
#     i +=1

#q2
# j =100
# while j >= 1:
#     print(j)
#     j -= 1

#q3
# n = int(input("please enter a number :"))
# k = 1
# while k <=10:
#     print(n , "*" , k ,"=" , n*k)
#     k += 1


#q4
# nums = [1,4,9,16,25,36,64,81,100]
# indx = 0
# while indx < len(nums)  :
#     print(nums [indx])
#     indx +=1


#q5
# num =  (1,4,9,16,25,36,64,81,100)
# x = int(input("enter a number to find its index : "))
# i = 0
# while i < len(num):
#     if(num[i] == x ):
#         print("found at idx" , i)
#     i += 1


#q6   continue method
# i = 0
# while i <= 5 :
#     if(i == 3):
#         i+=1
#         continue
#     print(i)
#     i +=1    
#to skip any number we use continue


            #for loops
# reason 1  == to print the list in serial vice we use for loops
# list = [1,3,5,7,9,11,13,15,17,19]

# for num in list:
#     print(num)


#q8 using for loop

# list =  [1,4,9,16,25,36,64,81,100]

# for num in list :
#     print (num)


#q9
# tup =  (1,4,9,16,25,36,64,81,100) 
# print(tup)
# x = int(input("choose a number listed above to find its index : "))
# idx = 0 
# for val in tup:
#     if(val == x):
#         print("num found on index" , idx)
#     idx += 1    


#range = it returns a list starting from 0 by default and increase by 1 (by default) and stops before a specified number
#range function => range(start(default by 0) , stop , step (default by 1))

# nums = range (10)
# for num in nums:
#     print(num)

#q10

# for num in range(1 ,101,1):
#     print(num)

#q11

# for num in range(100 , 0 , -1):
#     print(num)

n = int(input("enter a number for its multiplication table : "))

for num in range(1 ,11):
    print(n , "*" , num , "=" , n*num)