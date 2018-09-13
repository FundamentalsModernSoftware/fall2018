import sys
if len(sys.argv) < 3:
    print('Too few arguments!')
elif len(sys.argv) > 3:
    print('Too many arguments!')
else:
    a = sys.argv[1]
    b = sys.argv[2]
    print(int(a) + int(b))
