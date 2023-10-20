def func(x, y):
    print("Run", x, y)
    return x*y, x/y

func(2, 5)

def mother(n):
    def child(m):
        return n*2 + m*3
    return child

# Use the function mother 
child_2 = mother(2)(3)
child_3 = mother(3)(2)

print(child_2)
print(child_3)


def do_sum(*args, **kwargs):
    s = sum(args) + sum(kwargs.values())
    return s

print(f"Sum = {do_sum(1, 2, 3, 4, 6, a = 1, b = 5)}")


x = 'Sekou'
def name_func(name):
    global x
    x = name
print(x)
print("changed")
name_func("Mamadou")
print(x)


try:
    x = 34/0
except Exception as e:
    print(e)
else:
    print(x)
finally:
    print("END")

X = [2, 5, 3]
carre = lambda x: x*2
my_list = [carre(x) for x in X]
print(my_list)

    
# raise excepiton in python 
raise Exception ('Yes')

