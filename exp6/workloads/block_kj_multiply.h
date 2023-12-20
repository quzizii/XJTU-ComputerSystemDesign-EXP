
#ifndef __MATMUL_BLOCK_KJ_MULTIPLY_H__
#define __MATMUL_BLOCK_KJ_MULTIPLY_H__

void multiply(double** A, double** B, double** C, int matrix_size, int block_size)
{
    // TODO: Put your matrix multiplication code with blocking over k, j here.
    int i, j, k, kk, jj;
    double sum;
    int real_n = block_size * (matrix_size / block_size);
    for (i = 0; i < matrix_size; i++)
        for (j = 0; j < matrix_size; j++)
            C[i][j] = 0.0;
    for (j = 0; j < real_n; j += block_size) {
        for (k = 0; k < real_n; k += block_size) { 
            for (i = 0; i < matrix_size; i++) {
                for(jj = j; jj < j + block_size; jj += 1){
                    sum = C[i][jj];
                    for(kk = k; kk < k + block_size; kk += 1){
                        sum += A[i][kk] * B[kk][jj];  
                    }
                    C[i][jj] = sum;
                }
            }
        }
    }
}

#endif // __MATMUL_BLOCK_KJ_MULTIPLY_H__
