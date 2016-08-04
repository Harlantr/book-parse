import operator
import time
import argparse
import os
import sys

def main(args):
    #Validate
    doc = validate_input(args.input)
    results_file = validate_output(args.output)

    #Get raw lowercase, alphabetical string
    print "\nReading input file..."
    txt = filter(lambda x: x.isalpha(), doc.read().lower())
    result = ''

    #Write out to results file
    for key, value in processed_file(txt):
        result += key + ': ' + str(value) + '\n'
    results_file.write(result)
    results_file.close()

def validate_input(input):
    try:
        return open(args.input, 'r')
    except IOError, e:
        print "Enter a valid input file"
        os._exit(1)

def validate_output(output):
    if output is not None:
        try:
            return open(args.output, 'w')
        except IOError, e:
            print "Enter a valid output file"
            os._exit(1)
    else:
        #Return new file in this folder
        return open('bookparseResults.txt', 'w') 

def processed_file(txt):
    print "Processing file..."

    #Set up progress bar
    toolbar_length = 40
    sys.stdout.write("[%s]" % (" " * toolbar_length))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_length+1)) # return to start of line, after '['

    length = len(txt)
    increment = length/toolbar_length
    dic = {}
    inc = 0

    for c in txt:
        inc += 1

        #Add character to dictionary if it doesn't exist yet
        #Add 1 to its value if it does
        dic[c] = 1 if not c in dic else dic[c] + 1

        if(inc >= (increment)):
            inc = 0
            sys.stdout.write("-")
            sys.stdout.flush()

    sys.stdout.write("\n")
    return sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    start = time.time()

    parser = argparse.ArgumentParser(description='Book Parse: String Parser/Letter Counter')
    parser.add_argument('-i','--input', help='Input File Location', required=True)
    parser.add_argument('-o','--output', help='Output File Location', required=False)
    args = parser.parse_args()

    main(args)

    end = time.time()
    print("Total time: %.2f seconds" % (end - start))
    # print "Total time: " + str((end - start))
