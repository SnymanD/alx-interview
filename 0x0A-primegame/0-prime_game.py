#!/usr/bin/pytho3
"""prime game"""


PlayerID = int
PlayerName = str
prime_map: 'dict[int, bool]' = {}


def sieveOfEratosthenes(n):
    """Returns an array indicating prime status for numbers 1 to n (inclusive)."""
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def playRound(r, prime_map):
    """Simulates a round of the game and returns the winner (0 for Maria, 1 for Ben)."""
    player = 0  # Maria starts first
    number_range = list(range(1, r + 1))
    
    def switch(player):
        return 1 - player

    while True:
        prime = 0
        for n in number_range:
            if prime_map[n]:
                prime = n
                break
        
        if prime == 0:
            return switch(player)
        
        number_range = [n for n in number_range if n % prime != 0]
        player = switch(player)

def isWinner(x, nums):
    """Determines the overall winner after x rounds of the game."""
    player_names = ["Maria", "Ben"]
    if x != len(nums):
        return None
    
    max_num = max(nums)
    prime_map = sieveOfEratosthenes(max_num)
    
    scores = [0, 0]
    for n in nums:
        winner = playRound(n, prime_map)
        scores[winner] += 1
    
    if scores[0] > scores[1]:
        return player_names[0]
    elif scores[1] > scores[0]:
        return player_names[1]
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output should be "Ben"
