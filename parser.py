import regex, nfa, dfa

INT = dfa.nfa_to_dfa(nfa.er_to_nfa(regex.INT))
STRING = dfa.nfa_to_dfa(nfa.er_to_nfa(regex.STRING))
VAR = dfa.nfa_to_dfa(nfa.er_to_nfa(regex.VAR))
NUM = dfa.nfa_to_dfa(nfa.er_to_nfa(regex.NUM))
CONST = dfa.nfa_to_dfa(nfa.er_to_nfa(regex.CONST))
SINGLE = dfa.nfa_to_dfa(nfa.er_to_nfa(regex.SINGLE))

dfas = {
    "INT": INT,
    "STRING": STRING,
    "NUM": NUM,
    "VAR": VAR,
    "CONST": CONST,
    "SINGLE": SINGLE
}

single_mapping = {
    '+': "PLUS",
    '-': "MINUS",
    '#': "MULTIPLY",
    '=': "EQUAL",
    '>': "BIGGER",
    '<': "SMALLER",
    ';': "SEMICOLON"
}

def process_string_dfa(dfa, string):
    current_state = dfa["initial"]
    word = ""

    for char in string:
        if (current_state, char) in dfa["transitions"]:
            word += char
            current_state = dfa["transitions"][(current_state, char)]
        else:
            return "ERRO"

    return current_state, word

def check_word(word):
    for name, DFA in dfas.items():
        result = process_string_dfa(DFA, word)

        if result != "ERRO":
            final_state, processed_word = result

            if final_state in DFA["final"]:
                if name == "SINGLE":
                    if processed_word in single_mapping:
                        return single_mapping[processed_word]
                    else:
                        return "ERRO"
                else:
                    return name
    return "ERRO"

