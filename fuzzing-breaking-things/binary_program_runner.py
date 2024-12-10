from program_runner import ProgramRunner
import subprocess

class BinaryProgramRunner(ProgramRunner):
    def run_process(self, inp: str = "") -> subprocess.CompletedProcess:
        return subprocess.run(self.program,
                              input=inp.encode(),
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

if __name__ == "__main__":
    bpr = BinaryProgramRunner("cat")
    print(bpr.run("hi, denis. are u alive?"))

