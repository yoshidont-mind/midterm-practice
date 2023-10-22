def main():
    seconds = 10
    for number in range(10):
        seconds -= 1
    if seconds:
        print("Wait", seconds, "seconds")
    else:
        print("The exam is over in", seconds, "seconds")

if __name__ == "__main__":
    main()
