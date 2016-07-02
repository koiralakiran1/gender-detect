"""
    Merge two CSV into one.
    Usage:
        python csv-merger.py <file1> <file2> <output-file>
"""

from sys import argv


def merge(file1, file2, output):
    with open(file1) as file1:
        data1 = file1.readlines()
    print len(data1)
    with open(file2) as file2:
        data2 = file2.readlines()
    print len(data2)
    data1.extend(data2)
    print len(data1)
    with open(output, 'w') as out:
        for d in data1:
            out.write(d)


def main():
    try:
        file1 = argv[1]
        file2 = argv[2]
        output = argv[3]
        merge(file1, file2, output)
    except:
        print '''
        Not enough arguments!
        Usage:
            python csv-merger.py file1 file2 output-file
        '''.strip()

if __name__ == '__main__':
    main()
