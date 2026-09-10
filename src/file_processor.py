import os
'''
File Processor Class and usage example
'''
from __future__ import print_function

import os
import time
from prettytable import PrettyTable

# Your File Processor Class Goes Here

class FileProcessor:
    def __init__(self):
        self.filePath = ''
        self.file_size = ''
        self.created_on = ''
        self.last_accessed = ''
        self.last_modified = ''
        self.file_type = ''
        self.header = ''
        self.HEADER_SIZE = 20
        self.last_err = ''

#Getting the necessary data from files for assignment

    def set_file_path(self, file_path):
        ''' Set the file path if valid
                 Obtain file system metadata from the file
                 return True if valid and set the self.file_path object variable
             '''
        if os.path.isfile(file_path):
            if os.access(file_path, os.R_OK):
                self.file_path = file_path
                stats = os.stat(self.file_path)  # Check Out https://docs.python.org/3/library/os.html#os.stat
                self.file_size = stats.st_size
                self.created_on = time.ctime(stats.st_ctime)
                self.last_accessed = time.ctime(stats.st_atime)
                self.last_modified = time.ctime(stats.st_mtime)
                if '.' in self.file_path:
                    self.file_type = self.file_path.split('.')[-1]
                else:
                    self.file_type = 'No Extension'
                self.last_err = ''
                return True
            else:
                self.file_path = ''
                self.last_err = 'Invalid File Path'
                return False
        else:
            self.file_path = ''
            self.last_err = 'File Does Not Exist'
            return False