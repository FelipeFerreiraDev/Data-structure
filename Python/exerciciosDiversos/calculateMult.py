# <----------------------------------- 1 ----------------------------------->
# Crie uma função que soma todos os argumentos não noemados
def soma(*args):
    print(*args)
    result = sum(args)
    return result

print(soma(1,2,3,4,5))

# <----------------------------------- 2 ----------------------------------->
# Crie uma função que soma todos os argumentos não noemados
def mult(*args):
    print(*args)
    total = 1
    for x in args:
        total *= x
    return total

print(mult(1,2,3))

# <----------------------------------- 3 ----------------------------------->
# Crie uma função para falar se um número é par ou impar
def checkIsPair(x):
    return x % 2 == 0

print(checkIsPair(2))