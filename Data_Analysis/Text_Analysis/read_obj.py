import pickle
import os
from os import walk
import sys
import codecs
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

import pandas as pd

# def save(obj):
#     print(obj.tfidf_lem_two)
#
#     with codecs.open('test.txt', 'w', encoding='utf-8') as f:
#         f.write(np.array2string(obj.tfidf_lem_two, precision=5, separator=','))
#
#     # input("Press enter to continue...")

def read_files(read_path, write_path):
    print("read_files")
    print(read_path)
    filenames = next(walk(read_path), (None, None, []))[2]  # [] if no file

    # Go through all files individually
    for file in filenames:
        file_location = read_path +'\\'+file.replace(" ", "_").split('.txt')[0]
        save_file_location = write_path +'\\'+file.replace(" ", "_").split('.txt')[0]
        keyword_file_name = file_location.replace(" ", "_").split('.')[0]+'.txt'
        write_bow = save_file_location.split('.')[0] + '_bow.csv'
        # write_ngram_two = save_file_location.split('.')[0] + '_ngram_two.csv'
        # write_ngram_three = save_file_location.split('.')[0] + '_ngram_three.csv'
        # write_tfidf = save_file_location.split('.')[0] + '_tfidf.csv'
        # write_tfidf_ngram_two = save_file_location.split('.')[0] + '_tfidf_ngram_two.csv'
        # write_tfidf_ngram_three = save_file_location.split('.')[0] + '_tfidf_ngram_three.csv'

        # print(file_location)
        # print(keyword_file_name)
        # print(write_tfidf)
        # input("Press enter to continue...")

        with open(keyword_file_name, 'rb') as read_file:
            obj = pickle.load(read_file)

        save(obj.bow_wt, obj.bow_stem, obj.bow_lem, write_bow)
        # save(obj.ngram_wt_two, obj.ngram_stem_two, obj.ngram_lem_two, write_ngram_two)
        # save(obj.ngram_wt_three, obj.ngram_stem_three, obj.ngram_lem_three, write_ngram_three)
        # save(obj.tfidf_wt, obj.tfidf_stem, obj.tfidf_lem, write_tfidf)
        # save(obj.tfidf_wt_two, obj.tfidf_stem_two, obj.tfidf_lem_two, write_tfidf_ngram_two)
        # save(obj.tfidf_wt_three, obj.tfidf_stem_three, obj.tfidf_lem_three, write_tfidf_ngram_three)

        # input("Press enter to continue...")

        # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        #     print(df_sorted)
        # save(obj)
# obj_pp
## file
# word_tokens, stemmed_content, lemma_content
# bow_wt, bow_stem, bow_lem
# ngram_wt_two, ngram_wt_three
# ngram_stem_two, ngram_stem_three
# ngram_lem_two, ngram_lem_three
# tfidf_wt, tfidf_stem, tfidf_lem
# tfidf_wt_two, tfidf_stem_two, tfidf_lem_two
# tfidf_wt_three, tfidf_stem_three, tfidf_lem_three

def save(obj1, obj2, obj3, write_file):

    # print(obj1)
    # print(obj2)
    # print(obj3)
    #
    # input("Press enter to continue...")

    df = pd.merge(obj1, obj2, how="outer", on=["label"])
    df = pd.merge(df, obj3, how="outer", on=["label"])

    cols = df.columns.tolist()
    cols.remove('label')
    cols.insert(0, 'label')

    df_tfidf = df[cols]
    df_sorted_tfidf = df_tfidf.sort_values(by=['label'], ascending=True).reset_index(drop=True)
    df_sorted_tfidf.to_csv(write_file)

def main():
    read_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\Feature_Engineering'))
    write_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\Datasets'))

    read_files(read_path, write_path)

main()
