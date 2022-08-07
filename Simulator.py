import sys
reg_dict = {"000":0,"001":0,"010":0, "011":0,"100":0,"101":0,"110":0,"111":0}
program_counter = 0
memory = []
halt=False
    

v = sys.stdin.read().split("\n")
v.pop(-1)
lfile=v

while ('' in lfile):
    lfile.remove([''])

instruction=lfile


for i in range(256):
    memory.append("0000000000000000")
 
for i in range(len(instruction)):
    memory[i]=instruction[i]


def underflow(value):
    if (value<0):
        return True
    else:
        return False
def overflow(value):
    if (value>=65535):
        return True
    else:
        return False

def add(instruction):
    global reg_dict
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    
    ans = int(reg_dict[reg2]) + int(reg_dict[reg1])
    if (overflow(ans)==True):
        reg_dict["111"]=8
    else:
        reg_dict[reg3]=ans
        reg_dict["111"]=0
    global program_counter
    program_counter +=1
def sub(instruction):
    global reg_dict
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    ans = reg_dict[reg2] - reg_dict[reg1]
    if (underflow(ans) == True):
        reg_dict["111"]=8
    else:
        reg_dict[reg3]=ans
        reg_dict["111"]=0
    global program_counter
    program_counter +=1
def and_op(instruction):
    global reg_dict
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    ans = bin(reg_dict(reg2)) and bin(reg_dict(reg1))
    reg_dict[reg3] = int(ans,2)
    global program_counter
    program_counter+=1 
    reg_dict["111"]=0
def or_op(instruction):
    global reg_dict
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    ans = bin(reg_dict(reg2)) or bin(reg_dict(reg1))
    reg_dict[reg3] = int(ans,2)
    global program_counter
    program_counter+=1 
    reg_dict["111"]=0
def xor_op(instruction):
    global reg_dict
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    ans = bin(reg_dict(reg2)^reg_dict(reg1))
    reg_dict[reg3] = int(ans,2)
    global program_counter
    program_counter+=1 
    reg_dict["111"]=0
def not_op(instruction):
    global reg_dict
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    ans = ""
    for bit in reg1:
        if bit=='1':
            ans+= '0'
        else:
            ans += '1'
    reg_dict[reg2] = int(ans,2)
    global program_counter
    program_counter+=1 
    reg_dict["111"]=0
def mov_imm(instruction):
    global reg_dict
    reg_temp =instruction[5:8]
    imm_val = int(instruction[8:16],2)
    reg_dict[reg_temp] = imm_val
    global program_counter
    program_counter +=1
    reg_dict["111"] = 0

def mov_reg(instruction):
    global reg_dict
    reg_temp = instruction[10:13]
    r_1 = instruction[13::]
    reg_dict[r_1] = reg_dict[reg_temp]
    global program_counter
    program_counter +=1
    reg_dict["111"] = 0    


def div(instruction):
    global reg_dict
    r_1 = instruction[10:13]
    r_2 = instruction[13:16]
    reg_dict["000"] = (reg_dict[r_1])//(reg_dict[r_2])
    reg_dict["001"] = (reg_dict[r_1])%(reg_dict[r_2])
    global program_counter
    program_counter +=1
    reg_dict["111"] = 0
def mul(instruction):
    global reg_dict
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    
    ans = reg_dict[reg2]*reg_dict[reg1]
    
    if (overflow(ans)==True):
        reg_dict["111"]=8
    else:
        reg_dict[reg3]=ans
        reg_dict["111"]=0
    global program_counter
    program_counter +=1

def cmp_(instruction):
    global reg_dict
    reg1=instruction[10:13]
    reg2=instruction[13:]
    reg_dict["111"]=0
    val1=reg_dict[reg1]
    val2=reg_dict[reg2]
    if(val1==val2):
        reg_dict["111"]=1
    elif(val1>val2):
        reg_dict["111"]=2
    else:
        reg_dict["111"]=4
    global program_counter
    program_counter+=1
def rs(instruction):
    global reg_dict
    reg_temp=instruction[5:8]
    imm_val=instruction[8:]
    reg_dict[reg_temp]=reg_dict[reg_temp]>>int(imm_val,2)
    global program_counter
    program_counter+=1
    reg_dict["111"]=0
