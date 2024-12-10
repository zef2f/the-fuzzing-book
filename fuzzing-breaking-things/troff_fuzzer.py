from random_fuzzer import RandomFuzzer
from troff_runner import TroffRunner

fuzz = RandomFuzzer(50, 500, 0, 255)
results = fuzz.runs(TroffRunner(), trials=10000)
print(results)
