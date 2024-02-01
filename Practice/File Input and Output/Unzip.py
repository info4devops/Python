# Program to unzip zip files

from zipfile import*
f=ZipFile('files.zip','r',ZIP_STORED)
names = f.namelist()
for name in names:
  print(name)
  f1=open(name,'r')
  print(f1.read())
  print()