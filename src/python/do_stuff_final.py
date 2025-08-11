import sys
import traceback

# Create override function to customize error messages upon exception
def custom_excepthook(exc_type, exc_value, exc_tb):
    tb_summary = traceback.extract_tb(exc_tb)
    
    exception_class = exc_type.__name__
    exception_value = str(exc_value)

    # Custom error message to be sent to stderr output    
    for filename, lineno, func, _ in tb_summary:
        sys.stderr.write(f'[{ exception_class}] Error of type "{ exception_value }" occurred in file "{filename}", line {lineno}, in {func}')
    


def do_stuff():
    print("Doing stuff...")
    sys.stdout.write("This is a message to stdout.\n")
    sys.stderr.write("This is a message to stderr.\n")

    # fail = (1 / 0)
    raise Exception("Something went wrong!")

    print("Stuff done!")
    

if __name__ == "__main__":
    # Override the default exception hook to use the custom function above for better error logging
    sys.excepthook = custom_excepthook

    # Do the stuff
    do_stuff()
    