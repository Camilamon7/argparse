import argparse
from statistics import mean, median

""" 
Write a command line tool that accepts a list of (one or more) 
numbers and returns their mean by default or, if the '-m' or '--median'
options are included, their median instead.

The mean and median functions from the statistics module have been
included for you.
"""
def mean(nums: list):
      return sum(nums) / len(nums)
def median(nums: list):
      nums.sort()
      n = len(nums)
      if n % 2 == 0:
              median1 = nums[n//2]
              median2 = nums [n//2 -1]
              median = (median1 + median2)/2
      else:
              median = nums[n//2]
      return median


parser = argparse.ArgumentParser(description='Does some math.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('-m', '--median', dest='accumulate', action='store_const',
                    const=median, default=mean,
                    help='find the median (default: find the mean)')

args = parser.parse_args()
print(args.accumulate(args.integers))
