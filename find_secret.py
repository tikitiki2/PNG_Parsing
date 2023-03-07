import zlib
import func
file_path=input('enter file path: ')
func.validate(file_path)

file=open(file_path,'rb')

chunks=func.save_chunks(file,file_path)

for index,val in enumerate(chunks):
    if val['type']==b'IEND':
        endindex=index
        break
    print(val)
message=chunks[-1]

if not message:
    print('could not find any chunks at end of file')
    exit(1)
print(message['data'])








