import re

# https://pynative.com/python-regex-metacharacters/

def camelCase(s):
    
    splitted_list = re.split('(?=[A-Z])', s)
    print(splitted_list)
    return len(splitted_list)


s = 'saveChangesInTheEditor'
print(camelCase(s))
    