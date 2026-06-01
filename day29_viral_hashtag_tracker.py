from collections import Counter
import heapq
import time

hashtags = [
    "#AI", "#Python", "#AI", "#Coding",
    "#Python", "#AI", "#DataScience",
    "#Coding", "#Python", "#Python",
    "#ML", "#AI", "#ML", "#AI"
]

k = 3

# Approach 1: Sorting
def top_k_sorting(tags, k):

    freq = {}

    for tag in tags:
        freq[tag] = freq.get(tag, 0) + 1

    sorted_tags = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_tags[:k]


# Approach 2: Heap
def top_k_heap(tags, k):

    freq = Counter(tags)

    return heapq.nlargest(
        k,
        freq.items(),
        key=lambda x: x[1]
    )


# Sorting Approach Timing
start = time.time()

sorting_result = top_k_sorting(
    hashtags,
    k
)

end = time.time()

print("Top K Hashtags (Sorting):")
print(sorting_result)

print(
    "Execution Time:",
    end - start,
    "seconds"
)

# Heap Approach Timing
start = time.time()

heap_result = top_k_heap(
    hashtags,
    k
)

end = time.time()

print("\nTop K Hashtags (Heap):")
print(heap_result)

print(
    "Execution Time:",
    end - start,
    "seconds"
)