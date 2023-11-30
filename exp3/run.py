from components.boards import HW1RISCVBoard
from components.processors import HW1TimingSimpleCPU, HW1MinorCPU
from components.cache_hierarchies import HW1MESITwoLevelCache
from components.memories import HW1DDR3_1600_8x8, HW1DDR3_2133_8x8, HW1LPDDR3_1600_1x32

from workloads.mat_mul_workload import MatMulWorkload

from gem5.simulate.simulator import Simulator

import sys
sys.path.append('/home/quzi/school/computer_system/gem5/src/python')

if __name__ == "__m5_main__":

	cpu = HW1TimingSimpleCPU()
	cache = HW1MESITwoLevelCache()
	memory = HW1DDR3_2133_8x8()
	board = HW1RISCVBoard(
	clk_freq="4GHz", processor=cpu, cache_hierarchy=cache, memory=memory
	)

	workload = MatMulWorkload(224)
	board.set_workload(workload)
	
	simulator = Simulator(board=board, full_system=False)
	simulator.run()
	
	print("Finished simulation.")
