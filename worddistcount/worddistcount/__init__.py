def calculate_distance(text, source, target):
    words, source, target = make_lower_case(text, source, target)

    start_idx_candidate = None
    for i, word in enumerate(words):
        if word == source:
            start_idx_candidate = i
        if word == target and start_idx_candidate is not None:
            end_idx_candidate = i
            return end_idx_candidate - start_idx_candidate - 1


def make_lower_case(text, source, target):
    words = [word.lower() for word in text.split()]
    return words, source.lower(), target.lower()


class WordDistanceCounter:
    def __init__(self, filename):
        self.filename = filename

    def load_txt_from_file(self):
        with open(self.filename) as txtFile:
            return txtFile.read()

    def find_shortest_distance(self, source, target):
        text = self.load_txt_from_file()
        return calculate_distance(text, source, target)


def main():
    word_counter = WordDistanceCounter("test/test_file.txt")
    result = word_counter.find_shortest_distance("motivation", "development")
    print(result)


if __name__ == '__main__':
    main()
