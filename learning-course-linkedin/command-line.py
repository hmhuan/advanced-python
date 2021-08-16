import sys

# Command line arguments
print('number of arguments: ', len(sys.argv))

print('arguments: ', sys.argv)

sys.argv.remove(sys.argv[0])
print('arguments: ', sys.argv)
