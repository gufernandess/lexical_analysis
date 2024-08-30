states_counter = 0
new_nfa = None

def merge_nfas(stack):
    symbol = stack.pop()

    global states_counter, new_nfa
    
    if symbol == ".":
        NFA_2 = stack.pop()
        NFA_1 = stack.pop()

        new_nfa = {
            "states": NFA_1['states'] + NFA_2['states'],
            "alphabet": list(set(NFA_1['alphabet'] + NFA_2['alphabet'])),
            "transitions": {**NFA_1['transitions'], **NFA_2['transitions']},
            "initial": NFA_1['initial'],
            "final": NFA_2['final']
        }

        for state in NFA_1['final']:
            if state in new_nfa['transitions']:
                new_nfa['transitions'][state]["$"] = [NFA_2['initial']]
            else:
                new_nfa['transitions'][state] = {"$": [NFA_2['initial']]}

        stack.append(new_nfa)

    elif symbol == "|":
        NFA_2 = stack.pop()
        NFA_1 = stack.pop()

        states_counter += 2

        new_nfa = {
            'states': NFA_1['states'] + NFA_2['states'] + [states_counter - 2, states_counter - 1],
            "alphabet": list(set(NFA_1['alphabet'] + NFA_2['alphabet'])),
            "transitions": {**NFA_1['transitions'], **NFA_2['transitions']},
            "initial": states_counter - 2,
            "final": [states_counter - 1]
        }

        new_nfa['transitions'][new_nfa['initial']] = {"$": [NFA_1['initial'], NFA_2['initial']]}

        for state in NFA_1['final']:
            new_nfa['transitions'][state] = {"$": [new_nfa['final'][0]]}

        for state in NFA_2['final']:
            new_nfa['transitions'][state] = {"$": [new_nfa['final'][0]]}

        stack.append(new_nfa)

    elif symbol == "*":
        NFA = stack.pop()

        states_counter += 2

        new_nfa = {
            "states": NFA['states'] + [states_counter - 2, states_counter - 1],
            "alphabet": NFA['alphabet'],
            "transitions": {**NFA['transitions']},
            "initial": states_counter - 2,
            "final": [states_counter - 1]
        }

        new_nfa['transitions'][new_nfa['initial']] = {"$": [new_nfa['final']]}
        new_nfa['transitions'][new_nfa['initial']] = {"$": [NFA['initial']]}
        new_nfa['transitions'][NFA['final'][-1]] = {"$": [new_nfa['final'][0]]}
        new_nfa['transitions'][new_nfa['final'][-1]] = {"$": [NFA['initial']]}

        stack.append(new_nfa)
    
    return new_nfa, stack

def make_stack(expression):
    RE_list = []

    global states_counter

    for symbol in expression:
        if symbol not in ["(", ")", "|", "*", "."]:
            states_counter += 2
            new_nfa = {
                "states": [states_counter - 2, states_counter - 1],
                "alphabet": [symbol],
                "transitions": {states_counter - 2: {symbol: [states_counter - 1]}},
                "initial": states_counter - 2,
                "final": [states_counter - 1]
            }

            RE_list.append(new_nfa)

        else:

            RE_list.append(symbol)
    
    return RE_list

def er_to_nfa(expression):
    stack = []
    NFA = None

    RE_list = make_stack(expression)

    for symbol in RE_list:
        if symbol != ')':
            stack.append(symbol)

            if stack[-1] == '(':
                stack.pop()

        else:
            NFA, stack = merge_nfas(stack)
            
    return NFA