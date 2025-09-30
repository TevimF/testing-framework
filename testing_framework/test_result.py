class TestResult:

    RUN_MSG = 'run'
    FAILURE_MSG = 'failed'
    ERROR_MSG = 'error'

    # ANSI escape codes for colors
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    def __init__(self, suite_name=None):
        self.run_count = 0
        self.failures = []
        self.errors = []

    def test_started(self):
        self.run_count += 1

    def add_failure(self, test):
        self.failures.append(test)

    def add_error(self, test):
        self.errors.append(test)

    def summary(self):
        color = self.RESET

        if len(self.errors) > 0:
            color = self.RED
        elif len(self.failures) > 0:
            color = self.YELLOW
        else:
            color = self.GREEN

        run_summary = f'{color}{self.run_count} {self.RUN_MSG}{self.RESET}'
        failures_summary = f'{color}{len(self.failures)} {self.FAILURE_MSG}{self.RESET}'
        errors_summary = f'{color}{len(self.errors)} {self.ERROR_MSG}{self.RESET}'
        return f'{run_summary}, {failures_summary}, {errors_summary}'
