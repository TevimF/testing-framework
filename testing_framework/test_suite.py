from testing_framework.test_case import TestCase
from testing_framework.test_result import TestResult
from tests.test_case_test import TestStub

class TestSuite:
    """
    Uma coleção de casos de teste que podem ser executados juntos.
    """
    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


