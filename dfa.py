def nfa_to_dfa(nfa):
    state_mapping = {}
    state_counter = 0

    def get_state_number(states):
        nonlocal state_counter

        state_tuple = tuple(sorted(states))

        if state_tuple not in state_mapping:
            state_mapping[state_tuple] = state_counter
            state_counter += 1

        return state_mapping[state_tuple]

    initial_closure = closure(nfa, [nfa["initial"]])
    initial_state_number = get_state_number(initial_closure)

    DFA = {
        "states": [initial_state_number],
        "alphabet": nfa["alphabet"],
        "transitions": {},
        "initial": initial_state_number,
        "final": []
    }

    stack = [initial_closure]
    visited_states = set([tuple(sorted(initial_closure))])

    while stack:
        current_states = stack.pop()
        current_state_number = get_state_number(current_states)

        for symbol in DFA["alphabet"]:
            new_states = DFAedge(nfa, current_states, symbol)
            if not new_states:
                continue
            
            new_state_number = get_state_number(new_states)

            if tuple(sorted(new_states)) not in visited_states:
                DFA["states"].append(new_state_number)
                visited_states.add(tuple(sorted(new_states)))
                stack.append(new_states)

            if new_state_number not in DFA["final"] and any(state in nfa["final"] for state in new_states):
                DFA["final"].append(new_state_number)

            DFA["transitions"][(current_state_number, symbol)] = new_state_number

    return DFA

def edge(nfa, state, symbol):
    closure_symbol = set()
    stack = [state]

    while stack:
        current_state = stack.pop()

        if nfa['transitions'].get(current_state):
            for next_state in nfa['transitions'][current_state].get(symbol, []):
                if next_state not in closure_symbol:
                    closure_symbol.add(next_state)
                    stack.append(next_state)

    return list(closure_symbol)

def closure(nfa, states):
    closure_states = set(states)
    stack = list(states)

    while stack:
        current_state = stack.pop()

        if current_state in nfa['transitions']:
            for epsilon_state in nfa['transitions'][current_state].get('$', []):
                if epsilon_state not in closure_states:
                    closure_states.add(epsilon_state)
                    stack.append(epsilon_state)

    return list(closure_states)

def DFAedge(nfa, states, symbol):
    DFAedge_states = set()

    for state in states:
        for edge_state in edge(nfa, state, symbol):
            DFAedge_states.update(closure(nfa, [edge_state]))

    return list(DFAedge_states)
