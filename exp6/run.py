from components.boards import HW4RISCVBoard
from components.processors import HW4O3CPU
from components.cache_hierarchies import HW4LargeCache, HW4MediumCache, HW4SmallCache
from components.memories import HW4DDR4

from workloads.roi_manager import exit_event_handler

from workloads.matmul_workload import IJKMatMulWorkload, IKJMatMulWorkload
from workloads.matmul_workload import BlockIJMatMulWorkload
from workloads.matmul_workload import BlockIKMatMulWorkload
from workloads.matmul_workload import BlockKJMatMulWorkload

from gem5.simulate.simulator import Simulator

import sys
sys.path.append('/home/quzi/school/computer_system/gem5/src/python')

if __name__ == "__m5_main__":

	cpu = HW4O3CPU()
	cache = HW4LargeCache()
	memory = HW4DDR4()
	board = HW4RISCVBoard(
	clk_freq="2GHz", processor=cpu, cache_hierarchy=cache, memory=memory
	)

	workload = BlockIJMatMulWorkload(128, 8)
	board.set_workload(workload)
	
	simulator = Simulator(board=board, full_system=False,
		on_exit_event = exit_event_handler)
	simulator.run()
