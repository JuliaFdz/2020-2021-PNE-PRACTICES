from pathlib import Path
FILENAME = "RNU6_269P"


#1)
text = Path(FILENAME).read_text()
lines = text.split('\n')
print(lines[0])

#2)
#text = Path(FILENAME).open()
#lines = text.readline()
#print(lines)

#3)
