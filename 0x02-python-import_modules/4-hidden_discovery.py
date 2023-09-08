#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    #printing all names sorted from directory
    for name in sorted(dir(hidden_4)):
        #ignoring names that start with __
        if name[:2] != '__':
            print("{}".format(name))
