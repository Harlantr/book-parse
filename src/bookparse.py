import operator
import time
import argparse
import os
import sys
import math

def main(args):
    results_file = validated_output_file(args.output)
    result = ''

    #Write out to results file
    for key, value in processed_file():
        result += key + ': ' + str(value) + '\n'

    results_file.write(result)
    results_file.close()

def validated_input_file(input):
    try:
        return open(args.input, 'r')
    except IOError, e:
        print 'Enter a valid input file'
        os._exit(1)

def validated_output_file(output):
    if output is not None:
        try:
            return open(args.output, 'w')
        except IOError, e:
            print 'Enter a valid output file'
            os._exit(1)
    else:
        #Return new file in this folder
        return open('bookparseResults.txt', 'w') 

def processed_file():
    #Set up progress bar
    toolbar_length = 40
    sys.stdout.write('[%s]' % (' ' * toolbar_length))
    sys.stdout.flush()
    sys.stdout.write('\b' * (toolbar_length+1))

    with validated_input_file(args.input) as file:
        dic = {}
        inc = 0

        #Determine amount of chunks (for progress bar update)
        file_size = os.path.getsize(args.input)
        chunk_size = 1024    #1 Kb - Possibly make this dynamic?
        total_chunks = file_size / chunk_size
        total_chunks = math.ceil(total_chunks)
        increment = total_chunks/toolbar_length

        #Iterate through chunks of the file
        for chunk in iter((lambda:file.read(chunk_size)),''):

            #Strip whitespace; count letters
            chunk_nws = "".join(chunk.lower().split())
            txt = filter(lambda x: x.isalpha(), chunk_nws)
            for c in txt:
                dic[c] = 1 if not c in dic else dic[c] + 1

            #Update progress bar
            inc += 1
            if(inc >= increment):
                inc = 0
                sys.stdout.write('-')
                sys.stdout.flush()

    sys.stdout.write('\n')
    return sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    start = time.time()

    parser = argparse.ArgumentParser(description='Book Parse: String Parser/Letter Counter')
    parser.add_argument('-i','--input', help='Input File Location', required=True)
    parser.add_argument('-o','--output', help='Output File Location', required=False)
    args = parser.parse_args()

    main(args)

    end = time.time()
    print('Total time: %.2f seconds' % (end - start))
