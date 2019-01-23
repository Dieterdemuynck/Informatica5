def yiq(rgb):
    y = round(rgb[0] * 0.299 + rgb[1] * 0.587 + rgb[2] * 0.114, 4)
    i = round(rgb[0] * 0.596 + rgb[1] * -0.274 + rgb[2] * -0.322, 4)
    q = round(rgb[0] * 0.211 + rgb[1] * -0.523 + rgb[2] * 0.312, 4)

    return y, i, q