words = ['this' , 'is', 'a', 'sentence', '.']
def reverse(iterable):
    x = list(iterable)
    
    begin = 0
    end = len(x)-1
    
    while begin < end:
        x[begin], x[end] = reverse(x[end]), reverse(x[begin])
        begin += 1
        end -= 1
    
    if isinstance(iterable, str):
        return "".join(x)
    
    return x

def twoPointers(alist):
    left = 0
    right = len(alist) - 1


    while left <= right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -=1


    return alist

print(words)
reverse_words = reverse(words)
reverse = twoPointers(words)
print(reverse)
print(reverse_words)