# 🔐 Mathematical Foundations of RSA Cryptography

## Overview

This document explains the mathematical concepts behind RSA, one of the most widely used public-key cryptosystems. We break down how prime numbers, modular arithmetic, and Euler’s theorem power secure encryption and decryption.

---

## 1. Prime Numbers (`p` and `q`)

* RSA starts by choosing two large **prime numbers**: `p` and `q`.
* A **prime number** has only two factors: 1 and itself.
* Example: `p = 61`, `q = 53`

### Why primes?

* The security of RSA depends on how hard it is to factor the product of two large primes.
* If `n = p * q`, it's easy to compute `n`, but hard to reverse (i.e., find `p` and `q` from `n`).

---

## 2. Modulus `n`

* Compute:

  ```
  n = p * q
  ```
* This `n` is part of both the **public** and **private keys**.
* All encryption/decryption is done **modulo `n`**.

---

## 3. Euler's Totient Function φ(n)

* For two primes `p` and `q`, Euler's totient is:

  ```
  φ(n) = (p - 1) * (q - 1)
  ```
* This function counts how many numbers less than `n` are **coprime** to `n`.

---

## 4. Public Exponent `e`

* Choose an integer `e` such that:

  ```
  1 < e < φ(n)
  gcd(e, φ(n)) = 1
  ```
* This means `e` is **coprime** to `φ(n)`.


---

## 5. Private Exponent `d`

* Find `d` such that:

  ```
  d ≡ e⁻¹ mod φ(n)  =>  d * e ≡ 1 mod φ(n)
  ```
* This means `d` is the **modular inverse** of `e` modulo `φ(n)`.
* It's computed using the **Extended Euclidean Algorithm**.

---

## 6. Key Pairs

* **Public Key**: `(e, n)`  → shared with everyone
* **Private Key**: `(d, n)` → kept secret

---

## 7. Encryption

* Convert message `m` (as a number):

  ```
  c = m^e mod n
  ```
* This produces ciphertext `c`.

---

## 8. Decryption

* Recover original message:

  ```
  m = c^d mod n
  ```
* Decryption works because of **Euler's Theorem**:

  ```
  m^(φ(n)) ≡ 1 mod n
  ```

  which ensures that:

  ```
  m^(ed) ≡ m mod n
  ```

---

## 9. Key Concept: Modulo and Congruence

* `a ≡ b mod n` means:

  ```
  a and b leave the same remainder when divided by n.
  ```
* Example:

  ```
  17 ≡ 5 mod 12
  ```

  (both leave remainder 5 when divided by 12)

---

## Summary Table

| Step | Math                                    | Purpose              |
| ---- | --------------------------------------- | -------------------- |
| 1    | Choose primes `p`, `q`                  | Basis of security    |
| 2    | `n = p * q`                             | Public modulus       |
| 3    | `φ(n) = (p-1)(q-1)`                     | Used to compute `d`  |
| 4    | Choose `e` s.t. `gcd(e, φ(n)) = 1`      | Public exponent      |
| 5    | Find `d` such that `d * e ≡ 1 mod φ(n)` | Private exponent     |
| 6    | Encrypt `c = m^e mod n`                 | Secure message       |
| 7    | Decrypt `m = c^d mod n`                 | Get original message |

---