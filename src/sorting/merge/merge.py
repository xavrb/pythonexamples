import random
import itertools
def crop(list_to_crop):
    a = []
    b = []
    for x in range(len(list_to_crop)):
        if x<(len(list_to_crop)/2):
            a.append(list_to_crop[x])
        else:
            b.append(list_to_crop[x]) 
    print("CROPPED:")
    print(a,b)
    return a,b

def merge_sort(toArrange):
    c = []
    d = []
    if len(toArrange)==1:
        return toArrange
    a,b = crop(toArrange)
    c = merge_sort(a)
    d = merge_sort(b)
    print("MERGE_SORT")
    print(c,d)
    return merge(c,d)
    
    
    
def merge(a,b):
    l = []
    if len(a)==1 and len(b)==1:
        if a[0]>b[0]:
            l.append(b)
            l.append(a)
        else:
            l.append(a)
            l.append(b)
        return l
    else:
        
        m = list(itertools.chain.from_iterable(a))
        n = list(itertools.chain.from_iterable(b))
        if a[len(a)-1]<=b[0]:
            return a+b
        else:
            return b+a

        
    
    
    
    
random.seed()
toArrange = []
for x in range(5):
    toArrange.append(random.randint(0,100))
arranged = []
print(toArrange)
arranged = merge_sort(toArrange)
print("arranged")
print(arranged)
