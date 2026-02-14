filename = input("Enter the filename: ").strip().lower()
def get_extension(filename):
    if '.' in filename and filename.count('.') == 1:
        name, extension = filename.split('.')
        return extension
    elif '.' in filename and filename.count('.') > 1:
        name, extension = filename.rsplit('.', 1)
        return extension
    else:
        return 'bin'

match get_extension(filename):
    case 'pdf':
        print("application/pdf")
    case 'txt':
        print("text/plain")
    case 'jpg' | 'jpeg':
        print("image/jpeg")
    case 'png':
        print("image/png")
    case 'gif':
        print("image/gif")
    case 'zip':
        print("application/zip")
    case 'bin':
        print("application/octet-stream")
    case '_':
        print("Unknown file type")

#Amma's code:
#filename = input("Enter the filename: ")
#get the rightmost extenstion fromm the string splits
#extension = filename.split('.')[-1]
#print (extension)
#match extension:
   # case 'gif' | 'jpg' | 'jpeg' | 'png':
   #     print(f"image/{extension}")
   # case 'pdf' | 'zip':
   #     print(f"application/{extension}")
   # case 'txt':
   #     print(f"text/{extension}")
   # case _:
   #     print("application/octet-stream")

