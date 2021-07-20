def forgetRed(pixels):
    for line in pixels:
        for i in range(len(line)):
            vorher = line[i]
            line[i] = (0, vorher[1], vorher[2])
    return pixels



# WR
# GB
#
# 255,255,255 255,000,000
# 000,255,000 000,000,255
#
# rgbrgbrgbrgb # interleaved
# rrrrggggbbbb # kanalweise