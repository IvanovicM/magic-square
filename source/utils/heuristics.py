import math

def h1(magic_square):
    return magic_square.violation_number()

def h2(magic_square):
    total_sum = 0
    for i in range(magic_square['n']):
        total_sum += abs(
            magic_square['sum_map']['r{}'.format(i)] - magic_square['sum']
        )
        total_sum += abs(
            magic_square['sum_map']['c{}'.format(i)] - magic_square['sum']
        )

    total_sum += abs(
        magic_square['sum_map']['d0'] - magic_square['sum']
    )
    total_sum += abs(
        magic_square['sum_map']['d1'] - magic_square['sum']
    )

    return total_sum