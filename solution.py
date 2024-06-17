# original code

"""class Solution:
    def coin_change(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1"""

# improved the code
# added constraint checks

from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        # Check constraint: 1 <= coins.length <= 12
        if not (1 <= len(coins) <= 12):
            raise ValueError("number of coins must be between 1 and 12.")

        # Check constraint: 1 <= coins[i] <= 2^31 - 1
        for coin in coins:
            if not (1 <= coin <= 2 ** 31 - 1):
                raise ValueError("value of coins must be between 1 and 2^31 - 1.")

        # Check constraint: 0 <= amount <= 10^4
        if not (0 <= amount <= 10 ** 4):
            raise ValueError("Amount must be between 0 and 10^4.")

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


solution = Solution()

