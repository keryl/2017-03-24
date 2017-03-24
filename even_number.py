def is_even_num(l):
    even_number = []
    for n in l:
        if n % 2 == 0:
            even_number.append(n)
    return even_number
