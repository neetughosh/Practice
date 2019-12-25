#python

"""
This is a shape class to have shape related functionalities
"""
class shapes(object):
    
    def __init__(self):
        pass
        
    """
    This function reads the file containing the polygon sides info
    """
    def read_Text_File(self, file_Path):
        text = []
        with open(file_Path, 'r') as read:
            text = "".join(read.readlines())
            text = [ [int(each_val) for each_val in val.split(",")] for val in text.splitlines()]
        return text

    """
    This function reads checks whether the polygon sides form a triangle
    """
    def checkTriangle(self, data) :
        if len(data) != 3 :
            return False
    
        if (((data[0] + data[2]) > data[1]) and ((data[0] + data[1]) > data[2]) and ((data[0] + data[1]) > data[2])) :
            return True
        else :
            return False
    
    """
    This function reads checks whether the polygon sides form a square
    """
    def checkSquare(self, data) :
        if (len(data) != 4) :
            return False
    
        if (sum(data)/4 == data[0]):
            return True
        else:
            return False
        """
    This function reads checks whether the polygon sides form a rectangle
    """
    def checkRectangle(self, data) :
        if (len(data) != 4) :
            return False
    
        if (len(set(data)) == 2):
            return True
        else :
            return False

# create shapes object
find_shape = shapes()
polygons = find_shape.read_Text_File('polygons.txt')
(triangles, squares, rectangles, others, union) = ([], [], [], [], [])


# loop over all the polygons
for i in range(len(polygons)):
    data = polygons[i]

    if (len(data) == 3) :
        result = find_shape.checkTriangle(data)
        if (result == True) :
            triangles.append(data)
        else:
            others.append(data)
    elif (len(data) == 4) :
        result = find_shape.checkSquare(data)
        if (result == True) :
            squares.append(data)
        elif (find_shape.checkRectangle(data) == True) :
            rectangles.append(data)
        else :
            others.append(data)
    else:
        others.append(data)

union.append(triangles)
union.append(squares)
union.append(rectangles)
union.append(others)

print("Original polygons contents:", polygons)
print("Mutually exclusive sets:")
print("Triangles: " , triangles )
print("Squares: " , squares)
print("Rectangles: " , rectangles)
print("Others: " , others)
print("Union of all: " , union)
        
     
