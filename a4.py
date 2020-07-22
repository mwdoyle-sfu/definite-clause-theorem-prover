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
    for line in lines:
        print(line)
    print("\t\n{:d} new rule(s) added".format(len(lines)))

def run_interpreter():
    kb = set()

    while True:
        user_input = input('kb> ').split()

        if load(user_input):
            # load file
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
                    print("\"%s\" added to KB" % atom)
        
        elif user_input[0] == 'infer_all':
            # seperate rules and atoms
            rules = set()
            atoms = set()
            for clause in kb:
                if '<--' in clause:
                    rules.add(clause)
                else:
                    atoms.add(clause)
            print(rules)
            print(atoms)
            # infer shit from atoms
            



        elif user_input[0] == 'print':
            print(kb)
            
        else:
            print("Error: unknown command \"%s\"" % user_input[0])

            

if __name__ == '__main__':
    run_interpreter()
