def find_shortest_distance(text, source, target):
    words = text.split(" ")
    return words.index(target) - words.index(source) - 1
