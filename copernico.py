from utils.updates import *
from livepatch import livepatch

def main():
  check_for_updates()
  livepatch()

if __name__ == "__main__":
  main()
