def j(arg1, arg2):
    whole = arg1 + arg2
    whole = set(whole)
    arg1 = set(arg1)
    arg2 = set(arg2)
    intersection = arg1 & arg2

    return len(intersection)/float(len(whole))

