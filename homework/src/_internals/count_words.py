class CountWordsMixin:
    def count_words(self):
        """Count occurrences of each word using a plain dictionary."""
        word_counts_i = {}
        for word in self.words:
            word_counts_i[word] = word_counts_i.get(word, 0) + 1
        self.word_counts = word_counts_i