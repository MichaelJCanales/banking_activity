"""
A validation script to check if your data-analysis pipeline is operating as
intended.

To test the first part of your code, run:

python -m code.test.validate pt1

To test the first two parts of your pipeline, run:

python -m code.test.validate pt2

To test all the three parts of your pipeline, run:

python -m code.test.validate pt3

while in the `code/test` folder to test the completeness of your code.

The terminal output will tell you if your pipeline is successful.
"""
import sys
import os
from code.StockMetrics import StockMetrics



OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

file_path = os.path.join(".""data", "raw", "amzn.csv")
metrics = StockMetrics(r"C:\\Users\\Michael\\bank-activity\\data\\raw\\amzn.csv")

def pt1():
    # try to compute average
    try:
        avg_list = metrics.average01()
    except Exception as e:
        print(f"{FAIL}PT1 fails: exception occured: {e}{ENDC}")
        return 0

    # check if each row is correctly calculated
    ans = [96.639, 89.749, 90.540, 95.844, 96.468,
           101.187, 115.431, 118.949, 117.713]
    if avg_list != ans:
        print(f"{FAIL}PT1 fails: expected {ans}.\nRecieved {avg_list}{ENDC}")
        return 0

    print(f"{OKGREEN}PT1 passes! Nice work.{ENDC}")
    return 1


def pt2():
    # try to compute median
    try:
        med_list = metrics.median02()
    except Exception as e:
        print(f"{FAIL}PT2 fails: exception occured: {e}{ENDC}")
        return 0

    ans = [96.2015, 90.030502, 91.5, 95.141502, 95.941498, 
           101.359001, 115.384003, 119.680496, 118.635498]
    if med_list != ans:
        print(f"{FAIL}PT2 fails: expected {ans}.\nRecieved {med_list}{ENDC}")
        return 0

    # confirm to tester that all looks good!
    print(f"{OKGREEN}PT2 passes! Great job.{ENDC}")
    return 1


def pt3():
    # attempt to compute sample std-dev
    try:
        dev_list = metrics.stddev03()
    except Exception as e:
        print(f"{FAIL}PT3 fails: exception occured: {e}{ENDC}")
        return 0

    ans = [1.571, 3.888, 3.652, 1.473, 1.301, 1.142, 4.643, 1.665, 1.742]
    if dev_list != ans:
        print(f"{FAIL}PT3 fails: expected {ans}.\nRecieved {dev_list}{ENDC}")
        return 0

    # confirm to tester that all looks good!
    print(f"{OKGREEN}PT3 passes! You're the 🐐{ENDC}")
    return 1


if __name__ == "__main__":
    # run appropriate sections based on args
    if len(sys.argv) != 2:
        print(f"{FAIL}Error: Missing part of project to run.\
               \nUsage: python validate.py pt[1|2|3]{ENDC}")
    else:
        if sys.argv[1] == "pt1":
            pt1()
        elif sys.argv[1] == "pt2":
            pt1()
            pt2()
        elif sys.argv[1] == "pt3":
            pt1()
            pt2()
            pt3()
