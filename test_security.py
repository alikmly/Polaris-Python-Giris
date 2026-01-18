from security import check_password

def test_strong_passwords():
    assert check_password("A1!") == True
    assert check_password("Deneme.123") == True
    assert check_password("@9Z") == True

def test_missing_criteria():
    assert check_password("a1.") == False
    assert check_password("Deneme!") == False
    assert check_password("Deneme123") == False

def test_empty_or_invalid():
    assert check_password("") == False
    assert check_password("   ") == False
    assert check_password("123456") == False