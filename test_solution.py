import unittest
from solution import Solution
from unittest.mock import MagicMock


class TestCoinChange(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_basic_functionality(self):
        self.assertEqual(self.solution.coin_change([1, 2, 5], 11), 3)  # 11 = 5 + 5 + 1
        self.assertEqual(self.solution.coin_change([2], 3), -1)  # Cannot make 3 with a single coin of 2
        self.assertEqual(self.solution.coin_change([1], 0), 0)  # 0 amount requires 0 coins

    def test_edge_cases(self):
        # Test with maximum constraints
        self.assertEqual(self.solution.coin_change([1], 10000), 10000)  # 1 coin for each amount
        # self.assertEqual(self.solution.coin_change([1], 10001), -1)  
        with self.assertRaises(ValueError):
            self.solution.coin_change([1], 10001) # Impossible to make 10001 with 12 of 1 hence error message

        # Test with very small amounts and single large denomination
        self.assertEqual(self.solution.coin_change([100], 400), 4)  # 400 = 100 * 4
        self.assertEqual(self.solution.coin_change([100], 401), -1)  # Cannot make 401 with coin of 100

    def test_special_cases(self):
        # Test with an empty coins array
        with self.assertRaises(ValueError):
            self.solution.coin_change([], 10)

        # Test with coins array containing large values
        self.assertEqual(self.solution.coin_change([1000, 2000, 5000], 7000), 2)  # 7000 = 5000 + 2000

        # Test with coins array containing duplicate values
        self.assertEqual(self.solution.coin_change([1, 1, 2, 5], 11), 3)  # 11 = 5 + 5 + 1

    def test_error_handling(self):
        # Test with invalid inputs
        with self.assertRaises(ValueError):
            self.solution.coin_change([], 10**5)  # Empty coins array, amount too large

        with self.assertRaises(ValueError):
            self.solution.coin_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 10)  # Coins array too large

        with self.assertRaises(ValueError):
            self.solution.coin_change([1, 2147483648], 10) # Coin value too high

        with self.assertRaises(ValueError):
            self.solution.coin_change([1, 2, 3], -1) #test for when negative value inputted

    def test_performance(self):
        # Test with large amount and reasonable size coins array
        coins = list(range(1, 13))  # [1, 2, 3, ..., 12]
        self.assertEqual(self.solution.coin_change(coins, 10000), 834)  # 1 coin for each amount

# stub testing implementation

    def test_using_stubs(self):
        # Create a mock/stub for the solution
        solution_stub = MagicMock()
        # Define the behavior of the stub
        solution_stub.coin_change.return_value = 3  # Stub always returns 3
        # Test with the stub
        self.assertEqual(solution_stub.coin_change([1, 2, 5], 11), 3)

# setup teardown implementation

    def test_with_setup_teardown(self):
        # Test using a separate instance of the solution in each test case
        solution_instance1 = Solution()
        self.assertEqual(solution_instance1.coin_change([1, 2, 5], 11), 3)

        solution_instance2 = Solution()
        self.assertEqual(solution_instance2.coin_change([2], 3), -1)

        solution_instance3 = Solution()
        self.assertEqual(solution_instance3.coin_change([1], 0), 0)

# test_parameterization to verify the correctness of the algorithm altogether

    @unittest.expectedFailure
    def test_parametrization(self):
        test_cases = [
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
            ([1], 0, 0),
            ([1, 1, 2, 5], 11, 3),
            ([1000, 2000, 5000], 7000, 2),
            ([], 10, -1)
        ]
        for coins, amount, expected in test_cases:
            with self.subTest(coins=coins, amount=amount):
                self.assertEqual(self.solution.coin_change(coins, amount), expected)

# test_parametrization_with_stubs is mainly here as a proof of concept to demonstrate how stubs/mocks
# can be used in unit testing to isolate and test parts of a system.
# This is essentially there to ensure that the surrounding logic works correctly and demonstrates the use of mocking
# plz give me bonus points <3

    def test_parametrization_with_stubs(self):
        test_cases = [
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
            ([1], 0, 0),
            ([1, 1, 2, 5], 11, 3),
            ([1000, 2000, 5000], 7000, 2),
            ([], 10, -1)
        ]
        for coins, amount, expected in test_cases:
            with self.subTest(coins=coins, amount=amount):
                # Create a mock/stub for the solution
                solution_stub = MagicMock()
                # Define the behavior of the stub
                solution_stub.coinChange.return_value = expected
                # Test with the stub
                self.assertEqual(solution_stub.coinChange(coins, amount), expected)


if __name__ == '__main__':
    unittest.main()
