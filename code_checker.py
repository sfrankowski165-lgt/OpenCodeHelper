
import ast

def check_code(code):
    try:
        ast.parse(code)
        return "No syntax errors found!"
    except SyntaxError as error:
        return (
            f"Syntax error on line {error.lineno}: "
            f"{error.msg}"
        )

print("Welcome to OpenCodeHelper!")
print("Enter Python code to check:")

code = input("> ")
print(check_code(code))
