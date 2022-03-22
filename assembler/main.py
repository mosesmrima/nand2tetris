#!/usr/bin/python3
import sys
from parser import strip_space
from parser import assemble


def main():
    asm_path = sys.argv[1]
    hack_path = asm_path.replace(".asm", ".hack")

    with open(asm_path, "rt") as f, open(hack_path, "wt") as h:
        lines = f.readlines()
        for line in lines:
            if line.isspace() or (line.strip().startswith("//")):
                pass
            else:
                line = strip_space(line)
                line = assemble(line)
                h.write(line + "\n")


if __name__ == "__main__":
    main()
