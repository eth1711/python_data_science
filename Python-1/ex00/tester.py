from give_bmi import give_bmi, apply_limit

height = [4, 4.1]
weight = [165.3, 160.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
