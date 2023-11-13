from Source.Wallet import wallet

def test_getbalance():
    obj = wallet(0)
    obj.set_balance(20)
    assert obj.get_balance() == 20

def test_removebalance():
    obj = wallet(50)
    obj.remove_balance(20)
    assert obj.get_balance() == 30
    
def test_setbalance():
    obj = wallet(0)
    obj.set_balance(40)
    assert obj.get_balance() == 40
