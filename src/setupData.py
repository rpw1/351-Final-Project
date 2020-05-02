import gzip

# This file is used to decompress the mnist dataset files

with gzip.open('./compressedData/train-images-idx3-ubyte.gz', 'rb') as f:
    file_content = f.read()
    new_file = open('./mnistData/train-images-idx3-ubyte', 'wb')
    new_file.write(file_content)

with gzip.open('./compressedData/train-labels-idx1-ubyte.gz', 'rb') as f:
    file_content = f.read()
    new_file = open('./mnistData/train-labels-idx1-ubyte', 'wb')
    new_file.write(file_content)

with gzip.open('./compressedData/t10k-images-idx3-ubyte.gz', 'rb') as f:
    file_content = f.read()
    new_file = open('./mnistData/t10k-images-idx3-ubyte', 'wb')
    new_file.write(file_content)

with gzip.open('./compressedData/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    file_content = f.read()
    new_file = open('./mnistData/t10k-labels-idx1-ubyte', 'wb')
    new_file.write(file_content)