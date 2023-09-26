import asyncio # asyncio is a library to write concurrent code using the async/await syntax.
import random # random is a library to generate random numbers.

# This function is a coroutine that sleeps for one second and then prints a message.
async def first_coroutine():
	print("First Coroutine Started")
	await asyncio.sleep(random.randint(1, 5))
	print("First Coroutine Ended")

# This function is a coroutine that sleeps for one second and then prints a message.
async def second_coroutine():
	print("Second Coroutine Started")
	await asyncio.sleep(random.randint(1, 5))
	print("Second Coroutine Ended")

# This function is a coroutine that prints a message, creates two tasks from the coroutines above, and then prints another message.
async def main():
	print("Main started")
	task1 = asyncio.create_task(first_coroutine())
	task2 = asyncio.create_task(second_coroutine())
	await asyncio.gather(task1, task2)
	print("Main Resumed")

if __name__ == "__main__":
	event_loop = asyncio.get_event_loop()
	event_loop.run_until_complete(main())