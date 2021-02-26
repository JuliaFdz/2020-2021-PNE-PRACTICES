from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P"

# -- Open and read the file
file = Path(FILENAME).open()

# -- Print the contents on the console
print(file)





#ORIGINAAAAAL:
# -- Constant with the new of the file to open
#FILENAME = "RNU6_269P"

# -- Open and read the file
#file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
#print(file_contents)



#FILENAME = "RNU6_269P"

#1)
#try:
#    file_contents = Path(FILENAME).read_text()
#    print(file_contents)
#except FileNotFoundError:
#    print('Something wrong has happend.')

#2)
#f = open(FILENAME, 'r')
#data = f.read()
#print(data)

#3)
#with open(FILENAME) as reader:
#    print(reader.read())


