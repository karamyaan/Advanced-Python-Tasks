"""This function negate all in elements,which are between 3 and 8 """

def negate(lst):
    return [-i if i >= 3 and i <= 8 else i for i in lst]
    
print(negate([1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ])) 