import sys

def print_arguments():
    script_name = sys.argv[0]
    arguments = ' '.join(sys.argv[1:])
    print(f"Script: {script_name}")
    print(f"Script & Variables: {script_name} {arguments}")

print_arguments()

def helloWorld():
    print('Hello World')

helloWorld()
