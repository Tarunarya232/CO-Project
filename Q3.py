import sys
from math import floor

v = sys.stdin.read().split("\n")
v.pop(-1)
# print(v)
l = []
for i in v:
    m = i.split(' ')
    l.append(m)
lfile=l
# print(lfile)

u = 0
# a=open("file.txt",'r')
u = 0
# a=open("file.txt",'r')
# lfile = [['var', 'x'], ['mov', 'R1', '$4'], ['mov', 'R2', '$4'], ['cmp', 'R1', 'R2'], ['mov', 'FLAGS', 'R3'], ['mov', 'R4', '$1'], ['cmp', 'R3', 'R4'], ['jgt', 'label'], ['label:', 'hlt']]
# # print(lfile)
lout = []


while ([''] in lfile):
    lfile.remove([''])

lf = []
reg_addr = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}
dicInstruction = {"add": "10000", "sub": "10001", "mul": "10110", "xor": "11010", "or": "11011", "and": "11100",
                  "div": "10111", "not": "11101", "cmp": "11110", "hlt": "01010"}

Global_Error = []

def funcA(lst, j):
    l = []
    if (lst[0] == "add"):
        l.append("10000")
        l.append("00")
        for i in reg_addr:
            if (i == lst[1]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[2]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[3]):
                l.append(reg_addr.get(i))
                break
        s = ("").join(l)
        lout.append(s)
        # print(s)
    elif(lst[0]=="addf"):
      # l.append("10000")
      l.append("00000")
      l.append("00")
      for i in reg_addr:
         if (i == lst[1]):
            l.append(reg_addr.get(i))
            break
      for i in reg_addr:
         if (i == lst[2]):
            l.append(reg_addr.get(i))
            break
      for i in reg_addr:
         if (i == lst[3]):
            l.append(reg_addr.get(i))
            break
      s = ("").join(l)
      lout.append(s)
      # print(s)
    elif (lst[0] == "mul"):
        l.append("10110")
        l.append("00")
        for i in reg_addr:
            if (i == lst[1]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[2]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[3]):
                l.append(reg_addr.get(i))
                break
        s = ("").join(l)
        lout.append(s)
        # print(s)
    elif (lst[0] == "sub"):
        l.append("10001")
        l.append("00")
        for i in reg_addr:
            if (i == lst[1]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[2]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[3]):
                l.append(reg_addr.get(i))
                break
        s = ("").join(l)
        lout.append(s)
        # print(s)
    elif (lst[0] == "subf"):
      l.append("00001")
      l.append("00")
      for i in reg_addr:
         if (i == lst[1]):
               l.append(reg_addr.get(i))
               break
      for i in reg_addr:
         if (i == lst[2]):
               l.append(reg_addr.get(i))
               break
      for i in reg_addr:
         if (i == lst[3]):
               l.append(reg_addr.get(i))
               break
      s = ("").join(l)
      lout.append(s)
      # print(s)
    elif (lst[0] == "xor"):
        l.append("11010")
        l.append("00")
        for i in reg_addr:
            if (i == lst[1]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[2]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[3]):
                l.append(reg_addr.get(i))
                break
        s = ("").join(l)
        lout.append(s)
        # print(s)
    elif (lst[0] == "or"):
        l.append("11011")
        l.append("00")
        for i in reg_addr:
            if (i == lst[1]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[2]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[3]):
                l.append(reg_addr.get(i))
                break
        s = ("").join(l)
        lout.append(s)
        # print(s)
    elif (lst[0] == "and"):
        l.append("11100")
        l.append("00")
        for i in reg_addr:
            if (i == lst[1]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[2]):
                l.append(reg_addr.get(i))
                break
        for i in reg_addr:
            if (i == lst[3]):
                l.append(reg_addr.get(i))
                break
        s = ("").join(l)
        # print(s)
        lout.append(s)


from itertools import chain

reg_codd = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "Flags": "111"}


def isRegister(a):  # This Function checks whether any instruction is register or not
    if (a in reg_codd):
        return True
    else:
        return False


def isFlags(a):  # This Function checks whether any instruction is flag or not
    if (a == "FLAGS"):
        return True
    else:
        return False


def variable(lst):  # This Function returns the dictionary of variables which stores the variable defined in it
    var_dict = {"var": []}
    for i in range(len(lst)):
        if (lst[i][0] == "var"):
            var_dict["var"].append(lst[i][1])
        else:
            pass


def hltpresentornot(lst):  # This function will return whether "HALT" is present in assembly code or not
    elem = 'hlt'
    res1 = elem in chain(*lst)
    if (res1):
        return True
    else:
        return False


