import asyncio # asyncio is a library to write concurrent code using the async/await syntax.

async def my_coroutine():
	print("Coroutine Started")
	await asyncio.sleep(1)
	print("Coroutine Ended")

async def main():
	print("Main started")
	await asyncio.gather(my_coroutine()) # gather() is a helper function that wraps a list of awaitables into a single awaitable.
	print("Main ended")

# The asyncio.run() function to run the main() coroutine and automatically close the event loop when the coroutine is done.
asyncio.run(main())