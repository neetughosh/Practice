#python
       
def pattern(num_arr):
    """
    This function converts the pattern [2, 4, 6, 8, 9, 15] to [4, 16, 64]
    """

    # store the first number in a temp variable
    temp = num_arr[0]
    res_arr = []
    
    # apply pow(2*n, 2) if 2*n is present in the first array
    for val in sorted(a):
        if temp in a:
            res_arr.append(temp**2)
        temp = temp * 2
    return res_arr    

a =  [2, 4, 6, 8, 9, 15, 16, 64] #to [4, 16, 64]
print(pattern(a))


   

#javascript

#const numbers = [2, 4, 6, 8, 9, 15, 16, 64];
#
#// Expected result: [4, 16, 64]
#
#// Sorting numbers ascending.
#numbers.sort((n1, n2) => n1 > n2);
#
#const lastNbr = numbers[numbers.length - 1];
#
#const res = [];
#let number = numbers[0];
#while (number <= lastNbr) {
#  if (numbers.indexOf(number) !==-1) {
#    res.push(Math.pow(number, 2));
#  }
#  number *= 2;
#}
#
#console.log(res);





    

