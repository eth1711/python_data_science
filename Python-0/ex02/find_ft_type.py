def all_thing_is_obj(object: any) -> int:
	if type(object) == int or type(object) == float:
		print("Type not found")
	elif type(object) == str:
		print("Brian is in the kitchen :", str)
	elif type(object) == tuple or type(object) == dict or type(object) == list or type(object) == set:
		print((str.capitalize(type(object).__name__)), ":", type(object))
	return 42