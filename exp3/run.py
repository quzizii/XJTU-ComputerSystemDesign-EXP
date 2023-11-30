from components.boards import HW1RISCVBoard
from components.processors import HW1TimingSimpleCPU, HW1MinorCPU    # import two kinds of CPU
from components.cache_hierarchies import HW1MESITwoLevelCache
from components.memories import HW1DDR3_1600_8x8, HW1DDR3_2133_8x8, HW1LPDDR3_1600_1x32    # import three kinds of memory

from workloads.mat_mul_workload import MatMulWorkload    # import workloads

from gem5.simulate.simulator import Simulator

import sys
sys.path.append('/home/quzi/school/computer_system/gem5/src/python')

if __name__ == "__m5_main__":

	cpu = HW1TimingSimpleCPU()    # here needs to be changed
	cache = HW1MESITwoLevelCache()
	memory = HW1DDR3_2133_8x8()    # here needs to be changed
	board = HW1RISCVBoard(
	clk_freq="4GHz", processor=cpu, cache_hierarchy=cache, memory=memory    # here needs to be changed
	)

	workload = MatMulWorkload(224)    # use new workloads and give a suitable mat_size
	board.set_workload(workload)
	
	simulator = Simulator(board=board, full_system=False)
	simulator.run()
	
	print("Finished simulation.")
