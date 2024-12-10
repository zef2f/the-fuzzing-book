from typing import Any

from runner import Runner

class PrintRunner(Runner):
    """ simple runner, printing the input """

    def run(self, inp: str) -> Any:
        print(inp)
        return(inp, Runner.UNRESOLVED)

if __name__ == "__main__":
    pr = PrintRunner()
    pr.run("hi, denis. are u rly alive?")
