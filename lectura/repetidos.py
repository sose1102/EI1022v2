import sys
from typing import TextIO


def read_data(f: TextIO) -> list[int]:
    lines = f.readlines()
    return [int(line) for line in lines]

def process(data: list[int]) -> bool:
    data.sort()
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
        #for j in range(i+1, len(data)):
        #    if data[i] == data[j]:
                return True
    return False

def show_result(result: bool):
    print("No hay repetidos"
          if not result
          else "Hay repetidos")

if __name__ == "__main__":
    nums = read_data(sys.stdin)
    m = process(nums)
    show_result(m)