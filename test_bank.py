from bank import bankOper

def test_deposit():
    totalBal, updatedBal = bankOper(30000,25000,0)

    assert totalBal == 30000
    assert updatedBal == 25000

def test_withdraw():
    totalBal, updatedBal = bankOper(100000,40000,10000)

    assert totalBal == 140000
    assert updatedBal == 130000

def test_anyamount():
    totalBal, updatedBal = bankOper(150000,0,135000)

    assert totalBal == 150000
    assert updatedBal == 135000
