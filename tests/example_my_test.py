from testing_framework.test_case import TestCase
from testing_framework.test_result import TestResult

class MyTest(TestCase):
    """
    Esta é uma classe de exemplo para demonstrar o uso de TestCase.
    Observe como set_up e tear_down são chamados para cada teste.
    """
    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')



if __name__ == '__main__':
    test_result = TestResult()

    print("--- test_a ---")
    test_a = MyTest("test_a")
    test_a.run(test_result)

    print("--- test_b ---")
    test_b = MyTest("test_b")
    test_b.run(test_result)

    print("--- test_c ---")
    test_c = MyTest("test_c")
    test_c.run(test_result)

    print(test_result.summary())



