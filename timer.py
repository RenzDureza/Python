import time


def timer(t):
    while t:
        min, sec = divmod(t, 60)
        displayTime = '{:02d}:{:02d}'.format(min, sec)
        print(displayTime, end="\r")
        time.sleep(1)
        t -= 1

    print("Times Up!!")


def main():
    t = int(input("Enter the time in seconds: "))
    timer(t)


if __name__ == "__main__":
    main()
