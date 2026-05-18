import time
import random

agent_ids = list(range(1000000))
agent_ids.append(999999)

random.shuffle(agent_ids)

# Brute Force Duplicate Detection
# Time Complexity: O(n²)

def brute_force_duplicate(ids):

    for i in range(len(ids)):

        for j in range(i + 1, len(ids)):

            if ids[i] == ids[j]:
                return True

    return False


# Optimized Duplicate Detection Using Sets
# Time Complexity: O(n)

def optimized_duplicate(ids):

    seen = set()

    for id in ids:

        if id in seen:
            return True

        seen.add(id)

    return False


start = time.time()

optimized_result = optimized_duplicate(agent_ids)

end = time.time()

print("Optimized Solution:")
print("Duplicate Found:", optimized_result)
print("Execution Time:", end - start, "seconds")



small_ids = [1, 2, 3, 4, 5, 3]

start = time.time()

brute_result = brute_force_duplicate(small_ids)

end = time.time()

print("\nBrute Force Solution:")
print("Duplicate Found:", brute_result)
print("Execution Time:", end - start, "seconds")