def findLabel(main_lst):  # This function will return a dictionary which will return labels with their specified address
    dic = dict()
    for i in range(len(main_lst)):
        if (main_lst[i][0][-1] == ':'):
            len_str = len(main_lst[i][0])
            str_temp = main_lst[i][0][:len_str - 1]
            dic[str_temp] = 0
        else:
            pass
    count_sen = 0
    for i in range(len(main_lst)):
        if (main_lst[i][0] == "var"):
            pass
        elif (main_lst[i][0][-1] == ':'):
            len_str1 = len(main_lst[i][0])
            str_temp1 = main_lst[i][0][:len_str - 1]
            dic[str_temp] = count_sen
            count_sen = count_sen + 1
        else:
            count_sen = count_sen + 1
    return dic


def error(lst, op):  # Function to check Errors and returns a dictionary
    try:

        lstA = ["add", "mul", "sub", "xor", "or", "and","addf","subf"]
        lstB = ["mov", "rs", "ls","movf"]
        lstC = ["not", "cmp", "mov", "div"]
        lstD = ["ld", "st"]
        lstE = ["jmp", "jlt", "jgt", "je"]
        lstF = ["hlt"]
        lstres = lstA + lstB + lstC + lstD + lstE + lstF
        lstG = []
        err = {"Flags": [], "reg": [], "imm": [], "hlt": [], "hltmiss": [], "error": [], "label": [], "general": [],
               "len": [], "var": []}
        for i in range(len(lst)):
            if (lst[i][0] in lstA):
                if (len(lst[i]) == 4):
                    if (isRegister(lst[i][1]) == True and isRegister(lst[i][2]) == True and isRegister(lst[i][3]) == True):
                        pass
                    else:
                        if (isFlags(lst[i][1])==True or isFlags(lst[i][2])==True or isFlags(lst[i][3])==True):
                            print("Incorrect Use of Flags at line ", i + 1)
                            Global_Error.append(1)
                            return
                        elif (isRegister(lst[i][1]) == False or isRegister(lst[i][2]) == False or isRegister(lst[i][3]) == False):
                            print("Incorrect Use of Registers at line ", i + 1)
                            Global_Error.append(1)
                            return
                        else:
                            pass
                else:
                    print("Invalid Syntax at line ", i + 1)
                    Global_Error.append(1)
                    return
            if (lst[i][0] in lstB):
                if (len(lst[i]) == 3):
                    if (isRegister(lst[i][1]) and lst[i][2][0] == "$"):
                        d = int(lst[i][2][1:])
                        if (0 <= d <= 255):
                            pass
                        else:
                            print("Immediate Value out of range at line ", i + 1)
                            Global_Error.append(1)
                            return
                    else:
                        if (lst[i][1] == "FLAGS" and lst[i][2][0] == "$"):
                            print("Incorrect Use of Flags at line ", i + 1)
                            Global_Error.append(1)
                            return 1
                        # elif (isRegister(lst[i][1]) == False):
                        #     print("Incorrecct Use of Registers at line ", i + 1)
                        #     Global_Error.append(1)
                        #     return 1
                        else:
                            pass
                else:
                    print("Invalid Syntax at line ", i + 1)
                    Global_Error.append(1)
                    return 1
            if (lst[i][0] in lstC):
                if (len(lst[i]) == 3):
                    if ((isRegister(lst[i][1]) == True and isFlags(lst[i][2]) == True) or (isRegister(lst[i][2])==True and isFlags(lst[i][1])==True)):
                        pass
                    elif (isFlags(lst[i][1]) == True and isFlags(lst[i][2])==True):
                        print("Incorrect Use of Flags at line ", i + 1)
                        Global_Error.append(1)
                        return 1
                    else:
                        pass
                else:
                    print("Invalid Syntax at line ", i + 1)
                    Global_Error.append(1)
                    return
            if (lst[i][0] in lstD):
                if (len(lst[i]) == 3):
                    if (isRegister(lst[i][1])):
                        d = variable(lst)
                        if (lst[i][2] in d["var"]):
                            pass
                        else:
                            err["error"].append(i)
                    else:
                        print("Incorrecct Use of Registers at line ", i + 1)
                        Global_Error.append(1)
                        return 1

                else:
                    print("Invalid Syntax at line ", i + 1)
                    Global_Error.append(1)
                    return
            if (lst[i][0] in lstE):
                if (len(lst[i]) == 2):
                    if (lst[i][1] in op):
                        pass
                    else:
                        print("Invalid Use of Label at line ", i + 1)
                        Global_Error.append(1)
                        return
                else:
                    print("Invalid Syntax at line ", i + 1)
                    Global_Error.append(1)
                    return 1

            if (lst[i][0] == "hlt"):
                if (len(lst[i]) == 1):
                    if (lst[i][0] == "hlt" and i != len(lst) - 1):
                        print("Halt Misplaced at line ", i + 1)
                        Global_Error.append(1)
                        return
                    else:
                        pass
                else:
                    print("Invalid Syntax at line ", i + 1)
                    Global_Error.append(1)
                    return
            if (hltpresentornot(lst) == 0):
                print("Halt Missing")
                return
            if (lst[i][0] not in lstres):
                if (lst[i][0] == "var"):
                    if (len(lst[i]) == 2):
                        pass
                    else:
                        print("Undefined Variable used at line ", i + 1)
                        Global_Error.append(1)
                        return
                elif (lst[i][0] in op):
                    print("Undefined Label Used at line ", i + 1)
                    Global_Error.append(1)
                    return
                elif (lst[i][0][-1] == ":"):
                    pass
                else:
                    print("Syntax Error at line ", i + 1)
                    Global_Error.append(1)
                    return
            else:
                pass
    except:
        return 0


