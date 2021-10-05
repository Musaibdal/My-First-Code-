def input_stats(filename):
    text=open(filename)
    f = text.readlines()
    longest = ""
    for i in f:
        if len(i) > len(longest):
            longest = i

    print("longest line = ", len(longest))
    print(longest)
m="carroll.txt"
n=input_stats(m)