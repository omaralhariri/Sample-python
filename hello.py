import math
import os
import sys
from urllib import request

import requests

print(sys.version)
# print(sys.version_info)
print(sys.executable)

r = requests.get("http://python.org")
print(r.status_code)

name = "omar"


def main():
    print("hey {}!".format(name))


if __name__ == "__main__":
    main()
