from math import sqrt


def binnen_of_buiten(middelpunt,punt_op_cirkel, willekeurig_punt):
    m_x, m_y = middelpunt
    p_x, p_y = punt_op_cirkel
    q_x, q_y = willekeurig_punt
    r = sqrt(pow(m_x - p_x, 2) + pow(m_y - p_y, 2))
    s = sqrt(pow(m_x - q_x, 2) + pow(m_y - q_y, 2))
    if r == s:
        return('op', round(s, 4))
    elif r < s:
        return('buiten', round(s, 4))
    else :
        return('binnen', round(s, 4))


print(binnen_of_buiten((0, 0),(1, 1),(-1, -1)))











