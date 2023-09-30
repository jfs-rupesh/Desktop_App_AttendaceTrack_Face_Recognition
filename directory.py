import sys
import os
def create(dir):
    dirname=dir
    cur=os.getcwd()
    print(cur)
    path='C:\Python27\faceverification\dataSet'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
		
