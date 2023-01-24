def concatenate(*args, **kwargs):
    result = ''
    for word in args:
        result += word
    for word, value in kwargs.items():
        if word in result:
            result = result.replace(word, value)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
