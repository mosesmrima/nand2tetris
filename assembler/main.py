#!/usr/bin/python3
import sys
from parser import strip_space
from parser import assemble


def main():
    path = sys.argv[1]
    with open(path, "r") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            if line.isspace() or (line.strip().startswith("//")):
                pass
            else:
                line = strip_space(line)
                print(assemble(line))


if __name__ == "__main__":
    main()
