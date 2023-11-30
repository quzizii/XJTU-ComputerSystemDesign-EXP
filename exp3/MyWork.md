# 操作步骤

## run.py修改

首先需要修改工作负载，具体代码部分为：

```
from workloads.mat_mul_workload import MatMulWorkload    # import workloads


    workload = MatMulWorkload(224)    # use new workloads and give a suitable mat_size
```

实验3中，前半部分修改CPU模型与缓存时钟频率，具体代码部分为：

```
from components.processors import HW1TimingSimpleCPU, HW1MinorCPU    # import two kinds of CPU


cpu = HW1TimingSimpleCPU()    # here needs to be changed
# cpu = HW1MinorCPU()

board = HW1RISCVBoard(
clk_freq="1GHz", processor=cpu, cache_hierarchy=cache, memory=memory    # here needs to be changed
)
# board = HW1RISCVBoard(
# clk_freq="2GHz", processor=cpu, cache_hierarchy=cache, memory=memory
# )
# board = HW1RISCVBoard(
# clk_freq="4GHz", processor=cpu, cache_hierarchy=cache, memory=memory
# )
```
    
后半部分修改CPU模型与内存模型，具体代码部分为：

```
from components.processors import HW1TimingSimpleCPU, HW1MinorCPU    # import two kinds of CPU
from components.memories import HW1DDR3_1600_8x8, HW1DDR3_2133_8x8, HW1LPDDR3_1600_1x32    # import three kinds of memory


cpu = HW1TimingSimpleCPU()    # here needs to be changed
# cpu = HW1MinorCPU()

memory = HW1DDR3_1600_8x8()    # here needs to be changed
# memory = HW1DDR3_2133_8x8()
# memory = HW1LPDDR3_1600_1x32() 
```




## 命令行运行
命令行代码较为类似，运行不同模型时，只需要每次更改run.py之后，在运行时更改对应的输出目录即可。因此仅列举一个示例

```
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt --outdir=exp_32/timing_213388 -re ./run.py 
Redirecting stdout to exp_32/timing_213388/simout
Redirecting stderr to exp_32/timing_213388/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ 
```

