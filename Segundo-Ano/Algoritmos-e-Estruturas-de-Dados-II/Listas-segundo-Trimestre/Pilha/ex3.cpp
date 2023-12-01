#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

typedef struct Node
{
    char data;
    struct Node *next;
} Node;

typedef struct
{
    Node *top;
} Stack;

void initialize(Stack *stack)
{
    stack->top = NULL;
}

void push(Stack *stack, char value)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = stack->top;
    stack->top = newNode;
}

char pop(Stack *stack)
{
    if (stack->top == NULL)
    {
        return '\0';
    }
    char value = stack->top->data;
    Node *temp = stack->top;
    stack->top = stack->top->next;
    free(temp);
    return value;
}

bool isEmpty(Stack *stack)
{
    return stack->top == NULL;
}

char peek(Stack *stack)
{
    if (!isEmpty(stack))
    {
        return stack->top->data;
    }
    return '\0';
}

bool isOperator(char c)
{
    return (c == '+' || c == '-' || c == '*' || c == '/');
}

int precedence(char c)
{
    if (c == '+' || c == '-')
    {
        return 1;
    }
    else if (c == '*' || c == '/')
    {
        return 2;
    }
    return 0;
}

bool evaluateExpression(char *expression, double *result)
{
    Stack operatorStack;
    initialize(&operatorStack);

    Stack operandStack;
    initialize(&operandStack);

    for (int i = 0; expression[i] != '\0'; i++)
    {
        char currentChar = expression[i];
        if (currentChar == ' ')
        {
            continue;
        }
        else if (currentChar == '(')
        {
            push(&operatorStack, currentChar);
        }
        else if (currentChar == ')')
        {
            while (!isEmpty(&operatorStack) && peek(&operatorStack) != '(')
            {
                char op = pop(&operatorStack);
                if (!isEmpty(&operandStack))
                {
                    double operand2 = pop(&operandStack);
                    double operand1 = pop(&operandStack);
                    double result;
                    switch (op)
                    {
                    case '+':
                        result = operand1 + operand2;
                        break;
                    case '-':
                        result = operand1 - operand2;
                        break;
                    case '*':
                        result = operand1 * operand2;
                        break;
                    case '/':
                        if (operand2 == 0)
                        {
                            printf("Erro: Divisao por zero\n");
                            return false;
                        }
                        result = operand1 / operand2;
                        break;
                    }
                    push(&operandStack, result);
                }
            }
            if (!isEmpty(&operatorStack) && peek(&operatorStack) == '(')
            {
                pop(&operatorStack);
            }
            else
            {
                printf("Erro: Parenteses desbalanceados\n");
                return false;
            }
        }
        else if (isOperator(currentChar))
        {
            while (!isEmpty(&operatorStack) && precedence(peek(&operatorStack)) >= precedence(currentChar))
            {
                char op = pop(&operatorStack);
                if (!isEmpty(&operandStack))
                {
                    double operand2 = pop(&operandStack);
                    double operand1 = pop(&operandStack);
                    double result;
                    switch (op)
                    {
                    case '+':
                        result = operand1 + operand2;
                        break;
                    case '-':
                        result = operand1 - operand2;
                        break;
                    case '*':
                        result = operand1 * operand2;
                        break;
                    case '/':
                        if (operand2 == 0)
                        {
                            printf("Erro: Divisao por zero\n");
                            return false;
                        }
                        result = operand1 / operand2;
                        break;
                    }
                    push(&operandStack, result);
                }
            }
            push(&operatorStack, currentChar);
        }
        else if (isdigit(currentChar))
        {
            double operand = currentChar - '0';
            while (isdigit(expression[i + 1]) || expression[i + 1] == '.')
            {
                if (expression[i + 1] == '.')
                {
                    i++;
                    double multiplier = 0.1;
                    while (isdigit(expression[i + 1]))
                    {
                        operand += (expression[i + 1] - '0') * multiplier;
                        multiplier *= 0.1;
                        i++;
                    }
                }
                else
                {
                    operand = operand * 10 + (expression[i + 1] - '0');
                }
                i++;
            }
            push(&operandStack, operand);
        }
        else
        {
            printf("Erro: Caractere invalido na expressao\n");
            return false;
        }
    }

    while (!isEmpty(&operatorStack))
    {
        char op = pop(&operatorStack);
        if (op == '(')
        {
            printf("Erro: Parenteses desbalanceados\n");
            return false;
        }
        if (!isEmpty(&operandStack))
        {
            double operand2 = pop(&operandStack);
            double operand1 = pop(&operandStack);
            double result;
            switch (op)
            {
            case '+':
                result = operand1 + operand2;
                break;
            case '-':
                result = operand1 - operand2;
                break;
            case '*':
                result = operand1 * operand2;
                break;
            case '/':
                if (operand2 == 0)
                {
                    printf("Erro: Divisao por zero\n");
                    return false;
                }
                result = operand1 / operand2;
                break;
            }
            push(&operandStack, result);
        }
    }

    if (!isEmpty(&operandStack))
    {
        *result = pop(&operandStack);
        return isEmpty(&operatorStack);
    }
    else
    {
        printf("Erro: Expressao vazia\n");
        return false;
    }
}

int main()
{
    char expression[100];
    double result;

    printf("Digite uma expressao aritmetica: ");
    fgets(expression, sizeof(expression), stdin);

    if (evaluateExpression(expression, &result))
    {
        printf("A expressao e valida e o resultado e: %lf\n", result);
    }

    return 0;
}
