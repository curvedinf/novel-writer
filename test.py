import sys

from writer import LlamacppWriter

writer = LlamacppWriter()
response = writer.write(sys.argv[1])
print(response)
