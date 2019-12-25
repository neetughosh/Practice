# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")

def count_nbr_digits(number):
    count=0
    while(number>0):
        count=count+1
        number=number//10
    return count    

def solution(A, K):
    # write your code in Python 3.
    nbr_cell_edges = count_nbr_digits(max(A))
    
    if(len(A)<K):
        nbr_of_plus = len(A)+1
        n = len(A)+1
    else:
        nbr_of_plus = K+1
        n = K+1
        
    len_arr = len(A)
    print("len_arr"+ str(len_arr))
    arr_count = 0
    
    while (len_arr-1):
            
        
        for i in range(nbr_of_plus-1):
            print("+", end ="")
            for j in range(nbr_cell_edges):
                print("-", end ="") 
        print("+", end ="")
        print("")
#        if(len_arr< nbr_of_plus -1):
#            nbr_of_plus = len_arr 
        
        for i in range(nbr_of_plus-1):
            print("|" , end ="")
            print("n="+str(n))
            print("len===="+str(len_arr))
            nbr_space = nbr_cell_edges-count_nbr_digits(A[arr_count])
#            if(len_arr > n -1):
#                nbr_space = nbr_cell_edges-count_nbr_digits(A[arr_count])
#                print(" "*nbr_space + str(A[arr_count]), end ="")
#            else:
#                nbr_space = nbr_cell_edges
#                print(" "*nbr_space, end ="")
                
            arr_count += 1 
        print("|" , end ="")  
        print("") 
#        len_arr = len_arr-(nbr_of_plus-1)
        
#        if(len_arr > nbr!_of_plus):
        len_arr = len_arr-(nbr_of_plus-1)
        print("len"+str(len_arr))    
            
            
            
    for i in range(nbr_of_plus-1):
        print("+", end ="")
        for j in range(nbr_cell_edges):
            print("-", end ="") 
    print("+", end ="")    
        
solution([4,35,80, 123, 12345, 44, 8, 5, 24, 3], 4)        


