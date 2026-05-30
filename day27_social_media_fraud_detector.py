def detect_duplicate(posts, k):
    seen = {}

    for i in range(len(posts)):
       if posts[i] in seen:
            if i - seen[posts[i]] <= k:
                return True
            
            seen[posts[i]] = i

    return False

posts = [
    "Hello World",
    "AI is awesome",
    "Python",
    "Hello World",
    "Data Science",
    "Python"
]

k = 3

print("Social Media Events:")
print(posts)

if detect_duplicate(posts, k):
    print(f"\nFraud Alert: Duplicate content found within {k} posts.")
else:
    print(f"\nNo suspicious activity detected within {k} posts.")