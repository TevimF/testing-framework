from testing_framework.test_loader import TestLoader
from testing_framework.test_suite import TestSuite
from testing_framework.test_runner import TestRunner
from tests.test_case_test import TestCaseTest
from tests.test_suite_test import TestSuiteTest
from tests.test_loader_test import TestLoaderTest


def run_all_tests():
    loader = TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_load_suite = loader.make_suite(TestLoaderTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_all_tests()