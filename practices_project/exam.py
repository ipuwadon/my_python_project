print("Python" + "Code")

ls = ["a", 1, "b", 2]
print(ls)
ls.remove("b")
print(ls)

ls2 = ["a", 1, "b", 2]
print(ls)
ls2.pop(3)
print(ls2)

ls3 = ["a", 1, "b", 2]
print(ls3)
del ls3[:]
print(ls3)

print('Python' *3 + ' is fund')

sampleSet = {"Jodi", "Eric", "Garry"}
#sampleSet.add("Vicki")
sampleSet.add("Nicky")
print(sampleSet)

print(3 * "Abc")

print(10 % 3)
print(3 % 10)

_my_vari = "sting"
#2myVariable = 'string'
myVariable = "str"

result = True and False
print(result)

my_tuple = (1, 2, 'c', 'd', 'f', 6)
print(my_tuple)
print(my_tuple[2])

for i in range(5):
    print(i)
else:
    print("this is else block")

sampleList = ["A", "B", "C"]
#sampleList.append(2, "Z")
sampleList.append("Z")
print(sampleList)

salary = 8000

def printSalary():
    salary = 12000
    print("Salary:", salary)

printSalary()
print("Salary:", salary)

for i in range(10, 15, 1):
    print(i, end=', ')

p, q, r = 10, 20, 30
print(p, q, r)

str_v = "pynative"
print(str_v[0:3])

print(5 ** 2)

def calculation(num1, num2=4):
    res = num1 * num2
    print(res)

calculation(5, 6)

print(5 ** 3)

print("James" * 2 * 3)

print(type([]))

a = [1, 2, 3]
b = a
b.append(4)
print(a)
c = a.copy()
c.append(5)
print(a)
print(c)

#for x in range(0.5, 5.5, 0.5):
#  print(x)

#my-var = 1
#print(my-var)

num = int(5)
print(num)
var_float = float(2.8)
print(var_float)
print(type(num))

var_str = "Hello"[0]
print(var_str)

var_str = " Hello "
print(var_str.strip())
print(var_str.upper())
print(var_str.replace("H", "B"))

if var_float == var_str:
    print("Same")
else:
    print("Not Same")

print(4 % 2)
print(int(4**0.5)+1)
for i in range(2, 3):
    print(i)

x = 5
x += 3
print(x)

def is_perfect(n: int) -> bool:
    divisors = [i for i in range(1, n) if n % i == 0]

    #for x in range(1, n):
    #    print(n, x, float(n % x))

    if sum(divisors) == n:
        return True
    return False

print("is_perfect ", is_perfect(28))

def find_perfect():
    for x in range(1, 100):
        rs = is_perfect(x)
        if rs:
            print(f"{x} is Perfect number")

find_perfect()

# Prime number
numbers = [2,3,4,5,6,7,8,9,10]
rs = [n for n in numbers if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print(rs)

num = 153
digits = str(num)
power = len(digits)
total = sum(int(d) ** power for d in digits)
print(total)