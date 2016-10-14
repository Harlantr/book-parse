'''
Book Parse is an ultra-efficient Python string parser.
'''

import operator
import time
import argparse
import os
import sys
import math

CHUNK_SIZE = 1024 #1 Kb

def main():
    '''
    Main thread execution.
    '''
    start_time = time.time()

    # Get arguments
    parser = argparse.ArgumentParser(description='Book Parse: String Parser/Letter Counter')
    parser.add_argument('-i', '--input', help='Input File Location', required=True)
    parser.add_argument('-o', '--output', help='Output File Location', required=False)
    args = parser.parse_args()

    with _validated_output_file(args.output) as results_file:
        result = ''

        #Write out to results file
        for key, value in _ordered_dic(args.input):
            result += '%s: %s\r\n' % (key, str(value))

        results_file.write(result)

    end_time = time.time()
    print 'Total time: %.2f seconds' % (end_time - start_time)

def _validated_input_file(i_file):
    try:
        return open(i_file, 'r')
    except IOError:
        print 'Enter a valid input file'
        sys.exit(1)

def _validated_output_file(o_file):
    if o_file is not None:
        try:
            return open(o_file, 'w')
        except IOError:
            print 'Enter a valid output file'
            sys.exit(1)
    else:
        #Return new file in this folder
        return open('bookparseResults.txt', 'w') 

def read_in_chunks(input_file, chunk_size=CHUNK_SIZE):
    '''
    Lazy function (generator) to read the file piece by piece.
    '''
    while True:
        data = input_file.read(chunk_size)
        if not data:
            break
        yield data

def _ordered_dic(i_file):
    #Set up progress bar
    toolbar_length = 40
    sys.stdout.write('[ %s]' % (' ' * toolbar_length))
    sys.stdout.flush()
    sys.stdout.write('\b' * (toolbar_length + 1))

    with _validated_input_file(i_file) as input_file:
        dic = {}
        inc = 0

        #Determine number of chunks (for progress bar update)
        file_size = os.path.getsize(i_file)
        total_chunks = math.ceil(file_size / CHUNK_SIZE)
        increment = total_chunks / toolbar_length

        #Iterate through chunks of the file
        for chunk in read_in_chunks(input_file):
            for char in [x for x in chunk.lower() if x.isalpha()]:
                dic[char] = 1 if not char in dic else dic[char] + 1

            #Update progress bar
            inc += 1
            if inc >= increment:
                inc = 0
                sys.stdout.write('-')
                sys.stdout.flush()

    sys.stdout.write('\n')
    return sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    main()
