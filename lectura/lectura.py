import sys
from typing import TextIO

def read_data(f: TextIO) -> list[int]:
    lines = f.readlines()
    return [int(lines) for line in lines]

def show_results(nums: list[int]):
    for num in nums:
        print(num)

if __name__ == "__main":
    nums = read_data(sys.stdin)
    show_results(nums)