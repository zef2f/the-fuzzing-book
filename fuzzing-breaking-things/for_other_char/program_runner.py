from runner import Runner
from typing import Union, List, Tuple
from outcome import Outcome

import subprocess

class ProgramRunner(Runner):

    def __init__(self, program: Union[str, List[str]]):
        self.program = program

    def run_process(self, inp: str = "") -> subprocess.CompletedProcess:
        return subprocess.run(self.program,
                              input=inp,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              universal_newlines=True)

    def run(self, inp: str = "") -> Tuple[subprocess.CompletedProcess, Outcome]:
        result = self.run_process(inp)

        if result.returncode == 0:
            outcome = self.PASS
        elif result.returncode < 0:
            outcome = self.FAIL
        else:
            outcome = self.UNRESOLVED

        return (result, outcome)

if __name__ == "__main__":
    pr = ProgramRunner("cat")
    print(pr.run("2232"))
