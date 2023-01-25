def age_assignment(*args, **kwargs):
    names = {}
    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        names[name] = age

    sorted_names = dict(sorted(names.items(), key=lambda x: x[0]))
    result = ''
    for name, age in sorted_names.items():
        result += f"{name} is {age} years old.\n"
    return result


# --- TESTS ---
print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))