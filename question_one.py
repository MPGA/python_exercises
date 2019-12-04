list_number = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

def Multiply_by_two(list_number):
    total = 0    
    for a in list_number:
         total= [a*2 for a in list_number]
    return total
    
print(Multiply_by_two(list_number))
