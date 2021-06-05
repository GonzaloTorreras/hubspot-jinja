import os

from hsJinja.hsJinja import hsJinja

TEMPLATES = os.path.join(os.getcwd(), "templates")
OUTPUT = os.path.join(os.getcwd(), "output")
print(TEMPLATES)
test = hsJinja(TEMPLATES,OUTPUT)

test.main()
