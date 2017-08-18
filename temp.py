class Parse:
    """text string_parser class"""

    __TestFactorPair = {'{': '}', '(': ')'}


    def count_length(self, d):
        """count string index by finished parse"""
        l = len(d[1]) - len(d[2])
        if d[0] != "":
            l += len(d[0] + self.__TestFactorPair[d[0]])
        return  l+sum(map(self.count_length, d[2]))

    def parse_markup(self, head, st):
        """parse '{' factor """

        d = [head, "", []]
        idx = 0
        while idx < len(st):
            if head != "" and st[idx] == self.__TestFactorPair[head]:
                break
            if st[idx] in self.__TestFactorPair:
                c = self.parse_markup(st[idx], st[idx + 1:])
                d[2].append(c)
                d[1] += ""
                idx += self.count_length(c)
            else:
                d[1] += st[idx]
                idx += 1
        return tuple(d)

class TargetFile:

    """open input file read only"""
    def __init__(self, filename):
        self.fname = filename
        self.f = open(self.fname, 'r')

    def get_file_obj(self):
        return self.f

    def close_file_obj(self):
        self.f.close()


import re


class Regex:

    target_ptn = re.compile(r'^(\*+[\s]*)(test|input|option)[\s]*$')

    def search_ptn(self, target_str):
        return self.target_ptn.search(target_str)


def main():

    td = {'test': [],'input': [],'option': []}
    tdl = []
    regex = Regex()
    targetfile = open('test.org', 'r')
    for l in targetfile.readlines():
        m = regex.search_ptn(l)
        if m:
            operate = m.group(2)
            if m.group(2)=='test':
                tdl.append(td)
                td = {'test': [], 'input': [], 'option': []}
        else:
            td[operate].append(l)
    print(tdl)




if __name__ == '__main__':
    main()

