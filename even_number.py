def even_num(l):

    # first, we will ensure l is of type "list"

    if type(l) != list:
        return "argument passed is not a list of numbers"

    # secondly, check l is a list of numbers only

    for n in l:
        if not (type(n) == int or type(n) == float):
            return "some elements in your list are not numbers"

    # else find even numbers in it

    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
