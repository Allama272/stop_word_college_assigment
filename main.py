from collections import Counter
import string


def remove_punctuation(text):
# I am also removing punctaution since it treated words like "craft," and "craft" differently
  punctuation = string.punctuation
  return ''.join([char for char in text if char not in punctuation])

def remove_stopwords(text, stopwords):
  words = remove_punctuation(text).lower().split()
  return [word for word in words if word not in stopwords]

def main():
  with open("paragraphs.txt", "r") as f:
    text = f.read()

  import nltk
  nltk.download('stopwords')
  from nltk.corpus import stopwords
  stopwords_list = stopwords.words('english')
  processed_text = remove_stopwords(text, stopwords_list)

  word_counts = Counter(processed_text)
  sorted_word_counts = word_counts.most_common(None)
  print("Word Frequency Count:")
  for word, count in sorted_word_counts:
    print(f"{word}: {count}")

if __name__ == "__main__":
  main()
