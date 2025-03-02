def get_tuple():
    elements = input().split()
    return tuple(bool(int(e)) for e in elements)

def all_true(t):
    return all(t)

tuplee = get_tuple()
print(f"Tuple: {tuplee}")
print(f"All elements: {all_true(tuplee)}")
