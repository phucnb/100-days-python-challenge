from main import encrypt, decrypt, generate_key

def test_generate_key():
    assert generate_key('helloword', 'phuc') == 'phucphucp'
    assert generate_key('123456789', 'pppppppp') == 'ppppppppp'
    assert generate_key('123456789', 'Abcde') == 'AbcdeAbcd'
    assert generate_key('0000', 'Abcde') == 'Abcde'
    assert generate_key('0000', 'Abcd') == 'Abcd'
    
    
def test_encrypt():
    assert encrypt("this a a text", '3dsf*sj23') == '(M]Z*Ujs3(Jl['
    assert encrypt("this a a text", 'shortkey') == 'hQYftMe[s]Uki'
    assert encrypt("this a a text", 'keylongerthantext') == '`Nc`oPgGriNZc'
    
def test_decrypt():
    assert decrypt("(M]Z*Ujs3(Jl[", '3dsf*sj23') == 'this a a text'
    assert decrypt("hQYftMe[s]Uki", 'shortkey') == 'this a a text'
    assert decrypt("`Nc`oPgGriNZc", 'keylongerthantext') == 'this a a text'