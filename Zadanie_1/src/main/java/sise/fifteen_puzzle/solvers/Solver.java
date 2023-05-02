package sise.fifteen_puzzle.solvers;

import sise.fifteen_puzzle.model.Node;
import sise.fifteen_puzzle.model.State;

import java.util.HashSet;

public abstract class Solver {
    private final HashSet<Node> closedStateList = new HashSet<>();
    private final State targetState;
    public static int NUMBER_OF_VISITED_STATES = 0;
    public static int NUMBER_OF_PROCESSED_STATES = 0;
    public static int MAX_ACHIEVED_RECURSION_DEPTH = 0;
    public static int CURRENT_RECURSION_DEPTH = 0;

    public Solver(State targetState) {
        this.targetState = targetState;
    }

    public abstract String solve(Node primaryNode);

    public void addNewClosedState(Node newNode) {
        if (newNode != null) {
            closedStateList.add(newNode);
        }
    }

    /*
        Getters
     */

    public HashSet<Node> getClosedStateList() {
        return closedStateList;
    }

    public State getTargetState() {
        return targetState;
    }
}
