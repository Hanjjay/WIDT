def ciper():
    decbook = {
        '5':'a','6':'A',
        'd':'b','E':'B',
        '!':'c','?':'C',
        '=':'d','+':'D',
        '3':'e','@':'E',
        ',':'f','<':'F',
        '`':'g','~':'G',
        '#':'h','V':'H',
        ')':'i',')':'I',
        '$':'l','A':'L',
        '0':'m','Q':'M',
        'x':'n','.':'N',
        '3':'o','W':'O',
        '*':'p','%':'P',
        '{':'r',']':'R',
        '|':'s','7':'S',
        'n':'t','D':'T',
        ';':'u','q':'U',
        'g':'v','>':'V',
        '^':'y','m':'Y',
        ' ':'z','k':'Z',
        'J':' '
    }
    encbook = {}
    for k in decbook:
        val = decbook[k]
        encbook[val] = k
    return encbook,decbook

def encrypt(msg,encbook):
    for c in msg:
        if c in encbook:
            msg = msg.replace(c,encbook[c])
    return msg

def decrypt(msg,decbook):
    for c in decbook:
        if c in decbook:
            msg = msg.replace(c,decbook[c])
    return msg

if __name__=='__main__':
    
    plaintext = 'Hi My name is han jay nice to meet you'
    encbook,decbook = ciper()
    ciphertext = encrypt(plaintext,encbook)
    print(ciphertext)
    
    deciphertext = decrypt(ciphertext,decbook)
    print(deciphertext)