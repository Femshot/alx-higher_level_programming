#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
print("---------------------")

best_score = __import__('10-best_score').best_score

a_dictionary = {'John': -12, 'Bob': -14, 'Mike': -14, 'Molly': -16, 'Adam': -10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

print("now with alternate new algorithm")

best_score = __import__('10-best_score_2').best_score

a_dictionary = {'John': -12, 'Bob': -14, 'Mike': -14, 'Molly': -16, 'Adam': -10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

