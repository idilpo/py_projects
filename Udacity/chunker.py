# If you have an iterable that is too large to fit in memory in full being able to take and use chunks of it at a time can be
# very valuable. Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.


def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
