num = [10,23,45,70,11,15,-20,2.4]

# If number is not present return -1

def linearSearch(a_list, target):
    
    for i in a_list:
        if i == target:
            return a_list.index(i)

target = input("Test: ") 
target = float(target)
test = linearSearch(num, target)
print(test)
