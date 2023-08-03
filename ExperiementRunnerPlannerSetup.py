import os, sys

# Add EPICpy folder to path
working_dir = os.getcwd()
os.chdir("../EPICpy")
sys.path.append(os.getcwd())
os.chdir(working_dir)


from runner import Runner
from Internal_Representation.problem_predicate import ProblemPredicate
from Internal_Representation.state_novelty import StateNovelty
from Solver.Parameter_Selection.ParameterSelector import ParameterSelector
from Solver.Search_Queues.Greedy_Best_First_Search_Queue import GBFSSearchQueue
from Solver.Search_Queues.Greedy_Best_First_Search_Queue_Newest_First import GBFSSearchQueueNewestFirst
from Solver.Search_Queues.Novelty_GBFS_Search_Queue import NoveltyGBFSQueue
from Solver.Search_Queues.Novelty_GBFS_Search_Queue_Oldest_First import NoveltyGBFSOldestFirstQueue
from Solver.Search_Queues.Novelty_TreeDistance_GBFS_Search_Queue import NoveltyTreeDistanceGBFSSearchQueue
from Solver.Search_Queues.search_queue_dual_heuristic_HammingDistance import SearchQueueGBFSDualHammingDistance
from Solver.Search_Queues.search_queue_dual_heuristic_TreeDistance import SearchQueueGBFSDualTreeDistance
from Solver.Search_Queues.search_queue_dual_heuristic_Landmarks import SearchQueueGBFSDualLandmarks
from Solver.Heuristics.hamming_distance_partial_order import HammingDistancePartialOrder
from Solver.Heuristics.seen_states_pruning import SeenStatesPruning
from Solver.Heuristics.no_pruning import NoPruning
from Solver.Heuristics.hamming_distance_seen_states import HammingDistanceSeenStatesPruning
from Solver.Heuristics.tree_distance_seen_states import TreeDistanceSeenStatesPruning
from Solver.Heuristics.tree_distance import TreeDistance
from Solver.Heuristics.landmarks import Landmarks
from Solver.Heuristics.landmarks_no_reachability import LandmarksNoReachability
from Solver.Solving_Algorithms.partial_order_novelty import PartialOrderNoveltySolver
from Solver.Solving_Algorithms.partial_order_novelty_light import PartialOrderNoveltyLightSolver
from Solver.Solving_Algorithms.partial_order_novelty_no_reset import PartialOrderNoveltyNoResetSolver
from Solver.Solving_Algorithms.partial_order_novelty_level_2 import PartialOrderNoveltyLevelTwoSolver
from Solver.Solving_Algorithms.partial_order_novelty_methods import PartialOrderNoveltyMethodsSolver
from Solver.Solving_Algorithms.partial_order_novelty_methods_only import PartialOrderNoveltyMethodsOnlySolver
from Solver.Solving_Algorithms.partial_order_novelty_methods_no_reset import PartialOrderNoveltyMethodsNoResetSolver
from Solver.Solving_Algorithms.partial_order_novelty_methods_tasks import PartialOrderNoveltyMethodsTasksSolver
from Solver.Solving_Algorithms.partial_order_novelty_level_2_no_reset import PartialOrderNoveltyLevelTwoNoResetSolver
from Solver.Solving_Algorithms.partial_order_hamming_novelty import PartialOrderHammingNoveltySolver
from Solver.Solving_Algorithms.partial_order_hamming_novelty_no_reset import PartialOrderHammingNoveltyNoResetSolver
from Solver.Models.PandaVerifyModel import PandaVerifyModel
from Solver.Progress_Tracking.panda_verify_format import PandaVerifyFormatTracker


