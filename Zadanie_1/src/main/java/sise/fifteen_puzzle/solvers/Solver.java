package sise.fifteen_puzzle.solvers;

import sise.fifteen_puzzle.model.Node;
import sise.fifteen_puzzle.model.State;

import java.util.HashSet;

public abstract class Solver {
    private final HashSet<Node> closedStateList = new HashSet<>();
    private final State targetState;
    private static int NUMBER_OF_VISITED_STATES = 0;
    private static int NUMBER_OF_PROCESSED_STATES = 0;
    private static int MAX_ACHIEVED_RECURSION_DEPTH = 0;
    private static int CURRENT_RECURSION_DEPTH = 0;

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

    public static int getNumberOfVisitedStates() {
        return NUMBER_OF_VISITED_STATES;
    }

    public static int getNumberOfProcessedStates() {
        return NUMBER_OF_PROCESSED_STATES;
    }

    public static int getMaxAchievedRecursionDepth() {
        return MAX_ACHIEVED_RECURSION_DEPTH;
    }

    public static int getCurrentRecursionDepth() {
        return CURRENT_RECURSION_DEPTH;
    }

    /*
        Setters
     */

    public static void setNumberOfVisitedStates(int numberOfVisitedStates) {
        NUMBER_OF_VISITED_STATES = numberOfVisitedStates;
    }

    public static void setNumberOfProcessedStates(int numberOfProcessedStates) {
        NUMBER_OF_PROCESSED_STATES = numberOfProcessedStates;
    }

    public static void setMaxAchievedRecursionDepth(int maxAchievedRecursionDepth) {
        MAX_ACHIEVED_RECURSION_DEPTH = maxAchievedRecursionDepth;
    }

    public static void setCurrentRecursionDepth(int currentRecursionDepth) {
        CURRENT_RECURSION_DEPTH = currentRecursionDepth;
    }
}
