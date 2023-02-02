def benchmark(func):
    from time import time
    def inner(*args):
        st = time()
        res = func(*args)
        et = time()
        print(f'Время выполнения {st-et}')
        return res
    return inner


@benchmark
def fetch_webpage(url):
    import requests
    return requests.get(url)



fetch_webpage('https://google.com')