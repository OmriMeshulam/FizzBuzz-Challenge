# Fizzbuzz in Python.
#
# This is the straightforward, traditional version with nested
# if-statements.
#

class FizzBuzz():
    """Class doing FizzBuzz."""

    def do_fizzbuzz(self, m):
        """Return m, fizz, buzz or fizzbuzz as appropriate."""
        if (m % 15) == 0:
            return 'fizzbuzz'
        elif (m % 3) == 0:
            return 'fizz'
        elif (m % 5) == 0:
            return 'buzz'
        else:
            return '%i' % m

    def print_table(self, n):
        """Print the FizzBuzz table up to n."""
        for i in range(1, n+1):
            print (self.do_fizzbuzz(i))

# Main program section.
fb = FizzBuzz()
fb.print_table(100)
