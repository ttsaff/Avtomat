lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

def filter_add_num(num):
    if(num % 3 == 0 and num < 30):
        return True
    else:
        return False

filter_add = filter(filter_add_num, lst)

print("Отфильтрованный список: ", list(filter_add))