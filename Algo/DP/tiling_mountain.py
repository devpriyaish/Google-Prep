MOD = 1000000007

def solve(W, H, N):
    # Minimum ribbon square calculation
    ribbon_square = min(N, W*H)
    # Calculate plains
    plains = (ribbon_square // W) + 1
    # Return the result
    return ((f(1, ribbon_square, W, H) - plains) + MOD) % MOD

def f(w, ribbon, W, H, dp=None):
    if ribbon < 0: 
        return 0
    if w > W: 
        return 1
    if dp is None:
        dp = [[None] * (ribbon + 1) for _ in range(W + 1)]
    if dp[w][ribbon] is not None: 
        return dp[w][ribbon]
    
    scenes = 0
    for length in range(H + 1):  # Include H as valid length
        scenes = (scenes + f(w + 1, ribbon - length, W, H, dp)) 
    
    dp[w][ribbon] = scenes
    return scenes % MOD

# Example usage
if __name__ == "__main__":
    W, H, N = 3, 2, 6
    print(solve(W, H, N))  # Replace with actual inputs

# Expected Output
24
