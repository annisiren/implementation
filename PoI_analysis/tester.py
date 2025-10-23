if not t_list:
    print("new topic")
    t_list.append(row['topic'])
    if not lo_list:
        print("new lo")
        lo_list.append(row['lo'])
        er_dict = row
        lo_dict[row['lo']] = er_dict

        print("new ER")
        print(er_dict)

    elif row['lo'] not in lo_list and lo_list:
        print("new lo")
        lo_list.append(row['lo'])
        er_dict = row
        lo_dict[row['lo']] = er_dict
    else:
        print("old lo")
        er_dict = row
        lo_dict[row['lo']] = er_dict
    t_dict[row['topic']] = lo_dict

elif row['topic'] not in t_list and t_list:
    print("new topic 2")
    t_list.append(row['topic'])
    if row['lo'] not in lo_list and lo_list:
        print("new lo")
        lo_list.append(row['lo'])
        er_dict = row
        lo_dict[row['lo']] = er_dict
    else:
        print("old lo")
        er_dict = row
        lo_dict[row['lo']] = er_dict
    t_dict[row['topic']] = lo_dict
else:
    print("old topic")
    if row['lo'] not in lo_list and lo_list:
        print("new lo")
        lo_list.append(row['lo'])
        er_dict = row
        lo_dict[row['lo']] = er_dict
    else:
        print("old lo")
        er_dict = row
        lo_dict[row['lo']] = er_dict
    t_dict[row['topic']] = lo_dict