# Sparse Text Program

def createModifiedFile(input_file, outputfile):
    '''
        For text file input_file, creates a new version in file outputfile
        in which all instances of the letter 'e' are removed.
    '''

    empty_str = ''
    num_total_chars = 0
    num_removals = 0

    #create list of vowels
    vowels = ['a','e','i','o','u','A','E','I','O','U']


    for line in input_file:
        #there is a new line at the end
        if line[-1] == '\n':
            # save original line length
            orig_line_length = len(line) - 1
            num_total_chars = num_total_chars + orig_line_length

            # remove all occurrances of vowels
            modified_line = line
            for c in vowels:
                modified_line = modified_line.replace(c, empty_str)

            num_removals = num_removals + \
                           (orig_line_length - (len(modified_line) - 1))

        #there is no new line at the end
        else:
            # save original line length
            orig_line_length = len(line)
            num_total_chars = num_total_chars + orig_line_length

            # remove all occurrances of vowels
            modified_line = line
            for c in vowels:
                modified_line = modified_line.replace(c, empty_str)

            num_removals = num_removals + \
                           (orig_line_length - len(modified_line))

        # simulataneouly output line to screen and output file
        print(modified_line.strip('\n'))
        output_file.write(modified_line)

    return (num_total_chars, num_removals)


# --- main

# open files for reading and writing
file_name = input('Enter file name (including file extension): ')
input_file = open(file_name, 'r')
new_file_name = 'new_' + file_name
output_file = open(new_file_name, 'w')

# create file with all letter e removed
print()
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# close current input and output files
input_file.close()
output_file.close()

# display percentage of characters removed
print()
print(num_removals, "vowels removed")
print(num_removals, "out of", num_total_chars, "characters removed")
print('Percentage of data lost:',
      int((num_removals / num_total_chars) * 100), '%')
print('Modified text in file', new_file_name)

