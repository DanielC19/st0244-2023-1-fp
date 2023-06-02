import os

def readFile(filename:str) -> list[str] :
    f = open(f'{os.getcwd()}/test/cs1.txt', 'r')
    string = f.read()
    return string.split('\n')

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

def hasFreeVariables(t:str, x:str) -> bool :
    if x in t :
        return True
    return False

def typeIsVar(t:str) -> bool :
    if t == 'Nat' :
        return False
    if t == 'Bool' :
        return False
    if '->' in t :
        return False
    return True

def typeIsRestType(t:str) -> bool :
    if '->' in t :
        return True
    return False

def unify(
        constraints:list[str],
        typeReplace:str = None,
        typeReplacing:str = None,
        unifications:list[str] = []
    ) -> list[str] :

    if len(constraints) == 0 : return unifications

    if typeReplace is not None and typeReplacing is not None :
        for i in range(0, len(constraints)) :
            constraints[i] = constraints[i].replace(typeReplace, typeReplacing)

    constraint = constraints[0]
    constraintsLeft = constraints[1:]

    c = constraint.split('=')
    s = c[0].strip()
    t = c[1].strip()

    if s == t :
        return unify(constraintsLeft)
    elif typeIsVar(s) and not hasFreeVariables(t, s) :
        unifications.append(f'{s} |-> {t}')
        return unify(constraintsLeft, s, t)
    elif typeIsVar(t) and not hasFreeVariables(s, t) :
        unifications.append(f'{t} |-> {s}')
        return unify(constraintsLeft, t, s)
    elif typeIsRestType(s) and typeIsRestType(t) :
        const1 = f"{s.split('->')[0].strip()} = {t.split('->')[0].strip()}"
        const2 = f"{s.split('->')[1].strip()} = {t.split('->')[1].strip()}"
        constraintsLeft.append(const1, const2)
        return unify(constraintsLeft)
    else :
        raise ReferenceError()

if __name__ == '__main__' :
    try :
        constraints = readFile('cs1.txt')
        if len(constraints) == 0 :
            raise IndexError()
        if not verifyConstraint(constraints) :
            raise AttributeError()

        subs = unify(constraints)
        print('The constraint set unifies using the substitution:')
        for sub in subs :
            print(sub)

    except AttributeError :
        print('The constraint set is not defined properly.')
    except IndexError :
        print('The constraint set is empty.')
    except ReferenceError :
        print('The constraint set does not unify :(')