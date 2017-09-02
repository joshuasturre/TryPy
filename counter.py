def test(limit):
    if limit == 'quit':
        quit()
    from random import randint
    import time
    start_time = time.time()
    x = 2
    y = 0
    while y < int(limit):
        x = x * x
        y = y + 1
        print(y, len(str(x)), time.time() - start_time)
    print('Finished in', (time.time() - start_time))
while True:
    test(input('Limit (suggest 21):'))
