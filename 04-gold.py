print(sum(len(l.split(" "))==len(set("".join(sorted(s))for s in l.split(" ")))for l in map(str.strip, __import__("sys").stdin.readlines())))
