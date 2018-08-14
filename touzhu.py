#!/usr/bin/env python

import os
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print "ERROR: the parameters you putting is less than 3"
        sys.exit(1)

    odds1 = float(sys.argv[1])
    putting_sum_one = float(sys.argv[2])
    odds2 = float(sys.argv[3])
    one_rate = 1.03
    two_rate = 1.03
    one_back_rate = 0.014
    two_back_rate = 0.014


    getting_sum_one = putting_sum_one * odds1 * one_rate

    putting_sum_two = getting_sum_one/odds2

    getting_sum_two = putting_sum_two * odds2

    back_rate = putting_sum_one * one_rate * one_back_rate + putting_sum_two * two_back_rate
    
    gain_one_side = getting_sum_one - putting_sum_one - putting_sum_two/two_rate + back_rate
    gain_another_side = getting_sum_two - putting_sum_one - putting_sum_two/two_rate + back_rate

    print "one side: (%s + %s) * %s = %s, gain %s" % (putting_sum_one, putting_sum_one * (one_rate - 1)odds1, getting_sum_one, gain_one_side)
    print "another side: (%s + %s) * %s = %s, gain %s" % (putting_sum_two/two_rate, putting_sum_two/two_rate * (two_rate - 1)odds2, getting_sum_two, gain_another_side)
