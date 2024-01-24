b = int(input("Введите желаемое число матрицы:"))

def test (a) :
    if a <= 0:
        print("Число слишком маленькое")
    else:
        matrix = [[0] * a for _ in range(a)]

        for row in matrix:
            print(row)
            
        test2(a)

def test2 (a) :
    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечентное число')

test(b)