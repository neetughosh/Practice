import copy
list1 = []
def permute(a, l, r): 
    if l==r:
        list1.append(copy.deepcopy(a))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]  
            
string = "ABcd"
n = len(string) 
a = list(string) 
print(permute(a, 0, n-1)  )
print(list1)
print((len(list1)))
    

