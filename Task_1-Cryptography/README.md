# Task 1 — Cryptography Challenge

## Objective
Decode the given ciphertext to recover the flag in the expected `BYTE{...}` format.

## Initial Ciphertext
```text
QkFJTntiQTczX1E4Ul9BcmhIQ19YNHlHY0R9
```

## Approach and Methodology

### Step 1: Base64 Decoding
I started by checking whether the given string used a common encoding format. I used an online Base64 decoder website (CyberChef) to decode the original string.

The decoded output was:

```text
BAIN{bA73_Q8R_ArhHC_X4yGcD}
```

The result still looked encoded, so I continued investigating possible cipher techniques.

### Step 2: Beaufort Cipher
I explored classical cipher techniques and used the Beaufort cipher with the key `CYBR` to decode the remaining text.

This transformation produced the final flag.

### Step 3: Verification
I used my Python solution to reproduce the cipher-decoding process and verify the result.

## Final Flag

```text
BYTE{bY73_L8A_ChuKA_B4dLaV}
```

## Tools Used
- Online Base64 decoder website - CyberChef
- Python 3
- Beaufort cipher
- ChatGPT for understanding decoding and ciphers
- Gemini for help me identify the Beaufort cipher and key
- Terminal for running and verifying the solution

## Key Learnings
- Online encoding tools can help identify and decode common formats.
- Base64 is an encoding scheme, whereas the Beaufort cipher is a keyed encryption technique.
- Layered challenges may require multiple decoding steps.
- Verifying each step helps make the solution reproducible.

## Files
- `solve.py` — Python script used for the cipher-decoding process.
