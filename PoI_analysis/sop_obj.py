from copy import deepcopy
import statistics

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

class Course:
    def __init__(self, topic):
        self.topic = topic
        self.tree = []

class Topic:
    def __init__(self, tier, title, lo):
        self.tier = tier
        self.title = title
        self.ls_p_s = 0
        self.ls_p_i = 0
        self.ls_i_v = 0
        self.ls_i_a = 0
        self.ls_o_i = 0
        self.ls_o_d = 0
        self.ls_pr_a = 0
        self.ls_pr_r = 0
        self.ls_u_s = 0
        self.ls_u_g = 0
        #
        # self.ct_text = 0
        # self.ct_video = 0
        # self.ct_image = 0
        # self.ct_website = 0
        # self.ct_audio = 0
        #
        # self.d_shallow = 0
        # self.d_general = 0
        # self.d_deep = 0
        #
        # self.bt_remember = 0
        # self.bt_understand = 0
        # self.bt_apply = 0
        # self.bt_analyze = 0
        # self.bt_evaluate = 0
        # self.bt_create = 0
        #
        # self.p_adaptive = 0
        # self.p_adaptable = 0
        # self.p_none = 0
        # List of LO objects
        self.lo = lo

    #  Statistics
    # CCV values
        self.ls_mean = 0
        self.ls_std = 0
        self.ls_ccv = 0

        # self.ct_mean = 0
        # self.ct_std = 0
        # self.ct_ccv = 0
        #
        # self.d_mean = 0
        # self.d_std = 0
        # self.d_ccv = 0
        #
        # self.bt_mean = 0
        # self.bt_std = 0
        # self.bt_ccv = 0
        #
        # self.p_mean = 0
        # self.p_std = 0
        # self.p_ccv = 0
    # VCV values
        self.list_ls_p_s = []
        self.list_ls_p_i = []
        self.list_ls_i_v = []
        self.list_ls_i_a = []
        self.list_ls_o_i = []
        self.list_ls_o_d = []
        self.list_ls_pr_a = []
        self.list_ls_pr_r = []
        self.list_ls_u_s = []
        self.list_ls_u_g = []

        # self.list_ct_text = []
        # self.list_ct_video = []
        # self.list_ct_image = []
        # self.list_ct_website = []
        # self.list_ct_audio = []
        #
        # self.list_d_shallow = []
        # self.list_d_general = []
        # self.list_d_deep = []
        #
        # self.list_bt_remember = []
        # self.list_bt_understand = []
        # self.list_bt_apply = []
        # self.list_bt_analyze = []
        # self.list_bt_evaluate = []
        # self.list_bt_create = []
        #
        # self.list_p_adaptive = []
        # self.list_p_adaptable = []
        # self.list_p_none = []
        ## Mean
        self.mean_ls_p_s = 0
        self.mean_ls_p_i = 0
        self.mean_ls_i_v = 0
        self.mean_ls_i_a = 0
        self.mean_ls_o_i = 0
        self.mean_ls_o_d = 0
        self.mean_ls_pr_a = 0
        self.mean_ls_pr_r = 0
        self.mean_ls_u_s = 0
        self.mean_ls_u_g = 0

        # self.mean_ct_text = 0
        # self.mean_ct_video = 0
        # self.mean_ct_image = 0
        # self.mean_ct_website = 0
        # self.mean_ct_audio = 0
        #
        # self.mean_d_shallow = 0
        # self.mean_d_general = 0
        # self.mean_d_deep = 0
        #
        # self.mean_bt_remember = 0
        # self.mean_bt_understand = 0
        # self.mean_bt_apply = 0
        # self.mean_bt_analyze = 0
        # self.mean_bt_evaluate = 0
        # self.mean_bt_create = 0
        #
        # self.mean_p_adaptive = 0
        # self.mean_p_adaptable = 0
        # self.mean_p_none = 0

        ## STD
        self.std_ls_p_s = 0
        self.std_ls_p_i = 0
        self.std_ls_i_v = 0
        self.std_ls_i_a = 0
        self.std_ls_o_i = 0
        self.std_ls_o_d = 0
        self.std_ls_pr_a = 0
        self.std_ls_pr_r = 0
        self.std_ls_u_s = 0
        self.std_ls_u_g = 0

        # self.std_ct_text = 0
        # self.std_ct_video = 0
        # self.std_ct_image = 0
        # self.std_ct_website = 0
        # self.std_ct_audio = 0
        #
        # self.std_d_shallow = 0
        # self.std_d_general = 0
        # self.std_d_deep = 0
        #
        # self.std_bt_remember = 0
        # self.std_bt_understand = 0
        # self.std_bt_apply = 0
        # self.std_bt_analyze = 0
        # self.std_bt_evaluate = 0
        # self.std_bt_create = 0
        #
        # self.std_p_adaptive = 0
        # self.std_p_adaptable = 0
        # self.std_p_none = 0

        ## CCV
        self.vcv_ls_p_s = 0
        self.vcv_ls_p_i = 0
        self.vcv_ls_i_v = 0
        self.vcv_ls_i_a = 0
        self.vcv_ls_o_i = 0
        self.vcv_ls_o_d = 0
        self.vcv_ls_pr_a = 0
        self.vcv_ls_pr_r = 0
        self.vcv_ls_u_s = 0
        self.vcv_ls_u_g = 0

        # self.vcv_ct_text = 0
        # self.vcv_ct_video = 0
        # self.vcv_ct_image = 0
        # self.vcv_ct_website = 0
        # self.vcv_ct_audio = 0
        #
        # self.vcv_d_shallow = 0
        # self.vcv_d_general = 0
        # self.vcv_d_deep = 0
        #
        # self.vcv_bt_remember = 0
        # self.vcv_bt_understand = 0
        # self.vcv_bt_apply = 0
        # self.vcv_bt_analyze = 0
        # self.vcv_bt_evaluate = 0
        # self.vcv_bt_create = 0
        #
        # self.vcv_p_adaptive = 0
        # self.vcv_p_adaptable = 0
        # self.vcv_p_none = 0

    def aggregate(self):
        for LO in self.lo:
            self.ls_p_s = self.ls_p_s + LO.ls_p_s
            self.ls_p_i = self.ls_p_i + LO.ls_p_i
            self.ls_i_v = self.ls_i_v + LO.ls_i_v
            self.ls_i_a = self.ls_i_a + LO.ls_i_a
            self.ls_o_i = self.ls_o_i + LO.ls_o_i
            self.ls_o_d = self.ls_o_d + LO.ls_o_d
            self.ls_pr_a = self.ls_pr_a + LO.ls_pr_a
            self.ls_pr_r = self.ls_pr_r + LO.ls_pr_r
            self.ls_u_s = self.ls_u_s + LO.ls_u_s
            self.ls_u_g = self.ls_u_g + LO.ls_u_g
            #
            # self.ct_text = self.ct_text + LO.ct_text
            # self.ct_video = self.ct_video + LO.ct_video
            # self.ct_image = self.ct_image + LO.ct_image
            # self.ct_website = self.ct_website + LO.ct_website
            # self.ct_audio = self.ct_audio + LO.ct_audio
            #
            # self.d_shallow = self.d_shallow + LO.d_shallow
            # self.d_general = self.d_general + LO.d_general
            # self.d_deep = self.d_deep + LO.d_deep
            #
            # self.bt_remember = self.bt_remember + LO.bt_remember
            # self.bt_understand = self.bt_understand + LO.bt_understand
            # self.bt_apply = self.bt_apply + LO.bt_apply
            # self.bt_analyze = self.bt_analyze + LO.bt_analyze
            # self.bt_evaluate = self.bt_evaluate + LO.bt_evaluate
            # self.bt_create = self.bt_create + LO.bt_create
            #
            # self.p_adaptive = self.p_adaptive + LO.p_adaptive
            # self.p_adaptable = self.p_adaptable + LO.p_adaptable
            # self.p_none = self.p_none + LO.p_none

    def C_CV(self):
        # print('LO CCV')
        # Learning style
        self.ls_mean = round(
            statistics.mean([self.ls_p_s, self.ls_p_i, self.ls_i_v, self.ls_i_a, self.ls_o_i, self.ls_o_d, self.ls_pr_a,
                             self.ls_pr_r, self.ls_u_s, self.ls_u_g]), 2)

        self.ls_std = round(statistics.stdev(
            [self.ls_p_s, self.ls_p_i, self.ls_i_v, self.ls_i_a, self.ls_o_i, self.ls_o_d, self.ls_pr_a,
             self.ls_pr_r, self.ls_u_s, self.ls_u_g]), 2)

        self.ls_ccv = round(deepcopy(self.ls_std / self.ls_mean), 2)

        # # Content type
        #
        # self.ct_mean = round(statistics.mean(
        #     [self.ct_text, self.ct_video, self.ct_image, self.ct_website, self.ct_audio]), 2)
        #
        # self.ct_std = round(statistics.stdev(
        #     [self.ct_text, self.ct_video, self.ct_image, self.ct_website, self.ct_audio]), 2)
        #
        # self.ct_ccv = round(deepcopy(self.ct_std / self.ct_mean), 2)
        #
        # # Depth
        #
        # self.d_mean = round(statistics.mean(
        #     [self.d_shallow, self.d_general, self.d_deep]), 2)
        #
        # self.d_std = round(statistics.stdev(
        #     [self.d_shallow, self.d_general, self.d_deep]), 2)
        #
        # self.d_ccv = round(deepcopy(self.d_std / self.d_mean), 2)
        #
        # # Bloom's Taxonomy
        #
        # self.bt_mean = round(statistics.mean(
        #     [self.bt_remember, self.bt_understand, self.bt_apply, self.bt_analyze,
        #      self.bt_evaluate, self.bt_create]), 2)
        #
        # self.bt_std = round(statistics.stdev(
        #     [self.bt_remember, self.bt_understand, self.bt_apply, self.bt_analyze,
        #      self.bt_evaluate, self.bt_create]), 2)
        #
        # self.bt_ccv = round(deepcopy(self.bt_std / self.bt_mean), 2)
        #
        # # Personalization
        #
        # self.p_mean = round(statistics.mean([self.p_adaptive, self.p_adaptable, self.p_none]), 2)
        #
        # self.p_std = round(statistics.stdev([self.p_adaptive, self.p_adaptable, self.p_none]), 2)
        #
        # self.p_ccv = round(deepcopy(self.p_std / self.p_mean), 2)

    def V_CV(self):
        # print('LO VCV')

        for LO in self.lo:
            self.list_ls_p_s.append(LO.ls_p_s)
            self.list_ls_p_i.append(LO.ls_p_i)
            self.list_ls_i_v.append(LO.ls_i_v)
            self.list_ls_i_a.append(LO.ls_i_a)
            self.list_ls_o_i.append(LO.ls_o_i)
            self.list_ls_o_d.append(LO.ls_o_d)
            self.list_ls_pr_a.append(LO.ls_pr_a)
            self.list_ls_pr_r.append(LO.ls_pr_r)
            self.list_ls_u_s.append(LO.ls_u_s)
            self.list_ls_u_g.append(LO.ls_u_g)

            # self.list_ct_text.append(LO.ct_text)
            # self.list_ct_video.append(LO.ct_video)
            # self.list_ct_image.append(LO.ct_image)
            # self.list_ct_website.append(LO.ct_website)
            # self.list_ct_audio.append(LO.ct_audio)
            #
            # self.list_d_shallow.append(LO.d_shallow)
            # self.list_d_general.append(LO.d_general)
            # self.list_d_deep.append(LO.d_deep)
            #
            # self.list_bt_remember.append(LO.bt_remember)
            # self.list_bt_understand.append(LO.bt_understand)
            # self.list_bt_apply.append(LO.bt_apply)
            # self.list_bt_analyze.append(LO.bt_analyze)
            # self.list_bt_evaluate.append(LO.bt_evaluate)
            # self.list_bt_create.append(LO.bt_create)
            #
            # self.list_p_adaptive.append(LO.p_adaptive)
            # self.list_p_adaptable.append(LO.p_adaptable)
            # self.list_p_none.append(LO.p_none)

        # VCV values
        ## Mean
        self.mean_ls_p_s = self.mean(self.list_ls_p_s)
        self.mean_ls_p_i = self.mean(self.list_ls_p_i)
        self.mean_ls_i_v = self.mean(self.list_ls_i_v)
        self.mean_ls_i_a = self.mean(self.list_ls_i_a)
        self.mean_ls_o_i = self.mean(self.list_ls_o_i)
        self.mean_ls_o_d = self.mean(self.list_ls_o_d)
        self.mean_ls_pr_a = self.mean(self.list_ls_pr_a)
        self.mean_ls_pr_r = self.mean(self.list_ls_pr_r)
        self.mean_ls_u_s = self.mean(self.list_ls_u_s)
        self.mean_ls_u_g = self.mean(self.list_ls_u_g)

        # self.mean_ct_text = self.mean(self.list_ct_text)
        # self.mean_ct_video = self.mean(self.list_ct_video)
        # self.mean_ct_image = self.mean(self.list_ct_image)
        # self.mean_ct_website = self.mean(self.list_ct_website)
        # self.mean_ct_audio = self.mean(self.list_ct_audio)
        #
        # self.mean_d_shallow = self.mean(self.list_d_shallow)
        # self.mean_d_general = self.mean(self.list_d_general)
        # self.mean_d_deep = self.mean(self.list_d_deep)
        #
        # self.mean_bt_remember = self.mean(self.list_bt_remember)
        # self.mean_bt_understand = self.mean(self.list_bt_understand)
        # self.mean_bt_apply = self.mean(self.list_bt_apply)
        # self.mean_bt_analyze = self.mean(self.list_bt_analyze)
        # self.mean_bt_evaluate = self.mean(self.list_bt_evaluate)
        # self.mean_bt_create = self.mean(self.list_bt_create)
        #
        # self.mean_p_adaptive = self.mean(self.list_p_adaptive)
        # self.mean_p_adaptable = self.mean(self.list_p_adaptable)
        # self.mean_p_none = self.mean(self.list_p_none)

        ## STD
        self.std_ls_p_s = self.stdev(self.list_ls_p_s)
        self.std_ls_p_i = self.stdev(self.list_ls_p_i)
        self.std_ls_i_v = self.stdev(self.list_ls_i_v)
        self.std_ls_i_a = self.stdev(self.list_ls_i_a)
        self.std_ls_o_i = self.stdev(self.list_ls_o_i)
        self.std_ls_o_d = self.stdev(self.list_ls_o_d)
        self.std_ls_pr_a = self.stdev(self.list_ls_pr_a)
        self.std_ls_pr_r = self.stdev(self.list_ls_pr_r)
        self.std_ls_u_s = self.stdev(self.list_ls_u_s)
        self.std_ls_u_g = self.stdev(self.list_ls_u_g)

        # self.std_ct_text = self.stdev(self.list_ct_text)
        # self.std_ct_video = self.stdev(self.list_ct_video)
        # self.std_ct_image = self.stdev(self.list_ct_image)
        # self.std_ct_website = self.stdev(self.list_ct_website)
        # self.std_ct_audio = self.stdev(self.list_ct_audio)
        #
        # self.std_d_shallow = self.stdev(self.list_d_shallow)
        # self.std_d_general = self.stdev(self.list_d_general)
        # self.std_d_deep = self.stdev(self.list_d_deep)
        #
        # self.std_bt_remember = self.stdev(self.list_bt_remember)
        # self.std_bt_understand = self.stdev(self.list_bt_understand)
        # self.std_bt_apply = self.stdev(self.list_bt_apply)
        # self.std_bt_analyze = self.stdev(self.list_bt_analyze)
        # self.std_bt_evaluate = self.stdev(self.list_bt_evaluate)
        # self.std_bt_create = self.stdev(self.list_bt_create)
        #
        # self.std_p_adaptive = self.stdev(self.list_p_adaptive)
        # self.std_p_adaptable = self.stdev(self.list_p_adaptable)
        # self.std_p_none = self.stdev(self.list_p_none)

        ## CCV
        self.vcv_ls_p_s = self.vcv(self.list_ls_p_s)
        self.vcv_ls_p_i = self.vcv(self.list_ls_p_i)
        self.vcv_ls_i_v = self.vcv(self.list_ls_i_v)
        self.vcv_ls_i_a = self.vcv(self.list_ls_i_a)
        self.vcv_ls_o_i = self.vcv(self.list_ls_o_i)
        self.vcv_ls_o_d = self.vcv(self.list_ls_o_d)
        self.vcv_ls_pr_a = self.vcv(self.list_ls_pr_a)
        self.vcv_ls_pr_r = self.vcv(self.list_ls_pr_r)
        self.vcv_ls_u_s = self.vcv(self.list_ls_u_s)
        self.vcv_ls_u_g = self.vcv(self.list_ls_u_g)

        # self.vcv_ct_text = self.vcv(self.list_ct_text)
        # self.vcv_ct_video = self.vcv(self.list_ct_video)
        # self.vcv_ct_image = self.vcv(self.list_ct_image)
        # self.vcv_ct_website = self.vcv(self.list_ct_website)
        # self.vcv_ct_audio = self.vcv(self.list_ct_audio)
        #
        # self.vcv_d_shallow = self.vcv(self.list_d_shallow)
        # self.vcv_d_general = self.vcv(self.list_d_general)
        # self.vcv_d_deep = self.vcv(self.list_d_deep)
        #
        # self.vcv_bt_remember = self.vcv(self.list_bt_remember)
        # self.vcv_bt_understand = self.vcv(self.list_bt_understand)
        # self.vcv_bt_apply = self.vcv(self.list_bt_apply)
        # self.vcv_bt_analyze = self.vcv(self.list_bt_analyze)
        # self.vcv_bt_evaluate = self.vcv(self.list_bt_evaluate)
        # self.vcv_bt_create = self.vcv(self.list_bt_create)
        #
        # self.vcv_p_adaptive = self.vcv(self.list_p_adaptive)
        # self.vcv_p_adaptable = self.vcv(self.list_p_adaptable)
        # self.vcv_p_none = self.vcv(self.list_p_none)

    def mean(self, list):
        return round(statistics.mean(list), 2)

    def stdev(self, list):
        return round(statistics.stdev(list), 2)

    def vcv(self, list):
        try:
            return round(statistics.stdev(list), 2)/round(statistics.mean(list), 2)
        except:
            return 'N/A'

