import argparse
import string


def calculate_distance(text: str, source: str, target: str):
    """Calculates a distance between source and target within text."""

    words, source, target = prepare_input_strings(text, source, target)

    start_idx_candidate = None
    for i, word in enumerate(words):
        if word == source:
            start_idx_candidate = i
        if word == target and start_idx_candidate is not None:
            end_idx_candidate = i
            return end_idx_candidate - start_idx_candidate - 1


def prepare_input_strings(text: str, source: str, target: str) -> {str, str, str}:
    """Helper function for input preparation."""

    words = [trim_and_lower(word) for word in text.split()]
    return words, trim_and_lower(source), trim_and_lower(target)


def trim_and_lower(source: str) -> str:
    """Trims punctuation and make letters lower case."""

    return source.translate(str.maketrans('', '', string.punctuation)).lower()


class WordDistanceCounter:
    """Class expect filename in constructor but don't do any IO before call find_shortest_distance function."""

    def __init__(self, filename: str):
        self.filename = filename

    def load_txt_from_file(self):
        with open(self.filename) as txtFile:
            return txtFile.read()

    def find_shortest_distance(self, source: str, target: str):
        """Main find distance method.

         Loads the file content each time being invoked and applies calculate_distance() function on it.

         """
        text = self.load_txt_from_file()
        return calculate_distance(text, source, target)


def main():
    filename, start_word, end_word = parse_args()
    word_counter = WordDistanceCounter(filename)
    result = word_counter.find_shortest_distance(start_word, end_word)
    print(result)


def parse_args():
    parser = argparse.ArgumentParser(description='Counts word distance between the words',
                                     usage='%(prog)s [options]')
    parser.add_argument('filename', help='file with the text')
    parser.add_argument('start', help='word count start from')
    parser.add_argument('end', help='word count ends with')
    args = parser.parse_args()
    return args.filename, args.start, args.end


if __name__ == '__main__':
    main()
