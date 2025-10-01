from venv import create

from fontTools.misc.cython import returns

import sop_obj as func
from csv import DictReader
from copy import deepcopy
import csv

# Topic { LO { ER{}}}

# tier,title,ls_perception,ls_input,ls_organization,ls_processing,ls_understanding,ct,d,bt,p

def open_file(filepath):
    with (open(filepath, encoding="utf-8-sig") as csvfile):
        csv_reader = DictReader(csvfile)
        data = list(csv_reader)
        course = func.Course([])

        T_list = []
        ER_list = []
        LO_list = []
        er_tag = None
        lo_tag = None
        er_temp = None
        lo_temp = None

        for row in reversed(data):

            if row['tier'].startswith('ER'):
                if er_temp and row['tier'].endswith('_1'):
                    er_tag = True
                    er_temp = False
                else:
                    if not row['tier'].endswith('_1'):
                        er_tag = True
                        er_temp = True
                    else:
                        er_tag = False
                ER = func.EducationalResource(row['tier'], row['title'], er_tag, row['LS: Perception'], row['LS: Input'], row['LS: Organization'],
                     row['LS: Processing'], row['LS: Understanding'], row['CT'], row['D'], row['BT'], row['P'])
                ER.C_CV()
                ER_list.append(ER)

            elif row['tier'].startswith('LO'):
                if lo_temp and row['tier'].endswith('_1'):
                    er_tag = True
                    lo_temp = False
                else:
                    if not row['tier'].endswith('_1'):
                        lo_tag = True
                        lo_temp = True
                    else:
                        lo_tag = False
                LO = func.LearningObject(row['tier'],row['title'], lo_tag, row['P'], 0)
                LO.er = deepcopy(sorted(ER_list, key=lambda x: x.tier))
                LO.aggregate()
                LO.C_CV()
                LO.V_CV()
                LO_list.append(LO)
                ER_list = []

            elif row['tier'].startswith('T'):
                Topic = func.Topic(row['tier'], row['title'], 0)
                Topic.lo = deepcopy(sorted(LO_list, key=lambda x: x.tier))
                Topic.aggregate()
                Topic.C_CV()
                Topic.V_CV()
                T_list.append(Topic)
                LO_list = []

        course.topic = deepcopy(sorted(T_list, key=lambda x: x.tier))

    return course

def tree(course):
    #   Build tree structure for course and save into file all potential paths through course
    course_list = []
    topic = []
    lo = []
    er = []
    c = func.Tree('course')

    for topic_ in course.topic:
        topic_tree = func.Tree(topic_.tier)
        topic.append(topic_tree)
        for LO_ in topic_.lo:
            lo_tree = func.Tree(LO_.tier)
            lo.append(lo_tree)
            for ER_ in LO_.er:
                er.append(func.Tree(ER_.tier))
            lo_tree.children = deepcopy(er)
            er = []
        topic_tree.children = deepcopy(lo)
        lo = []
        # input("Press enter to continue...")
    c.children = deepcopy(topic)

    return c

def get_paths(t, paths=None, current_path=None):
    if paths is None:
        paths = []
    if current_path is None:
        current_path = []

    current_path.append(t.value)
    if len(t.children) == 0:
        paths.append(current_path)
    else:
        for child in t.children:
            get_paths(child, paths, list(current_path))
    return paths

