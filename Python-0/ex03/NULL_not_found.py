def NULL_not_found(object: any) -> int:
    ft_type = type(object)
    if object is None:
        print("Nothing :", object, ft_type)
    elif ft_type == float and object != object:
        print("Cheese :", object, ft_type)
    elif ft_type == int and object == 0:
        print("Zero :", object, ft_type)
    elif ft_type == str and object == '':
        print("Empty :", object, ft_type)
    elif ft_type == bool and object is False:
        print("Fake :", object, ft_type)
    else:
        print("Type not found")
        return 1
    return 0
