from components.boards import HW2RISCVBoard
from components.processors import HW2TimingSimpleCPU, HW2MinorCPU
from components.cache_hierarchies import HW2MESITwoLevelCache
from components.memories import HW2DDR3_1600_8x8

from workloads.daxpy_workload import DAXPYWorkload
from workloads.hello_world_workload import HelloWorkload
from workloads.roi_manager import exit_event_handler

from gem5.simulate.simulator import Simulator

import sys
sys.path.append('/home/quzi/school/computer_system/gem5/src/python')

if __name__ == "__m5_main__":
	cpu = HW2TimingSimpleCPU()
	cache = HW2MESITwoLevelCache()
	memory = HW2DDR3_1600_8x8()
	board = HW2RISCVBoard(
		clk_freq="4GHz", processor=cpu, cache_hierarchy=cache, memory=memory,
	)
	# workload = DAXPYWorkload()
	workload = HelloWorkload()
	board.set_workload(workload)
	simulator = Simulator(board=board, full_system=False, on_exit_event=exit_event_handler)
	simulator.run()
	print("Finished simulation.")
