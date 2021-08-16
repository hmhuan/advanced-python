import tempfile
# create temp file
tempFile = tempfile.TemporaryFile()

tempFile.write(b"Save this special number for me: 12345678")
tempFile.seek(0)
# read from temp file
print(tempFile.read())

tempFile.close()