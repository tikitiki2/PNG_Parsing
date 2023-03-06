#check if there is an input
import struct
def read_chunk(file):
    # read the length of the next chunk
    length_bytes = file.read(4)
    length = int.from_bytes(length_bytes, byteorder='big')
    # read the chunk type
    chunk_type = file.read(4)
    # read the chunk data
    chunk_data = file.read(length)
    # read the CRC checksum
    crc_bytes = file.read(4)
    crc = int.from_bytes(crc_bytes, byteorder='big')
    # return the chunk type and data size
    return chunk_type, length,chunk_data,crc_bytes

def save_chunks(file):
    chunks = []
    # read all bytes in file and save to a list so that we can now acces all the bytes and write into them
    while True:
        chunk_type, size, chunk_data, crc = read_chunk(file)

        chunk = {
            'length': size,
            'type': chunk_type,
            'data': chunk_data,
            'crc': crc,
        }
        chunks.append(chunk)
        if chunk_type == b'IEND':
            break
    return chunks
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)