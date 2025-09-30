from .test_result import TestResult


class TestCase:
    """
    Cada método de teste em uma subclasse de TestCase é executado como um teste individual.
    """
    def __init__(self, test_method_name):
        """
        Inicializa uma nova instância do caso de teste.
        :param test_method_name: O nome do método de teste a ser executado.
        """
        self.test_method_name = test_method_name

    def run(self, result: TestResult):
        """
        Ciclo de vida completo de um teste: a configuração, o método de teste e a limpeza.
        """
        # 1. Prepara o ambiente de teste
        # 1.1 teste iniciado
        result.test_started()
        # 1.2 configuração do ambiente
        self.set_up()

        # 2. Obtém o método de teste real a partir do seu nome e o executa
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()
        except AssertionError as e:
            # falha na asserção (resultado esperado diferente do resultado atual)
            result.add_failure(self.test_method_name)
        except Exception as e:
            # erro inesperado (exceção não tratada)
            result.add_error(self.test_method_name)

        # 3. Limpa o ambiente de teste após a execução
        # tear down
        self.tear_down()



    def set_up(self):
        """
        Método de preparação (hook) executado antes de cada método de teste.
        """
        # Esse método será sobrescrito em subclasses
        pass

    def tear_down(self):
        """
        Método de limpeza (hook) executado após cada método de teste.
        """
        # Esse método será sobrescrito em subclasses
        pass
