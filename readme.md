Latitude Coding
Chris Lim
24/07/2021
Developed and tested on Python 3.9.6

Dependencies - pytest

usage - python ffp.py <config_file> <input_file> <output_file>

<config_file> - path/filename of JSON config/spec file
<input_file>  - fixed file to parse
<output_file> - output filename and path

Test cases have been implemented via Pytest in the test_ffp.py file

Included dockerfile executes the test cases via pytest. To run manually please use the run the dockerfile with /bin/bash

Assumption that any commas in the actual data itself would be escaped per column as per the Python CSV writer