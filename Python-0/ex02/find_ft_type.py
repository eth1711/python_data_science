def all_thing_is_obj(object: any) -> int:
    if type(object) is int or type(object) is float:
        print("Type not found")
    elif type(object) is str:
        print("Brian is in the kitchen :", str)
    elif type(object) is tuple or type(object) is dict or \
            type(object) is list or type(object) is set:
        print((str.capitalize(type(object).__name__)), ":", type(object))
    return 42
