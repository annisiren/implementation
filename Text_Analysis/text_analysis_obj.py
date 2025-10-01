import time
import os
from os import walk
import pickle
import gc
import numpy
import json

import ta_obj as TA_OBJ
# import ta_pre_processing as TA_PP
# import ta_feature_engineering as TA_FE

START_TIME = time.time()

def read_files(read_path, write_path_pp, write_path_fe):
    print("read_files")
    print(read_path)
    filenames = next(walk(read_path), (None, None, []))[2]  # [] if no file
    obj_list_pp = []
    obj_list_fe = []

    # Go through all files individually
    for file in filenames:
        filename = read_path+'\\'+file
        file_location_pp = write_path_pp +'\\'+file.replace(" ", "_").split('.txt')[0]
        file_location_fe = write_path_fe +'\\'+file.replace(" ", "_").split('.txt')[0]
        keyword_file_name_pp = file_location_pp.replace(" ", "_").split('.')[0]+'.txt'
        keyword_file_name_fe = file_location_fe.replace(" ", "_").split('.')[0]+'.txt'

        with open(filename, 'r', encoding='utf-8') as file:
            obj_pp = TA_OBJ.pre_processing(filename, file.read())

        obj_fe = TA_OBJ.feature_engineering(obj_pp)

        # print(obj_fe.tfidf_wt[0])
        # input("Press enter to continue...")
        # print(read_path+'\\test.csv')
        # numpy.savetxt(read_path+'\\test.csv', obj_fe.tfidf_wt[0], delimiter=",")
        # obj_fe.tfidf_wt[0].to_csv(read_path+'\\test.csv', encoding='utf-8')
        # print(obj_fe.tfidf_wt_two)

        # obj_list_pp.append(obj_pp)
        # obj_list_fe.append(obj_fe)

        save_files(keyword_file_name_pp, obj_pp, keyword_file_name_fe, obj_fe)

        del obj_pp
        del obj_fe
        gc.collect()

    # print(len(obj_list_pp))
    # print(len(obj_list_fe))
    return 0

def save_files(keyword_file_name_pp, obj_pp, keyword_file_name_fe,obj_fe):
    # Checks if the result file exists
    if not os.path.exists(keyword_file_name_pp):
        # save pre-processed content into df and df into files
        print(keyword_file_name_pp)
        with open(keyword_file_name_pp, 'wb') as write_file:
            pickle.dump(obj_pp, write_file)
    else:
        print(keyword_file_name_pp+" file exists.")
    # input("Press enter to continue...")

    # Checks if the result file exists
    if not os.path.exists(keyword_file_name_fe):
        # save pre-processed content into df and df into files
        print(keyword_file_name_fe)
        with open(keyword_file_name_fe, 'wb') as write_file:
            pickle.dump(obj_fe, write_file)
    else:
        print(keyword_file_name_fe+" file exists.")
    # input("Press enter to continue...")

def main():
    read_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\Lecture_Transcripts'))
    pp_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\Pre-Processing'))
    fe_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Text_Analysis\\Feature_Engineering'))

    read_files(read_path, pp_path, fe_path)

    # input("Press enter to continue...")

print("My program took", time.time() - START_TIME, "to run")
main()
