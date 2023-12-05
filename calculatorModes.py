def infixa_a_postfixa(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    for char in expression:
        if char.isalnum():
            output.append(char)

            print("output: " + str(output))
        elif char in "+-*/":
            while (stack and stack[-1] in "+-*/" and precedence[stack[-1]] >= precedence[char]):
                output.append(stack.pop())
                print("output: " + str(output))
            stack.append(char)
            print("stack: " + str(stack))
        elif char == '(':
            stack.append(char)
            print("stack: " + str(stack))
        elif char == ')':
            while (stack and stack[-1] != '('):
                output.append(stack.pop())
                print("output: " + str(output))
            stack.pop()
            print("stack: " + str(stack))

    while stack:
        output.append(stack.pop())
        print("output: " + str(output))

    return ''.join(output)

def infixa_a_prefixa(expression):
    def reverse(expression):
        return expression[::-1]

    def infix_to_prefix(expression):
        expression = reverse(expression)
        expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')
        expression = infixa_a_postfixa(expression)
        return reverse(expression)

    return infix_to_prefix(expression)

def equivaler_postfixa(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char not in operators:
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)

    return stack[0]

while True:
    user_input = input("Digite uma expressão matemática ou '0' para sair: ")
    if user_input.lower() == '0':
        break
    choice = input("Escolha infixa, postfixa e prefixa: ").lower()
    if choice == 'infixa':
        print(f"Infixa: {user_input}")
        evaluate = input("Deseja calcular a expressão infixa? (S/N): ").lower()
        if evaluate == 's':
            postfixa_expressao = infixa_a_postfixa(user_input)
            result = equivaler_postfixa(postfixa_expressao)
            print(f"Resultado da expressão infixa: {result}")
    elif choice == 'postfixa':
        postfixa_expressao = infixa_a_postfixa(user_input)
        print(f"Postfixa: {postfixa_expressao}")
        evaluate = input("Deseja calcular a expressão postfixa? (S/N): ").lower()
        if evaluate == 's':
            result = equivaler_postfixa(postfixa_expressao)
            print(f"Resultado da expressão postfixa: {result}")
    elif choice == 'prefixa':
        prefixa_expressao = infixa_a_prefixa(user_input)
        print(f"Prefixa: {prefixa_expressao}")
        evaluate = input("Deseja calcular a expressão prefixa? (S/N): ").lower()
        if evaluate == 's':
            postfixa_expressao = infixa_a_postfixa(prefixa_expressao)
            result = equivaler_postfixa(postfixa_expressao)
            print(f"Resultado da expressão prefixa: {result}")
    else:
        print("Escolha inválida. Tente novamente.")
