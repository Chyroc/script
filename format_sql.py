# encoding: utf8

import os
import sys

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        print('请输入参数')
        exit(1)

    file = argv[1]
    if not os.curdir.startswith('.'):
        file = '{}/{}'.format(os.curdir, file)

    max_in_tale_width = 0
    lines = []
    with open(file) as f:
        lines = []

        # max width
        for i in f:
            i = i.rstrip('\n')
            lines.append(i)
            max_in_tale_width = max(max_in_tale_width, len(i))

    for k in range(len(lines)):
        if k + 1 < len(lines) and lines[k + 1].startswith('  COMMENT'):
            print('{}{}{}'.format(lines[k], ' ' * (max_in_tale_width - len(lines[k])), lines[k + 1]))
            k += 1
        elif lines[k].startswith('  COMMENT'):
            pass
        else:
            print('{}'.format(lines[k]))
