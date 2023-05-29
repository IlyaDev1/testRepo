from lib import Window
from lib2 import User


bd = [User() for i in range(10)]
bd[0].name = 'ilya'
print(bd[0].name)
