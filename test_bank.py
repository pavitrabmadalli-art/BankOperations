from bank import bankOper

def test_deposit():
    totalBal, updatedBal = bankOper(200000,30000,0)

    assert totalBal == 230000
    assert updatedBal == 230000

def test_withdraw():
    totalBal, updatedBal = bankOper(100000,40000,10000)

    assert totalBal == 140000
    assert updatedBal == 130000

def test_anyamount():
    totalBal, updatedBal = bankOper(150000,0,135000)

    assert totalBal == 150000
    assert updatedBal == 15000
