# Python Asynchronous Comprehension Project

This project is about Python's asynchronous comprehension. It covers how to write an asynchronous generator, how to use async comprehensions, and how to type-annotate generators.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators



## Tasks

1. **Async Generator**: Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

2. **Async Comprehensions**: Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

3. **Run time for four parallel comprehensions**: Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.

## Author

[salihabrik](https://github.com/salihabrik)