#!/usr/bin/env python3

import sys

_file = sys.argv[1]
ini_file = None 
try:
  ini_file = sys.argv[2]
except:
  ini_file = "texstudio.ini"
finally:
  if ini_file == None:
    ini_file = "texstudio.ini"
  try:
    origin = open(ini_file, "r").readlines()
  except:
    print("File " + ini_file + " does not exist")
  else:
    file_content = open(_file, "r").readlines()
    for line in range(0, len(file_content)):
        items = file_content[line].split('=')
        if len(items) > 0:
            command = items[0]
            for line_ini in range(0, len(origin)):
                or_items = origin[line_ini].split('=')
                if len(or_items) > 0:
                    or_command = or_items[0]
                    if or_command == command:
                        origin[line_ini] = file_content[line]
                        break

    to_write = open(ini_file, "w")
    to_write.writelines(origin)
    to_write.close()
