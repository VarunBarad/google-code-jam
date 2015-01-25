#!/usr/bin/python3

# Problem : https://code.google.com/codejam/contest/351101/dashboard#s=p1
__author__ = 'Varun Barad'


def main():
    no_of_test_cases = int(input())
    for i in range(no_of_test_cases):
        words = input().split(' ')
        print('Case #{0}: {1}'.format((i+1), ' '.join(words[::-1])))

if __name__ == '__main__':
    main()