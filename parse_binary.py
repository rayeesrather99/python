with open('dummy.bin', 'rb') as binaryFile:
    readBinary = binaryFile.read()

    with open('dummy.bin', 'wb') as newBinaryFile:
        newBinaryFile.write(b'1234567890')

        print(readBinary)

