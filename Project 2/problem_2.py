# -*- coding: utf-8 -*-
import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    assert suffix, 'provide valid suffix to search file type'
    assert path, 'Invalid path provided'
    files = []
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            files.append(path)
    elif os.path.isdir(path):
        for file in os.listdir(path):
            files.extend(find_files(suffix, os.path.join( path, file )))
    
    return files
        



# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))
#False

# Does the file end with .py?
print ("./ex.py".endswith(".py"))
#True

print( find_files('.c', './testdir') )
#['./testdir\\subdir1\\a.c', './testdir\\subdir3\\subsubdir1\\b.c', './testdir\\subdir5\\a.c', './testdir\\t1.c']

print( find_files('.h', './testdir') )
#['./testdir\\subdir1\\a.h', './testdir\\subdir3\\subsubdir1\\b.h', './testdir\\subdir5\\a.h', './testdir\\t1.h']

print( find_files('.py', './testdir') )
#[]

#print( find_files('', './testdir') )
#AssertionError: provide valid suffix to search file type

#print( find_files(None, './testdir') )
# AssertionError; provide valid suffix to search file type

#print(find_files ('.h', None))
# AssertionError: Invalid path provided