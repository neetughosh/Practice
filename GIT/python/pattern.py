def count_nbr_digits(number):
    
    """
    Purpose :
        Calculates the number of digits in a number 
        
    Input Parameters:
        number : The number whose number of digits has to be calculated
        
    Return Value:
        Returns number of digits in a given number
        
    """
    # Converts the number into a string and calculates the size of the number string
    return len(str(number))

def print_top_bottom_edges(nbr_cell_row, nbr_each_cell_edges):
    
    """
    Purpose :
        Prints the top and bottom edges of the cell 
        
    Input Parameters:
        nbr_cell_row : Number of cells in a row
        nbr_each_cell_edges : The number of "-" needed to form a top/bottom edge of a cell
        
    Return Value:
        None
        
    """
    
    # Forms the top/bottom of a single cell
    string = "+" + "-" * nbr_each_cell_edges
    
    # Prints the edges for each cell in a row
    print(string * nbr_cell_row + "+")
    

def solution(A, K):
    
    """
    Purpose :
        Prints the format mentioned in the question 2 
        
    Input Parameters:
        A : Array of numbers to be printed in a particular format mentioned in the question 2
        K : The number of cells a row should have
            but if number of elements is less than K then K is Number of elements
        
    Return Value:
        None
        
    """
    
    # Number of "-" needed to form a top/bottom edge of a cell
    nbr_each_cell_edges = count_nbr_digits(max(A))    
    
    # Length of the array
    len_arr = len(A)
    
    # Array index(of A)
    array_index = 0
    
    # Finds the value number of cells in a row
    if len_arr < K:
        nbr_cell_row = len_arr
    else:
        nbr_cell_row = K
    
    # Prints the top and bottom edges of the cell
    print_top_bottom_edges(nbr_cell_row, nbr_each_cell_edges)
    
    # Loop to print the format mentioned in question 2 
    while(len_arr > 0):        
        
        if len_arr < K:
            nbr_cell_row = len_arr
            
        # Prints the contents of the cell along with left and right edges
        for i in range(nbr_cell_row):
            nbr_space = nbr_each_cell_edges - count_nbr_digits(A[array_index])
            string = "|" + " "*(nbr_space) + str(A[array_index])
            print(string, end = "")
            array_index += 1
        print("|")
            
        # Prints the top and bottom edges of the cell
        print_top_bottom_edges(nbr_cell_row, nbr_each_cell_edges)          
        
        len_arr -= K        
         
    
solution([4,35,80, 123, 12345, 44, 8, 5, 24, 3, 1], 3)        


