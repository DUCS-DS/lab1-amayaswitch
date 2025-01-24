# lab 1 
# Amaya Switch 
def find_max(lst):
    """return the maximum element"""

    current_max = lst[0]
    
    for num in lst:
        if num > current_max:
            current_max = num


    return current_max    

test_list = [2112*i % 2024 for i in range(10000)]

print(find_max(test_list))

