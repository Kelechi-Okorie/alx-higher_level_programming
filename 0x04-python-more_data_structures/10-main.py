#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
b_dictionary = {}
c_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
best_key = best_score(c_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
