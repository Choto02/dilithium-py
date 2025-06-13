from dilithium_py.ml_dsa import ML_DSA_44

import os


dilithium = ML_DSA_44

seed = os.urandom(32)
seed = bytes.fromhex("0f2ebf0e8faf87ca5f1d160b4c3988a13781f607f05f3d5679584750deda1f1c")

poly = dilithium.R.rejection_sample_ntt_poly(seed, 1, 3)
# A = dilithium._expand_matrix_from_seed(seed)


# Output file path
output_path = "C:\\Users\\sayeeda\\Desktop\\Dilithium\\dilithium-py-main\\src\\Output_files\\rejection_sample_output.txt"

# Write coefficients for all i, j from 0 to 3
with open(output_path, "w") as f:
    for j in range(4):
        for i in range(4):
            poly = dilithium.R.rejection_sample_ntt_poly(seed, i, j)
            for coeff in poly.coeffs:
                f.write(f"{hex(coeff)}\n")


# print(f"Matrix shape: {len(A._data)} x {len(A._data[0])}")


# print("Sample polynomial coefficients from A[0][0]:")
# print(A._data[0][0].coeffs)

