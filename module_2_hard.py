def generate_password(n):
    result = ''
    for i in range(1, 21):
        for j in range(i + 1, 21):
            sum_pair = i + j
            if n % sum_pair == 0:
                result += str(i) + str(j)
    return result
n = int(input('Введите число (от 3 до 20): '))
if 3 <= n <= 20:
    password = generate_password(n)
    print('Нужный пароль: ', password)
else:
    print('Число должно быть от 3 до 20. ')