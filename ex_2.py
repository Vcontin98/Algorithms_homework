a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def count(a_text):
    my_dict = {}
    word_list = a_text.split()
    for word in word_list:
        word = word.lower()
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return sorted(my_dict.items())

a = count(a_text) 

print(a)