def ls(instruction):
    global reg_dict
    reg_temp=instruction[5:8]
    imm_val=instruction[8:]
    reg_dict[reg_temp]=reg_dict[reg_temp]<<int(imm_val,2)
    global program_counter
    program_counter+=1
    reg_dict["111"]=0

def unconditional_jump(instruction):
    global program_counter
    global reg_dict
    memory_address=instruction[8:]
    program_counter=int(memory_address,2)
    reg_dict["111"]=0  

def jump_if_less_than(instruction):
    global program_counter
    global reg_dict
    if(reg_dict["111"]==4):
        memory_address=instruction[8:]
        program_counter=int(memory_address,2)
    else:
        program_counter+=1
    reg_dict["111"]=0

def jump_if_greater_than(instruction):
    global program_counter
    global reg_dict
    # print(instruction)
    print(reg_dict["111"])
    if(reg_dict["111"]==2):
        memory_address=instruction[8:]
        program_counter=int(memory_address,2)
        # print(program_counter)

    else :
        program_counter+=1    
    reg_dict["111"]=0

def jump_if_equal(instruction):
    global program_counter
    global reg_dict
    if(reg_dict["111"]==1):
        memory_address=instruction[8:]
        program_counter=int(memory_address,2)
    else:
        program_counter+=1
    reg_dict["111"]=0

def load(instruction):    
    reg=(instruction[5:8])
    memory_address=int(instruction[8:],2)
    # print(reg)
    # print(memory_address)
    reg_dict[reg]=(memory[memory_address])
    global program_counter
    program_counter+=1
    reg_dict["111"]=0

def store(instruction):
    global reg_dict
    global k
    global lfile
    reg=instruction[5:8]
    memory_address=instruction[8:]
    val=convert(reg_dict[reg],16)
    memory[int(len(lfile)+k)]=(val)
    global program_counter
    program_counter+=1
    reg_dict["111"]=0
    halt = False 
    k+=1
    # memory[len(lfile)+k]=("0000000000000"+reg)
def halt_f(instruction):
    global reg_dict
    reg_dict["111"]=0 
    global halt
    halt = True


def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if (int(n) < int(base)):
      return conver_tString[int(n)]
   else:
      return to_string(int(n)//int(base),base) + conver_tString[int(n) % int(base)]
def convert(n,digits):
    x = to_string(n,2)
    l = len(x)
    g = digits  - l
    y = "0"*g + str(x)
    return y



# 

lst=[]
k=0
l_st=[]
while(halt==False):
    str_=""
    print(program_counter)
    curr_ins=memory[(program_counter)]
    str_+=convert(program_counter,8)+" "
    call=curr_ins[0:5] 
    if(call=="10000"):
        add(curr_ins)
    elif(call=="10001"):
        sub(curr_ins)
    elif(call=="10010"):
        mov_imm(curr_ins)
    elif(call=="10011"):
        mov_reg(curr_ins)
    elif(call=="10100"):
        load(curr_ins)
    elif(call=="10101"):
        store(curr_ins)
    elif(call=="10110"):
        mul(curr_ins)    
    elif(call=="10111"):
        div(curr_ins)
    elif(call=="11000"):
        rs(curr_ins)
    elif(call=="11001"):
        ls(curr_ins)
    elif(call=="11010"):
        xor_op(curr_ins)
    elif(call=="11011"):
        or_op(curr_ins)
    elif(call=="11100"):
        and_op(curr_ins)
    elif(call=="11101"):
        not_op(curr_ins)    
    elif(call=="11110"):
        cmp_(curr_ins)
    elif(call=="11111"):
        unconditional_jump(curr_ins)
    elif(call=="01100"):
        jump_if_less_than(curr_ins)
    elif(call=="01101"):
        jump_if_greater_than(curr_ins)
    elif(call=="01111"):
        jump_if_equal(curr_ins)
    elif(call=="01010"):
        halt_f(curr_ins)
        halt = True
    for i in reg_dict.values():
        str_+=convert(i,16)+" "
    lst.append(str_)


for i in lst:
    print(i)
            
            

for i in memory:
    print(i)
