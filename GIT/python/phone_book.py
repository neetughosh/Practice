def solution(phone_numbers, phone_owners, number):
    
    """
    Purpose :
        Returns the name of the phone owner if present in the phone book else returns the phone number itself 
        
    Input Parameters:
        phone_numbers : The list of phone number in the phonebook
        phone_owners : The list of phone owners in the phonebook
        number : The phone number which has to be checked whether it is present in phonebook
        
    Return Value:
        Returns the name of the phone owner if present in the phone book else returns the phone number itself 
        
    """
    
    # Creating the phonebook dictinary with key as phone numbers and value as phone owner name
    phonebook_detail = {phone_numbers[i]:phone_owners[i] for i in range(len(phone_owners))}
        
    # Evaluating whether the phone number exists in phonebook dictionary
    # Returns name of phone owner if present in dictionary else returns the phone number itself
    if number in phonebook_detail.keys():
        return phonebook_detail[number]
    else:
        return number
    
print(solution([1,2,3,4,5], ["a","b", "c"], 6))
print(solution([1,2,3,4,5], ["a","b", "c"], 5) ) 
print(solution([1,2,3], ["a","b", "c"], 2) )   
        
