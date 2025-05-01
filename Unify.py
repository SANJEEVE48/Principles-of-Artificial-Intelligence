def unify(x, y, subs={}):
    if x == y: return subs
    if isinstance(x, str): return unify_var(x, y, subs)
    if isinstance(y, str): return unify_var(y, x, subs)
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for sx, sy in zip(x, y):
            subs = unify(sx, sy, subs)
            if subs is None: return None
        return subs
    return None

def unify_var(var, term, subs):
    if var in subs: return unify(subs[var], term, subs)
    if isinstance(term, str) and term in subs: return unify(var, subs[term], subs)
    subs[var] = term
    return subs

# Example usage:
x = ('f', 'X', 2)
y = ('f', 3, 2)
print(unify(x, y))  # Output: {'X': 3}
