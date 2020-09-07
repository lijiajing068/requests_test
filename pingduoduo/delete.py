import Result_check
ori_file = Result_check('Input: ')
new_file = open('Result_new.py', 'w')
for line in open(ori_file):
    if line:
        line = line[1:]
    new_file.write(line)
new_file.close()
Result_check('Done. Press any key to continue...')