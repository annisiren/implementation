import pickle
import os
from os import walk
import sys
import codecs
import numpy as np
import gc
np.set_printoptions(threshold=sys.maxsize)

import pandas as pd
import ta_obj as TA_OBJ

bt_words= ('remember define duplicate list memorize recall recognize repeat reproduce retrieve '
           'understand classify compare discuss exemplify explain infer interpret paraphrase summarize '
           'apply convert demonstrate discover discuss dramatize execute illustrate implement interpret prepare solve use '
           'analyze attribute classify compare contract criticize differentiate discriminate distinguish experiment organize question '
           'evaluate appraise argue check critique debate defend evaluate judge measure select support test verify '
           'create assemble construct design develop devise formulate generate organize plan produce rearrange rewrite')

def word_pp(word, words):
    obj_pp = TA_OBJ.pre_processing(word, words)
    obj_fe = TA_OBJ.feature_engineering(obj_pp)

    # write_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Text_Analysis\\word_search'))
    # save_file_location = write_path + '\\' + ('bloom_words.csv')
    # save(obj_fe.bow_wt, obj_fe.bow_stem, obj_fe.bow_lem, save_file_location )

    return obj_fe

def remove_similarities(obj):
    BTWords = word_pp('remember', bt_words)

    obj.bow_wt = obj.bow_wt[obj.bow_wt['label'].isin(BTWords.bow_wt['label'])]
    obj.bow_stem = obj.bow_stem[obj.bow_stem['label'].isin(BTWords.bow_stem['label'])]
    obj.bow_lem = obj.bow_lem[obj.bow_lem['label'].isin(BTWords.bow_lem['label'])]

    return obj

def read_files(read_path, write_path):
    print("read_files")
    print(read_path)
    filenames = next(walk(read_path), (None, None, []))[2]  # [] if no file

    # Go through all files individually
    for file in filenames:
        file_location = read_path +'\\'+file.replace(" ", "_").split('.txt')[0]
        save_file_location = write_path +'\\'+file.replace(" ", "_").split('.txt')[0]
        keyword_file_name = file_location.replace(" ", "_").split('.')[0]+'.txt'
        write_words = save_file_location.split('.')[0] + '_words.csv'

        with open(keyword_file_name, 'rb') as read_file:
            obj = pickle.load(read_file)

        obj = remove_similarities(obj)

        # input("Press enter to continue...")


        save(obj.bow_wt, obj.bow_stem, obj.bow_lem, write_words)


def save(obj1, obj2, obj3, write_file):
    # TODO: If empty do not save
    df = pd.merge(obj1, obj2, how="outer", on=["label"])
    df = pd.merge(df, obj3, how="outer", on=["label"])

    cols = df.columns.tolist()
    cols.remove('label')
    cols.insert(0, 'label')

    if df.empty:
        print('DataFrame is empty!')
    else:
        df_tfidf = df[cols]
        df_sorted_tfidf = df_tfidf.sort_values(by=['label'], ascending=True).reset_index(drop=True)
        df_sorted_tfidf.to_csv(write_file, index=False)

def main():

    read_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\Feature_Engineering'))
    write_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\word_search'))

    read_files(read_path, write_path)

main()
