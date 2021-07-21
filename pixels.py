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


# Assume RGBA tuples
def alpha_blend(upper, lower):
    height = len(lower)
    combined = []
    for row in range(height):
        width = len(lower[row])
        combined_row = []
        for col in range(width):
            r, g, b, alpha = upper[row][col]
            lr, lg, lb, lalpha = lower[row][col]
            ialpha = 1.0 - alpha
            combined_row.append((
                alpha * r + ialpha * lalpha * lr,
                alpha * g + ialpha * lalpha * lg,
                alpha * b + ialpha * lalpha * lb,
                1.0))
        combined.append(combined_row)
    return combined

class RGBA:
    def __init__(self, red, green, blue, alpha=1.0) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __repr__(self) -> str:
        return f"RGBA({self.red}, {self.green}, {self.blue}, {self.alpha})"
