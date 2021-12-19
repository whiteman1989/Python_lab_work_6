n = 1 #number in group

def gen_cubes(n):
    for i in range(n):
        yield i ** 3

print("Робота генератора на серії із 1 елемента: ", [i for i in gen_cubes(1)])
print("Робота генератора на серії з 10 елементів:", [i for i in gen_cubes(10)])