#! -*- code: utf-8 -*-

import sys

def main():
    print(f"Name of the script       :  {sys.argv[0]}")
    print(f"Arguments of the script :  {sys.argv[1:]}")
    
if __name__ == "__main__":
    main()

