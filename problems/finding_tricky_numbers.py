import sys
input = sys.stdin.readline

T = int(input())
TCs = []
for i in range(T):
    TCs.append([int(j) for j in input().split()])

DIGITS = 10
MAX_SIZE = 11
MOD = 1000000000000000000

Base = [[[0 for i in range(MAX_SIZE)] for i in range(MAX_SIZE)] for i in range(DIGITS)]
OneDigitCase = [1 for i in range(MAX_SIZE)]
OneDigitCase.append(9)
counts = []

TEN_TEN_MODULO_MODE = 999999937
def computeDifficultNumber(K, A):
    if (K < 10):
        return K
    
    if (A == 9):
        return computeDifficultNumberForNine(K)
    
    else:
        digitSequence = computeDifficultNumberForNotNine(K, A)
        digitSequence.reverse()

        result = 0
        multiplier = 1
        for i in range(0, len(digitSequence), 10):
            adder = 0
            tenPower = 1
            for j in range(9):
                if (i+j < len(digitSequence)):
                    adder += digitSequence[i+j] * tenPower
                    tenPower *= 10
            
            adder = adder % MOD
            adder = (adder * multiplier) % MOD
            result = (result + adder) % MOD
            
            multiplier = (multiplier * TEN_TEN_MODULO_MODE) % MOD

MOD_INVERSE_ELEVEN = 818181824
def computeDifficultNumberForNine(K):
    start = 1000
    exponent = (K - 10)
    binaryExponent = NumberToBinary(exponent)

    EXP_BASE = 10
    expFactor = EXP_BASE
    multiplier = 1

    if (len(binaryExponent) > 0 and binaryExponent[0] == 1):
        multiplier *= expFactor

    for i in range(len(binaryExponent)):
        expFactor = (expFactor * expFactor) % MOD
        if (binaryExponent[i] == 1):
            multiplier = (multiplier * expFactor) % MOD

    result = (start * multiplier) % MOD
    if (K % 2 == 0):
        result = (result - 10) % MOD
    else:
        result = (result - 1) % MOD
    
    result = (result * MOD_INVERSE_ELEVEN) % MOD

    return result

def NumberToBinary(num):
    bin = []
    while (num > 0):
        if (num % 2 == 0):
            bin.append(0)
        else:
            bin.append(1)
        
        num = num // 2

def computeDifficultNumberForNotNine(K, A):
    digitSequence = []

    numberOfDigits = 0
    digit = 0
    remainder = 0
    for i in range(len(counts[A]) - 1, -1, -1):
        if (K > counts[A][i][10]):
            numberOfDigits = i + 1
            remainder = K - counts[A][i][10]

            for j in range(10):
                if (remainder > counts[A][numberOfDigits][j]):
                    remainder -= counts[A][numberOfDigits][j]
                else:
                    digit = j
                    digitSequence.append(digit)
                    break
            break

    for p in range(numberOfDigits, -1, -1):
        for j in range(10):
            if (abs(j - digit) >= A):
                if (remainder > counts[A][p][j]):
                    remainder -= counts[A][p][j]
                else:
                    digit = j
                    digitSequence.append(digit)
                    break
    return digitSequence

def calculateBase():
    for A in range(DIGITS):
        for i in range(10):
            for j in range(10):
                if (abs(j-i) >= A):
                    Base[A][i][j] = 1
        for j in range(10):
            for i in range(10):
                Base[A][10][j] += Base[A][i][j]
        Base[A][10][10] = 1

def calculateVectors():
    for A in range(10):
        counts[A] = []
        vector = OneDigitCase
        newVector = vector
        counts[A].append()

        
calculateBase()
calculateVectors()
for i in TCs:
    print(computeDifficultNumber(K, A))
