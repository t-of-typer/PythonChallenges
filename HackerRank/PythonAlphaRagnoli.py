alpha = string.ascii_lowercase
    width = 4 * n - 3
    lines = []
    for i in range(n):
        # left part: descending letters from the nth letter downwards
        left_part = [alpha[n - 1 - j] for j in range(i + 1)]
        # right part: mirror of left_part without repeating the center
        right_part = left_part[:-1][::-1]
        # combine, join with dashes, then center with dashes as padding
        line = "-".join(left_part + right_part)
        lines.append(line.center(width, "-"))
    # top half + mirror of top without the last (middle) line
    return "\n".join(lines + lines[-2::-1])
