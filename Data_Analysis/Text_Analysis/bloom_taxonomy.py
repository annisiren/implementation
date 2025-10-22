import os
from os import walk
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
from scipy.stats import variation

import pandas as pd


def read_files(read_path, read_file, write_path):
    print("read_files")
    print(read_path)
    filenames = next(walk(read_path), (None, None, []))[2]  # [] if no file

    key_obj = pd.read_csv(read_file)

    key_obj = pd.DataFrame(key_obj).set_index('label')

    # Go through all files individually
    for file in filenames:
        file_location = read_path +'\\'+file.replace(" ", "_").split('.csv')[0]
        keyword_file_name = file_location.replace(" ", "_").split('.')[0]
        keyword_file_name = keyword_file_name.split('_words')[0]
        keyword_file_name = keyword_file_name.split('\\')[-1]

        obj = pd.read_csv(read_path+'\\'+file)

        obj = obj.rename(columns={'bow_wt': 'wt_'+keyword_file_name, 'bow_stem': 'stem_'+keyword_file_name, 'bow_lem': 'lem_'+keyword_file_name})

        # print(obj.to_string())
        # input("Press enter to continue...")

        key_obj = pd.merge(key_obj, obj, how="outer", on=['label'])
        # df = pd.merge(key_obj, obj, how="outer", on=["label"])

        # print(key_obj.to_string())
        # input("Press enter to continue...")

    key_obj.to_csv(write_path, index=False)

def word_pp(word, words):
    obj_pp = ta_obj.pre_processing(word, words)
    obj_fe = ta_obj.feature_engineering(obj_pp)

    return obj_fe

def find_taxonomy(write_path, file_name, bt_level, obj):
    print(file_name)
    save_file_location = write_path + '\\' + file_name + '_list.csv'

    key_obj = word_pp(file_name, bt_level)

    df = pd.merge(key_obj.bow_wt, key_obj.bow_stem, how="outer", on=["label"])
    df = pd.merge(df, key_obj.bow_lem, how="outer", on=["label"])

    cols = df.columns.tolist()
    cols.remove('label')
    cols.insert(0, 'label')

    df_tfidf = df[cols]
    key_obj = df_tfidf.sort_values(by=['label'], ascending=True).reset_index(drop=True)

    key_obj = pd.merge(key_obj, obj, how="inner", on=['label'])
    key_obj = key_obj.dropna(axis=1,how='all')

    df = find_level(key_obj, file_name)

    # print(key_obj.to_string())
    # input("Press enter to continue...")

    # key_obj.to_csv(save_file_location, index=False)

    return df

