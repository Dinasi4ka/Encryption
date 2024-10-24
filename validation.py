def validate_vigenere_key(key):
    if not key.isalpha():
        raise ValueError("Error: Key must only contain letters.")
    return key

def validate_gamma_key(key):
    if not key.isalpha():
        raise ValueError("Error: Key must only contain letters.")
    return key

def validate_rsa_keys(p, q, exponent):
    p, q, exponent = map(int, (p, q, exponent))
    if p <= 1 or q <= 1:
        raise ValueError("Error: p and q must be greater than 1.")
    if exponent <= 0:
        raise ValueError("Error: exponent must be greater than 0.")
    return p, q, exponent
