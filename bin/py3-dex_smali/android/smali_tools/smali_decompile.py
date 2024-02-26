"""
smali_decompile.py: Dex decompile helper.
Run this file directly to see what param takes to do.
"""

import os
import configparser
import sys, getopt

cur_path = os.path.split(os.path.realpath(__file__))[0]
config = configparser.ConfigParser()
config.read(os.path.join(cur_path, 'config.ini'), encoding='utf-8')
baksmali_tool_path = config.get('path', 'baksmali_tool')
if (not baksmali_tool_path or not os.path.exists(baksmali_tool_path)):
    print('Config [path] baksmali_tool not exist, please check.')
    sys.exit()

java_path = config.get('path', 'java_home')
if (not java_path):
    if (os.getenv('JAVA_HOME')):
        java_path = os.getenv('JAVA_HOME')
if (not java_path):
    print('Cannot find java path, config.ini set [path] java_home, or set Env JAVA_HOME, it\'s the same.')
    sys.exit()
os.putenv('PATH', java_path + ";" + os.getenv('PATH'))

# Take dex file and make sure list reverse
def list_dexfile(app_unzip_path):
    files = [x for x in os.listdir(app_unzip_path) if (x.endswith('.dex'))]
    files.sort(reverse=True)
    return files

# smali dex into each dex name folder
def smali_dex(dex_files, app_unzip_path, smali_output_path):
    for dex_name in dex_files:
        dex_path = os.path.join(app_unzip_path, dex_name)
        smali_name = os.path.splitext(dex_name)[0]
        smali_path = os.path.join(smali_output_path, smali_name)
        print('Decomplile %s ...' % dex_name)
        os.system('java -jar "%s" d "%s" -o "%s"' % (baksmali_tool_path, dex_path, smali_path))
        
# smali all dex into 'classes' folder
def smali_dex_all_in_one(dex_files, app_unzip_path, smali_output_path):
    for dex_name in dex_files:
        dex_path = os.path.join(app_unzip_path, dex_name)
        smali_name = 'classes'
        smali_path = os.path.join(smali_output_path, smali_name)
        print('Decomplile %s into %s ...' % (dex_name, smali_name))
        os.system('java -jar "%s" d "%s" -o "%s"' % (baksmali_tool_path, dex_path, smali_path))

def print_help():
    text = "Smali dex to smali_file.\n"  \
            "-h Show this help\n" \
            "-d Directory to unziped apk\n" \
            "-o Output path\n" \
            "-m [one|each] Decompile dex to single folder or each folder\n" \
            "eg. smali_decompile.py -d ~/test -o ~/test2 -m each\n"
    print(text)

def main(argv):
    app_unzip_path = ''
    smali_output_path = ''
    mode = ''

    try:
        opts, args = getopt.getopt(argv,"hd:o:m:")
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
        elif opt == '-d':
            app_unzip_path = arg
        elif opt == '-o':
            smali_output_path = arg
        elif opt == '-m' and arg in ('one', 'each'):
            mode = arg
        
    if (not app_unzip_path or not smali_output_path or not mode):
        print_help()
        sys.exit()
    
    dex_files = list_dexfile(app_unzip_path)
    print('dex file list:' + str(dex_files))
    if (not dex_files):
        print('dex file list empty!')
        sys.exit()
    
    if (mode == 'each'):
        smali_dex(dex_files, app_unzip_path, smali_output_path)
    elif (mode == 'one'):
        smali_dex_all_in_one(dex_files, app_unzip_path, smali_output_path)

if __name__ == "__main__":
   main(sys.argv[1:])
