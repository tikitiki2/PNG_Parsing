import zlib
import struct
import func

# main
# get file path check if file path is provided
file_path=input('enter file path: ')
tempe=func.find(file_path,'D:')
print(tempe)
if not file_path:
    print('no input file is provided')
    exit(1)

input_file=file_path
#try to open the file and catch any errors while doing so
try:
    file=open(input_file,'rb+')
except Exception as e :
    print('error occured while trying to open file path: ', e)
    exit(1)

# read header to check if it is png type
png_sig=[137, 80, 78, 71, 13, 10, 26, 10]
sig=file.read(8)

if list(sig)!=png_sig:
    print(f'{input_file} is not a valid png or is corrupted')
    exit(1)
print('file accepted')

# save chunks to chunk list
try:
    chunks=func.save_chunks(file)
except Exception as e:
    print(e)
    exit(1)
print('read_chunks is successful')


#rebuild png but add hello world after the IEND chunk
secret=input('enter secret to add to file: ')
if not secret:
    print('no input detected')
    exit(1)
temp=' '+secret
secret=b'secret'
#create a new chunk to add
try:
    compressed=temp.encode('utf-8')
    length=len(compressed)
    type=b'secret'
    crc=zlib.crc32(type+compressed).to_bytes(4,byteorder='big')
    new_chunk = length.to_bytes(4, byteorder='big') + type + compressed + crc
except Exception as e:
    print(e)
#write to end of file
file.write(new_chunk)
print('successfully added secret message at the end of the PNG image data')