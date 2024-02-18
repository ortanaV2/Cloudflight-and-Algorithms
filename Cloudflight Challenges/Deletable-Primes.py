def prime_check(num: int) -> bool:
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def separate(num: int) -> list[str]: return list(str(num))

def unite(num_list: list[str]) -> int: return int("".join(num_list))

def selection_branches(checkpoint_prime: int) -> list[int]: 
    possibilities = []
    for digit in separate(checkpoint_prime):
        single_change = int("".join(list(filter(lambda list_e: list_e != digit, separate(checkpoint_prime)))))
        if prime_check(single_change):  
            possibilities.append(single_change)
    return possibilities

def deletable_primes(inp: int) -> int:
            loop_list = [inp]
            for elements in loop_list:
                if elements > 9:
                    for numbers in selection_branches(elements):
                        loop_list.append(numbers)
                print(elements)
            print(loop_list)
            return sum(1 for primes in loop_list if primes < 10)

given_prime = 4567
print(deletable_primes(given_prime)) #Output -> 3