def label_error(lst):
    try:

        error_dict = dict()
        h = dict()
        ins_line = 0
        for i in range(len(lst)):
            if (lst[i][0][-1] == ":"):
                if (len(lst[i]) == 1):
                    print("Label not defined correctly at line ", i + 1)
                    Global_Error.append(1)
                    return 1
                elif (len(lst[i]) > 1):
                    check = 0
                    for j in range(1, len(lst[i])):
                        if (lst[i][j][-1] == ":"):
                            print("Label not defined correctly at line", i + 1)
                            Global_Error.append(1)
                            check = 1
                            return 1
                        else:
                            pass
                    if check == 1:
                        pass
                    else:
                        rem_lab_lst = lst[i][1:len(lst[i])]
                        ins_line = i
                        rem_lst = [rem_lab_lst]
                        ins_line = i
                        g = findLabel(rem_lst)
                        op = list(g.keys())
                        h = error(rem_lst, op)
    except:
        return 0
def variables(assemblyCode):
    try:
        check_rep_var = 0
        for i in range(len(assemblyCode)):
            if (assemblyCode[i][0] == "var" and check_rep_var == 0):
                pass
            elif (assemblyCode[i][0] != "var"):
                check_rep_var = 1
            elif (assemblyCode[i][0] == "var" and check_rep_var == 1):
                print("Varable defination is not correct at line", i + 1)
                Global_Error.append(1)
                return 1
    except:
        return 1

    return 0

var_dict = {}
n = len(lfile)
for i in lfile:
    if (i[0] == "var"):
        var_dict.update({str(i[1]): 0})
    else:
        break
count = 0
var_c = 0
var_l = []
for i in lfile:
    if (i[0] == "var"):
        var_c = var_c + 1
    else:
        count = count + 1
var_mem = n - var_c
for i in range(var_c):
    var_l.append(var_mem)
    var_mem = var_mem + 1
a = 0
for i in var_dict:
    var_dict[i] = var_l[a]
    a = a + 1

def floating_point(n):
    number=n
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int (dec)
    dec=dec/10
    res = bin(whole).lstrip("0b") + "."
    res_string=str(res)

    bin_string=""
    while dec != 1:
        dec=dec*2
        floor_num=floor(dec)
        floor_string=str(floor_num)
        bin_string=bin_string+floor_string
    final_number=res_string+bin_string
        

    split_number=final_number.split(".")
    split_number1=split_number[0]
    count=1
    for i in split_number1:
        if i=="1":
            break
        count=count+1
    count=len(split_number1)-count

    exp_count=count+3
    bin_exp_count=bin(exp_count).lstrip("0b")
    bin_exp_countStr=str(bin_exp_count)
    exp=""
    if len(str(bin_exp_countStr))<3:
        count1=3-len(bin_exp_countStr)
        for i in range(count1):
            exp="0"+exp
        bin_exp_countStr=exp+str(bin_exp_countStr)

    count_check=1
    counter=0
    mantissa=""
    for i in final_number:
        if (i=="1" and count_check==1):
            count_check=2
        elif(count_check==2 and i == "."):
            pass
        elif(count_check==2 and counter < 5):
            mantissa=mantissa+i
            counter=counter+1
    if (len(mantissa)<5):
        for i in range(5-len(mantissa)):
            mantissa=mantissa+"0"

    required_number=bin_exp_countStr+mantissa
    return required_number

def funcD(list, i):
    lstc = []
    if (list[0] == "st"):
        lstc.append("10101")
    elif (list[0] == "ld"):
        lstc.append("10100")

    t_reg = reg_addr.get(list[1])  # for reg adress
    lstc.append(t_reg)

    temp = list[2]
    temp_1 = var_dict.get(temp)
    temp_bin = (bin(temp_1)[2:])
    temp_str = str(temp_bin)
    temp_len = len(temp_str)
    temp_size = 8 - temp_len
    for i in range(temp_size):
        lstc.append("0")
    lstc.append(temp_str)
    ans = ("").join(lstc)
    # print(ans)
    lout.append(ans)


