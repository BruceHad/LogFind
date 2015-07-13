# argparse

https://docs.python.org/dev/library/argparse.html

The argparse module parses arguments from Command Line programs. The program
defines what arguments it requires, and argparse will figure out how to parse
those out of sys.argv.

Create a parser.

    parser = argparse.ArgumentParser()

Tell the parser about the arguments.

    parser.add_argument('integers', type=int, nargs='+')

To add an optional argument you seem to need to set a default with the action argument.

    parser.add_argument('-o', action='store_true')

The parser_args() method will inspect the command line and convert each
argument to the appropriate type and then invoke the appropriate action.

    parser.parse_args(['--sum', '7', '-1', '42'])
