import statistics
agesData = [10, 13, 14, 12, 11, 10, 11, 15]
"""
mean: 12.000000
median: 11.500000
"""
print('mean: %f' % statistics.mean(agesData))
print('median: %f' % statistics.median(agesData))

print('variance: %f' % statistics.variance(agesData)) # variance: 3.428571
print('std: %f' % statistics.stdev(agesData)) # std: 1.851640

