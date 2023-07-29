

def palindrome():
    while True:
        s1 = input('Введите строку ')
        s2 = s1[::-1]
        if s1 == s2:
            print('True')
        else:
            print('False')

palindrome()
