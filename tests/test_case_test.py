from testing_framework.test_case import TestCase
from testing_framework.test_result import TestResult

class TestStub(TestCase):
    """
    Esta é uma classe de teste stub para testar o ‘framework’ de teste.
    Ela contém três métodos de teste: um que passa, um que falha e um que gera um erro.
    """
    def test_success(self):
        self.assert_true(True)

    def test_failure(self):
        self.assert_false(True)

    def test_error(self):
        raise Exception

class TestSpy(TestCase):
    """
    TestSpy espiona a execução do modelo method (set_up, test_method, tear_down).
    Então se o teste passa, sabemos que todos os três métodos foram chamados.
    """
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.was_run = False
        self.was_set_up = False
        self.was_tear_down = False
        self.log = ""

    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"


class TestCaseTest(TestCase):
    """
    Esta é uma classe de teste para testar o ‘framework’ de teste.
    Ela contém três métodos de teste: um que passa, um que falha e um que gera um erro.
    """

    def set_up(self):
        self.result = TestResult()

    def test_result_success_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        self.assert_equal(self.result.run_count, 1)
        self.assert_equal(len(self.result.failures), 0)
        self.assert_equal(len(self.result.errors), 0)

    def test_result_failure_run(self):
        stub = TestStub('test_failure')
        stub.run(self.result)
        self.assert_equal(self.result.run_count, 1)
        self.assert_equal(len(self.result.failures), 1)
        self.assert_equal(len(self.result.errors), 0)

    def test_result_error_run(self):
        stub = TestStub('test_error')
        stub.run(self.result)
        self.assert_equal(self.result.run_count, 1)
        self.assert_equal(len(self.result.failures), 0)
        self.assert_equal(len(self.result.errors), 1)

    def test_result_multiple_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        stub = TestStub('test_failure')
        stub.run(self.result)
        stub = TestStub('test_error')
        stub.run(self.result)
        self.assert_equal(self.result.run_count, 3)
        self.assert_equal(len(self.result.failures), 1)
        self.assert_equal(len(self.result.errors), 1)

    def test_summary_coloring(self):
        """Verifica se o resumo começa com o código de cor adequado para cada cenário."""
        # sucesso → verde
        stub = TestStub('test_success')
        stub.run(self.result)
        self.assert_true(self.result.summary().startswith(TestResult.GREEN))

        # falha → amarelo
        self.result = TestResult()
        stub = TestStub('test_failure')
        stub.run(self.result)
        self.assert_true(self.result.summary().startswith(TestResult.YELLOW))

        # erro → vermelho
        self.result = TestResult()
        stub = TestStub('test_error')
        stub.run(self.result)
        self.assert_true(self.result.summary().startswith(TestResult.RED))

    def test_was_set_up(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_set_up)

    def test_was_run(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_run)

    def test_was_tear_down(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_tear_down)

    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_equal(spy.log, "set_up test_method tear_down")

    def test_assert_true(self):
        self.assert_true(True)

    def test_assert_false(self):
        self.assert_false(False)

    def test_assert_equal(self):
        self.assert_equal("", "")
        self.assert_equal("foo", "foo")
        self.assert_equal([], [])
        self.assert_equal(['foo'], ['foo'])
        self.assert_equal((), ())
        self.assert_equal(('foo',), ('foo',))
        self.assert_equal({}, {})
        self.assert_equal({'foo'}, {'foo'})

    def test_assert_in(self):
        animals = {'monkey': 'banana', 'cow': 'grass', 'seal': 'fish'}

        self.assert_in('a', 'abc')
        self.assert_in('foo', ['foo'])
        self.assert_in(1, [1, 2, 3])
        self.assert_in('monkey', animals)
        self.assert_in('banana', animals.values())


if __name__ == '__main__':
    # executa automaticamente todos os métodos que começam com 'test_'
    result = TestResult()
    test_methods = [name for name in dir(TestCaseTest) if name.startswith('test_')]

    for method in test_methods:
        test = TestCaseTest(method)
        test.run(result)

    print(result.summary())