def save_course(course):
    print("save course")
    fieldnames = ['topic','lo','er', 'ls_p_s', 'ls_p_i', 'ls_i_v', 'ls_i_a', 'ls_o_i', 'ls_o_d', 'ls_pr_a', 'ls_pr_r',
                  'ls_u_s', 'ls_u_g', 'ct_text', 'ct_video', 'ct_image', 'ct_website', 'ct_audio',
                  'd_shallow', 'd_general', 'd_deep', 'bt_remember', 'bt_understand', 'bt_apply',
                  'bt_analyze', 'bt_evaluate', 'bt_create', 'p_adaptive', 'p_adaptable', 'p_none']
    fieldnames_ccv = ['topic','lo','er', 'ls_mean', 'ls_std', 'ls_ccv', 'ct_mean', 'ct_std', 'ct_ccv', 'd_mean', 'd_std', 'd_ccv',
                        'bt_mean', 'bt_std', 'bt_ccv', 'p_mean', 'p_std', 'p_ccv']
    with open('value_topic.csv', 'w', newline='') as file_topic:
        with open('value_lo.csv', 'w', newline='') as file_lo:
            with open('value_er.csv', 'w', newline='') as file_er:
                file_topic.write(','.join([str(i) for i in fieldnames]))
                file_lo.write(','.join([str(i) for i in fieldnames]))
                file_er.write(','.join([str(i) for i in fieldnames]))
                for value in course.topic:
                    save_values(file_topic,value, value.tier, 0, 0)
                    for value_2 in value.lo:
                        save_values(file_lo, value_2, value.tier, value_2.tier, 0)
                        for value_3 in value_2.er:
                            save_values(file_er, value_3, value.tier, value_2.tier, value_3.tier)

    with open('ccv_topic.csv', 'w', newline='') as file_topic:
        with open('ccv_lo.csv', 'w', newline='') as file_lo:
            with open('ccv_er.csv', 'w', newline='') as file_er:
                file_topic.write(','.join([str(i) for i in fieldnames_ccv]))
                file_lo.write(','.join([str(i) for i in fieldnames_ccv]))
                file_er.write(','.join([str(i) for i in fieldnames_ccv]))
                for value in course.topic:
                    save_ccv(file_topic,value, value.tier, 0, 0)
                    for value_2 in value.lo:
                        save_ccv(file_lo, value_2, value.tier, value_2.tier, 0)
                        for value_3 in value_2.er:
                            save_ccv(file_er, value_3, value.tier, value_2.tier, value_3.tier)

    with open('mean_topic.csv', 'w', newline='') as file_topic:
        with open('mean_lo.csv', 'w', newline='') as file_lo:
            file_topic.write(','.join([str(i) for i in fieldnames]))
            file_lo.write(','.join([str(i) for i in fieldnames]))
            for value in course.topic:
                save_mean(file_topic,value, value.tier, 0, 0)
                for value_2 in value.lo:
                    save_mean(file_lo, value_2, value.tier, value_2.tier, 0)

    with open('stdev_topic.csv', 'w', newline='') as file_topic:
        with open('stdev_lo.csv', 'w', newline='') as file_lo:
            file_topic.write(','.join([str(i) for i in fieldnames]))
            file_lo.write(','.join([str(i) for i in fieldnames]))
            for value in course.topic:
                save_std(file_topic,value, value.tier, 0, 0)
                for value_2 in value.lo:
                    save_std(file_lo, value_2, value.tier, value_2.tier, 0)

    with open('vcv_topic.csv', 'w', newline='') as file_topic:
        with open('vcv_lo.csv', 'w', newline='') as file_lo:
            file_topic.write(','.join([str(i) for i in fieldnames]))
            file_lo.write(','.join([str(i) for i in fieldnames]))
            for value in course.topic:
                save_vcv(file_topic,value, value.tier, 0, 0)
                for value_2 in value.lo:
                    save_vcv(file_lo, value_2, value.tier, value_2.tier, 0)

def save_values(writer, value, topic, lo, er):
    save_data = [topic, lo, er,
                 value.ls_p_s, value.ls_p_i, value.ls_i_v, value.ls_i_a, value.ls_o_i,
                 value.ls_o_d, value.ls_pr_a, value.ls_pr_r, value.ls_u_s, value.ls_u_g,
                 value.ct_text, value.ct_video, value.ct_image, value.ct_website, value.ct_audio,
                 value.d_shallow, value.d_general, value.d_deep,
                 value.bt_remember, value.bt_understand,value.bt_apply,value.bt_analyze,
                 value.bt_evaluate,value.bt_create,
                 value.p_adaptive,value.p_adaptable,value.p_none]

    to_save = ','.join([str(i) for i in save_data])
    # print(to_save)
    writer.write('\n')
    writer.write(to_save)

