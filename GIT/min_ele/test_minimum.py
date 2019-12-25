import operation
import pytest

def test_min_sample1():
    arr = [7,6,5,4,3,2,1]
    min_ele = 1
    assert operation.minimum(arr) == min_ele
    
def test_min_sample2():
    arr = [1,2,3,4,5,6,7,8]
    min_ele = 1
    assert operation.minimum(arr) == min_ele
    
def test_min_sample3():
    arr = [100,99,98,5,78,230]
    min_ele = 5
    assert operation.minimum(arr) == min_ele    

def test_min_sample4():
    arr = [10000000000000000000000000000000,1111111111111111111111111, -1, -0.00000000000000000001, -11111111111111111111777777777777777777777777777777777777777777777777777777777777777777]
    min_ele = -111111111111111111117777777777777777777777777777777777777777777777777777777777777777777
    assert operation.minimum(arr) != min_ele    
    
def test_min_sample5():
    arr = []        
    with pytest.raises(IndexError):
        operation.minimum(arr)
        
def test_min_sample6():
    with pytest.raises(TypeError):
        operation.minimum()        