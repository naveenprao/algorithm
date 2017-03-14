import os

def say_hello():
    print 'Hello, World'

for i in xrange(5):
    say_hello()



# file with filename='/a.txt', -> [hqwnfqef]
# buf - array of bytes - [f, q]
# file_contains('/a.txt', ['f', 'q']) -> True
#

def file_contains(filename, buf): # True when file contains buf, otherwise false

# [a, b, c]
# b * pow(prime_number, pos_of_b)
# a * pow(prime, 0) + b * pow(prime, 1) + c * pow(prime, 2)  + d * pow(prime, 3)

# additive hash
# hash = ord(a) + ord(b) + ord(c)    // hash ( 'abc' )
# hash -= ord(a)
# hash += ord(d)                     // hash ( 'bcd' )


file_data = list()
# read file data into file_data

buf = list()
# read buf from user input

# assuming file data can fit in memory, search for buf in file
def file_contains(filedata, buf):
    buf_hash = getHash(buf)
    for i in xrange(len(file_data)-len(buf)):                    # 0..
        file_chunk_hash = getHash(file_data[i:i+len(buf)])
        if buf_hash == file_chunk_hash:
            match=compare_bytes(buf, file_data[i:i+len(buf)])    # Actual comparision 
            if match:
                return True
    return False

# function to get additive hash
def getHash(byte_array):
    return ord(byte_array)

# function that would make a byte by byte comparision
def compare_bytes(first, sec):
    return first == sec

# seeks to file_seek location and reads size bytes from file
# returns None if seek location is beyond file end.
def getFileChunk(file_handle, seek_loc, size):
    file_handle.seek(seek_loc)
    return file.handle.read(size)


total_file_size = 1000    # get from file metadata
memory_size = 100         # get from sys properties

file_seek_location = 0
file_handle = os.open(file_path)
while True:
    file_chunk = getFileChunk(file_handle, file_seek_location, memory_size)
    if file_chunk:
        found = file_contains(file_chunk, match_buf)
        if found:
            return True
        else:
            file_seek_location = file_seek_location + memory_size - len(match_buf)
    else:
        return False


# file_contains(file_data[0:99], buf)
# file_contains(file_data[99-len(buf): 99-len(buf)+99]


