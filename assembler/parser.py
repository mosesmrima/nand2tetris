import re

from code import destination, jump, computation


def strip_space(line):
    """
    This functions strips trailing white spaces & trailing comments
    :param line: the line to strip
    :return: return the stripped line
    """
    head, part, tail = line.partition("//")
    return head.strip()


def a_instruction(instruction):
    """
    This function converts a-instructions to their binary form
    :param instruction: the instruction to convert
    :return: the binary representation of the instruction
    """
    inst = instruction.replace("@", "")
    number = int(inst)
    code = "{0:b}".format(number)
    return code.zfill(16)


def c_instruction(instruction):
    """
    This function handles c-instructions
    :param instruction: the instruction
    :return: binary representation
    """
    dest, comp, jmp = re.split(r"=+|;+", instruction) + [None]
    dmnem = destination(dest)
    jmnen = jump(jmp)
    cmnem = computation(comp)
    return "111" + cmnem + dmnem + jmnen


def assemble(instruction):
    """
    This functions identifies the instruction type i.e. a-instruction or c-instruction &
    calls the corresponding function to unpack.
    :param instruction:  the instruction to unpack
    :return: th
    """
    if instruction.startswith("@"):
        code = a_instruction(instruction)
    else:
        code = c_instruction(instruction)
    return code
