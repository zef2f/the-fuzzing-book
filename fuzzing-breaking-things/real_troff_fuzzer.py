from random_fuzzer import RandomFuzzer
from binary_program_runner import BinaryProgramRunner

fuzz = RandomFuzzer(5, 500, 0, 255)
results = fuzz.runs(BinaryProgramRunner("troff"), trials=1000)
for i in range(len(results)):
    if results[i][1] != "PASS":
        print(results[i])
