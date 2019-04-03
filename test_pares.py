import ejemplo

def test_1:
    response=ejemplo.pares(1000,3000)
    assert response == True

def test_2:
    response=ejemplo.pares(1000,90)
    assert response == False

    
