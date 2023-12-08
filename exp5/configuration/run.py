from components.boards import HW3RISCVBoard
from components.processors import HW3BigCore, HW3LittleCore
from components.processors import HW3MediumCore1, HW3MediumCore2, HW3MediumCore3, HW3MediumCore4
from components.cache_hierarchies import HW3MESICache
from components.memories import HW3DDR4

from workloads.bfs_workload import BFSWorkload
from workloads.bubble_sort_workload import BubbleSortWorkload
from workloads.matmul_workload import MatMulWorkload

from gem5.simulate.simulator import Simulator

import sys
sys.path.append('/home/quzi/school/computer_system/gem5/src/python')

if __name__ == "__m5_main__":

	cpu = HW3MediumCore4()
	cache = HW3MESICache()
	memory = HW3DDR4()
	board = HW3RISCVBoard(
	clk_freq="2GHz", processor=cpu, cache_hierarchy=cache, memory=memory
	)

	workload = BubbleSortWorkload()
	board.set_workload(workload)
	
	simulator = Simulator(board=board, full_system=False)
	simulator.run()
	
	print("Finished simulation.")
	print("the area score is: ", cpu.get_area_score())
