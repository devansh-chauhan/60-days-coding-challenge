gems = ["Ruby", "Emerald", "Diamond"]
all_combinations = []

def generate_subsets(index, current_subset):
    if index == len(gems):
        
        all_combinations.append(current_subset[:])
        return

    current_subset.append(gems[index])

    generate_subsets(index + 1, current_subset)

    current_subset.pop()

    generate_subsets(index + 1, current_subset)


generate_subsets(0, [])

print("All Possible Gem Combinations:\n")

for combination in all_combinations:
    print(combination)

print("\nTotal Combinations:", len(all_combinations))