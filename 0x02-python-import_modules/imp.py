#!/usr/bin/python3
# import os
# os.write(1,b'#pythoniscool\n')

# __import__('os').write(1,b'#pythoniscool\n')
imp = __import__('os').write
print(imp(1,b'#pythoniscool\n'))
