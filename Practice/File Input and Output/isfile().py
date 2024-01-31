# Check the particular file is available of not
# for the we should us os.path.isfile(fname)

import os,sys
fname=input('Enter file name: ')
if os.path.isfile(fname):
  print(f'The file:{fname} is available')
else:
  print(f'The file:{fname} is not available')
  sys.exit(0)
