import zlib
import struct
import func

# main
# get file path check if file path is provided
file=func.validate()


#rebuild png but add hello world after the IEND chunk
secret=input('enter secret to add to file: ')
if not secret:
    print('no input detected')
    exit(1)
temp=' '+secret

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
exit(0)