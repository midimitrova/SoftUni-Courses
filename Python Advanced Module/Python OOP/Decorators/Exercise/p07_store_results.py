def store_results(function):
    def wrapper(*args):

        func_name = function.__name__
        func_result = function(*args)

        with open('results.txt', 'a') as file:
            file.write(f"Function {func_name} was called. Result: {func_result}\n")

        return file
    return wrapper



# --- test code ---
# @store_results
# def add(a, b):
#     return a + b
#
#
# @store_results
# def mult(a, b):
#     return a * b
#
# add(2, 2)
# mult(6, 4)
