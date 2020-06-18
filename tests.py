import sys
from models.country import Country
from tools.reader import Reader

try:
  pais = Country(sys.argv[1])
  print(pais.str_format())
except AssertionError as err:
  print(err)


