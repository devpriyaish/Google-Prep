def solve_magical_cows(input_data):
    """
    Solves the Magical Cows problem.
    
    :param input_data: A list of strings representing input lines.
    :return: A list of integers representing the results for each query.
    """
    # Parse the first line for the problem parameters
    max_cows, num_initial_farms, num_queries = map(int, input_data[0].split())
    
    # Initialize the DP table (list of lists)
    dp = [[0] * (max_cows + 1) for _ in range(51)]
    
    # Populate the initial farm sizes into day 0 of the DP table
    for i in range(1, num_initial_farms + 1):
        farm_size = int(input_data[i])
        dp[0][farm_size] += 1

    # Fill the DP table for each day
    for day in range(50):
        for cows in range(1, max_cows + 1):
            if cows * 2 <= max_cows:
                dp[day + 1][cows * 2] += dp[day][cows]
            else:
                dp[day + 1][cows] += 2 * dp[day][cows]

    # Answer the queries
    queries = map(int, input_data[num_initial_farms + 1:])
    results = [sum(dp[day]) for day in queries]
    
    return results


# Example input
input_data = [
    "2 5 3",   # max_cows=2, num_initial_farms=5, num_queries=3
    "1",       # Farm sizes
    "2",
    "1",
    "2",
    "1",
    "0",       # Query for day 0
    "1",       # Query for day 1
    "2"        # Query for day 2
]

# Get the results
output = solve_magical_cows(input_data)

# Print the results
print("\n".join(map(str, output)))

# Expected output
# 5
# 7
# 14
