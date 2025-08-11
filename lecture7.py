        #file i/o

# f = open('F:\\imp docs\\python\\azmath\\sample.txt' , 'w')
# demo = f.write('\n i am a new programmer')
# print (demo)

#r = read mode
#r+ = read and overwrite
#w = overwrite
#a = append
#a+ = append and write

    #with syntax
#eg 1
# with open('F:\\imp docs\\python\\azmath\\newfile.txt' , 'r') as f:
#     data = f.readline()
#     line = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()
#     print(data,line,line2,line3)


        #deleting a file
# import os
# os.remove("F:\\imp docs\\python\\azmath\\sample.txt")


    #practice 1 nad 2
# with open('F:\\imp docs\\python\\azmath\\practice.txt' , 'r+') as f:
#     data = f.read()

# new_data = data.replace("java","python")
# print(new_data)

# with open('F:\\imp docs\\python\\azmath\\practice.txt' , 'r') as f :
#      f.write(new_data)

    #q3
# with open('F:\\imp docs\\python\\azmath\\practice.txt' , 'r') as f:
#     data = f.read()
#     if (data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

