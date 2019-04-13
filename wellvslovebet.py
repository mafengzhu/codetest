
#!/usr/bin/env python

import os
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 4:
        print "ERROR: the parameters you putting is less than 3"
        sys.exit(1)

    odds1 = float(sys.argv[1])
    putting_one = float(sys.argv[3])
    odds2 = float(sys.argv[2])
    wellbet_rate = flaot(sys.argv[4])
    
    sum_one = putting_one * odds1 + putting_one * wellbet_rate

    putting_another = sum_one/(odds2 - 0.03)

    get_one = sum_one + 0.03 * putting_another - putting_one - putthing_another

    get_another = putting_another * odds2 - putting_one - putting_another + 114

    print "%s * %s, get %s" %(putting_one, odds1, get_one)
    print "%s * %s, get %s" %(putting_another, odds2, get_another)



