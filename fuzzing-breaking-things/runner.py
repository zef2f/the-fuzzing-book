from typing import Any

class Runner:
    """ base class for testing inputs """

    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    def __init__(self) -> None:
        """ initialize """
        pass

    def run(self, inp: str) -> Any:
        """ run the runner with given input """
        return (inp, Runner.UNRESOLVED)

if __name__ == "__main__":
    runner = Runner()
    assert runner.run("hello")[0] == "hello"
