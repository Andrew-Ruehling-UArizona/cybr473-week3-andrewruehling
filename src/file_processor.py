'''
Scripting Assignment #3 - File Processor
CYBR 473 - Violent Python
Andrew Ruehling
11 Sep 2026
'''
from __future__ import print_function

import os
import time
from prettytable import PrettyTable

# empty variables for now, filled in once file is actually processed

class FileProcessor:
    def __init__(self):
        self.file_path = ''
        self.file_size = ''
        self.created_on = ''
        self.last_accessed = ''
        self.last_modified = ''
        self.file_type = ''
        self.header = ''
        self.HEADER_SIZE = 20
        self.last_err = ''

# checks the path is real and readable, then grabs the metadata off it

    def set_file_path(self, file_path):
        ''' Set the file path if valid
                 Obtain file system metadata from the file
                 return True if valid and set the self.file_path object variable
             '''
        if os.path.isfile(file_path):
            if os.access(file_path, os.R_OK):
                self.file_path = file_path
                stats = os.stat(self.file_path)
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


# grabs first 20 bytes of the file

    def get_file_header(self):
        try:
            with open(self.file_path, 'rb') as file_to_read:
                self.header = file_to_read.read(self.HEADER_SIZE)
                self.last_err = ''
                return True
        except Exception as err:
            self.header = ''
            self.last_err = str(err)
            return False

# dumps everything into a table, header gets converted to hex here

    def print_file_details(self):
        ''' Print the metadata and the header, in hex, as a PrettyTable '''
        tbl = PrettyTable(['Attribute', 'Value'])

        tbl.add_row(['File Path', self.file_path])
        tbl.add_row(['File Size', self.file_size])
        tbl.add_row(['Created On', self.created_on])
        tbl.add_row(['Last Accessed', self.last_accessed])
        tbl.add_row(['Last Modified', self.last_modified])
        tbl.add_row(['Type', self.file_type])
        if self.header:
            header_hex = self.header.hex()
        else:
            header_hex = 'N/A'
        tbl.add_row(['Header (hex)', header_hex])

        tbl.align = "l"
        result_string = tbl.get_string()
        print(result_string)