def funcB(list, i):
    lstb = []
    if (list[0] == "mov"):  # for opcode
        lstb.append("10010")
    elif(list[0]=="movf"):
        lstb.append("00010")
        check_imm=1
    elif (list[0] == "ls"):
        lstb.append("11001")

    t_reg = reg_addr.get(list[1])  # for reg adress
    lstb.append(t_reg)
    if(check_imm==1):
      t_str = list[2]  # for immidiate value
      vg=float(t_str)
      rr=floating_point(vg)
      kk=str(rr)
      lstb.append(kk)
      ans = ("").join(lstb)
      lout.append(ans)
    else:
      t_str = list[2]  # for immidiate value
      t_str1 = t_str[1:]
      temp_int = int(t_str1)
      temp_bin = (bin(temp_int)[2:])
      temp_str = str(temp_bin)
      temp_len = len(temp_str)
      temp_size = 8 - temp_len
      for i in range(temp_size):
         lstb.append("0")
      lstb.append(temp_str)
      ans = ("").join(lstb)
      lout.append(ans)
      # print(ans)


def funcC(lst, i):
    if (lst[0] == "mov" and isRegister(lst[1]) and isRegister(lst[2])):
        opc = dicInstruction["mov"][0] + "00000" + reg_addr[lst[1]] + reg_addr[lst[2]]
        lout.append(opc)
        # print(opc)
    elif (isRegister(lst[1]) and isRegister(lst[2])):
        opc1 = dicInstruction[lst[0]] + "00000" + reg_addr[lst[1]] + reg_addr[lst[2]]
        lout.append(opc1)
        # print(opc1)
    else:
        print("Registers not correctly implemented")


label_dict = {}

count_of_label = 0
for i in lfile:
    if (i[0] == "var"):
        pass
    elif (i[0][-1] == ":"):
        t_len = len(i[0])
        t_str = i[0]
        t_fnl = t_str[:t_len - 1]
        label_dict.update({t_fnl: count_of_label})
        count_of_label = count_of_label + 1
    else:
        count_of_label = count_of_label + 1

def funcE(list, i):
    lste = []
    if (list[0] == "jmp"):
        lste.append("11111")
    elif (list[0] == "jlt"):
        lste.append("01100")
    elif (list[0] == "jgt"):
        lste.append("01101")
    elif (list[0] == "je"):
        lste.append("01111")

    lste.append("000")
    temp = list[1]
    temp_1 = label_dict.get(temp)
    temp_bin = (bin(temp_1)[2:])
    temp_str = str(temp_bin)
    temp_len = len(temp_str)
    temp_size = 8 - temp_len
    for i in range(temp_size):
        lste.append("0")
    lste.append(temp_str)
    ans = ("").join(lste)
    lout.append(ans)
    # print(ans)


# run=["jmp" ,"label"]
# print(funcE(run))

def funcF(lst, j):
    l = []
    l.append("01010")
    l.append("00000000000")
    s = ("").join(l)
    lout.append(s)
    # print(s)


def check(lst, i):
    if (lst[0] == "add" or lst[0] == "sub" or lst[0] == "mul" or lst[0] == "xor" or lst[0] == "or" or lst[0] == "and" or lst[0]=="addf" or lst[0]=="subf"):
        funcA(lst, i)
    elif (lst[0] == "mov" or lst[0] == "rs" or lst[0] == "ls" or lst[0]=="movf"):
        if (lst[2][0] == "mov"):
            temp_check = lst[2]
            if (temp_check[0] == "$"):
                funcB(lst, i)
            else:
                funcC(lst, i)
        else:
            funcB(lst, i)
    elif (lst[0] == "div" or lst[0] == "not" or lst[0] == "cmp"):
        funcC(lst, i)
    elif (lst[0] == "ld" or lst[0] == "st"):
        funcD(lst, i)  # check error for "Use of undefined variables"
    elif (lst[0] == "jmp" or lst[0] == "jlt" or lst[0] == "jgt" or lst[0] == "je"):
        funcE(lst, i)
    elif (lst[0] == "hlt"):
        funcF(lst, i)
    else:
        pass


g1 = findLabel(lfile)
op1 = list(g1.keys())
if (error(lfile, op1) == 0):
    pass
elif (label_error(lfile) == 0):
    pass
elif (variables(lfile) == 0):
    pass
if len(Global_Error) == 0:
    for i in range(len(lfile)):
        if (lfile[i] == []):
            continue
        elif (lfile[i][0][-1] == ":"):
            lfile[i].pop(0)
            check(lfile[i], i)
        else:
            # print(i)
            # print(dictofV)
            check(lfile[i], i)


for i in lout:
    sys.stdout.write(str(i))
    print()
# print(lout)

# o=open("output.txt","w")
# # o.close()
# # o=open("output.txt","a")
# for i in lout:
#     o.write(i)
#     o.write("\n")
