from caesar_cipher.caesar_cipher import encrypt,decrypt, crack
def test_encrypt_one():
    actual = encrypt('Omar zoubi',6)
    print(actual)
    expected = 'Usgx fuaho'
    assert actual == expected
    
def test_encrypt_ones():
    actual = encrypt('I live in Ramtha',13)
    print(actual)
    expected = 'V yvir va Enzgun'
    assert actual == expected

def test_decrypt_one():
    actual = decrypt('V yvir va Enzgun',13)
    expected = 'I live in Ramtha'
    assert actual == expected

def test_crack():
    expected = 'cat is amazing, and awsume'
    encrypted = encrypt(expected, 50)
    actual = crack(encrypted)
    assert actual == expected