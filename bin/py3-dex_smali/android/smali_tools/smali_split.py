"""
smali_split.py: A large number of smali files auto split and compile helper.
Run this file directly to see what param takes to do.
"""

import os
import shutil
import configparser
import sys, getopt

cur_path = os.path.split(os.path.realpath(__file__))[0]
config = configparser.ConfigParser()
config.read(os.path.join(cur_path, 'config.ini'), encoding='utf-8')
smali_tool_path = config.get('path', 'smali_tool')
if (not smali_tool_path or not os.path.exists(smali_tool_path)):
    print('config [path] smali_tool not exist, please check.')
    sys.exit()

java_path = config.get('path', 'java_home')
if (not java_path):
    if (os.getenv('JAVA_HOME')):
        java_path = os.getenv('JAVA_HOME')
if (not java_path):
    print('Cannot find java path, config.ini set [path] java_home, or set Env JAVA_HOME, it\'s the same.')
    sys.exit()
os.putenv('PATH', java_path + ";" + os.getenv('PATH'))

# The method num counter works roughly, which makes different from actual. 
# This num is better to be lower if there is something error in after compiling.
# smali统计的方法数与DEX实际限制的65535出入较大，如果还报错继续将改值调低即可
methods_limit = 40000
cur_dex_num = 1
cur_method_count = 0
smali_split_map = {}

# Uniform file seperator to current os standard.
def convert_path(path: str) -> str:
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)

# Count method num in smali file
def parse_smali_method_num(smali_path):
    count = 0
    with open(smali_path, 'r', 4096, 'utf-8') as f:
        text = f.readline()
        if (not text.startswith('.class')):
            print('Warning:Not a class smali file:' + str(smali_path))
            return 0
        while(text):
            text = f.readline()
            if (text.startswith('.method')):
                count += 1
    return count

# Recursive folder analysis
def parse_dir(entry_path):
    global cur_method_count, methods_limit, cur_dex_num, smali_split_map
    for file in os.listdir(entry_path):
        file_path = os.path.join(entry_path, file)
        if (os.path.isdir(file_path)):
            parse_dir(file_path)
        else:
            method_num = parse_smali_method_num(file_path)
            cur_method_count += method_num
            if (cur_method_count > methods_limit):
                print("Marking split dex:" + str(cur_dex_num))
                cur_method_count -= methods_limit
                cur_dex_num += 1
            if (not cur_dex_num in smali_split_map.keys()):
                smali_split_map[cur_dex_num] = []
            smali_split_map[cur_dex_num].append(file_path)

def split_smali_files(root_path, output_path):
    global smali_split_map
    for i in smali_split_map.keys():
        cur_workdir = ''
        if (i == 1):
            cur_workdir = os.path.join(output_path, 'classes') # Make it looking similar to normal dex structure.
        else:
            cur_workdir = os.path.join(output_path, 'classes' + str(i))
        
        print('Copying split %d file to dir %s' % (i, cur_workdir))
        smali_list = smali_split_map[i]
        for smali in smali_list:
            # Replace absolute path of smali file to relative path.
            dest_smali = cur_workdir + smali.replace(root_path, '')
            if (not os.path.exists(os.path.split(dest_smali)[0])):
                os.makedirs(os.path.split(dest_smali)[0])
            shutil.copy(smali, dest_smali)

# Compile smali file to dex.
def compile_smali(output_path):
    for i in smali_split_map.keys():
        smali_dir = ''
        dex_output_path = ''

        # Make it looking similar to normal dex structure.
        if (i == 1):
            smali_dir = os.path.join(output_path, 'classes')
            dex_output_path = os.path.join(output_path, 'classes.dex')
        else:
            smali_dir = os.path.join(output_path, 'classes' + str(i))
            dex_output_path = os.path.join(output_path, 'classes' + str(i) + '.dex')
        
        if (not os.path.exists(os.path.split(output_path)[0])):
            os.makedirs(os.path.split(output_path)[0])
        
        print('Smaling %s to %s' % (smali_dir, dex_output_path))
        ret = os.system('java -jar %s a %s -o %s' % (smali_tool_path, smali_dir, dex_output_path))
        if (ret != 0):
            raise Exception("Error ret:" + str(ret))

def print_help():
    text = "Auto split a large number of smali files into dex files.\n"  \
            "-h Show this help\n" \
            "-a Directory to all smali files.\n" \
            "-o Output path\n" \
            "eg. smali_split.py -a /test -o /test2\n"
    print(text)

def main(argv):
    smali_path = ''
    output_path = ''

    try:
        opts, args = getopt.getopt(argv,"ha:o:")
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    if (not opts):
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt == '-a':
            smali_path = arg
        elif opt == '-o':
            output_path = arg
        
    if (not smali_path or not output_path):
        print_help()
        sys.exit()

    output_path = convert_path(output_path)
    smali_path = convert_path(smali_path)
    output_path = os.path.join(output_path, 'output')
    
    print('Start parsing entry path:' + str(smali_path))
    parse_dir(smali_path)
    print('Total split:' + str(cur_dex_num))
    split_smali_files(smali_path, output_path)
    compile_smali(output_path)

if __name__ == "__main__":
   main(sys.argv[1:])
