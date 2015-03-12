#!/usr/bin/python3

# Problem : https://code.google.com/codejam/contest/619102/dashboard#s=p0
__author__ = 'vbarad'


def main():
    no_of_cases = int(input())

    for i in range(no_of_cases):
        no_of_wires = int(input())

        wires = []
        for j in range(no_of_wires):
            wire = input()
            wire = (int(wire.split(' ')[0]), int(wire.split(' ')[1]))
            wires.append(wire)

        count = 0
        for j in range(no_of_wires):
            for k in range(j, no_of_wires):
                if ((wires[j][0]-wires[k][0])*(wires[j][1]-wires[k][1])) < 0 :
                    count += 1

        output = 'Case #{0}: {1}'.format((i+1), count)
        print(output)


if __name__ == '__main__':
    main()