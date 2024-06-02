# -*- coding: utf-8 -*-
def all_variants(string_):
    i = 0
    k = 0
    j = 0
    for i in range(len(string_)):
        yield string_[i]
    for j in range(len(string_)):
        if string_[j] != string_[i]:
            mc = string_[j] + string_[i]
            yield mc
    for k in range(len(string_)):
        if string_[k] not in mc:
            yield string_[k] + mc

a = all_variants("abc")
for i in a:
    print(i)
