#!/usr/bin/python3

# Problem : https://code.google.com/codejam/contest/351101/dashboard#s=p0
__author__ = 'Varun Barad'


def main():
    no_of_test_cases = int(input())
    for i in range(no_of_test_cases):
        credit = int(input())
        no_of_items = int(input())
        items = input().split(' ')
        for j in range(no_of_items):
            items[j] = int(items[j])
        for j in range(no_of_items):
            if (credit-items[j]) in items[(j+1):]:
                break
        print('Case #{0}: {1} {2}'.format((i+1), (j+1), (items[(j+1):].index(credit-items[j])+j+2)))

if __name__ == '__main__':
    main()