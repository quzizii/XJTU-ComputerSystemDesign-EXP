from components.boards import HW5X86Board
from components.processors import HW5O3CPU
from components.cache_hierarchies import HW5MESITwoLevelCacheHierarchy
from components.memories import HW5DDR4

from workloads.roi_manager import exit_event_handler

from workloads.array_sum_workload import NaiveArraySumWorkload
from workloads.array_sum_workload import ChunkingArraySumWorkload
from workloads.array_sum_workload import NoResultRaceArraySumWorkload
from workloads.array_sum_workload import ChunkingNoResultRaceArraySumWorkload
from workloads.array_sum_workload import NoCacheBlockRaceArraySumWorkload
from workloads.array_sum_workload import ChunkingNoBlockRaceArraySumWorkload

from gem5.simulate.simulator import Simulator

import sys
sys.path.append('/home/quzi/school/computer_system/gem5/src/python')

if __name__ == "__m5_main__":

	cpu = HW5O3CPU(16)
	cache = HW5MESITwoLevelCacheHierarchy(1)
	memory = HW5DDR4()
	board = HW5X86Board(
	clk_freq="3GHz", processor=cpu, cache_hierarchy=cache, memory=memory
	)

	workload = NoCacheBlockRaceArraySumWorkload(32768, 16)
	board.set_workload(workload)
	
	simulator = Simulator(board=board, full_system=False,
		on_exit_event = exit_event_handler)
	simulator.run()
