#!/usr/bin/python3

# Problem : https://code.google.com/codejam/contest/351101/dashboard#s=p2
__author__ = 'Varun Barad'

key_map = {
    '2': ['a', 'b', 'c']
    , '3': ['d', 'e', 'f']
    , '4': ['g', 'h', 'i']
    , '5': ['j', 'k', 'l']
    , '6': ['m', 'n', 'o']
    , '7': ['p', 'q', 'r', 's']
    , '8': ['t', 'u', 'v']
    , '9': ['w', 'x', 'y', 'z']
    , '0': [' ']
}


def main():
    no_of_cases = int(input())
    for i in range(no_of_cases):
        message = input()
        output = ''
        for c in message:
            for k in key_map:
                if c in key_map[k]:
                    if len(output) > 0 and output[-1] == k:
                        output += ' '
                    output += (k*(key_map[k].index(c)+1))
                    break
        print('Case #{0}: {1}'.format((i+1), output))

if __name__ == '__main__':
    main()