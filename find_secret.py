
import func
file_path=input('enter file path: ')
func.validate(file_path)

file=open(file_path,'rb')

chunks=func.save_chunks(file,file_path)
for index,val in enumerate(chunks):
    if val['type']==b'IEND':
        endindex=index
        break
for i in range(endindex,len(chunks)):
    print(chunks[i])







