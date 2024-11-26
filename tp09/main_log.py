
from glob import glob
import re

def main():
    all_logs = glob("*.log")
    print(all_logs)

    for the_log in all_logs:
        with open(the_log) as f:

            for line in f:
                line = line.strip()
                # r = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
                r = re.findall("^(.+?)\s",line)
                print(r)
                # print(line)


if __name__=='__main__':
    main()
