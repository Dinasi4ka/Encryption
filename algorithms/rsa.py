from algorithms.cipher import Cipher

class RSACipher(Cipher):
    def __init__(self, p, q, exponent):
        super().__init__()
        
        if p <= 1 or q <= 1:
            raise ValueError("p and q must be greater than 1.")
        
        self.p = p
        self.q = q
        self.n = p * q  # Модуль n
        self.exponent = exponent  # Відкритий експонент e
        self.private_exponent = self._calculate_private_exponent(p, q, exponent)

    def _gcd(self, a, b):
        # Обчислює найбільший спільний дільник (НД)
        while b:
            a, b = b, a % b
        return a

    def _multiplicative_inverse(self, a, m):
        # Обчислює обернений елемент a в модулі m
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def _calculate_private_exponent(self, p, q, e):
        # Обчислює закритий експонент d
        phi = (p - 1) * (q - 1)  # Обчислюємо φ(n)
        
        if phi == 0:
            raise ValueError("φ(n) cannot be zero.")
        
        # Перевірка на те, що e та φ(n) взаємно прості
        if self._gcd(e, phi) != 1:
            raise ValueError("e and φ(n) must be coprime.")

        return self._multiplicative_inverse(e, phi)

    def encrypt(self, plaintext):
        plaintext = self._preprocess_text(plaintext)  # Попередня обробка тексту
        # Шифрування: c = m^e mod n
        return [
            pow(self._convert_to_num(char), self.exponent, self.n) 
            for char in plaintext if char in self._get_alphabet(plaintext)
        ]
