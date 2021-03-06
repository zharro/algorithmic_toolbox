# python3

import random

def max_pairwise_product_fast(numbers):
    maxIndex1 = -1

    for index1 in range(len(numbers)):
        if maxIndex1 == -1:
            maxIndex1 = index1
            continue

        if numbers[index1] > numbers[maxIndex1]:
            maxIndex1 = index1

    maxIndex2 = -1

    for index2 in range(len(numbers)):
        if maxIndex2 == -1 and maxIndex1 != index2:
            maxIndex2 = index2
            continue

        if index2 != maxIndex1 and numbers[index2] > numbers[maxIndex2]:
            maxIndex2 = index2

    return numbers[maxIndex1] * numbers[maxIndex2]


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    result = max_pairwise_product_fast(input_numbers)
    print(result)

    # Stress test

    # while True:
    #     n = random.randrange(2, 1000)
    #     numbers = random.sample(range(n), n)

    #     result = max_pairwise_product(numbers)
    #     resultFast = max_pairwise_product_fast(numbers)

    #     if(result != resultFast):
    #         print("Wrong answer! Numbers:{} Basic:{} Fast:{}".format(numbers, result, resultFast))
    #         break
    #     else:
    #         print("OK")
