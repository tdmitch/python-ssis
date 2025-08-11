def do_fail():
    print("Doing stuff...")
    print("Bad math: " + str(1/0))
    print("Stuff done!")

if __name__ == "__main__":
    do_fail()
    