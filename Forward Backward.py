def backward_chaining(goal, facts, rules):
    if goal in facts: return True
    return any(all(backward_chaining(g, facts, rules) for g in rule['antecedent']) for rule in rules if goal in rule['consequent'])

# Example usage:
facts = {'A', 'B'}
rules = [{'antecedent': ['A'], 'consequent': ['C']}, {'antecedent': ['C'], 'consequent': ['D']}]
print(backward_chaining('D', facts, rules))  # Output: True



def forward_chaining(facts, rules):
    while True:
        new_facts = set(fact for rule in rules for fact in rule['consequent'] if set(rule['antecedent']).issubset(facts) and fact not in facts)
        if not new_facts: break
        facts.update(new_facts)
    return facts

# Example usage:
facts = {'A', 'B'}
rules = [{'antecedent': ['A'], 'consequent': ['C']}, {'antecedent': ['C'], 'consequent': ['D']}]
print(forward_chaining(facts, rules))  # Output: {'A', 'B', 'C', 'D'}