def find_level(obj, bloom_level):

    df = pd.DataFrame(columns=['file_name','bloom_level','wt_num','stem_num','lem_num','weight','variance'])

    for name, values in obj.items():
        weight_mod = 0
        wt_count = 0
        stem_count = 0
        lem_count = 0
        wt_sum = 0
        stem_sum = 0
        lem_sum = 0
        variance_data = []

        if name.split('_',1)[0] == 'bow' or name == 'label' or name == 'Unnamed: 0' or name.split('_',1)[1] in df['file_name'].values:
            print(name + ' skip')
            continue
        elif name.split('_')[0] == 'wt':
            print(name)
            wt_count = obj[name].count()
            wt_sum = obj[name].sum()
            variance_data = variance_data + [item for item in obj[name].values.flatten().tolist() if not(pd.isnull(item) == True)]
            # print(variance_data)

            weight_mod = weight_mod + 1
            if 'stem_'+name.split('_',1)[1] in obj:
                stem = 'stem_'+name.split('_',1)[1]
                stem_count = obj[stem].count()
                stem_sum = obj[stem].sum()
                weight_mod = weight_mod + 1
                variance_data = variance_data + [item for item in obj[stem].values.flatten().tolist() if
                                                 not (pd.isnull(item) == True)]
                # print(variance_data)
                # print(stem)
            else:
                stem_count = 0
                stem_sum = 0

            if 'lem_'+name.split('_',1)[1] in obj:
                lem = 'lem_'+name.split('_',1)[1]
                lem_count = obj[lem].count()
                lem_sum = obj[lem].sum()
                weight_mod = weight_mod + 1
                variance_data = variance_data + [item for item in obj[lem].values.flatten().tolist() if
                                                 not (pd.isnull(item) == True)]
                # print(variance_data)
                # print(lem)
            else:
                lem_count = 0
                stem_sum = 0
        elif name.split('_')[0] == 'stem':
            wt = 0
            stem_count = obj[name].count()
            stem_sum = obj[name].sum()
            weight_mod = weight_mod + 1
            variance_data = variance_data + [item for item in obj[name].values.flatten().tolist() if
                                             not (pd.isnull(item) == True)]
            # print(variance_data)
            if 'lem_'+name.split('_',1)[1] in obj:
                lem = 'lem_'+name.split('_',1)[1]
                lem_count = obj[lem].count()
                lem_sum = obj[lem].sum()
                weight_mod = weight_mod + 1
                variance_data = variance_data + [item for item in obj[lem].values.flatten().tolist() if
                                                 not (pd.isnull(item) == True)]
                # print(variance_data)
                # print(lem)
            else:
                lem_count = 0
                lem_sum = 0
        elif name.split('_')[0] == 'lem':
            wt_count = 0
            wt_sum = 0
            stem_count = 0
            stem_sum = 0
            lem = 'lem_' + name.split('_', 1)[1]
            lem_count = obj[lem].count()
            lem_sum = obj[lem].sum()
            weight_mod = weight_mod + 1
            variance_data = variance_data + [item for item in obj[lem].values.flatten().tolist() if
                                             not (pd.isnull(item) == True)]
            # print(variance_data)

        weight = (wt_sum+stem_sum+lem_sum) / weight_mod
        variance = variation(variance_data, ddof=1)  #lambda x: np.std(variance_data, ddof=1) / np.mean(variance_data)

        # print(variance_data)
        # print(variance)
        # input("Press enter to continue...")

        # print(obj[name])
        # print(obj[name].count())
        # print(weight)
        # 'file_name','bloom_level', 'wt_num','stem_num','lem_num','weight'
        df = df._append({'file_name':name.split('_',1)[1],'bloom_level':bloom_level,'wt_num':wt_count,'stem_num':stem_count,'lem_num':lem_count,'weight':weight, 'variance':variance},ignore_index=True)

        # print(df.to_string())

        # input("Press enter to continue...")
        # print(obj[name])
        # print(obj[stem])
        # print(obj[lem])
        # print(obj[name]+obj[stem]+obj[lem])
        #
        # print(name)
        # print(values)
        # input("Press enter to continue...")

    # print(df.to_string())

    return df



def main():
    bt_remember = ('remember define duplicate list memorize recall recognize repeat reproduce retrieve')
    bt_understand = ('understand classify compare discuss exemplify explain infer interpret paraphrase summarize')
    bt_apply = (
        'apply convert demonstrate discover discuss dramatize execute illustrate implement interpret prepare solve use')
    bt_analyze = (
        'analyze attribute classify compare contract criticize differentiate discriminate distinguish experiment organize question')
    bt_evaluate = (
        'evaluate appraise argue check critique debate defend evaluate judge measure select support test verify')
    bt_create = (
        'create assemble construct design develop devise formulate generate organize plan produce rearrange rewrite')

    ## create bloom file into bloom_words.csv
    # read_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\word_search'))
    # read_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Text_Analysis\\bloom\\bloom.csv')) # simple list of bloom terms
    # write_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\bloom\\bloom_words.csv')) # full list of bloom terms + files
    #
    # read_files(read_path, read_file, write_path)

    ## create a bloom taxonomy list specific to tier level
    read_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Text_Analysis\\bloom\\bloom_words.csv'))
    write_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Text_Analysis\\bloom\\'))
    save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Text_Analysis\\bloom\\bloom_levels.csv'))

    key_obj = pd.read_csv(read_path)
    key_obj = pd.DataFrame(key_obj).set_index('label')

    df_remember = find_taxonomy(write_path, 'remember', bt_remember, key_obj)
    df_understand = find_taxonomy(write_path, 'understand', bt_understand, key_obj)
    df_apply = find_taxonomy(write_path, 'apply', bt_apply, key_obj)
    df_analyze = find_taxonomy(write_path, 'analyze', bt_analyze, key_obj)
    df_evaluate = find_taxonomy(write_path, 'evaluate', bt_evaluate, key_obj)
    df_create = find_taxonomy(write_path, 'create', bt_create, key_obj)

    df_add = [df_remember, df_understand, df_apply, df_analyze, df_evaluate, df_create]

    result = pd.concat(df_add)

    print(result)

    result.to_csv(save_path, index=False)

    # print(key_obj.to_string())
    # input("Press enter to continue...")

main()
