#!/usr/bin/env python

import os
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print "ERROR: the parameters you putting is less than 3"
        sys.exit(1)

    odds1 = sys.argv[1]
    putting_sum_one = sys.argv[2]
    odds2 = sys.argv[3]

    getting_sum_one = putting_sum_one * odds1

    putting_sum_two = odds1/odds2 * putting_sum_one

    getting_sum_two = putting_sum_two * odds1
    gain_one_side = getting_sum_one - putting_sum_one
    gain_another_side = getting_sum_two - putting_sum_two

    print "one side: %s * %s = %s, gain %s" % (putting_sum_one, odds1, getting_sum_one, gain_one_side)
    print "another side: %s * %s = %s, gain %s" % (putting_sum_two, odds2, getting_sum_two, gain_another_side)