def setup_controller(controller, strategy):
    """
    :param controller: Runner Object
    :param strategy: Integer correlating to some predefined planner configuration
    :return: String of path where results should be recorded
    """
    if strategy == 1:
        """Hamming Distance (Seen States)"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueue)
        controller.set_heuristic(HammingDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Hamming-Distance-seen-states-results.csv'
    elif strategy == 2:
        """Seen States Pruning"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueue)
        controller.set_heuristic(SeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/seen-state-breadth-first-results.csv'
    elif strategy == 3:
        """Tree Distance (Seen States)"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueue)
        controller.set_heuristic(TreeDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Tree-Distance-seen-states-results.csv'
    elif strategy == 4:
        """Novelty - Level 1 - Reset to 0 after task or method expansion"""
        controller.set_solver(PartialOrderNoveltySolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_reset-newest-results.csv'
    elif strategy == 5:
        """Tree Distance"""
        # controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueue)
        controller.set_heuristic(TreeDistance)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Tree-Distance-results.csv'
    elif strategy == 6:
        """Novelty - Level 1 - Reset to 0 after task or method expansion - Tree Distance Tie Breaker"""
        controller.set_solver(PartialOrderNoveltySolver)
        controller.set_search_queue(NoveltyTreeDistanceGBFSSearchQueue)
        controller.set_heuristic(TreeDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_reset-TreeDis-results.csv'
    elif strategy == 7:
        """Tree Distance (Seen States) - Newest First Search Queue"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueueNewestFirst)
        controller.set_heuristic(TreeDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Tree-Distance-seen-states-newest-first-results.csv'
    elif strategy == 8:
        """Hamming Distance (Seen States) - Newest First Search Queue"""
        # controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueueNewestFirst)
        controller.set_heuristic(HammingDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Hamming-Distance-seen-states-newest-first-results.csv'
    elif strategy == 9:
        """Tree Distance with Hamming Distance Tie Breaker"""
        # controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(SearchQueueGBFSDualHammingDistance)
        controller.set_heuristic(TreeDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Tree-Distance-seen-states-Hamming-Distance-tie-breaker-results.csv'
    elif strategy == 10:
        """Novelty - Level 1 - No reset after task or method expansion"""
        controller.set_solver(PartialOrderNoveltyNoResetSolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_No-Reset-results.csv'
    elif strategy == 11:
        """Novelty - Level 2 - Reset after task or method expansion"""
        controller.set_solver(PartialOrderNoveltyLevelTwoSolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_level2_reset-results.csv'
    elif strategy == 12:
        """Novelty - level1 - Checking for Novel Method"""
        controller.set_solver(PartialOrderNoveltyMethodsSolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Methods-results.csv'
    elif strategy == 13:
        """Novelty - Level 1 - Reset to 0 after task or method expansion - oldest first"""
        controller.set_solver(PartialOrderNoveltySolver)
        controller.set_search_queue(NoveltyGBFSOldestFirstQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_reset-Oldest-First-results.csv'
    elif strategy == 14:
        """Landmarks"""
        # controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueue)
        controller.set_heuristic(Landmarks)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Landmarks-results.csv'
    elif strategy == 15:
        """Novelty - Level 1 - Reset to 0 after task or method expansion - Hamming Distance Tie Breaker"""
        controller.set_solver(PartialOrderNoveltySolver)
        controller.set_search_queue(NoveltyTreeDistanceGBFSSearchQueue)
        controller.set_heuristic(HammingDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_reset-HamDis-results.csv'
    elif strategy == 16:
        """Novelty - Level 2 - No reset after task or method expansion"""
        controller.set_solver(PartialOrderNoveltyLevelTwoNoResetSolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_level2_no_reset-results.csv'
    elif strategy == 17:
        """Novelty - level1 - Checking for Novel Method - Oldest First"""
        controller.set_solver(PartialOrderNoveltyMethodsSolver)
        controller.set_search_queue(NoveltyGBFSOldestFirstQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Methods_oldest_first-results.csv'
    elif strategy == 18:
        """Novelty - Level 1 - No Reset to 0 after task or method expansion - Tree Distance Tie Breaker"""
        controller.set_solver(PartialOrderNoveltyNoResetSolver)
        controller.set_search_queue(NoveltyTreeDistanceGBFSSearchQueue)
        controller.set_heuristic(TreeDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_no_reset-TreeDis-results.csv'
    elif strategy == 19:
        """Novelty - Level 1 - No Reset to 0 after task or method expansion - Hamming Distance Tie Breaker"""
        controller.set_solver(PartialOrderNoveltyNoResetSolver)
        controller.set_search_queue(NoveltyTreeDistanceGBFSSearchQueue)
        controller.set_heuristic(HammingDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_no_reset-HamDis-results.csv'
    elif strategy == 20:
        """Novelty - Level 1 - Reset to 0 after task or method expansion - Landmarks Tie Breaker"""
        controller.set_solver(PartialOrderNoveltySolver)
        controller.set_search_queue(NoveltyTreeDistanceGBFSSearchQueue)
        controller.set_heuristic(Landmarks)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_reset-Landmarks-results.csv'
    elif strategy == 21:
        """Novelty - Level 1 - No Reset to 0 after task or method expansion - Landmarks Tie Breaker"""
        controller.set_solver(PartialOrderNoveltyNoResetSolver)
        controller.set_search_queue(NoveltyTreeDistanceGBFSSearchQueue)
        controller.set_heuristic(Landmarks)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Only_no_reset-Landmarks-results.csv'
    elif strategy == 22:
        """Landmarks with Hamming Distance Tie Breaker"""
        # controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(SearchQueueGBFSDualHammingDistance)
        controller.set_heuristic(Landmarks)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Landmarks-Hamming-Distance-tie-breaker-results.csv'
    elif strategy == 23:
        """Landmarks with Tree Distance Tie Breaker"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(SearchQueueGBFSDualTreeDistance)
        controller.set_heuristic(Landmarks)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Landmarks-Tree-Distance-tie-breaker-results.csv'
    elif strategy == 24:
        """Landmarks - Newest First Search Queue"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueueNewestFirst)
        controller.set_heuristic(Landmarks)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Landmarks-newest-first-results.csv'
    elif strategy == 25:
        """Hamming Distance with Tree Distance Tie Breaker"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(SearchQueueGBFSDualTreeDistance)
        controller.set_heuristic(HammingDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Hamming-Distance-seen-states-Tree-Distance-tie-breaker-results.csv'
    elif strategy == 26:
        """Tree Distance with Landmarks Tie Breaker"""
        # controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(SearchQueueGBFSDualLandmarks)
        controller.set_heuristic(TreeDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Tree-Distance-seen-states-landmarks-tie-breaker-results.csv'
    elif strategy == 27:
        """Hamming Distance with Landmarks Tie Breaker"""
        # controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(SearchQueueGBFSDualLandmarks)
        controller.set_heuristic(HammingDistanceSeenStatesPruning)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Hamming-Distance-seen-states-landmarks-tie-breaker-results.csv'
    elif strategy == 28:
        """Novelty - level1 - Checking for Novel Methods and Tasks"""
        controller.set_solver(PartialOrderNoveltyMethodsTasksSolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Methods_Tasks-results.csv'
    elif strategy == 29:
        """Novelty - level1 - Checking for Novel Methods and Tasks - Oldest First"""
        controller.set_solver(PartialOrderNoveltyMethodsTasksSolver)
        controller.set_search_queue(NoveltyGBFSOldestFirstQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Methods_Tasks_oldest_first-results.csv'
    elif strategy == 30:
        """Hamming Distance with Novelty Tie Breaker - Reset - Newest First"""
        controller.set_solver(PartialOrderHammingNoveltySolver)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Hamming-Novelty-Reset-Newest.csv'
    elif strategy == 31:
        """Hamming Distance with Novelty Tie Breaker - No Reset - Newest First"""
        controller.set_solver(PartialOrderHammingNoveltyNoResetSolver)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Hamming-Novelty-No-Reset-Newest.csv'
    elif strategy == 32:
        """Novelty - level1 - Checking for Novel Method - No Reset"""
        controller.set_solver(PartialOrderNoveltyMethodsNoResetSolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Facts_Methods_No_Reset-results.csv'
    elif strategy == 33:
        """Novelty - Checking for Novel Method - ONLY - Newest First"""
        controller.set_solver(PartialOrderNoveltyMethodsOnlySolver)
        controller.set_search_queue(NoveltyGBFSQueue)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Novelty_Methods_Only_Reset_Newest-results.csv'
    elif strategy == 34:
        """Landmarks - No Reachability"""
        controller.set_solver(PartialOrderNoveltyLightSolver)
        controller.set_search_queue(GBFSSearchQueue)
        controller.set_heuristic(LandmarksNoReachability)
        controller.set_model(PandaVerifyModel)
        controller.set_progress_tracker(PandaVerifyFormatTracker)
        return 'results/Landmarks_No_Reachability-results.csv'
    else:
        raise ValueError('Unknown strategy code: {}'.format(strategy))