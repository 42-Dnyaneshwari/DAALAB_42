def coin_change_ways(coins, total):
    # Create a table to store the number of ways to make change for each value from 0 to total
    dp = [0] * (total + 1)
    
    # There is 1 way to make change for 0 (no coins)
    dp[0] = 1
    
    # Iterate through each coin type
    for coin in coins:
        # For each coin, iterate through the possible values from coin to total
        for i in range(coin, total + 1):
            # For each value i, update the number of ways to make change
            dp[i] += dp[i - coin]
    
    return dp[total]

# Example usage
coins = [1, 2, 3]
total = 4

result = coin_change_ways(coins, total)
print(result)  # Output: 4
