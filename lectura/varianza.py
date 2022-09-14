import sys
from typing import TextIO

def read_data(f: TextIO) -> list[int]:
    lines = f.readlines()
    return [int(line) for line in lines]

def average(nums: list[int]) -> float:
    return sum(nums)/len(nums)

def process(nums: list[int]) -> float:
    s = 0
    av = average(nums)
    for num in nums:
        s += (num - av) ** 2
    return s/len(nums)

def show_results(s: float):
    print(s)

if __name__ == "__main__":
    nums = read_data(sys.stdin)
    s = process(nums)
    show_results(s)