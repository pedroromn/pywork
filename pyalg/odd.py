# python3
from datetime import datetime
import random
import time

def main():
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
            21, 23, 25, 27, 29, 31, 33, 35, 37,
            39, 41, 43, 45, 47, 49, 51, 53, 57, 59]

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute")

    wait_time = random.randint(1, 60)
    #print(wait_time)
    time.sleep(wait_time)

if __name__ == "__main__":
    main()
