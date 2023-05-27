from unittest import TestCase

from solution import Solution


class TestSolution(TestCase):
    def test_generateParenthesis_n_equals_3(self):
        solution = Solution()
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(solution.generateParenthesis(3), expected)

    def test_generateParenthesis_n_equals_1(self):
        solution = Solution()
        expected = ["()"]
        self.assertCountEqual(solution.generateParenthesis(1), expected)

    def test_generateParenthesis_n_equals_0(self):
        solution = Solution()
        with self.assertRaises(ValueError):
            solution.generateParenthesis(0)

    def test_generateParenthesis_n_equals_2(self):
        solution = Solution()
        expected = ["(())", "()()"]
        self.assertCountEqual(solution.generateParenthesis(2), expected)

    def test_generateParenthesis_n_equals_minus1(self):
        solution = Solution()
        with self.assertRaises(ValueError):
            solution.generateParenthesis(-1)

    def test_generateParenthesis_n_equals_9(self):
        solution = Solution()
        with self.assertRaises(ValueError):
            solution.generateParenthesis(9)

    #  Для довольно больших n я сравниваю только количество элементов,
    #  Потому что число комбинаций достаточно велико и проверка каждого конкретного варианта становится неудобной,
    #  Но мы знаем ожидаемое количество элементов последовательности благодаря числам Каталана
    def test_generateParenthesis_n_equals_6(self):
        solution = Solution()
        self.assertEqual(len(solution.generateParenthesis(6)), 132)

    def test_generateParenthesis_n_equals_7(self):
        solution = Solution()
        self.assertEqual(len(solution.generateParenthesis(7)), 429)

    def test_generateParenthesis_n_equals_8(self):
        solution = Solution()
        self.assertEqual(len(solution.generateParenthesis(8)), 1430)

    # Так же тут были добавлены тесты на проверку того, что будет, если передать n типа переменной отличной от int
    # Это было сделано, так как нам в рамках ограничений одназначно не указали каким типом может быть n
    # Сказано было только, что 1 <= n <= 8
    def test_generateParenthesis_n_is_float(self):
        solution = Solution()
        with self.assertRaises(ValueError):
            solution.generateParenthesis(5.8)

    def test_generateParenthesis_n_is_str(self):
        solution = Solution()
        with self.assertRaises(ValueError):
            solution.generateParenthesis('some')
