import nltk
nltk.download('all')
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion

from collections import Counter
import string
import inspect

import pandas as pd
import numpy as np

# class word_processing:
#     def __init__(self, obj_fe):
#         self.obj_fe = obj_fe
#         self.bow_wt = self.obj_fe.bow_wt
#         self.bow_stem = self.obj_fe.bow_stem
#         self.bow_lem = self.obj_fe.bow_lem
#
#     def words(self):
#
#         print("self")
#
#         return "self"


class pre_processing:
    def __init__(self, file, content):
        self.file = file
        self.content = content.lower()
        self.word_tokens = self.tokenize()
        self.stemmed_content = self.stem()
        self.lemma_content = self.lemmatize()

    def stem(self):
        ps = PorterStemmer()
        return [ps.stem(word) for word in self.word_tokens]

    def lemmatize(self):
        lemma = WordNetLemmatizer()
        return [lemma.lemmatize(word) for word in self.word_tokens]

    def tokenize(self):
        STOP_WORDS = set(stopwords.words('english'))
        content = self.content.replace("Error:","")
        content = content.translate(str.maketrans('', '', string.punctuation))
        content = content.translate(str.maketrans('', '', string.digits))
        content = ' '.join(word for word in content.split() if len(word)>2)

        word_tokens = word_tokenize(content)
        return [word for word in word_tokens if not word.lower() in STOP_WORDS]

class feature_engineering:
    def __init__(self, obj_pp):
        self.obj_pp = obj_pp
        self.word_tokens = self.obj_pp.word_tokens
        self.stemmed_content = self.obj_pp.stemmed_content
        self.lemma_content = self.obj_pp.lemma_content

        self.bow_wt, self.bow_stem, self.bow_lem = self.bow()

        self.ngram_wt_two, self.ngram_wt_three = self.ngram(self.word_tokens, 'wt')
        self.ngram_stem_two, self.ngram_stem_three = self.ngram(self.stemmed_content, 'stem')
        self.ngram_lem_two, self.ngram_lem_three = self.ngram(self.lemma_content, 'lem')

        self.tfidf_wt = self.tfidf_content([' '.join(self.word_tokens)], ['tfidf_wt','label'])
        self.tfidf_stem = self.tfidf_content([' '.join(self.stemmed_content)], ['tfidf_stem','label'])
        self.tfidf_lem = self.tfidf_content([' '.join(self.lemma_content)], ['tfidf_lem','label'])

        self.tfidf_wt_two = self.tfidf_ngram([' '.join(self.word_tokens)], 2, ['tfidf_wt_two','label'])
        self.tfidf_stem_two = self.tfidf_ngram([' '.join(self.stemmed_content)], 2, ['tfidf_stem_two','label'])
        self.tfidf_lem_two = self.tfidf_ngram([' '.join(self.lemma_content)], 2, ['tfidf_lem_two','label'])

        self.tfidf_wt_three = self.tfidf_ngram([' '.join(self.word_tokens)], 3, ['tfidf_wt_three','label'])
        self.tfidf_stem_three = self.tfidf_ngram([' '.join(self.stemmed_content)], 3, ['tfidf_stem_three','label'])
        self.tfidf_lem_three = self.tfidf_ngram([' '.join(self.lemma_content)], 3, ['tfidf_lem_three','label'])



    def bow(self):
        bow_wt = Counter(self.word_tokens)
        bow_wt = pd.DataFrame.from_dict(bow_wt, orient='index').reset_index()
        bow_wt = bow_wt.rename(columns={'index': 'label', 0: 'bow_wt'})

        bow_stem = Counter(self.stemmed_content)
        bow_stem = pd.DataFrame.from_dict(bow_stem, orient='index').reset_index()
        bow_stem = bow_stem.rename(columns={'index': 'label', 0: 'bow_stem'})

        bow_lem = Counter(self.lemma_content)
        bow_lem = pd.DataFrame.from_dict(bow_lem, orient='index').reset_index()
        bow_lem = bow_lem.rename(columns={'index': 'label', 0: 'bow_lem'})

        return bow_wt, bow_stem, bow_lem

    def ngram(self, content, label):
        content_twogram = (pd.Series(nltk.ngrams(content, 2)).value_counts())
        # content_twogram = content_twogram[content_twogram > 1]
        df_two_gram = pd.DataFrame({'label':content_twogram.index, label+'_two_gram':content_twogram.values})
        content_threegram = (pd.Series(nltk.ngrams(content, 3)).value_counts())
        # content_threegram = content_threegram[content_threegram > 1].to_frame
        df_three_gram = pd.DataFrame({'label':content_threegram.index, label+'_three_gram':content_threegram.values})

        # print(content_twogram)
        # print(content_threegram)
        #
        # input("Press enter to continue...")

        return df_two_gram, df_three_gram

    def tfidf_content(self, content, label):
        vectorizer = TfidfVectorizer(analyzer = 'word', stop_words='english')
        tfidf_wm = vectorizer.fit_transform(content)
        tfidf_tokens = vectorizer.get_feature_names_out()

        df = pd.DataFrame(np.dstack((tfidf_wm.toarray(),tfidf_tokens))[0], columns=label)

        # print(df)

        # print(len(tfidf_wm.toarray()))
        # print(len(tfidf_tokens))
        # print(tfidf_wm.toarray()[0])
        # print(tfidf_tokens)

        # input("Press enter to continue...")

        return df

    def tfidf_ngram(self, content, num, label):
        vectorizer = TfidfVectorizer(analyzer='word', stop_words='english', ngram_range=(num,num))
        tfidf_wm = vectorizer.fit_transform(content)
        tfidf_tokens = vectorizer.get_feature_names_out()

        df = pd.DataFrame(np.dstack((tfidf_wm.toarray(), tfidf_tokens))[0], columns=label)

        # print(tfidf_tokens)
        # print(tfidf_wm.toarray())
        # input("Press enter to continue...")

        return df

