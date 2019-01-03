import random
import jieba


def store(l):
    with open("dicts_out.txt", "w") as f:
        for i in l.keys():
            f.write(i)
            f.write(":  \n________________")
            for j in l[i]:
                f.write(j[0])
                f.write("_")
                f.write(str(int(1000000* j[1])))
                f.write("___")
            f.write("\n")


def getjieba():
    with open("input.txt") as f:
        s = f.read()
    list_s = jieba.cut(s)
    with open("jieba_out.txt", 'w') as f:
        for i in list_s:
            f.write(i)
            f.write("\n")


def run_a_result():
    chars = {}
    s = []
    # with open("input.txt") as f:
    # s = f.read()
    with open("jieba_out.txt") as f:
        while 1:
            i = f.readline()
            if i == "\n":
                pass
            else:
                s.append(i[:-1])
            if not i:
                break

    s_new = list(zip(s, s[1:]))
    for i, j in s_new:
        if i in chars.keys():
            if j in chars[i].keys():
                chars[i][j] += 1
            else:
                chars[i][j] = 1
        else:
            chars[i] = {}
            if j in chars[i].keys():
                chars[i][j] += 1
            else:
                chars[i][j] = 1

    # for i in ("。","！","”","　","“"):
    # chars.pop(".")

    for i in ("。", "！", "”", "　", "7", "8"):
        if i in chars.keys():
            chars.pop(i)

    for i in chars.keys():
        count = 0
        for j in chars[i].keys():
            count += chars[i][j]
        for j in chars[i].keys():
            chars[i][j] = chars[i][j] / count
            if j  == "的":
                chars[i][j] /= 4
        temp = sorted(list(chars[i].items()), key=lambda x: -x[1])
        chars[i] = temp

    temp = []
    for i in chars.keys():
        if not chars[i]:
            temp.append(i)
    for i in temp:
        chars.pop(i)
    #store(chars)

    next_char = begin_char = random.choice(list(chars.keys()))
    s_out = begin_char
    while 1:
        if not (next_char in chars.keys()):
            break

        else:
            if next_char == "，":
                x = random.randint(0, len(chars["，"]) - 1)
                next_char = chars[next_char][x][0]
            else:
                q = random.random()
                if(q > 0.2):
                    x = random.randint(0, len(chars[i]) - 1)
                else:
                    x = random.randint(0, min(len(chars[i]) - 1, 30))
                next_char = chars[next_char][x][0]

        s_out += "\n" if (next_char in ("，", "…","？")) else next_char

        if s[-1] != "," and (
                len(s_out) > 5 and s_out[-1] == s_out[-2] == s_out[-3]
                or (len(s_out) > 6 and s_out[-1] == s_out[-3] == s_out[-5])
                or (len(s_out) > 8 and s_out[-1] == s_out[-4] == s_out[-7])
                or (len(s_out) > 10 and s_out[-1] == s_out[-5] == s_out[-9])
                or (len(s_out) > 12 and s_out[-1] == s_out[-6] == s_out[-11])
                or (len(s_out) > 14 and s_out[-1] == s_out[-7] == s_out[-13])
                or (len(s_out) > 16 and s_out[-1] == s_out[-8] == s_out[-15])
        ):
            s_out += "\n"
            next_char = random.choice(list(chars.keys()))
            s_out += next_char
        #print(s_out)

    #print(s_out)
    return s_out
    # print(chars)

def get_poem():
    s = run_a_result()
    while len(s) < 50:
        s += "\n"
        s += run_a_result()
    return s

def main():
    #getjieba()
    s = get_poem()
    print(s)

if __name__ == '__main__':
   main()