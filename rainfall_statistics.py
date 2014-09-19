__author__ = 'dwight'

# Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program should
# calculate and display the total rainfall for the year, the average monthly rainfall, and the months with the highest
# and lowest amounts.

import validate


MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')


def main():
    print('Rainfall Statistics Calculator\n' + '-------------------------------')
    monthly_rainfall = input_monthly_rainfall()
    print('\nTotal Rainfall: ' + str(calc_total_rainfall(monthly_rainfall)) + ' inches')
    print('Average Rainfall: ' + str(calc_average_monthly_rainfall(monthly_rainfall)) + ' inches')

    high_month = MONTHS[monthly_rainfall.index(max(monthly_rainfall))]
    low_month = MONTHS[monthly_rainfall.index(min(monthly_rainfall))]
    print('Month with highest rainfall: ' + high_month)
    print('Month with lowest rainfall: ' + low_month)


def input_monthly_rainfall():
    rainfall_list = [0] * len(MONTHS)

    for index in range(len(rainfall_list)):
        month_rainfall = input('Enter rainfall for ' + MONTHS[index] + ' (inches): ')
        rainfall_list[index] = float(validate.validate_rainfall(month_rainfall, MONTHS[index]))

    return tuple(rainfall_list)

def calc_total_rainfall(monthly_rainfall_list):
    total_rainfall = 0

    for month in monthly_rainfall_list:
        total_rainfall += month

    return total_rainfall


def calc_average_monthly_rainfall(monthly_rainfall_list):
    return calc_total_rainfall(monthly_rainfall_list) / len(monthly_rainfall_list)


main()