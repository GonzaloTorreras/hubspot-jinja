import os

from hsJinja.hsJinja import hsJinja

TEMPLATES = os.getcwd() + "templates"
OUTPUT = "output"
print(TEMPLATES)
test = hsJinja(TEMPLATES,OUTPUT)

test.main()
