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
    def set_file_path(self, file_path):