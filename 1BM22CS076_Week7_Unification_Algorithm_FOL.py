class Compound:
    """Represents a compound expression with an operator and arguments."""
    def __init__(self, op, args):
        self.op = op
        self.args = args

    def __repr__(self):
        return f"{self.op}({', '.join(map(str, self.args))})"

def unify(x, y, theta=None):
    if theta is None:
        theta = {}  # Initialize substitution if not provided

    if theta is None:  # Failure case
        return None
    elif x == y:  # Identical terms
        return theta
    elif is_variable(x):  # x is a variable
        return unify_var(x, y, theta)
    elif is_variable(y):  # y is a variable
        return unify_var(y, x, theta)
    elif is_compound(x) and is_compound(y):  # Both are compound terms
        if x.op != y.op or len(x.args) != len(y.args):
            return None  # Different operators or argument lengths
        return unify(x.args, y.args, theta)  # Unify their arguments
    elif is_list(x) and is_list(y):  # Both are lists
        if not x and not y:  # Both lists are empty
            return theta
        elif not x or not y:  # One list is empty
            return None
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))  # Unify head and tail
    else:
        return None  # Failure

def unify_var(var, x, theta):
    if var in theta:  # If var already has a substitution
        return unify(theta[var], x, theta)
    elif x in theta:  # If x already has a substitution
        return unify(var, theta[x], theta)
    elif occurs_check(var, x):  # Check if var occurs in x
        return None  # Failure to avoid infinite recursion
    else:
        theta[var] = x  # Add substitution {var -> x}
        return theta

def is_variable(x):
    return isinstance(x, str) and x.islower()  # Variables are lowercase strings

def is_compound(x):
    return isinstance(x, Compound)

def is_list(x):
    return isinstance(x, list)

def occurs_check(var, x):
    if var == x:
        return True
    elif is_compound(x):
        return any(occurs_check(var, arg) for arg in x.args)
    elif is_list(x):
        return any(occurs_check(var, element) for element in x)
    return False

def parse_input(term):
    """
    Parses user input to create Compound objects, lists, or variables.
    Input format:
      - Variables: single lowercase letters (e.g., `x`)
      - Compound terms: `f(a, b)`
      - Lists: `[a, b, c]`
    """
    term = term.strip()

    # Handle lists
    if term.startswith("[") and term.endswith("]"):
        elements = term[1:-1].split(",")
        return [parse_input(e.strip()) for e in elements]

    # Handle compound terms
    elif "(" in term and term.endswith(")"):
        op = term[:term.index("(")].strip()
        args = term[term.index("(") + 1:-1].split(",")
        return Compound(op, [parse_input(arg.strip()) for arg in args])

    # Handle variables and constants
    else:
        return term

# Main program
if __name__ == "__main__":
    print("Unification Algorithm")
    print("Input terms in the following format:")
    print(" - Variables: single lowercase letters (e.g., x)")
    print(" - Compound terms: f(a, b)")
    print(" - Lists: [a, b, c]\n")

    term1 = input("Enter the first term: ")
    term2 = input("Enter the second term: ")

    # Parse user input
    parsed_term1 = parse_input(term1)
    parsed_term2 = parse_input(term2)

    # Perform unification
    result = unify(parsed_term1, parsed_term2)

    # Output the result
    if result is None:
        print("\nUnification failed.")
    else:
        print("\nUnification succeeded. Substitution:", result)
