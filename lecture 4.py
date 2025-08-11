#dict

# names = {
#     "azmath" : 18,
#     "rehan"  : 16,
#     "mehreen" : 12,
# }

#nested dict
# student = {
#     "name" : "rehan hussain",
#     "subjects" : {
#         "phy" : 80,
#         "chem" : 75,
#         "math" : 90,
#     }
# }

# print(student["subjects"])
#         #dict methods
#dict_name.keys() = returns all keys
#dict_name.values() = returns all values
#dict_name.items() = returns all (key , value) pairs as tuples
#dict_name.get("key") = returns the key according to value
#dict_name.update({}) = inserts the specified item to the dict 

#sets = it is mutable also elements are immutable and unodered
# nums = {1,2,3,4,5,6,7,8}
#empty set =>  set = set{} 

#set ignores duplicate value
    #set method
# set_name.add(elements) = adds an element
# set_name.remove(element) = removes the element
# set_name.clear() = empties the set
# set_name.pop() = removes a random value
#set1.union(set 2) = combine both set values and returns new
#set1.intersection(set 2) = combines common values and returns new

# print(type(nums))

        #practice 1

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture" , "list of facts & figures"]
}

print(dictionary)

        #practice 2

classroom = {
    "python","java" , "c++" , "python" , "java" , "javascript" ,
    "java","pyhton","c++","c"
}

print(len(classroom))

        #practice 3

marks = {}

x = int(input("please enter phy marks : "))
marks.update({"phy" : x})

y = int(input("please enter chem marks : "))
marks.update({"chem" : y})

z = int(input("please enter math marks : "))
marks.update({"math" : x})

print(marks)

        #practice 4

answer = {
    ("float" , 9.0)
    ("int" , 9)
}

print(answer)