# Function to compute binomial coefficients using dynamic programming
def binomial_coefficient(n, k):
    # Create a 2D table to store binomial coefficients
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    # Calculate value of binomial coefficients using bottom-up DP
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base case: C(n, 0) = C(n, n) = 1
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                # Recursive relation: C(n, k) = C(n-1, k-1) + C(n-1, k)
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    # Return the result: C(n, k)
    return dp[n][k]


n = 5  # Total number of items
k = 2  # Number of items to choose
    
# Call the function to compute binomial coefficient C(n, k)
result = binomial_coefficient(n, k)
    
print(f"Binomial Coefficient C({n}, {k}) is: {result}")
