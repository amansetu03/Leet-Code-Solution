def toggle(wr_seg, rig_seg):
    tgc = 0
    for i in range(9):
        if wr_seg[i] != rig_seg[i]:
            tgc += 1
            if tgc > 1:
                return False
    return tgc == 1


def find_match_digit(map, segment_row):
    cur_match = []
    for i in range(10):
        if segment_row == map[i]:
            cur_match.append(i)
        elif toggle(segment_row, map[i]):
            cur_match.append(i)
    return cur_match


def number_genration(digit_array, index, curr_number, digit, ts):
    if index == digit:
        ts[0] += curr_number
        return
    for k in digit_array[index]:
        number_genration(digit_array, index + 1, curr_number * 10 + k, digit, ts)


def calculate_final_sum(digit_array):
    ts = [0]
    digit = len(digit_array)
    number_genration(digit_array, 0, 0, digit, ts)

    return ts[0]


def main():
    map = [''] * 10


    for _ in range(3):
        l = input().strip()
        for i in range(10):
            map[i] += l[i * 3:(i + 1) * 3]
    input_sagment_map = [""] * 50
    num = 0
    for _ in range(3):
        l = input().strip()
        for i in range(len(l) // 3):
            input_sagment_map[i] += l[i * 3: (i + 1) * 3]
        num = len(l) // 3

    digit_array = []
    for i in range(num):
        match = find_match_digit(map, input_sagment_map[i])
        if not match:
            return "Invalid"
        digit_array.append(match)

    final_sum = calculate_final_sum(digit_array)
    return final_sum

if __name__ == "__main__":
    print(main(),end="")

