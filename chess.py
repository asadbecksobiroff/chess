signs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nums = list(range(1, 9))

def pawn(loc_sign, loc_num):
    order = -1
    if loc_num != 1 and order == -1:
        return [(loc_sign, loc_num+order)]
    elif loc_num != 8 and order == 1:
        return [(loc_sign, loc_num-order)]

def rook(loc_sign, loc_num):
    nodes = [(loc_sign, i) for i in range(1, 9) if i != loc_num]
    nodes += [(i, loc_num) for i in signs if i != loc_sign]      
    return nodes

def knight(loc_sign, loc_num):
    loc_sign_index = signs.index(loc_sign)
    nodes = []
    methods = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
            
    for i in methods:
        sign_index = loc_sign_index + i[0] 
        num = loc_num + i[1]
        if 0 <= sign_index < 8 and 0 < num <= 8:
            nodes.append((signs[sign_index], num))
        
    return nodes

def bishop(loc_sign, loc_num):
    loc_sign_index = signs.index(loc_sign)
    nodes = []
    start = loc_num - loc_sign_index
    i = 0
    while start <= 8:
        if start != loc_num:
            nodes.append((signs[i], start))
        i += 1
        start += 1
        
    start = loc_num + loc_sign_index
    i = 0
    while start >= 1:
        if start != loc_num:
            nodes.append((signs[i], start))
        i += 1
        start -= 1
 
    return nodes

def queen(loc_sign, loc_num):
    nodes = rook(loc_sign, loc_num)
    nodes += bishop(loc_sign, loc_num)
    return nodes

def king(loc_sign, loc_num):
    order = -1
    check = lambda sign_index, num: True if 0<=sign_index<8 and 0<num<=8 else False
    loc_sign_index = signs.index(loc_sign)
    nodes = []
    nodes = [(signs[loc_sign_index-1+i], loc_num+order*1) for i in range(3) if check(loc_sign_index-1+i, loc_num+order*1)]
    
    if check(loc_sign_index, loc_num - order*1):
        nodes.append((loc_sign, loc_num - order*1))
    return nodes


def direction(figure, loc_sign, loc_num):
    """Ushbu funksiya figura qaysi kattaklarga
    yurishi mumkinligini qaytaradi"""
    
    order = -1
    loc_sign_index = signs.index(loc_sign)
    
    if figure == 'pawn':
        return pawn(loc_sign, loc_num)
        
    elif figure == 'rook':
        return rook(loc_sign, loc_num)
    
    elif figure == 'knight':
        return knight(loc_sign, loc_num)

    elif figure == 'bishop':
       return bishop(loc_sign, loc_num)
         
    
    elif figure == 'queen':
        return queen(loc_sign, loc_num)
    
    elif figure == 'king':
        return king(loc_sign, loc_num)
    
        


if __name__ == '__main__':
    loc = direction('king', 'e', 7)
    print(loc)    

# rook, knight, bishop, queen, king, pawn