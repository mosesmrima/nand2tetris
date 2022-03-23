#!/usr/bin/python3
import sys

from symbols import labels, initialize
from symbols import variables
from parser import strip_space
from parser import assemble


def main():
    asm_path = sys.argv[1]
    hack_path = asm_path.replace(".asm", ".hack")
    symbol_table = initialize()
    with open(asm_path, "rt") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            if line.isspace() or (line.strip().startswith("//")):
                pass
            else:
                line = strip_space(line)
                key = labels(line)
                if key is not None:
                    symbol_table.update({key: count})
                count = count if line.startswith("(") else count + 1

        free = 16
        for line in lines:
            if line.isspace() or (line.strip().startswith("//")):
                pass
            else:
                line = strip_space(line)
                key = variables(line, symbol_table)
                if key is not None:
                    symbol_table.update({key: free})
                    free += 1
                    try:
                        int(key)
                        symbol_table.pop(key)
                        free -= 1
                    except ValueError:
                        pass

    with open(asm_path, "rt") as f, open(hack_path, "wt") as h:
        lines = f.readlines()
        for line in lines:
            if line.isspace() or (line.strip().startswith("//")):
                pass
            else:
                line = strip_space(line)
                if not line.strip().startswith("("):
                    line = assemble(line, symbol_table)
                    h.write(line + "\n")


if __name__ == "__main__":
    main()
