__author__ = 'nrao'
import definition
codec = definition.Codec()

def build_tree(pre_order, p_st, p_en, in_order, i_st, i_en):
    lookup = dict()
    for i in range(len(in_order)):
        lookup[in_order[i]] = i

    def builder(pre_st, pre_en, in_st, in_en):
        if pre_en <= pre_st or in_en <= in_st:
            return None
        root_nd = pre_order[pre_st]
        root_ino_idx = lookup[root_nd]
        left_size = root_ino_idx - in_st
        l_p_st = pre_st + 1
        l_p_en = pre_st + 1 + left_size
        l_i_st = in_st
        l_i_en = root_ino_idx

        r_p_st = pre_st + 1 + left_size
        r_p_en = pre_en
        r_i_st = root_ino_idx + 1
        r_i_en = in_en

        return definition.TreeNode.init(pre_order[pre_st],
                                        builder(l_p_st, l_p_en, l_i_st, l_i_en),
                                        builder(r_p_st, r_p_en, r_i_st, r_i_en))

    return builder(p_st, p_en, i_st, i_en)

i_order = "FBAEHCDIG"
p_order = "HBFEACDGI"

root = build_tree(p_order, 0, len(p_order), i_order, 0, len(i_order))
serialized = codec.serialize(root)
print serialized