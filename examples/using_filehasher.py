# Using the File Hasher Class
from examples.filehasher_class import FileHasher

print("Hash File Class Demonstration\n")

file_name = input("Enter file to hash: ")

obj = FileHasher()

print("\nProcessing File ...\n")

if obj.set_file_path(file_name):
    if obj.set_hash_type('SHA256'):
        if obj.hash_file():
            print("Path:               ", obj.file_path)
            print("File Size:          ", '{:,}'.format(obj.file_size), "Bytes")
            print("File Created Time:  ", obj.create_time)
            print("File Modified Time: ", obj.modified_time)
            print("Hash Type:          ", obj.hash_type)
            print("Hash Value:         ", obj.file_hash)
        else:
            print("Hashing Failed: ", obj.last_err)
    else:
        print("Failed to Set HashType: ", obj.last_err)
else:
    print("File Name Error: ", obj.last_err)

print("\nScript End")
