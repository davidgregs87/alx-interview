#!/usr/bin/python3
'''
 Log parsing
'''
import sys


file_size = 0
stat = {
    '200': 0, '301': 0, '400': 0,
    '401': 0, '403': 0, '404': 0,
    '405': 0, '500': 0
}


def disp_stat():
    ''' prints log metrics '''
    print('File size: {}'.format(file_size))
    for k, v in sorted(stat.items()):
        if v > 0:
            print('{}: {}'.format(k, v))


if __name__ == '__main__':
    lineNum = 0
    try:
        for line in sys.stdin:
            line = line.split()
            lineNum += 1
            try:
                file_size += int(line[-1])
                if line[-2] in stat.keys():
                    stat[line[-2]] += 1
            except (IndexError, ValueError):
                pass
            if lineNum % 10 == 0:
                disp_stat()
    except KeyboardInterrupt:
        disp_stat()
        raise
    else:
        disp_stat()
