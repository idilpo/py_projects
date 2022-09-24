print(dir(__builtins__)) # for viewing built-in namespaces

import random

first_name = "Jaya"
last_name = "Bodegard"

def print_variables():
    random_number = random.randint(0, 9)
    print(first_name)
    print(last_name)
    print(random_number)

print(globals()) # globals() --> for global namespaces
print()



print(' -- Globals Namespace with empty script -- \n')
print(globals())

global_variable = "global"

def print_global():
  global_variable = "nested global"
  nested_variable = 'nested value'


print(' \n -- Globals Namespace non-empty script -- \n')
print(globals())



