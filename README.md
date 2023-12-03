# Data Encryption Standard(DES) Algorithm Implementation.

## Main steps

DES bystkhdm 56 bit key bs l initial key bykon 64 bits fa lazm n-discard kol 8th bit abl manbd l DES process.

1. 64 bit plaintext btdkhol 3ala el initial permutation (IP) function.
2. performing IP function.
3. IP produces two halves from the permuted block (left , right). 
4. Each half goes through 16 rounds of encryption process.
5. Right and left halves are then rejoined and a final permutation is performed on the combined block. (64 bit ciphertext produced)

## Initial Permutation steps

1. Key transformation. 
    - Discarding each 8th bit from 64-bit key ashan yb2a 56 bits.
    -han2smhom two halves kol wahed 28 bits w han3ml left circular shift.
    -han-select ml 56 bits dol 48-bit subkey.

2. Expansion Permutation.
    - kda ehna andna 64-bit plaintext l hwa mt2sm 32 right w 32 left.
    - right half haykon expanded mn 32 l 48 bits.
    - l 32 bits dol byt2smo l 8 blocks kol wahed 4 bits w haykon kol wahed expanded fa yb2a 6 (2 bits added per block).
    - ba3ml XOR l right half da l hwa 48 bits ma3 l 48-bit key.
    - resulting output is given to to the S-box substitution.

3. S-box Substitution.

4. P-box Substitution.

5. XOR and Swap.