class LearningObject:
    def __init__(self, tier, title, tag, p, er):
        self.tier = tier
        self.title = title
        self.tag = tag
        self.ls_p_s = 0
        self.ls_p_i = 0
        self.ls_i_v = 0
        self.ls_i_a = 0
        self.ls_o_i = 0
        self.ls_o_d = 0
        self.ls_pr_a = 0
        self.ls_pr_r = 0
        self.ls_u_s = 0
        self.ls_u_g = 0

        # self.ct_text = 0
        # self.ct_video = 0
        # self.ct_image = 0
        # self.ct_website = 0
        # self.ct_audio = 0
        #
        # self.d_shallow = 0
        # self.d_general = 0
        # self.d_deep = 0
        #
        # self.bt_remember = 0
        # self.bt_understand = 0
        # self.bt_apply = 0
        # self.bt_analyze = 0
        # self.bt_evaluate = 0
        # self.bt_create = 0

        # self.p = p
        # if self.p.lower().strip() == 'adaptive':
        #     self.p_adaptive = 1
        #     self.p_adaptable = 0
        #     self.p_none = 0
        # elif self.p.lower().strip() == 'adaptable':
        #     self.p_adaptive = 0
        #     self.p_adaptable = 1
        #     self.p_none = 0
        # elif self.p.lower().strip() == 'none':
        #     self.p_adaptive = 0
        #     self.p_adaptable = 0
        #     self.p_none = 1
        # else:
        #     self.p_adaptive = 0
        #     self.p_adaptable = 0
        #     self.p_none = 0
        # List of ER objects
        self.er = er

    #  Statistics
        # CCV values
        self.ls_mean = 0
        self.ls_std = 0
        self.ls_ccv = 0

        # self.ct_mean = 0
        # self.ct_std = 0
        # self.ct_ccv = 0
        #
        # self.d_mean = 0
        # self.d_std = 0
        # self.d_ccv = 0
        #
        # self.bt_mean = 0
        # self.bt_std = 0
        # self.bt_ccv = 0
        #
        # self.p_mean = 0
        # self.p_std = 0
        # self.p_ccv = 0

        # VCV values
        self.list_ls_p_s = []
        self.list_ls_p_i = []
        self.list_ls_i_v = []
        self.list_ls_i_a = []
        self.list_ls_o_i = []
        self.list_ls_o_d = []
        self.list_ls_pr_a = []
        self.list_ls_pr_r = []
        self.list_ls_u_s = []
        self.list_ls_u_g = []

        # self.list_ct_text = []
        # self.list_ct_video = []
        # self.list_ct_image = []
        # self.list_ct_website = []
        # self.list_ct_audio = []
        #
        # self.list_d_shallow = []
        # self.list_d_general = []
        # self.list_d_deep = []
        #
        # self.list_bt_remember = []
        # self.list_bt_understand = []
        # self.list_bt_apply = []
        # self.list_bt_analyze = []
        # self.list_bt_evaluate = []
        # self.list_bt_create = []
        #
        # self.list_p_adaptive = []
        # self.list_p_adaptable = []
        # self.list_p_none = []

        ## Mean
        self.mean_ls_p_s = 0
        self.mean_ls_p_i = 0
        self.mean_ls_i_v = 0
        self.mean_ls_i_a = 0
        self.mean_ls_o_i = 0
        self.mean_ls_o_d = 0
        self.mean_ls_pr_a = 0
        self.mean_ls_pr_r = 0
        self.mean_ls_u_s = 0
        self.mean_ls_u_g = 0

        # self.mean_ct_text = 0
        # self.mean_ct_video = 0
        # self.mean_ct_image = 0
        # self.mean_ct_website = 0
        # self.mean_ct_audio = 0
        #
        # self.mean_d_shallow = 0
        # self.mean_d_general = 0
        # self.mean_d_deep = 0
        #
        # self.mean_bt_remember = 0
        # self.mean_bt_understand = 0
        # self.mean_bt_apply = 0
        # self.mean_bt_analyze = 0
        # self.mean_bt_evaluate = 0
        # self.mean_bt_create = 0
        #
        # self.mean_p_adaptive = 0
        # self.mean_p_adaptable = 0
        # self.mean_p_none = 0

        ## STD
        self.std_ls_p_s = 0
        self.std_ls_p_i = 0
        self.std_ls_i_v = 0
        self.std_ls_i_a = 0
        self.std_ls_o_i = 0
        self.std_ls_o_d = 0
        self.std_ls_pr_a = 0
        self.std_ls_pr_r = 0
        self.std_ls_u_s = 0
        self.std_ls_u_g = 0

        # self.std_ct_text = 0
        # self.std_ct_video = 0
        # self.std_ct_image = 0
        # self.std_ct_website = 0
        # self.std_ct_audio = 0
        #
        # self.std_d_shallow = 0
        # self.std_d_general = 0
        # self.std_d_deep = 0
        #
        # self.std_bt_remember = 0
        # self.std_bt_understand = 0
        # self.std_bt_apply = 0
        # self.std_bt_analyze = 0
        # self.std_bt_evaluate = 0
        # self.std_bt_create = 0
        #
        # self.std_p_adaptive = 0
        # self.std_p_adaptable = 0
        # self.std_p_none = 0

        ## VCV
        self.vcv_ls_p_s = 0
        self.vcv_ls_p_i = 0
        self.vcv_ls_i_v = 0
        self.vcv_ls_i_a = 0
        self.vcv_ls_o_i = 0
        self.vcv_ls_o_d = 0
        self.vcv_ls_pr_a = 0
        self.vcv_ls_pr_r = 0
        self.vcv_ls_u_s = 0
        self.vcv_ls_u_g = 0

        # self.vcv_ct_text = 0
        # self.vcv_ct_video = 0
        # self.vcv_ct_image = 0
        # self.vcv_ct_website = 0
        # self.vcv_ct_audio = 0
        #
        # self.vcv_d_shallow = 0
        # self.vcv_d_general = 0
        # self.vcv_d_deep = 0
        #
        # self.vcv_bt_remember = 0
        # self.vcv_bt_understand = 0
        # self.vcv_bt_apply = 0
        # self.vcv_bt_analyze = 0
        # self.vcv_bt_evaluate = 0
        # self.vcv_bt_create = 0
        #
        # self.vcv_p_adaptive = 0
        # self.vcv_p_adaptable = 0
        # self.vcv_p_none = 0

    def aggregate(self):
        for ER in self.er:
            self.ls_p_s = self.ls_p_s + ER.ls_p_s
            self.ls_p_i = self.ls_p_i + ER.ls_p_i
            self.ls_i_v = self.ls_i_v + ER.ls_i_v
            self.ls_i_a = self.ls_i_a + ER.ls_i_a
            self.ls_o_i = self.ls_o_i + ER.ls_o_i
            self.ls_o_d = self.ls_o_d + ER.ls_o_d
            self.ls_pr_a = self.ls_pr_a + ER.ls_pr_a
            self.ls_pr_r = self.ls_pr_r + ER.ls_pr_r
            self.ls_u_s = self.ls_u_s + ER.ls_u_s
            self.ls_u_g = self.ls_u_g + ER.ls_u_g

            # self.ct_text = self.ct_text + ER.ct_text
            # self.ct_video = self.ct_video + ER.ct_video
            # self.ct_image = self.ct_image + ER.ct_image
            # self.ct_website = self.ct_website + ER.ct_website
            # self.ct_audio = self.ct_audio + ER.ct_audio
            #
            # self.d_shallow = self.d_shallow + ER.d_shallow
            # self.d_general = self.d_general + ER.d_general
            # self.d_deep = self.d_deep + ER.d_deep
            #
            # self.bt_remember = deepcopy(self.bt_remember) + ER.bt_remember
            # self.bt_understand = deepcopy(self.bt_understand) + ER.bt_understand
            # self.bt_apply = deepcopy(self.bt_apply) + ER.bt_apply
            # self.bt_analyze = deepcopy(self.bt_analyze) + ER.bt_analyze
            # self.bt_evaluate = deepcopy(self.bt_evaluate) + ER.bt_evaluate
            # self.bt_create = deepcopy(self.bt_create) + ER.bt_create
            #
            # self.p_adaptive = self.p_adaptive + ER.p_adaptive
            # self.p_adaptable = self.p_adaptable + ER.p_adaptable
            # self.p_none = self.p_none + ER.p_none

    def C_CV(self):

        # Learning style
        self.ls_mean = round(
            statistics.mean([self.ls_p_s, self.ls_p_i, self.ls_i_v, self.ls_i_a, self.ls_o_i, self.ls_o_d, self.ls_pr_a,
                             self.ls_pr_r, self.ls_u_s, self.ls_u_g]), 2)

        self.ls_std = round(statistics.stdev(
            [self.ls_p_s, self.ls_p_i, self.ls_i_v, self.ls_i_a, self.ls_o_i, self.ls_o_d, self.ls_pr_a,
             self.ls_pr_r, self.ls_u_s, self.ls_u_g]), 2)

        self.ls_ccv = round(deepcopy(self.ls_std / self.ls_mean), 2)

        # # Content type
        #
        # self.ct_mean = round(statistics.mean(
        #     [self.ct_text, self.ct_video, self.ct_image, self.ct_website, self.ct_audio]), 2)
        #
        # self.ct_std = round(statistics.stdev(
        #     [self.ct_text, self.ct_video, self.ct_image, self.ct_website, self.ct_audio]), 2)
        #
        # self.ct_ccv = round(deepcopy(self.ct_std / self.ct_mean), 2)
        #
        # # Depth
        #
        # self.d_mean = round(statistics.mean(
        #     [self.d_shallow, self.d_general, self.d_deep]), 2)
        #
        # self.d_std = round(statistics.stdev(
        #     [self.d_shallow, self.d_general, self.d_deep]), 2)
        #
        # self.d_ccv = round(deepcopy(self.d_std / self.d_mean), 2)
        #
        # # Bloom's Taxonomy
        #
        # self.bt_mean = round(statistics.mean(
        #     [self.bt_remember, self.bt_understand, self.bt_apply, self.bt_analyze,
        #      self.bt_evaluate, self.bt_create]), 2)
        #
        # self.bt_std = round(statistics.stdev(
        #     [self.bt_remember, self.bt_understand, self.bt_apply, self.bt_analyze,
        #      self.bt_evaluate, self.bt_create]), 2)
        #
        # self.bt_ccv = round(deepcopy(self.bt_std / self.bt_mean), 2)
        #
        # # Personalization
        #
        # self.p_mean = round(statistics.mean([self.p_adaptive, self.p_adaptable, self.p_none]), 2)
        #
        # self.p_std = round(statistics.stdev([self.p_adaptive, self.p_adaptable, self.p_none]), 2)
        #
        # try:
        #     self.p_ccv = round(deepcopy(self.p_std / self.p_mean), 2)
        # except:
        #     self.p_ccv = 'N/A'

    def V_CV(self):
        # print('LO VCV')

        for ER in self.er:
            self.list_ls_p_s.append(ER.ls_p_s)
            self.list_ls_p_i.append(ER.ls_p_i)
            self.list_ls_i_v.append(ER.ls_i_v)
            self.list_ls_i_a.append(ER.ls_i_a)
            self.list_ls_o_i.append(ER.ls_o_i)
            self.list_ls_o_d.append(ER.ls_o_d)
            self.list_ls_pr_a.append(ER.ls_pr_a)
            self.list_ls_pr_r.append(ER.ls_pr_r)
            self.list_ls_u_s.append(ER.ls_u_s)
            self.list_ls_u_g.append(ER.ls_u_g)

            # self.list_ct_text.append(ER.ct_text)
            # self.list_ct_video.append(ER.ct_video)
            # self.list_ct_image.append(ER.ct_image)
            # self.list_ct_website.append(ER.ct_website)
            # self.list_ct_audio.append(ER.ct_audio)
            #
            # self.list_d_shallow.append(ER.d_shallow)
            # self.list_d_general.append(ER.d_general)
            # self.list_d_deep.append(ER.d_deep)
            #
            # self.list_bt_remember.append(ER.bt_remember)
            # self.list_bt_understand.append(ER.bt_understand)
            # self.list_bt_apply.append(ER.bt_apply)
            # self.list_bt_analyze.append(ER.bt_analyze)
            # self.list_bt_evaluate.append(ER.bt_evaluate)
            # self.list_bt_create.append(ER.bt_create)
            #
            # self.list_p_adaptive.append(ER.p_adaptive)
            # self.list_p_adaptable.append(ER.p_adaptable)
            # self.list_p_none.append(ER.p_none)

        # VCV values
        ## Mean
        self.mean_ls_p_s = self.mean(self.list_ls_p_s)
        self.mean_ls_p_i = self.mean(self.list_ls_p_i)
        self.mean_ls_i_v = self.mean(self.list_ls_i_v)
        self.mean_ls_i_a = self.mean(self.list_ls_i_a)
        self.mean_ls_o_i = self.mean(self.list_ls_o_i)
        self.mean_ls_o_d = self.mean(self.list_ls_o_d)
        self.mean_ls_pr_a = self.mean(self.list_ls_pr_a)
        self.mean_ls_pr_r = self.mean(self.list_ls_pr_r)
        self.mean_ls_u_s = self.mean(self.list_ls_u_s)
        self.mean_ls_u_g = self.mean(self.list_ls_u_g)

        # self.mean_ct_text = self.mean(self.list_ct_text)
        # self.mean_ct_video = self.mean(self.list_ct_video)
        # self.mean_ct_image = self.mean(self.list_ct_image)
        # self.mean_ct_website = self.mean(self.list_ct_website)
        # self.mean_ct_audio = self.mean(self.list_ct_audio)
        #
        # self.mean_d_shallow = self.mean(self.list_d_shallow)
        # self.mean_d_general = self.mean(self.list_d_general)
        # self.mean_d_deep = self.mean(self.list_d_deep)
        #
        # self.mean_bt_remember = self.mean(self.list_bt_remember)
        # self.mean_bt_understand = self.mean(self.list_bt_understand)
        # self.mean_bt_apply = self.mean(self.list_bt_apply)
        # self.mean_bt_analyze = self.mean(self.list_bt_analyze)
        # self.mean_bt_evaluate = self.mean(self.list_bt_evaluate)
        # self.mean_bt_create = self.mean(self.list_bt_create)
        #
        # self.mean_p_adaptive = self.mean(self.list_p_adaptive)
        # self.mean_p_adaptable = self.mean(self.list_p_adaptable)
        # self.mean_p_none = self.mean(self.list_p_none)

        ## STD
        self.std_ls_p_s = self.stdev(self.list_ls_p_s)
        self.std_ls_p_i = self.stdev(self.list_ls_p_i)
        self.std_ls_i_v = self.stdev(self.list_ls_i_v)
        self.std_ls_i_a = self.stdev(self.list_ls_i_a)
        self.std_ls_o_i = self.stdev(self.list_ls_o_i)
        self.std_ls_o_d = self.stdev(self.list_ls_o_d)
        self.std_ls_pr_a = self.stdev(self.list_ls_pr_a)
        self.std_ls_pr_r = self.stdev(self.list_ls_pr_r)
        self.std_ls_u_s = self.stdev(self.list_ls_u_s)
        self.std_ls_u_g = self.stdev(self.list_ls_u_g)

        # self.std_ct_text = self.stdev(self.list_ct_text)
        # self.std_ct_video = self.stdev(self.list_ct_video)
        # self.std_ct_image = self.stdev(self.list_ct_image)
        # self.std_ct_website = self.stdev(self.list_ct_website)
        # self.std_ct_audio = self.stdev(self.list_ct_audio)
        #
        # self.std_d_shallow = self.stdev(self.list_d_shallow)
        # self.std_d_general = self.stdev(self.list_d_general)
        # self.std_d_deep = self.stdev(self.list_d_deep)
        #
        # self.std_bt_remember = self.stdev(self.list_bt_remember)
        # self.std_bt_understand = self.stdev(self.list_bt_understand)
        # self.std_bt_apply = self.stdev(self.list_bt_apply)
        # self.std_bt_analyze = self.stdev(self.list_bt_analyze)
        # self.std_bt_evaluate = self.stdev(self.list_bt_evaluate)
        # self.std_bt_create = self.stdev(self.list_bt_create)
        #
        # self.std_p_adaptive = self.stdev(self.list_p_adaptive)
        # self.std_p_adaptable = self.stdev(self.list_p_adaptable)
        # self.std_p_none = self.stdev(self.list_p_none)

        ## CCV
        self.vcv_ls_p_s = self.vcv(self.list_ls_p_s)
        self.vcv_ls_p_i = self.vcv(self.list_ls_p_i)
        self.vcv_ls_i_v = self.vcv(self.list_ls_i_v)
        self.vcv_ls_i_a = self.vcv(self.list_ls_i_a)
        self.vcv_ls_o_i = self.vcv(self.list_ls_o_i)
        self.vcv_ls_o_d = self.vcv(self.list_ls_o_d)
        self.vcv_ls_pr_a = self.vcv(self.list_ls_pr_a)
        self.vcv_ls_pr_r = self.vcv(self.list_ls_pr_r)
        self.vcv_ls_u_s = self.vcv(self.list_ls_u_s)
        self.vcv_ls_u_g = self.vcv(self.list_ls_u_g)

        # self.vcv_ct_text = self.vcv(self.list_ct_text)
        # self.vcv_ct_video = self.vcv(self.list_ct_video)
        # self.vcv_ct_image = self.vcv(self.list_ct_image)
        # self.vcv_ct_website = self.vcv(self.list_ct_website)
        # self.vcv_ct_audio = self.vcv(self.list_ct_audio)
        #
        # self.vcv_d_shallow = self.vcv(self.list_d_shallow)
        # self.vcv_d_general = self.vcv(self.list_d_general)
        # self.vcv_d_deep = self.vcv(self.list_d_deep)
        #
        # self.vcv_bt_remember = self.vcv(self.list_bt_remember)
        # self.vcv_bt_understand = self.vcv(self.list_bt_understand)
        # self.vcv_bt_apply = self.vcv(self.list_bt_apply)
        # self.vcv_bt_analyze = self.vcv(self.list_bt_analyze)
        # self.vcv_bt_evaluate = self.vcv(self.list_bt_evaluate)
        # self.vcv_bt_create = self.vcv(self.list_bt_create)
        #
        # self.vcv_p_adaptive = self.vcv(self.list_p_adaptive)
        # self.vcv_p_adaptable = self.vcv(self.list_p_adaptable)
        # self.vcv_p_none = self.vcv(self.list_p_none)

    def mean(self, list):
        return round(statistics.mean(list), 2)

    def stdev(self, list):
        try:
            return round(statistics.stdev(list), 2)
        except:
            return 'N/A'

    def vcv(self, list):
        try:
            return round(statistics.stdev(list), 2)/round(statistics.mean(list), 2)
        except:
            return 'N/A'

