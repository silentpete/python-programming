#!/bin/python
import argparse

def main():
  parser = argparse.ArgumentParser(description='Put a long description here of the overall program.')
  parser.add_argument('--option', type=str, help='can set an option')
  args = parser.parse_args()

  if args.option == "option":
    print('option=' + args.option)
  else:
    print('option=' + str(args.option))

if __name__ == '__main__':
  main()
