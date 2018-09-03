import sys
import adder

def main(args):
    """It have the methods for functioning the addition operation. """
    result = adder.summing(args[1:])     # calling the summing method from the adder module 
    if result != None:
        adder.result_value(result)        # calling the result_value method from the adder module
     
if __name__ == '__main__':
    main(sys.argv)