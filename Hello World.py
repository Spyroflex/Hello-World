def print_w():
    print("W")

def print_o():
    print("O")

def print_r():
    print("R")

def print_l():
    print("L")

def print_d():
    print("D")

def print_space():
    print(" ")

def hello_world():
    h = lambda x: print(x)
    h("H")
    e = lambda x: print(x, end="")
    e("E")
    l = lambda x: print(x, end="")
    l("L")
    l("L")
    o = lambda x: print(x)
    o("O")
    print_space()
    w = lambda x: print(x)
    w("W")
    o("O")
    r = lambda x: print(x)
    r("R")
    l("L")
    d = lambda x: print(x)
    d("D")
    print("!")

hello_world()
