#
# Example file for working with conditional statements
#


def main():
    x, y = 1000, 1000

    # conditional flow uses if, elif, else
    if(y<x):
        st="x is less than y"
    elif (x==y):
        st="x is equal to y"
    else:
        st="y is greater than y"

    print(st)

    # conditional statements let you use "a if C else b"
    st="x is less than y" if(x>y) else "x is hello"
    print(st)

if __name__ == "__main__":
    main()
