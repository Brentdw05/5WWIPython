

def yiq(rgb):
    r, g, b = rgb
    y = 0.299 * r + 0.587 * g + 0.114 * b
    i = 0.596 * r + (-0.274) * g + (-0.322) * b
    q = 0.211 * r + (-0.523) * g + 0.312 * b
    y = round(y, 4)
    i = round(i, 4)
    q = round(q, 4)
    opl = (y, i, q)
    return opl


print(yiq((255, 0, 0)))
