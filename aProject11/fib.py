#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib(n, calculation_method=0):
    """
    Функции вычисления числа фибоначчи.
    """
    def fib_td(n):
        """
        Динамическое программирование назад.
        """
        if n <= 1:
            f[n] = n
        else:
            f[n] = fib_td(n - 1) + fib_td(n-2)
        return f[n]

    def fib_bu(n):
        """
        Динамическое программирование вперед.
        """
        f = [-1] * (n+1)
        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]

    def fib_bu_imroved(n, calculation_method):
        """
        Уменьшенным памяти.
        """
        if n <= 1:
            return n
        
        prev, curr = 0, 1

        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        return curr

    if calculation_method == 0:
        f = [-1]*(n+1)
        return fib_td(n)
    if calculation_method == 1:
        return fib_bu(n)
    
    if calculation_method == 2:
        return fib_bu_imroved(n,2)
    
    else:
        print(
            f"Неизвестраня функция {calculation_method}"
        )


if __name__ == '__main__':
    N = 10
    print(f"Число Фибоначчи({N}):")
    print(f"{fib(N, 0) = }")
    print(f"{fib(N, 1) = }")
    print(f"{fib(N, 2) = }")