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
