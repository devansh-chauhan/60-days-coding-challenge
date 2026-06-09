def find_content_children(greed, cookies):
    greed.sort()
    cookies.sort()

    child = 0
    cookie = 0
    while child < len(greed) and cookie < len(cookies):
        if cookies[cookie] >= greed[child]:
            child += 1

        cookie += 1

    return child

greed_factors = [1, 2, 3]
cookie_sizes = [1, 1]

result = find_content_children(
    greed_factors,
    cookie_sizes
)

print("Greed Factors:", greed_factors)
print("Cookie Sizes:", cookie_sizes)
print("\nHappy Children:", result)