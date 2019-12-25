from inspect import signature

def provide(**provided_kwargs):
    
    """
    Purpose :
        Its the decorator that provides the decorated  function with all keyword argument
        
    Input Parameters:
        provided_kwargs : keyword argument
        
    Return Value:
        Decorated function
        
    """
    
    def decorator(fun):
        def decorated(*args,**kwargs): 
            
            fun_args = {} 
            
            # Fetch the function argument list
            # Update the fun_args with decorator keyword arguments            
            for i in provided_kwargs.keys():
                function_arguments = signature(fun).parameters.keys()
                if i in function_arguments or "kwargs" in function_arguments:
                    fun_args.update({i:provided_kwargs[i]})
                    
            # Update the fun_args with decorated keyword arguments            
            fun_args.update(kwargs)            
            
            return fun(*args, **fun_args)
        return decorated
    return decorator    

@provide()
def add(a,b):
    print(a+b)
    
add(1,2)
