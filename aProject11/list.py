#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_bottom_up(a):
    """
    Поиск длины наибольшей возрастающей подпоследовательности.
    """
    n = len(a)
    D = []

    for i in range(n):
        D.append(1)
        for j in range(i):
            if a[j] < a[i] and D[j] + 1 > D[i]:
                D[i] = D[j]+1

    ans = max(D)

    return ans


def using_prev(prev, m_index):
    """
    Восстановление НВП с помощью списка prev
    """
    l = []
    while True:
        l.append(m_index)
        if prev[m_index] == -1:
            break
        m_index = prev[m_index]

    l.reverse()
    return l


def without_prev(d, ans, m_index):
    """
    Восстановление НВП без помощи списка prev
    """
    l = []
    while True:
        l.append(m_index)
        if ans == 1:
            break
        ans -= 1
        while True:
            m_index -= 1
            if d[m_index] == ans and a[m_index] < a[l[-1]]:
                break
    l.reverse()
    
    return l


def list_bottom_up_2(a):
    """
    Поиск длины и самой НВП.
    """
    n = len(a)
    d, prev = [], []
    for i in range(n):
        d.append(1)
        prev.append(-1)
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j]+1
                prev[i] = j

    ans, max_index = 0, 0
    for i, item in enumerate(d):
        if ans < item:
            ans, max_index = item, i

    list_using_prev = using_prev(prev, max_index)
    list_without_prev = without_prev(d, ans, max_index)

    return ans, (list_using_prev, list_without_prev)


if __name__ == '__main__':
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    print(list_bottom_up(a))
    print(list_bottom_up_2(a))