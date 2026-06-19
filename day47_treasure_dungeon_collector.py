def greedy_rob(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 2
    return total

def house_robber(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(
            dp[i - 1],           
            dp[i - 2] + nums[i]  
        )

    return dp[-1]

treasure = [2, 7, 9, 3, 1]
print("Treasure Rooms:", treasure)
print("\nGreedy Result:", greedy_rob(treasure))
print("DP Result:", house_robber(treasure))