def bool_range(x, y, z):
    return (x >= y and x <= z)

def check_range(x, y, z):
    if bool_range(x, y, z):
        return 'x jest między y a z'
    return 'x NIE jest między y a z'

def unique_list(list):
    unique_li = []    
    counter = -1
    for el in list:
        counter += 1        
        if (list[counter + 1 : len(list) : 1].count(el) > 0):
            continue        
        unique_li.append(el)
    return unique_li


my_list = [1,3,5,6,4,3,2,3,3,4,3,4,5,6,6,4,3,2,12,3,5,63,4,5,3,3,2]
#print(unique_list(my_list))
#print(list(set(my_list)))

def volume_of_sphere(radius):
    pi = 3.14
    return round(4 * pi * (radius**3) / 3, 2)

def num_fact(x):
    if (x == 0):
        return 1
    return x * num_fact(x - 1)