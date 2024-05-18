# Because this is a class, we can add more analysis in the future possibly
# A class for each of the stock and their 
class AnalysedArticle:
    def __init__(self, newsLink):
        self.positive_scores = []
        self.negative_scores = []
        self.paragaphs = []
        self.newsLink = newsLink


    def add_score(self, label, score):
        if label == 'positive':
            self.positive_scores.append(score)
        elif label == 'negative':
            self.negative_scores.append(score)
    
    def add_paragaph(self, paragaph):
        self.paragaphs.append(paragaph);

    def average_positive(self):
        return sum(self.positive_scores) / len(self.positive_scores) if self.positive_scores else 0
    
    def average_negative(self):
        return sum(self.negative_scores) / len(self.negative_scores) if self.negative_scores else 0

    def lengths_match(self):
        return len(self.negative_scores) == len(self.paragaphs)

    def print_arrays(self):
        if self.lengths_match():
            for i in range(len(self.positive_scores)):
                print(f"Paragraph {i+1}: {self.paragaphs[i]}")
                print(f"Positive Score: {self.positive_scores[i]}")
                print(f"Negative Score: {self.negative_scores[i]}")
                print("---")
        else:
            print("The lengths of positive_scores, negative_scores, and paragraphs do not match.")
    
    def print_most_positive(self):
        if self.positive_scores:
            max_positive_index = self.positive_scores.index(max(self.positive_scores))
            print("Most Positive Paragraph:")
            print(f"Paragraph: {self.paragaphs[max_positive_index]}")
            print(f"Positive Score: {self.positive_scores[max_positive_index]}")
        else:
            print("No positive scores available.")

    def print_most_negative(self):
        if self.negative_scores:
            min_negative_index = self.negative_scores.index(min(self.negative_scores))
            print("Most Negative Paragraph:")
            print(f"Paragraph: {self.paragaphs[min_negative_index]}")
            print(f"Negative Score: {self.negative_scores[min_negative_index]}")
        else:
            print("No negative scores available.")
