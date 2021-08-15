import hashlib
import sys
import os

def file_as_bytes(var, var2):
    with open(var, 'r') as f:
        files = [i for i in [j[2] for j in os.walk(var2)][0]] #files in directory
        text = f.readlines() #read file with hash-sum
        for i in range(len(text)):
            name_file = text[i].split()[0]
            encoding = text[i].split()[1]
            hash_sum = text[i].split()[2]

            for name in files: #search matches for file name and file name in a directory
                if name == name_file:
                    name_file_directory = name
                    break

            if name_file_directory != name_file:
                print(f"{name_file} NOT FOUND")
                continue
            else:
                #hash-sum of files in directory
                if encoding == "md5":
                    hash_file = list(hashlib.md5(open(f"{os.path.join(var2, name_file_directory)}", "rb").read()).hexdigest())
                elif encoding == "sha1":
                    hash_file = list(hashlib.sha1(open(f"{os.path.join(var2, name_file_directory)}", "rb").read()).hexdigest())
                elif encoding == "sha256":
                    hash_file = list(hashlib.sha256(open(f"{os.path.join(var2, name_file_directory)}", "rb").read()).hexdigest())

                if hash_sum == "".join(hash_file):
                    print(f"{name_file} OK")
                elif hash_sum != "".join(hash_file):
                    print(f"{name_file} FAIL")
        return


file_as_bytes(sys.argv[1], sys.argv[2])
