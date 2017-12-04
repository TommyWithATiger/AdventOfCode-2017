print(sum(len(l.split(" "))==len(set(l.split(" ")))for l in map(str.strip, __import__("sys").stdin.readlines())))
