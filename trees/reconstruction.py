__author__ = 'nrao'
from algorithm.datastructures import definition

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


def reconstruct_tree(in_order, pre_order):
    idx = [0]

    def _helper(st_idx, en_idx):
        # print in_order[st_idx:en_idx], st_idx, en_idx, idx[0]
        if st_idx >= en_idx: #or idx[0] >= len(pre_order):
            print "None", st_idx, en_idx
            return None
        split = inorder_lookup[pre_order[idx[0]]]
        idx[0] += 1
        print in_order[split], "|", in_order[st_idx:split], "|", in_order[split+1:en_idx], "|", st_idx, "|", en_idx
        return definition.TreeNode.init(in_order[split], _helper(st_idx, split), _helper(split+1, en_idx))

    return _helper(0, len(in_order))

i_order = "FBAEHCDIG"
p_order = "HBFEACDGI"

inorder_lookup = dict()
for i in range(len(i_order)):
    inorder_lookup[i_order[i]] = i

root = build_tree(p_order, 0, len(p_order), i_order, 0, len(i_order))
serialized = codec.serialize(root)
print serialized

print i_order
new_root = reconstruct_tree(i_order, p_order)
serialized = codec.serialize(new_root)
print serialized