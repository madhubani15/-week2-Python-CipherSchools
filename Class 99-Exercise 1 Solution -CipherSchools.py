def sqaure_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

# list,str
numbers = list(range(1,11))
print(sqaure_list(numbers))
