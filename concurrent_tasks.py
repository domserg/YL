def gen1(n):
    for i in range(n):
        yield i


def gen2(s):
    for i in s:
        yield i


g1 = gen1(5)
g2 = gen2("Hello world")
tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
