def name_to_length(names):
    return {name: len(name) for name in names}

names = ["ana", "bruno", "carla", "daniel"]
print(name_to_length(names))
