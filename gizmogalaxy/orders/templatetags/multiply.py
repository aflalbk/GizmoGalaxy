from django import template

register = template.Library()

@register.simple_tag(name='multiply')
def multiply(num1, num2):
    try:
        print("num1 =", num1)
        print("num2 =", num2)
        num1 = float(num1) if num1 else 0  # Convert empty string to 0
        num2 = float(num2) if num2 else 0
        return num1 * num2
    except ValueError as e:
        return f"Error: {e}"  # Return error message instead of crashing
    