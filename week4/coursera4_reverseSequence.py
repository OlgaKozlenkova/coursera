def rev_seq():
    n = int(input())
    if n != 0:
        rev_seq()
        print(n)
    else:
        print(0)


rev_seq()
