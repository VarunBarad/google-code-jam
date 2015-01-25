#!/usr/bin/python3

# Problem : https://code.google.com/codejam/contest/32016/dashboard#s=p0
__author__ = 'Varun Barad'


def main():
    no_of_cases = int(input())

    for i in range(no_of_cases):
        length = input()
        v1 = [int(x) for x in input().split(' ')]
        v2 = [int(x) for x in input().split(' ')]

        v1 = sorted(v1, reverse=False)
        v2 = sorted(v2, reverse=True)

        product = 0

        for (x, y) in zip(v1, v2):
            product += (int(x)*int(y))
        print('Case #{0}: {1}'.format((i+1), product))


if __name__ == '__main__':
    main()