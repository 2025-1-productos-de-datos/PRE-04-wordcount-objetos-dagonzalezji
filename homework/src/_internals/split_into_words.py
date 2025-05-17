class SplitIntoWordsMixin:
    def split_into_words(self):
        """Split lines into individual words and clean punctuation."""
        words_i = []
        for line in self.lines:
            words_i.extend(word.strip(",.!?") for word in line.split())
        self.words = words_i