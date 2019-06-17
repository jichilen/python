def gen_fib(num):
    if num == 1:return 0
    if num == 2:return 1
    cal = 2
    a = 0
    b = 1
    while cal < num:
        b, a = a + b, b
        cal += 1
        yield b

def frog_jump(n):
    fib = gen_fib(n+2)
    for i in fib:
        continue
    return i

if __name__ == '__main__':
    n = 10
    fib = gen_fib(n)
    for i in fib:
        continue
    print(i)
    print(frog_jump(1))
    print(frog_jump(2))
    print(frog_jump(3))
    print(frog_jump(4))
    print(frog_jump(100))
