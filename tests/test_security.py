from app.core.security import hash_password, verify_password


def test_correct_password_is_verified():
    password = "Example-Strong-Password-123!"

    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password) is True


def test_incorrect_password_is_rejected():
    hashed_password = hash_password("Example-Strong-Password-123!")

    assert verify_password("Wrong-Password-456!", hashed_password) is False


def test_same_password_produces_different_hashes():
    password = "Example-Strong-Password-123!"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash


def test_hash_does_not_contain_plain_text_password():
    password = "Example-Strong-Password-123!"

    hashed_password = hash_password(password)

    assert password not in hashed_password
