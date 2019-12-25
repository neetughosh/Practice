# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")

def count_nbr_digits(number):
    return len(str(number))

def solution(A, K):
    nbr_cell_edges = count_nbr_digits(max(A))
    
    if(len(A)<K):
        nbr_of_plus = len(A)+1
    else:
        nbr_of_plus = K+1
        
    len_arr = len(A) 
    len_arr_type = len(A)
    arr_count = 0
    
    while (len_arr > 0):
        
        for i in range(nbr_of_plus-1):
            print("+", end ="")
            for j in range(nbr_cell_edges):
                print("-", end ="") 
        print("+", end ="")
        print("")
        for i in range(nbr_of_plus-1):
            print("|" , end ="")
            if(arr_count < len_arr_type):                
                nbr_space = nbr_cell_edges-count_nbr_digits(A[arr_count])
                print(" "*nbr_space + str(A[arr_count]), end ="")
            else:
                nbr_space = nbr_cell_edges
                print(" "*nbr_space, end ="")
            arr_count += 1 
        print("|" , end ="")  
        print("")        
        
        len_arr = len_arr-(nbr_of_plus-1)
    for i in range(nbr_of_plus-1):
        print("+", end ="")
        for j in range(nbr_cell_edges):
            print("-", end ="") 
    print("+", end ="")  
         
    
solution([4,35,80, 123, 12345, 44, 8, 5, 24, 3, 1], 4)        


