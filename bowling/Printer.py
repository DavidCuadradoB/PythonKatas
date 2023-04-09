def print_frames(frames):
    print("GAME!")
    for i, frame in enumerate(frames):
        print("Turn {}".format(i+1))
        if frame.is_strike():
            print("X")
        elif frame.is_spare():
            print("{}/".format(frame.firstTry))
        elif frame.firstTry == 0 and frame.secondTry > 0:
            print("-{}".format(frame.secondTry))
        elif frame.firstTry > 0 and frame.secondTry == 0:
            print("{}-".format(frame.firstTry))
        else:
            print("--")



