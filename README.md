## Usage


from jsondatahelper import flatten, unflatten

# Flatten Standard Dictionary
dictionary = {"test":"dictionary","with":{"nested":"values"}}
flattend_dictionary = flatten(dictionary)

# Reverse Flattening Process
dictionary = unflatten(flattend_dictionary)