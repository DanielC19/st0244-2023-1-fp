import os

# Read file and split it to return list
def readFile(filename:str) -> list[str] :
    f = open(f'{os.getcwd()}/test/{filename}', 'r')
    string = f.read()
    f.close()
    return string.split('\n')

# Verify the constraints have a proper form
def verifyConstraint(constraints:list[str]) -> bool :
    for constraint in constraints :
        if not '=' in constraint :
            return False
        if not len(constraint.split('=')) == 2 :
            return False
        for t in constraint.split('=') :
            if not t.strip()[0].isalpha() :
                return False
    return True

# Check type `t` has `x` as a free variable
def hasFreeVariables(t:str, x:str) -> bool :
    eTypes = t.split('->')
    for eType in eTypes :
        if not ('Nat' in eType or 'Bool' in eType) and x in eType:
            return True
    return False

# Check if type is Var
def typeIsVar(t:str) -> bool :
    if t == 'Nat' :
        return False
    if t == 'Bool' :
        return False
    if '->' in t :
        return False
    return True

# Check if type has the form of type - rest type
def typeIsRestType(t:str) -> bool :
    if '->' in t :
        return True
    return False

def unify(
        cList:list[str],
        typeReplace:str = None,
        typeReplacing:str = None,
        unifications:list[str] = None
    ) -> list[str] :

    if unifications is None:
        unifications = []

    if len(cList) == 0 : return unifications

    if typeReplace is not None and typeReplacing is not None :
        for i in range(0, len(cList)) :
            e = cList[i]
            if not ('Nat' in e or 'Bool' in e) and not '->' in e :
                cList[i] = e.replace(typeReplace, typeReplacing)
            elif ('Nat' in e or 'Bool' in e) and not '->' in e :
                continue
            else :
                eRestTypes = e.split('=')
                for eRestType in eRestTypes :
                    eTypes = eRestType.split('->')
                    for eType in eTypes :
                        if not 'Nat' in eType or not 'Bool' in eType:
                            cList[i] = e.replace(typeReplace, typeReplacing)

    # Define current constraint and next ones
    constraint = cList[0]
    constraintsLeft = cList[1:]

    c = constraint.split('=')
    s = c[0].strip()
    t = c[1].strip()

    # Unify algorithm logic
    if s == t :
        return unify(constraintsLeft, unifications = unifications)
    elif typeIsVar(s) and not hasFreeVariables(t, s) :
        unifications.append(f'{s} |-> {t}')
        return unify(constraintsLeft, s, t, unifications)
    elif typeIsVar(t) and not hasFreeVariables(s, t) :
        unifications.append(f'{t} |-> {s}')
        return unify(constraintsLeft, t, s, unifications)
    elif typeIsRestType(s) and typeIsRestType(t) :
        const1 = f"{s.split('->')[0].strip()} = {t.split('->')[0].strip()}"
        const2 = f"{s.split('->')[1].strip()} = {t.split('->')[1].strip()}"
        constraintsLeft.append(const1)
        constraintsLeft.append(const2)
        return unify(constraintsLeft, unifications = unifications)
    else :
        raise ReferenceError()

# Call unify function and handles Exceptions
def main(filename:str) -> None:
    try :
        constraints = readFile(filename)
        if len(constraints) == 0 :
            raise IndexError()
        if not verifyConstraint(constraints) :
            raise AttributeError()

        subs = unify(constraints)
        print('\nThe constraint set unifies using the substitution:')
        for sub in subs :
            print(sub)

    except AttributeError :
        print('The constraint set is not defined properly.')
    except IndexError :
        print('The constraint set is empty.')
    except ReferenceError :
        print('The constraint set does not unify :(')

# Main function to execute
if __name__ == '__main__' :
    main("cs1.txt")
    main("cs2.txt")
    main("cs3.txt")
    main("cs4.txt")
    main("cs5.txt")