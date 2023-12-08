## 修改代码

> 修改processor.py逻辑如下，主要添加所需的核心：
```
class HW3BigCore(HW3O3CPU):
    def __init__(self):
        super().__init__(width=12, rob_size=352, num_int_regs=280, num_fp_regs=224)

class HW3LittleCore(HW3O3CPU):
    def __init__(self):
        super().__init__(width=4, rob_size=152, num_int_regs=100, num_fp_regs=84)

class HW3MediumCore1(HW3O3CPU):
    def __init__(self):
        super().__init__(width=4, rob_size=352, num_int_regs=100, num_fp_regs=84)

class HW3MediumCore2(HW3O3CPU):
    def __init__(self):
        super().__init__(width=4, rob_size=152, num_int_regs=200, num_fp_regs=184)

class HW3MediumCore3(HW3O3CPU):
    def __init__(self):
        super().__init__(width=12, rob_size=152, num_int_regs=100, num_fp_regs=84)

class HW3MediumCore4(HW3O3CPU):
    def __init__(self):
        super().__init__(width=8, rob_size=252, num_int_regs=150, num_fp_regs=134)
```

> 之后需要修改具体的运行文件run.py，由于文件过长不展示，可在/configuration/run.py中查看


##  具体运行脚本：
exp_51：并没有什么改动，最终查看stats.txt即可，文件在result/exp_51/下
```
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_51/BigBFS ./run.py 
Redirecting stdout to exp_51/BigBFS/simout
Redirecting stderr to exp_51/BigBFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_51/LittleBFS ./run.py 
Redirecting stdout to exp_51/LittleBFS/simout
Redirecting stderr to exp_51/LittleBFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_51/LittleBuuble ./run.py 
Redirecting stdout to exp_51/LittleBuuble/simout
Redirecting stderr to exp_51/LittleBuuble/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_51/BigBuuble ./run.py 
Redirecting stdout to exp_51/BigBuuble/simout
Redirecting stderr to exp_51/BigBuuble/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_51/BigMatmul ./run.py 
Redirecting stdout to exp_51/BigMatmul/simout
Redirecting stderr to exp_51/BigMatmul/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir=exp_51/LittleMatmul ./run.py 
Redirecting stdout to exp_51/LittleMatmul/simout
Redirecting stderr to exp_51/LittleMatmul/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ 
```
exp_52：在代码中还添加了打印CPU面积，会将结果输出到simout中。
```
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir ./exp_52/BigBFS ./run.py 
Redirecting stdout to ./exp_52/BigBFS/simout
Redirecting stderr to ./exp_52/BigBFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir ./exp_52/LittleBFS ./run.py 
Redirecting stdout to ./exp_52/LittleBFS/simout
Redirecting stderr to ./exp_52/LittleBFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir ./exp_52/Medium1BFS ./run.py 
Redirecting stdout to ./exp_52/Medium1BFS/simout
Redirecting stderr to ./exp_52/Medium1BFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir ./exp_52/Medium2BFS ./run.py 
Redirecting stdout to ./exp_52/Medium2BFS/simout
Redirecting stderr to ./exp_52/Medium2BFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir ./exp_52/Medium3BFS ./run.py 
Redirecting stdout to ./exp_52/Medium3BFS/simout
Redirecting stderr to ./exp_52/Medium3BFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$ gem5.opt -re --outdir ./exp_52/Medium4BFS ./run.py 
Redirecting stdout to ./exp_52/Medium4BFS/simout
Redirecting stderr to ./exp_52/Medium4BFS/simerr
quzi@quzi:~/school/computer_system/gem5-assignment-template$
```




## 绘图
在问题中需要绘制帕累托前沿图，因此编写了plot.py用于绘图，其中静态给出了六个CPU核心的面积与效能。运行`
python ./plot.py 
`即可