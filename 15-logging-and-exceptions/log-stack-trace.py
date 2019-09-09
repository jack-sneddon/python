import logging

# exceptions prevent crashes

a=5
b=0

try:
    c=a/b
except Exception as e :
    logging.error("Exception occured", exc_info=True)

# if I know there is danger, I might be more specific in my catch
try:
    c=a/b
except ZeroDivisionError:
    print("you can't dvide by zero!")

