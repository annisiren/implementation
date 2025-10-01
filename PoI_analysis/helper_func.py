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