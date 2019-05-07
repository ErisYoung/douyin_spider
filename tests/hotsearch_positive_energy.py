
def func():
    a=4
    while True:

        for i in range(5):
            print(i)
            a -= 1
            if a==1:
                return
            yield a

if __name__ == '__main__':
    list_c=func()
    print(list(list_c))