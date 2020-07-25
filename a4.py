"""
    Assignment 4
    Matthew Doyle
    301322233
    mwdoyle@sfu.ca
"""
# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_expression(e):
    return e == '<--' or e == '&'

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def even_elements(a):
    return a[::2]

def odd_elements(a):
    return a[1::2]

def load(usr_inpt):
    if usr_inpt[0] == 'load' and len(usr_inpt) == 2 and usr_inpt[1].endswith('.txt'):
        return True
    else:
        return False

def tell(usr_inpt):
    if usr_inpt[0] == 'tell':
        return True
    else:
        return False

def read_file(usr_inpt):       
    with open(usr_inpt) as f_in:
        lines = (line.rstrip() for line in f_in) 
        lines = list(line for line in lines if line)
    return lines
    
def valid_clause(lines):
    # check for invalid cluases
    clauses = []
    for line in lines:
        clauses.append(line.split())
    for clause in clauses:
        atoms = even_elements(clause)
        expressions = odd_elements(clause)
        # check atoms
        for atom in atoms:
            if not is_atom(atom):
                return False
        # check expressions
        for expression in expressions:
            if not is_expression(expression):
                return False
    return True

def print_out(lines):
    # print out
    print("  {:d} definite clauses read in:".format(len(lines)))
    for line in lines:
        print("   ",line)
    print()

# https://stackoverflow.com/a/29980091
class sset(set):
    def __str__(self):
        return ', '.join([str(i) for i in self])


def run_interpreter():
    # look into ordered sets https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set
    kb = set()

    while True:
        user_input = input('kb> ').split()

        # load command 
        if load(user_input):
            try:
                lines = read_file(user_input[1])
            except:
                print("File not Found")
                continue  
            # check for valid clauses
            if not valid_clause(lines):
                print("Error: %s is not a valid knowledge base" % user_input[1])
                continue
            else:
                # clear current kb
                kb.clear()
                # print loaded cluases
                print_out(lines)
                # load lines into KB
                kb.update(lines)
            
        # tell command    
        elif tell(user_input):
            if len(user_input) <= 1:
                print("Error: tell needs at least one atom")
                continue
            
            atoms = user_input[1::]
            for atom in atoms:
                if not is_atom(atom):
                    print("Error: \"%s\" is not a valid atom" % atom)
                    continue
                elif atom in kb:
                    print("atom \"%s\" already known to be true" % atom)
                else:
                    kb.add(atom)
                    print("  \"%s\" added to KB" % atom)
            print()

        # infer_all command
        elif user_input[0] == 'infer_all':
            # seperate rules and atoms
            rules = set()
            atoms = set()
            already_known = set()
            infered = set()
            for clause in kb:
                if '<--' in clause:
                    rules.add(clause)
                else:
                    atoms.add(clause)
                    already_known.add(clause)
            #  infer algorithm
            clauses = []
            for line in rules:
                clauses.append(line.split())
            # for clause in clauses:
            for i in range(len(clauses)):
                rule_atoms = even_elements(clauses[i])
                if rule_atoms[0] in kb:
                    continue
                if all(item in atoms for item in rule_atoms[1::]):
                    infered.add(rule_atoms[0])
                    # causing added atom to be printed
                    atoms.add(rule_atoms[0])
                    kb.add(rule_atoms[0])
                    # restart loop
                    i = 0



            print("  Newly inferred atoms:")
            if len(infered) == 0:
                print("    <none>")
            else:
                print("   ",sset(infered))
            print("  Atoms already known to be true:")
            print("   ",sset(already_known))
            print()










        # print all command for debugging
        elif user_input[0] == 'print':
            print(kb)
            
        else:
            print("Error: unknown command \"%s\"" % user_input[0])

            

if __name__ == '__main__':
    run_interpreter()
