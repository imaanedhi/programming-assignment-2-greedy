from collections import deque
import sys


def read_input(filename):
    with open(filename, "r") as f:
        parts = f.read().strip().split()

    k = int(parts[0])
    m = int(parts[1])
    requests = list(map(int, parts[2:]))

    if len(requests) != m:
        raise ValueError(f"Expected {m} requests, found {len(requests)}")

    return k, m, requests


def fifo_misses(k, requests):
    cache = set()
    order = deque()
    misses = 0

    for x in requests:
        if x in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.add(x)
            order.append(x)
        else:
            victim = order.popleft()
            cache.remove(victim)
            cache.add(x)
            order.append(x)

    return misses


def lru_misses(k, requests):
    cache = set()
    last_used = {}
    misses = 0

    for t, x in enumerate(requests):
        if x in cache:
            last_used[x] = t
            continue

        misses += 1

        if len(cache) < k:
            cache.add(x)
        else:
            victim = min(cache, key=lambda item: last_used[item])
            cache.remove(victim)
            del last_used[victim]
            cache.add(x)

        last_used[x] = t

    return misses


def optff_misses(k, requests):
    cache = set()
    misses = 0
    n = len(requests)

    for i, x in enumerate(requests):
        if x in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.add(x)
            continue

        victim = None
        farthest_next_use = -1

        for item in cache:
            next_use = float("inf")
            for j in range(i + 1, n):
                if requests[j] == item:
                    next_use = j
                    break

            if next_use > farthest_next_use:
                farthest_next_use = next_use
                victim = item

        cache.remove(victim)
        cache.add(x)

    return misses


def main():
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    k, m, requests = read_input(input_file)

    fifo = fifo_misses(k, requests)
    lru = lru_misses(k, requests)
    optff = optff_misses(k, requests)

    print(f"FIFO  : {fifo}")
    print(f"LRU   : {lru}")
    print(f"OPTFF : {optff}")


if __name__ == "__main__":
    main()