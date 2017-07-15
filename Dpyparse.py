"""parse text file for input test data"""
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

