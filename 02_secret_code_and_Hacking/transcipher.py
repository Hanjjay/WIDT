ENC = 0
DEC = 1
def pareseKey(key):
    tmp = []
    key = key.upper()
    
    for i, k in enumerate(key):
        tmp.append((i ,k))
        
    tmp = sorted(tmp, key = lambda x:x[1])
    
    enc_table = {}
    dec_table = {}
    for i,r in enumerate(tmp):
        enc_table[r[0]] = i
        dec_table[i] = r[0]
        
    return enc_table, dec_table
    def transpsition(msg,key,mode):
    msgsize = len(msg)
    keysize = len(key)
    ret = ''
    
    filler = ''
    if msgsize%keysize !=0:
        filler = '0'*(keysize - msgsize%keysize)
    
    msg = msg.upper()
    msg += filler
    
    enc_table , dec_table = pareseKey(key)
    
    if mode == ENC:
        table = enc_table
    else:
        talbe = dec_table
    
    if mode == ENC:                   #암호화
        buf = ['']*keysize
        for i , c in enumerate(msg):
            col = i%keysize
            index = table[col]
            buf[index] += c
        for text in buf:
            ret += text
    
    else :                            #복호화
        blocksize = int(msgsize/keysize)
        buf =  ['']*keysize
        pos = 0
        for i in range(keysize):
            text = msg[pos:pos+blocksize]
            index = talbe[i]
            buf[index] +=text
            pos += blocksize
            
        for i in range(blocksize):
            for j in range(keysize):
                if buf[j][i] != '0':
                    ret +=buf[j][i]
                    
    return ret
def main():
    key ='jay'
    msg = 'ABCDEFGHIJKLMNOPQRXTUVWXYZ'
    print(msg)
    enctext = transpsition(msg,key,ENC)
    print(enctext)
    dectext = transpsition(enctext,key,DEC)
    print(dectext)
if __name__ == '__main__':
    main()