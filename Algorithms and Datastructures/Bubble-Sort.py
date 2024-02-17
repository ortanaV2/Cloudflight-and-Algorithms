#Official
def bubble_sort(array: list) -> list:
    for e in range(len(array)):
        for i in range(len(array)-e-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            print(i, array) #Understanding
    return array

bubble_sort([4, 6, 2, 5, 6, 9, 1])

#Self-Training
import random
from typing import Union

def bubble_sort(inp: Union[list, tuple], reverse: bool = False) -> Union[list, tuple]:
    while True:
        change_count: int = 0
        for index, element in enumerate(inp):
            try:
                if reverse:
                    if inp[index+1] > element:
                        inp.remove(element)
                        inp.insert(index+1, element)
                        change_count += 1
                    else: continue
                if not reverse:
                    if inp[index+1] < element:
                        inp.remove(element)
                        inp.insert(index+1, element)
                        change_count += 1
                    else: continue
            except IndexError: pass
        if change_count == 0: break
    return inp
