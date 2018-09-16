class WordDistanceCounter:
    def __init__(self, filename):
        self.filename = filename

    def load_file(self):
        with open(self.filename) as txtFile:
            return txtFile.read()

    def find_shortest_distance(self, source, target):
        text = self.load_file()
        words = text.split(" ")
        return words.index(target) - words.index(source) - 1
