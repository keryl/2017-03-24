def even_num(l):

    # first, we will ensure l is of type "list"
    if type(l) != list:
        return "argument passed is not a list of numbers"

    # else l is a list so find even numbers in it

    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