def save_ccv(writer, value, topic, lo, er):
    save_data = [topic, lo, er,
                 value.ls_mean, value.ls_std, value.ls_ccv,
                 value.ct_mean, value.ct_std, value.ct_ccv,
                 value.d_mean, value.d_std, value.d_ccv,
                 value.bt_mean, value.bt_std, value.bt_ccv,
                 value.p_mean, value.p_std, value.p_ccv]

    to_save = ','.join([str(i) for i in save_data])
    # print(to_save)
    writer.write('\n')
    writer.write(to_save)

def save_mean(writer, value, topic, lo, er):
    save_data = [topic, lo, er,
                 value.mean_ls_p_s, value.mean_ls_p_i, value.mean_ls_i_v, value.mean_ls_i_a, value.mean_ls_o_i,
                 value.mean_ls_o_d, value.mean_ls_pr_a, value.mean_ls_pr_r, value.mean_ls_u_s, value.mean_ls_u_g,
                 value.mean_ct_text, value.mean_ct_video, value.mean_ct_image, value.mean_ct_website, value.mean_ct_audio,
                 value.mean_d_shallow, value.mean_d_general, value.mean_d_deep,
                 value.mean_bt_remember, value.mean_bt_understand,value.mean_bt_apply,value.mean_bt_analyze,
                 value.mean_bt_evaluate,value.mean_bt_create,
                 value.mean_p_adaptive,value.mean_p_adaptable,value.mean_p_none]

    to_save = ','.join([str(i) for i in save_data])
    # print(to_save)
    writer.write('\n')
    writer.write(to_save)

def save_std(writer, value, topic, lo, er):
    save_data = [topic, lo, er,
                 value.std_ls_p_s, value.std_ls_p_i, value.std_ls_i_v, value.std_ls_i_a, value.std_ls_o_i,
                 value.std_ls_o_d, value.std_ls_pr_a, value.std_ls_pr_r, value.std_ls_u_s, value.std_ls_u_g,
                 value.std_ct_text, value.std_ct_video, value.std_ct_image, value.std_ct_website, value.std_ct_audio,
                 value.std_d_shallow, value.std_d_general, value.std_d_deep,
                 value.std_bt_remember, value.std_bt_understand,value.std_bt_apply,value.std_bt_analyze,
                 value.std_bt_evaluate,value.std_bt_create,
                 value.std_p_adaptive,value.std_p_adaptable,value.std_p_none]

    to_save = ','.join([str(i) for i in save_data])
    # print(to_save)
    writer.write('\n')
    writer.write(to_save)

def save_vcv(writer, value, topic, lo, er):
    save_data = [topic, lo, er,
                 value.vcv_ls_p_s, value.vcv_ls_p_i, value.vcv_ls_i_v, value.vcv_ls_i_a, value.vcv_ls_o_i,
                 value.vcv_ls_o_d, value.vcv_ls_pr_a, value.vcv_ls_pr_r, value.vcv_ls_u_s, value.vcv_ls_u_g,
                 value.vcv_ct_text, value.vcv_ct_video, value.vcv_ct_image, value.vcv_ct_website, value.vcv_ct_audio,
                 value.vcv_d_shallow, value.vcv_d_general, value.vcv_d_deep,
                 value.vcv_bt_remember, value.vcv_bt_understand,value.vcv_bt_apply,value.vcv_bt_analyze,
                 value.vcv_bt_evaluate,value.vcv_bt_create,
                 value.vcv_p_adaptive,value.vcv_p_adaptable,value.vcv_p_none]

    to_save = ','.join([str(i) for i in save_data])
    # print(to_save)
    writer.write('\n')
    writer.write(to_save)