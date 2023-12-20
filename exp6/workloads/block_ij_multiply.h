
#ifndef __MATMUL_BLOCK_IJ_MULTIPLY_H__
#define __MATMUL_BLOCK_IJ_MULTIPLY_H__

void multiply(double** A, double** B, double** C, int matrix_size, int block_size)
{
    // TODO: Put your matrix multiplication code with blocking over i, j here.
    int i, j, k, ii, jj;
    double sum;
    int real_n = block_size * (matrix_size / block_size);
    for (i = 0; i < matrix_size; i++)
        for (j = 0; j < matrix_size; j++)
            C[i][j] = 0.0;
    for (i = 0; i < real_n; i += block_size) { 
        for (j = 0; j < real_n; j += block_size) {
            for(ii = i; ii < i + block_size; ii += 1){
                for(jj = j; jj < j + block_size; jj += 1){
                    sum = C[ii][jj];
                    for (k = 0; k < matrix_size; k++) {
                        sum += A[ii][k] * B[k][jj];  
                    }
                    C[ii][jj] = sum;
                }
            }
        }
    }
}

#endif // __MATMUL_BLOCK_IJ_MULTIPLY_H__
