import re


def getfunctionlist(file) :
    file_object = open(file)
    pattern1 = r"(\w+)\s+[\*,&]*\s*(\w+)\s*\("
    pattern2 = r"(enum \w+)\s+[\*,&]*\s*(\w+)\s*\("     #匹配返回值是enum类型的函数
    pattern3 = r"(struct \w+)\s+[\*,&]*\s*(\w+)\s*\("   #匹配返回值是struct类型的函数

    functionname = []
    for line in file_object:
        if re.match(pattern1, line):
            functionname.append(line)
        elif re.match(pattern2, line):
            functionname.append(line)
        elif re.match(pattern3, line):
            functionname.append(line)

    file_object.close()
    return functionname
