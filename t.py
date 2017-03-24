def typeof(x):

    type_of_x = type(x)

    if type_of_x == str:
        return 'string'
    elif type_of_x == int or type_of_x == float:
        return 'number'
    elif type_of_x == list:
        return 'array'
    elif type_of_x == dict:
        return 'dict'
    else:
        return 'unknown'