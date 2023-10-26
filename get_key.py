import re
def get_key(file):
    key = ""
    multidetermiter = ["_",".","-"," "]
    for i in reversed(file):
        if i in multidetermiter:
            key = i
            break
    if key:
        part = file.split(key)
        after = key.join(part[:-1])
        if len(after) > 5 :
            return after
    return file

def get_key_v1(file):
    my_dict = {}
    key = ""
    x = re.findall(r" \(\d_\d\)"+"_", file)
    y = re.findall(r" \(\d{2}_\d{2}\)", file)
    z1 = re.findall(r" \(\d{2}_\d\)", file)
    z2 = re.findall(r" \(\d_\d{2}\)", file)
    z3 = re.findall(r" \(\d_\d\)", file)
    x1 = re.findall("-\d_\d", file)
    if x:
        part = file.split(x[-1])
        file = x[-1].join(part[:-1])
    elif y:
        file = file.replace(str(y[-1]), "1")
    elif z1:
        file = file.replace(str(z1[-1]), "1")
    elif z2:
        file = file.replace(str(z2[-1]), "1")
    elif z3:
        file = file.replace(str(z3[-1]), "1")
    elif x1:
        file = file.replace(str(x1[-1]), "1")

    for i in reversed(file):
        if i == '-':
            key = i
            break
        elif i == '.':
            key = i
            break
        elif i == ' ':
            key = i
            break
        elif i == '/':
            key = i
            break
        elif i == '#':
            key = i
            break
        elif i == '_':
            key = i
            break
    if key:
        x = file.split(key)
        after = key.join(x[:-1])
        if len(after) > 4 :         #or after.isdigit()    or  len(after) != 8 and len(after) != 7 and
            return after
    return file