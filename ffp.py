#Chris Lim
#24/7
#Latitude Coding Problem #1
#For the purposes of this exercise I will assume the following:
# - Exception are allowed to be thrown, sometimes error is better than silent failure, these will be verified in the test cases
#usage ffp.py <config_file> <input_file> <output_file>


import json
import csv
import logging
import sys
import os
from datetime import datetime

#open the fixed file, parse according to input offset_list and return as a list of rows 
def readFixedFile(input_file, encoding, offset_list):
    data_file = open(input_file, "r", encoding=encoding)
    parsed = []
    for line in data_file:
        row = []
        for f in offset_list.values():
            row.append(line[f[0]:f[1]].strip())
        logging.debug(row)
        parsed.append(row)
    return parsed
    
#open the CSV file and return as a list of rows 
def readCSV(input_file, encoding, skipheader=False):
    with open(input_file, "r", newline='', encoding=encoding) as f:
        if(skipheader):
            next(f)
        reader = csv.reader(f)
        data = list(reader)
    return data

#read config file and return as a object
def readConfig(config_file):
    config = open(config_file, "r")
    data = json.load(config)
    config.close()
    return data

#parse file 
#config_file - path of config file containing spec to parse against
#input_file  - path of fixed file to parse
#output_file - path of the output CSV
def parse(config_file, input_file, output_file):
    

    logging.basicConfig(filename='parser.log', encoding='utf-8', level=logging.DEBUG)
    logger = logging.getLogger("logger")
    logger.debug ("-------------------{}-------------------".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) 

    try:
        #open and parse the config file
        data = readConfig(config_file)
        logger.debug(json.dumps(data, indent = 4, sort_keys=True))
        
        column_names = data["ColumnNames"]
        delimited_encoding = data["DelimitedEncoding"]
        fixed_encoding = data["FixedWidthEncoding"]
        include_header = data["IncludeHeader"]
        offsets = data["Offsets"]

        logging.debug("Column names: {}".format(str(column_names)))
        logging.debug("Delimiter encoding: {}".format(str(delimited_encoding)))
        logging.debug("Fixed encoding: {}".format(str(fixed_encoding)))
        logging.debug("Header: {}".format( str(include_header)))
        logging.debug("Offsets: {}".format(str(offsets)))

        if (len(column_names) != len(offsets)):
            #config file is a problem
            raise Exception("Number of column names does not match")
            
        #calculate the indexes for each column
        current_offset = 0
        offset_list  = {}
        for k, offset in zip(column_names,offsets):
            offset_list[k] = (current_offset, current_offset+int(offset))
            current_offset+=int(offset)
        logging.debug("Offsets: ".format(str(offset_list)))
    
        #open the file to parse and build the list of parsed rows
        parsed = readFixedFile(input_file, fixed_encoding, offset_list)
                
        if not os.path.exists('output'):
            os.mkdir('output')

                
        #write the CSV
        with open(output_file, 'w', encoding=delimited_encoding, newline='') as f:      
            
            writer = csv.writer(f)
            
            # write the header if specified
            if(str.lower(include_header) == "true"):
                writer.writerow(offset_list)

            # write the parsed rows
            writer.writerows(parsed)
            
    except FileNotFoundError  as FFE:
        msg = "File error: {}".format(FFE)
        print(msg)
        logging.error(msg)
        raise FileNotFoundError(FFE)
        
    

if __name__=='__main__':
    
    #if there aren't 3 arguments specified exit immediately
    if (len(sys.argv) != 4):
        print("usage - ffp.py <config_file> <input_file> <output_file>")
        quit()
    
    config_file = (str(sys.argv[1]))
    input_file = str(sys.argv[2])
    output_file = str(sys.argv[3])
    
    parse(config_file, input_file, output_file)
    
  
    

#test cases
#header on/off
#commas
#trim
#extra characters
#input encoding
#output encoding