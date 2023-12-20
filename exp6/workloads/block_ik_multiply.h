
#ifndef __MATMUL_BLOCK_IK_MULTIPLY_H__
#define __MATMUL_BLOCK_IK_MULTIPLY_H__

void multiply(double** A, double** B, double** C, int matrix_size, int block_size)
{
    // TODO: Put your matrix multiplication code with blocking over i, k here.
    int i, j, k, kk, ii;
    double sum;
    int real_n = block_size * (matrix_size / block_size);
    for (i = 0; i < matrix_size; i++)
        for (j = 0; j < matrix_size; j++)
            C[i][j] = 0.0;
    for (i = 0; i < real_n; i += block_size) {
        for (k = 0; k < real_n; k += block_size) { 
            for (j = 0; j < matrix_size; j++) {
                for(ii = i; ii < i + block_size; ii += 1){
                    sum = C[ii][j];
                    for(kk = k; kk < k + block_size; kk += 1){
                        sum += A[ii][kk] * B[kk][j];  
                    }
                    C[ii][j] = sum;
                }
            }
        }
    }
}

#endif // __MATMUL_BLOCK_IK_MULTIPLY_H__
