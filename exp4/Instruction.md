
## 步骤一

修改run.py，更改负载
```
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_41/daxpy ./run.py 
Redirecting stdout to exp_41/daxpy/simout
Redirecting stderr to exp_41/daxpy/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_41/helloworld ./run.py 
Redirecting stdout to exp_41/helloworld/simout
Redirecting stderr to exp_41/helloworld/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ 
```

## 步骤二

修改run.py，更改CPU模型及参数
```
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_42/issue2float3 ./run.py 
Redirecting stdout to exp_42/issue2float3/simout
Redirecting stderr to exp_42/issue2float3/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_42/issue3float2 ./run.py 
Redirecting stdout to exp_42/issue3float2/simout
Redirecting stderr to exp_42/issue3float2/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_42/issue6float1 ./run.py 
Redirecting stdout to exp_42/issue6float1/simout
Redirecting stderr to exp_42/issue6float1/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ 
```

## 步骤三

修改run.py，更改CPU模型参数
```
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_43/int4float8 ./run.py 
Redirecting stdout to exp_43/int4float8/simout
Redirecting stderr to exp_43/int4float8/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_43/int2float8 ./run.py 
Redirecting stdout to exp_43/int2float8/simout
Redirecting stderr to exp_43/int2float8/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_43/int4float4 ./run.py 
Redirecting stdout to exp_43/int4float4/simout
Redirecting stderr to exp_43/int4float4/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ 
```