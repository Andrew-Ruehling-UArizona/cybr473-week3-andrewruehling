'''
Scripting Assignment #3 - Creating a File Processing Object

---
Scenario:

You find that you have to often read and process files for your investigation.
You want to create a class that can be easily used for your cyber team.
The File Processor class will extract relevant data for you without having to repeat code.

---

To start, review the examples in the examples folder and expand on them.

1) Create a class named FileProcessor and place it in file_processor.py 
   a) Create an Init method that takes in a filename as you deem appropriate.
   The method will:
      i) Verify the file exists
      ii) Extract key file system metadata from the file
          and store them as instance attributes.
          At a minimum, extract:
           - File Path
           - File Size
           - Created On Date
           - Last Access Date
           - Last Modified Date
           - Type
          (If any of this metadata cannot be extracted, elegantly handle the missing data)
   b) Create a get_file_header Method which will
      i) Extract the first 20 bytes of the header and store them in an instance attribute
   c) Create a print_file_details Method which will
      i) Print the metadata
      ii) Print the hex representation of the header
      iii) Outputs everything in a Pretty Table

2) Demonstrate the use of the new class by importing it below and:
   a) prompt the user for a directory path (use the examples directory for testing and for your submission)
   b) using the os.walk() method extract the filenames from the directory path and the subdirectories
   c) Loop through each filename and instantiate an object using the FileProcessor Class
   d) Using the object
      i) invoke the get_file_header Method
      ii) invoke the print_file_details Method
      
3) Submit
   A) Screenshot of the final result in your IDE showing one file's details
   B) Copy and paste your entire output into a .txt file as you processed all the files in the examples folder.
   C) Your Scripts (This File Edited and file_processor.py completed)
'''

from file_processor import FileProcessor





        
        