import time
from datetime import datetime

cache = {}
cache_alive = {}


def cached(max_size=None, seconds=None):
    def cached_func(func):
        def wrapper(*args, **kwargs):
            if seconds:
                deleted = 0
                for i in range(0, len(cache_alive)):
                    if (datetime.now() - cache_alive[list(cache_alive.keys())[i-deleted]]).seconds > seconds and args in cache:
                        del cache_alive[args]
                        del cache[args]
                        deleted += 1

            if args:
                if args not in cache:
                    result = func(*args, **kwargs)
                    cache[args] = result
                    if seconds:
                        cache_alive[args] = datetime.now()
                    if max_size:
                        if len(cache) > max_size:
                            del cache[list(cache.keys())[0]]
                    return result
                else:
                    return cache[args]
            elif kwargs:
                if kwargs not in cache:
                    result = func(*args, **kwargs)
                    cache[kwargs] = result
                    if seconds:
                        cache_alive[args] = datetime.now()
                    if max_size:
                        if len(cache) == max_size:
                            del cache[cache.keys()[0]]
                    return result
                else:
                    return cache[kwargs]

        return wrapper

    return cached_func


@cached(max_size=2, seconds=2)
def slow_function(x):
       print(f"Вычисляю для {x}...")
       return x ** 2
# Первый вызов — вычисляется
print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(3))  # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(3))  # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
time.sleep(3)
print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4
print(slow_function(3))