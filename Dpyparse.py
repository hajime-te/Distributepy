"""parse text file for input test data"""
import re


class Regex:

    target_ptn = re.compile(r'^(\*+[\s]*)(test|input|option)[\s]*$')

    def search_ptn(self, target_str):
        return self.target_ptn.search(target_str)

class File:
    
    def open_file_ro(self, target_file):
        return open(target_file, 'r')

def exec(arg_list):
    for args in arg_list:
        print("echo '"+' '.join(args["input"])+"' | python3 "+' '.join(args["option"]))

def main():

    td = {'test': [], 'input': [], 'option': []}
    tdl = []
    regex = Regex()
    file_c = File()
    target_file = file_c.open_file_ro('test.org')
    for l in target_file.readlines():
        m = regex.search_ptn(l)
        if m:
            operate = m.group(2)
            if m.group(2) == 'test':
                tdl.append(td)
                td = {'test': [], 'input': [], 'option': []}
        else:
            td[operate].append(l)
    tdl.append(td)
    exec(tdl[1:])




if __name__ == '__main__':
    main()

