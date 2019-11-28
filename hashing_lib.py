# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:30:18 2019

@author: Angelo
"""
import time
import numpy as np

def min_max(minimum, maximum, string):
    orders = list(map(lambda x: ord(x), string))
    minimum = min(min(orders), minimum)
    maximum = max(max(orders), maximum)
    return (minimum, maximum)

def hashcii(string, minimum, coefficients, function):
    orders = np.array(list(map(lambda x: (ord(x)-(minimum-1)), string)))

    return np.dot(coefficients, orders)/function

def bloomfilter_add(hash_values, bloomfilter, length):

    for hash in hash_values:
        bloomfilter[int(hash%length)] = 1


def bloomfilter_check(hash_values, bloomfilter, length):
    is_inside = True
    for hash in hash_values:
        if bloomfilter[int(hash%length)] == 0:
            is_inside = False
            break
    return is_inside

def BloomFilter(file1, file2):
    
    start = time.time()

    first_assignment = True
    with open(file1, "r") as file:
        for line in file:

            if first_assignment:
                minimum = min(list(map(lambda x: ord(x), line.strip())))
                maximum = 0
                first_assignment = False

            minimum, maximum = min_max(minimum, maximum, line.strip())
    maximum -= minimum

    hash_functions = [2, 3, 5, 7, 11]

    coefficients = np.array(list(map(lambda x: maximum ** x, [i for i in range(20)])))

    length = 100000000 #length of the bloom filter
    bloomfilter = np.zeros(length)
    
    with open(file1, "r") as file:
        for line in file:
            hash = []
            for function in hash_functions:
                hash.append(hashcii(line.strip(), minimum, coefficients, function))

            #bloom
            bloomfilter_add(hash, bloomfilter, length)

    counter = 0

    with open(file2, "r") as file:
        for line in file:

            hash = []
            for function in hash_functions:
                hash.append(hashcii(line.strip(), minimum, coefficients, function))

            # bloom
            if bloomfilter_check(hash, bloomfilter, length):
                counter += 1

    end=time.time()
    print("Number of hash function used: ", len(hash_functions))
    print("Number of duplicates detected", counter)
    print("Probability of false positive")
    print("Execution time", end - start)

BloomFilter("passwords1.txt","passwords2.txt")