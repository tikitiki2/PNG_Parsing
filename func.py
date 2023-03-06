#check if there is an input
import struct
def read_chunk(file):
    # read the length of the next chunk
    length_bytes = file.read(4)
    
    length = int.from_bytes(length_bytes, byteorder='big')
    
    #this print returns 2303741511 which is the size of the file it should be a much lower number for each chunk
    # read the chunk type
    chunk_type = file.read(4)
    # read the chunk data
    chunk_data = file.read(length)
    # read the CRC checksum
    crc_bytes = file.read(4)
    crc = int.from_bytes(crc_bytes, byteorder='big')
    # return the chunk type and data size
    
    return chunk_type, length,chunk_data,crc_bytes
import time
def save_chunks(file,file_path):
    validate(file_path)
    file.seek(8)
    chunks = []
    while True:
        chunk_type, size, chunk_data, crc = read_chunk(file)

        if not chunk_type:
            break
        
        chunk = {
            'length': size,
            'type': chunk_type,
            'data': chunk_data,
            'crc': crc,
        }
        chunks.append(chunk)

    return chunks



def validate(file_path):

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
        print(f'the sig provided was {list(sig)}')
        print(f'{input_file} is not a valid png or is corrupted')
        exit(1)
    file.close()
    print('file accepted')
    return file_path
    