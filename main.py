def swap_keys_values(d):
    return {v: k for k, v in d.items()}

def sort_swapped_keys(d):
    swapped = swap_keys_values(d)
    return dict(sorted(swapped.items()))

# test
mapping = {'one': 1, 'two': 2, 'three': 3}
print(sort_swapped_keys(mapping))
