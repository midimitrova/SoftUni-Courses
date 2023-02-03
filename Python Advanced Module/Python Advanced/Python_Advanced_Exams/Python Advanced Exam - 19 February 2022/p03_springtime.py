def start_spring(**kwargs):
    spring_collection = {}
    for key, value in kwargs.items():
        if value not in spring_collection.keys():
            spring_collection[value] = []
        spring_collection[value].append(key)

    sorted_dict = sorted(spring_collection.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for type, objects in sorted_dict:
        result.append(f'{type}:')
        for value in sorted(objects):
            result.append(f"-{value}")
    return "\n".join(result)


# --- TEST CODE ---
# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower", }
# print(start_spring(**example_objects))
#
#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
#
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
