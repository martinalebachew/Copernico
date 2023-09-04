from colorama import Fore

def print_color(statement, color=None):
  if not color:
    print(statement)
  else:
    print(color + statement + Fore.RESET)


def print_error(statement):
  print_color(statement, Fore.RED)


def print_success(statement):
  print_color(statement, Fore.GREEN)
