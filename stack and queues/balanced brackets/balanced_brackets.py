

import sys
sys.path.append("../")
from stack import *



def balanced_brackets(brackets):
    stack_bracket = Stack()
    for bracket in brackets:
        if stack_bracket.isEmpty():
            stack_bracket.push(bracket)
            continue
        if is_bracket_matching(stack_bracket.peek(),bracket):
            stack_bracket.pop()
            continue
        stack_bracket.push(bracket)

    return stack_bracket.isEmpty()


def is_bracket_matching(open,close):
    if open == "[":
        return close == "]"

    if open == "(":
        return close == ")"
    if open == "{":
        return close == "}"

    return False


brackets = "[()][{}]{[({})[]]}"
if balanced_brackets(brackets) :
    print "yup the brackets are balanced"
else :
    print "nope the brackets are not balanced"
