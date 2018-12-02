try:
    f = open('mytextfile.txt', 'w')
    # f = open('mytextfile.txt', 'r')
    f.write("Hello, how are you?")
except IOError:
    print("Something went wrong")
else:
    print("Success!")
finally:
    f.close()
