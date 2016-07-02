from collections import Counter
from sys import argv


def main():
    output = []
    finaloutput = []
    try:
        filename = argv[1]
        output_name = argv[2]
    except:
        print '''Not enough arguments.
            Usage: python generate.py <starting_filename> <output_filename>
        '''
        exit(0)
    with open(filename) as file:
        data = file.readlines()

    # Skip the csv headers
    data = data[1:]
    print "Read {} names from the file.".format(len(data))

    # Parse CSV data to Python List
    for d in data:
        values = d.split(',')
        name = values[0].lower()
        firstname = name.split(' ')[0]  # Take only the first name
        gender = values[1].lower()
        output.append("{},{}".format(firstname, gender))

    withcount = Counter(output)
    for key, value in withcount.items():
        finaloutput.append("{},{}\n".format(key.strip(), value))

    finaloutput.sort()

    with open(output_name, 'w') as finalfile:
        for line in finaloutput:
            finalfile.write(line)
    print "Completed. Unique Names scraped: {}".format(len(finaloutput))
    print "Saved to: %s" % (output_name)

if __name__ == "__main__":
    main()
