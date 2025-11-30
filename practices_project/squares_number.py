squares = [x**2 for x in range(1, 21) if x % 2 ==0]
print(squares)

for index, value in enumerate(squares):
    print(f"index = {index}, value = {value}")