#!/usr/bin/env python3

import sys
try:
    salary = int(sys.argv[1])
    salary_tax = salary - 3500

    if salary_tax <= 1500:
        tax = salary_tax * 0.03
    elif salary_tax > 1500 and salary_tax <= 4500:
        tax = salary_tax * 0.1 - 105
    elif salary_tax > 4500 and salary_tax <= 9000:
        tax = salary_tax * 0.2 - 555
    elif salary_tax > 9000 and salary_tax <= 35000:
        tax = salary_tax * 0.25 - 1005
    elif salary_tax > 35000 and salary <= 55000:
        tax = salary_tax * 0.3 - 2755
    elif salary_tax > 55000 and salary <= 80000:
        tax = salary_tax * 0.35 - 5505
    else:
        tax = salary_tax * 0.45 - 13505
    print(format(tax, ".2f"))
except:
    print("Parameter Error")
