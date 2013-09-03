#!/usr/bin/python
#encoding=utf-8
import time

# 插入
def insertion_sort(sort_list):
    iter_len = sort_list.__len__()
    if iter_len < 2:
        return sort_list
    for i in range(1,iter_len):
        key = sort_list[i]
        j = i - 1
        while j>=0 and key < sort_list[j]:
            sort_list[j+1] = sort_list[j]
            j -= 1
        sort_list[j+1] = key
    return sort_list
#冒泡
def bubble_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return sort_list
    for i in range(iter_len - 1):
        for j in range(iter_len -1):
            if sort_list[j]>sort_list[j+1]:
                sort_list[j],sort_list[i] = sort_list[i],sort_list[j]
    return sort_list
#选择
def selection_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return sort_list
    for i in range(1,len(sort_list)-1):
        smallest = sort_list[i]
        location = i
        for j in range(i,iter_len):
            if sort_list[j] < smallest:
                smallest = sort_list[i]
                location = j
        if i!=location:
            sort_list[i],sort_list[location]=sort_list[location],sort_list[i]
    return sort_list

if __name__ == '__main__':
    l = [12132,24334,1237,56,2111,4,57,234,24,55,8433,94]
    print insertion_sort(l)
    print bubble_sort(l)
    print selection_sort(l)
