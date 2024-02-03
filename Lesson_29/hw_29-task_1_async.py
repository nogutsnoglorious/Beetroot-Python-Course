import asyncio

async def async_fibonacci(n):
    if n <= 1:
        return n
    else:
        return await async_fibonacci(n-1) + await async_fibonacci(n-2)

async def async_factorial(n):
    if n == 0:
        return 1
    else:
        return n * await async_factorial(n-1)

async def async_square(n):
    return n * n

async def async_cube(n):
    return n * n * n

async def main():
    numbers = range(1, 11)
    tasks = []
    for number in numbers:
        tasks.append(async_fibonacci(number))
        tasks.append(async_factorial(number))
        tasks.append(async_square(number))
        tasks.append(async_cube(number))
    
    results = await asyncio.gather(*tasks)
    fibs, facts, squares, cubes = results[::4], results[1::4], results[2::4], results[3::4]
    print("Fibonacci:", fibs)
    print("Factorial:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)

if __name__ == "__main__":
    import time
    start_time = time.time()
    asyncio.run(main())
    async_duration = time.time() - start_time
    print(f"Async execution time: {async_duration} seconds")
