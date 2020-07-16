# Air Pollution/Cancer Correlation Program

import math


def openFiles():
    '''
        Prompts the user for the file names to open, opens the files,
        and returns the file objects for each in a tuple of the form
        (pollution_datafile, cancer_datafile).

        Raises an OSError exception if the files are not successfully
        opened after four attempts of entering file names.
    '''

    # init
    pollution_datafile_opened = False
    cancer_datafile_opened = False
    num_attempts = 4

    # prompt for file names and attempt to open files
    while ((not pollution_datafile_opened) or \
           (not cancer_datafile_opened)) \
            and (num_attempts > 0):
        try:

            if not cancer_datafile_opened:
                file_name = input('Enter lung cancer data from filename: ')
                cancer_datafile = open(file_name, 'r')
                cancer_datafile_opened = True

            if not pollution_datafile_opened:
                file_name = input('Enter air pollution data from filename: ')
                pollution_datafile = open(file_name, 'r')
                pollution_datafile_opened = True

        except OSError:
            print('File not found:', file_name + '.', 'Please reenter\n')
            num_attempts = num_attempts - 1

    # if one or more files not opened, raise OSError exception
    if not pollution_datafile_opened or not cancer_datafile_opened:
        raise OSError('Too many attempts of reading input files')

    # return file objects if successfully opened
    else:
        return (pollution_datafile, cancer_datafile)


def readFiles(pollution_datafile, cancer_datafile):
    '''
        Reads the data from the provided file objects smoking_datafile
        and cancer_datafile. Returns a list of the data read from each
        in a tuple of the form (pollution_datafile, cancer_datafile).
    '''

    # init
    pollution_data = []
    cancer_data = []
    empty_str = ''

    # read past file headers
    pollution_datafile.readline()
    cancer_datafile.readline()

    # read pollution data files
    eof = False

    while not eof:

        # read line of data from each file
        line = pollution_datafile.readline()

        # check if at end-of-file of both files
        if line == empty_str:
            eof = True

        # append line of data to each list
        else:
            pollution_data.append(line.strip().split(','))

    eof = False

    # read cancer data files
    while not eof:

        # read line of data from each file
        line = cancer_datafile.readline()

        # check if at end-of-file of both files
        if line == empty_str:
            eof = True

        # append line of data to each list
        else:
            cancer_data.append(line.strip().split(','))

    #close pollution data file
    pollution_datafile.close()
    #close cancer data file
    cancer_datafile.close()
    # return list of data from each file
    return (pollution_data, cancer_data)


def calculateCorrelation(pollution_data, cancer_data):
    '''
        Calculates and returns the correlation value for the data
        provided in lists pollution_data and cancer_data
    '''

    # init
    sum_pollution_vals = sum_cancer_vals = 0
    sum_pollution_sqrd = sum_cancer_sqrd = 0
    sum_products = 0

    #get length of datas
    num_pollution_values = len(pollution_data)
    num_cancer_values = len(cancer_data)

    #init list
    total_pollution_states = []
    total_cancer_states = []

    #list of states that are in both datas
    total_states = []

    #add states in list
    for k in range(0, num_pollution_values):
        total_pollution_states.append(pollution_data[k][0])

    for k in range(0, num_cancer_values):
        total_cancer_states.append(cancer_data[k][0])

    #add states that are in both lists
    for k in range(0, len(total_pollution_states)):
        if total_pollution_states[k] in total_cancer_states:
            total_states.append(total_pollution_states[k])

    #sort list
    total_states.sort()

    #make new data with states only in both data
    new_pollution_data = [data for data in pollution_data if data[0] in total_states]
    new_cancer_data = [data for data in cancer_data if data[0] in total_states]

    #sort lists for calculation
    new_pollution_data.sort()
    new_cancer_data.sort()

    num_values = len(new_pollution_data)

    # calculate intermediate correlation values
    for k in range(0, num_values):
        sum_pollution_vals = sum_pollution_vals + float(new_pollution_data[k][1])
        sum_cancer_vals = sum_cancer_vals + float(new_cancer_data[k][1])

        sum_pollution_sqrd = sum_pollution_sqrd + \
                           float(new_pollution_data[k][1]) ** 2
        sum_cancer_sqrd = sum_cancer_sqrd + \
                          float(new_cancer_data[k][1]) ** 2

        sum_products = sum_products + float(new_pollution_data[k][1]) * \
                       float(new_cancer_data[k][1])

    # calculate and display correlation value
    numer = (num_values * sum_products) - \
            (sum_pollution_vals * sum_cancer_vals)

    denom = math.sqrt(abs( \
        ((num_values * sum_pollution_sqrd) - (sum_pollution_vals ** 2)) * \
        ((num_values * sum_cancer_sqrd) - (sum_cancer_vals ** 2)) \
        ))

    return numer / denom


# ---- main

# program greeting
print('This program will determine the correlation (-1 to 1) between')
print('data on air pollution and incidences of lung cancer\n')

try:
    # open data files
    pollution_datafile, cancer_datafile = openFiles()

    # read data
    pollution_data, cancer_data = readFiles(pollution_datafile, cancer_datafile)

    # calculate correlation value
    correlation = calculateCorrelation(pollution_data, cancer_data)

    # display correlation value
    print('r_value = ', correlation)

except OSError as e:
    print(e)
    print('Program terminated ...')
