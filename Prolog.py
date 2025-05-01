from pyswip import Prolog

# Initialize Prolog interpreter
prolog = Prolog()

# Define some facts
prolog.assertz("father(john, mike)")
prolog.assertz("father(mike, jim)")

# Query the Prolog engine
result = list(prolog.query("father(X, Y)"))

# Print the results
for sol in result:
    print(f'{sol["X"]} is father of {sol["Y"]}')