class EducationalResource:
    def __init__(self, tier,title, tag, ls_perception,ls_input,ls_organization,ls_processing,ls_understanding,ct,d,bt,p):
        self.tier = tier
        self.title = title
        self.tag = tag
        self.ls_perception = ls_perception
        self.ls_input = ls_input
        self.ls_organization = ls_organization
        self.ls_processing = ls_processing
        self.ls_understanding = ls_understanding
        if ls_perception.lower().strip() == 'p:s':
            self.ls_p_s = 1
            self.ls_p_i = 0
        else:
            self.ls_p_s = 0
            self.ls_p_i = 1
        if ls_input.lower().strip() == 'i:v':
            self.ls_i_v = 1
            self.ls_i_a = 0
        else:
            self.ls_i_v = 0
            self.ls_i_a = 1
        if ls_organization.lower().strip() == 'o:i':
            self.ls_o_i = 1
            self.ls_o_d = 0
        elif ls_organization.lower().strip() == 'o:d':
            self.ls_o_i = 0
            self.ls_o_d = 1
        else:
            self.ls_o_i = 0
            self.ls_o_d = 0
        if ls_processing.lower().strip() == 'pr:a':
            self.ls_pr_a = 1
            self.ls_pr_r = 0
        elif ls_processing.lower().strip() == 'pr:r':
            self.ls_pr_a = 0
            self.ls_pr_r = 1
        else:
            self.ls_pr_a = 0
            self.ls_pr_r = 0
        if ls_understanding.lower().strip() == 'u:s':
            self.ls_u_s = 1
            self.ls_u_g = 0
        elif ls_understanding.lower().strip() == 'u:g':
            self.ls_u_s = 0
            self.ls_u_g = 1
        else:
            self.ls_u_s = 0
            self.ls_u_g = 0

        self.ct = ct
        if self.ct.lower().strip() == 'text':
            self.ct_text = 1
            self.ct_video = 0
            self.ct_image = 0
            self.ct_website = 0
            self.ct_audio = 0
        elif self.ct.lower().strip() == 'video':
            self.ct_text = 0
            self.ct_video = 1
            self.ct_image = 0
            self.ct_website = 0
            self.ct_audio = 0
        elif self.ct.lower().strip() == 'image':
            self.ct_text = 0
            self.ct_video = 0
            self.ct_image = 1
            self.ct_website = 0
            self.ct_audio = 0
        elif self.ct.lower().strip() == 'website':
            self.ct_text = 0
            self.ct_video = 0
            self.ct_image = 0
            self.ct_website = 1
            self.ct_audio = 0
        elif self.ct.lower().strip() == 'audio':
            self.ct_text = 0
            self.ct_video = 0
            self.ct_image = 0
            self.ct_website = 0
            self.ct_audio = 1
        else:
            self.ct_text = 0
            self.ct_video = 0
            self.ct_image = 0
            self.ct_website = 0
            self.ct_audio = 0

        self.d = d
        if self.d.lower().strip() == 'shallow':
            self.d_shallow = 1
            self.d_general = 0
            self.d_deep = 0
        elif self.d.lower().strip() == 'general':
            self.d_shallow = 0
            self.d_general = 1
            self.d_deep = 0
        elif self.d.lower().strip() == 'deep':
            self.d_shallow = 0
            self.d_general = 0
            self.d_deep = 1
        else:
            self.d_shallow = 0
            self.d_general = 0
            self.d_deep = 0

        self.bt = bt
        self.bt_remember = 0
        self.bt_understand = 0
        self.bt_apply = 0
        self.bt_analyze = 0
        self.bt_evaluate = 0
        self.bt_create = 0
        if 'remember' in self.bt.lower():
            self.bt_remember = 1
        if 'understand' in self.bt.lower():
            self.bt_understand = 1
        if 'apply' in self.bt.lower():
            self.bt_apply = 1
        if 'analyze' in self.bt.lower():
            self.bt_analyze = 1
        if 'evaluate' in self.bt.lower():
            self.bt_evaluate = 1
        if 'create' in self.bt.lower():
            self.bt_create = 1

        self.p = p
        if self.p.lower().strip() == 'adaptive':
            self.p_adaptive = 1
            self.p_adaptable = 0
            self.p_none = 0
        elif self.p.lower().strip() == 'adaptable':
            self.p_adaptive = 0
            self.p_adaptable = 1
            self.p_none = 0
        elif self.p.lower().strip() == 'none':
            self.p_adaptive = 0
            self.p_adaptable = 0
            self.p_none = 1
        else:
            self.p_adaptive = 0
            self.p_adaptable = 0
            self.p_none = 0

    #  Statistics
        self.ls_mean = 0
        self.ls_std = 0
        self.ls_ccv = 0

        self.ct_mean = 0
        self.ct_std = 0
        self.ct_ccv = 0

        self.d_mean = 0
        self.d_std = 0
        self.d_ccv = 0

        self.bt_mean = 0
        self.bt_std = 0
        self.bt_ccv = 0

        self.p_mean = 0
        self.p_std = 0
        self.p_ccv = 0

    def C_CV(self):
        # print('ER CCV: '+self.tier)

        # Learning style
        self.ls_mean = round(statistics.mean([self.ls_p_s,self.ls_p_i,self.ls_i_v,self.ls_i_a,self.ls_o_i,self.ls_o_d, self.ls_pr_a,
                                       self.ls_pr_r,self.ls_u_s,self.ls_u_g]),2)

        self.ls_std = round(statistics.stdev([self.ls_p_s,self.ls_p_i,self.ls_i_v,self.ls_i_a,self.ls_o_i,self.ls_o_d, self.ls_pr_a,
                                       self.ls_pr_r,self.ls_u_s,self.ls_u_g]),2)

        self.ls_ccv = round(deepcopy(self.ls_std/self.ls_mean),2)

        # Content type

        self.ct_mean = round(statistics.mean(
                [self.ct_text, self.ct_video,self.ct_image,self.ct_website,self.ct_audio ]), 2)

        self.ct_std = round(statistics.stdev(
            [self.ct_text, self.ct_video,self.ct_image,self.ct_website,self.ct_audio ]), 2)

        self.ct_ccv = round(deepcopy(self.ct_std / self.ct_mean), 2)

        # Depth

        self.d_mean = round(statistics.mean(
                [self.d_shallow,self.d_general,self.d_deep ]), 2)

        self.d_std = round(statistics.stdev(
            [self.d_shallow,self.d_general,self.d_deep ]), 2)

        self.d_ccv = round(deepcopy(self.d_std / self.d_mean), 2)

        # Bloom's Taxonomy

        self.bt_mean = round(statistics.mean(
                [self.bt_remember, self.bt_understand, self.bt_apply,self.bt_analyze,
                 self.bt_evaluate, self.bt_create ]), 2)

        self.bt_std = round(statistics.stdev(
            [self.bt_remember, self.bt_understand, self.bt_apply,self.bt_analyze,
                 self.bt_evaluate, self.bt_create ]), 2)

        try:
            self.bt_ccv = round(deepcopy(self.bt_std / self.bt_mean), 2)
        except:
            self.bt_ccv = 'N/A'

        # Personalization

        self.p_mean = round(statistics.mean([self.p_adaptive, self.p_adaptable,self.p_none ]), 2)

        self.p_std = round(statistics.stdev([self.p_adaptive, self.p_adaptable,self.p_none ]), 2)

        try:
            self.p_ccv = round(deepcopy(self.p_std / self.p_mean), 2)
        except:
            self.p_ccv = 'N/A'