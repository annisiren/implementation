from csv import DictReader
import hierarchy_func as hierarchy

def open_file(filepath):
    with (open(filepath, encoding="utf-8-sig") as csvfile):
        csv_reader = DictReader(csvfile)
        data = list(csv_reader)

        er_list = []
        lo_list = []
        t_list = []

        past_t = ''
        past_lo = ''

        for row in data:

            current_t = row['topic']
            current_lo = row['lo']
            current_er = row['er']

            ER = hierarchy.EducationalResource(current_t, current_lo, current_er, row)

            if past_t == '':
                er_list.append(ER)
                past_t = current_t
                past_lo = current_lo
            elif current_t == past_t:
                if current_lo == past_lo:
                    er_list.append(ER)
                elif current_lo != past_lo:
                    LO = hierarchy.LearningObject(current_t, past_lo, er_list)
                    er_list = []
                    er_list.append(ER)

                    lo_list.append(LO)
                past_t = current_t
                past_lo = current_lo
            elif current_t != past_t:
                LO = hierarchy.LearningObject(past_t, past_lo, er_list)
                lo_list.append(LO)
                T = hierarchy.Topic(past_t, lo_list)
                t_list.append(T)
                lo_list = []
                er_list = []
                er_list.append(ER)

                past_t = current_t
                past_lo = current_lo

    LO = hierarchy.LearningObject(past_t, past_lo, er_list)
    lo_list.append(LO)
    T = hierarchy.Topic(past_t, lo_list)
    t_list.append(T)

    course = hierarchy.Course(t_list)
    return course


