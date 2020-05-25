#! /usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser(description='makes values from numbers')
parser.add_argument('numbers', type=int, nargs=6, help='the numbers to use')
parser.add_argument('target', type=int, nargs='?', help='the value to aim for, less than 1000, greater than 0')

def numbergram(numbers, target):
    operators = ['+', '-', '*', '/']
    sums = generateSums(numbers, operators)
    for num in sums:
        calcs = extractCalcNumber(num, sums[num])
        for calc in calcs:
            value = parse(calc)
            realcalc = addInBrackets(calc)
            if args.target != None:
                if value == target:
                    print(realcalc, '=', value)
                    found = True
            else:
                print(realcalc, '=', value)

    if not found:
        print('no solution found')

def generateSums(numbers, operators):
    sums = {}
    for i, number in enumerate(numbers):
        rest = [numbers[j] for j, _ in enumerate(numbers) if i != j]
        sums[number] = {}
        for operator in operators:
            if len(rest) == 1:
                for r in rest:
                    sums[number][operator] = r
            else:
                sums[number][operator] = generateSums(rest, operators)
    return sums

def extractCalcNumber(number, parts):
    for op in parts:
        for part in extractCalcOp(op, parts[op]):
            yield str(number) + part

def extractCalcOp(op, parts):
    if isinstance(parts, dict):
        for num in parts:
            for part in extractCalcNumber(num, parts[num]):
                yield op + part
    else:
        yield op + str(parts)

def parse(calc):
    numbers = [int(s) for s in re.split('[+-/*]',calc)]
    ops = list(filter(lambda op: op != '', re.split('\d+',calc)))

    result = numbers[0]
    for i, number in enumerate(numbers[1:]):
        if ops[i] == '+':
            result += number
        elif ops[i] == '-':
            result -= number
        elif ops[i] == '*':
            result = result * number
        elif ops[i] == '/':
            result = result / number
    return result

def addInBrackets(calc):
    numbers = re.split('[+-/*]',calc)
    ops = list(filter(lambda op: op != '', re.split('\d+',calc)))
    realcalc = '((((('+numbers[0]
    for i, number in enumerate(numbers[1:]):
        realcalc += ops[i] + number + ')'
    return realcalc

if __name__ == '__main__':
    args = parser.parse_args()
    numbergram(args.numbers, args.target)
