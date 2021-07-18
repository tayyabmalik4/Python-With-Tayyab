# ////////we use argparse and sys module to build it
# ///////argparse module woks that-------The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
# ///////sys module works that ---- ------The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.
# //////using this module we run the program in the powershall and this is fot users command interfarance like python provides the user interfarance



import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x +args.y
    elif args.o=='sub':
        return args.x - args.y
    elif args.o =='mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "Invalid Cradials"

if __name__ =='__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('--x',type=float, default=1.0,help="if you kind any help please contect the AI Robort")
    parser.add_argument('--y',type=float, default=3.0, help="if you kind any help please contect the Jarviz")
    parser.add_argument('--o', type=str, default="add",help= "if you kind any help please contect the Davil robort of the davils")
    args= parser.parse_args()
    sys.stdout.write(str(calc(args)))
