#!/usr/bin/python3

def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_n ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_n + 1, start):
                sieve[multiple] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    def game_winner(n):
        prime_moves = 0
        is_prime = sieve[:n + 1]
        for p in primes:
            if p > n:
                break
            if is_prime[p]:
                prime_moves = prime_moves + 1
                for multiple in range(p, n + 1, p):
                    is_prime[multiple] = False
        return prime_moves % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if game_winner(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    # Example usage
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))
