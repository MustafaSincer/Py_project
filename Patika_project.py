
def flatten(liste):
    flat_list = []
    for i in liste:
        if isinstance(i,list):
            flat_list += flatten(i)
        else :
            flat_list.append(i)
    return flat_list


a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

b = flatten(a)
b

def reversed_list(list_1):
    reversed = []
    for i in list_1:
        if isinstance(i,list):
            reversed.append(reversed_list(i))
        else:
            reversed.append(i)

    return reversed[::-1]

k = [[1, 2], [3, 4], [5, 6, 7]]

j = reversed_list(k)
print(j)
