from runner import Runner
from print_runner import PrintRunner
from typing import Tuple, List
from outcome import Outcome
import subprocess

class Fuzzer:

    def __init__(self) -> None:
        """constructor"""
        pass

    def fuzz(self) -> str:
        """return fuzz input"""
        return ""

    def run(self, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess, Outcome]:
        return runner.run(self.fuzz())

    def runs(self, runner: Runner = PrintRunner(), trials: int = 10) \
            -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        """ run runner with fuzz input, trials time """
        return [self.run(runner) for i in range(trials)]

if __name__ == "__main__":
    fuzzer = Fuzzer()
    results = fuzzer.runs(trials=3)
    print(results)
