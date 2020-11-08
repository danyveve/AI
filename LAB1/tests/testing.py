from controller.Controller_class import Controller
from problem.Problem_class import Problem
from state.State_class import State


def tests():
    '''
        TESTING FOR 4x4:                        //solved
        3 0 0 2                                 3 4 1 2
        0 1 4 0                                 2 1 4 3
        1 2 0 4                                 1 2 3 4
        0 3 2 1                                 4 3 2 1
    '''

    # state
    to_be_completed = [0, 0, 0, 0, 0, 0]
    sudoku_size = 4
    state = State(to_be_completed, sudoku_size)
    assert (state.getValues() == [0, 0, 0, 0, 0, 0])
    assert (state.getSize() == 6)
    assert (state.getSudoku_size() == 4)
    assert (
    state.nextStates(0) == [State([1, 0, 0, 0, 0, 0], 4), State([2, 0, 0, 0, 0, 0], 4), State([3, 0, 0, 0, 0, 0], 4),
                            State([4, 0, 0, 0, 0, 0], 4)])
    assert(State([1,0,0,0,0,0], 4).nextStates(0) == [])

    #problem
    problem = Problem("testInput")
    assert(problem.getSudokuSize() == 4)
    assert(problem.getFrequencyVector() == [3, 3, 2, 2])
    assert(problem.getGaps() == 6)
    assert(problem.getInitialBoard() == [[3, 0, 0, 2], [0, 1, 4, 0], [1, 2, 0, 4], [0, 3, 2, 1]])
    assert(problem.getRoot() == state)
    assert(problem.heuristics(State([1,1,1,1,1,1], 4)) == 9)
    assert (problem.heuristics(State([1, 1, 1, 1, 1, 4], 4)) == 3)

    #controller
    controller = Controller(problem)
    solution1 = controller.BFS(controller.getProblem().getRoot())
    solution2 = controller.BestFS(controller.getProblem().getRoot())
    solution3 = controller.BestFS2(controller.getProblem().getRoot())
    assert(solution1 == [[3, 4, 1, 2], [2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    assert(solution2 == [[3, 4, 1, 2], [2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    assert(solution3 == [[3, 4, 1, 2], [2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

