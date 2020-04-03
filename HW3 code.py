def postfixEval (postfixExpr):
    stack = []
    tokenList = postfixExpr.split()
    
    for token in tokenList:
        if token in "0123456789":
            stack.append(int(token))
        else:
            if len(stack) < 2:
                print('message....')
                exit()
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = doMath(token,operand1,operand2)
            stack.append(result)
        return stack.pop()
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1-op2
instr = input('enter a postfix expression : ')
print(postfixEval(instr))