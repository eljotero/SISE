package sise.fifteen_puzzle.solvers;

import sise.fifteen_puzzle.model.Node;
import sise.fifteen_puzzle.model.State;
import java.util.PriorityQueue;

public class AStarSolver extends Solver {

    private final String usedHeuristic;
    private final PriorityQueue<Node> openStateList = new PriorityQueue<>();

    public AStarSolver(State targetState, String usedHeuristic) {
        super(targetState);
        this.usedHeuristic = usedHeuristic;
    }

    public void addNewOpenState(Node newNode) {
        if (newNode != null) {
            openStateList.add(newNode);
        }
    }

    @Override
    public String solve(Node primaryNode) {
        StringBuilder stringBuilder = new StringBuilder();
        addNewOpenState(primaryNode);
        NUMBER_OF_VISITED_STATES++;
        while (!openStateList.isEmpty()) {
            Node childNode = openStateList.poll();
            if (!getClosedStateList().contains(childNode) && childNode != null) {
                if (childNode.getCurrentState().getRecursionDepth() > MAX_ACHIEVED_RECURSION_DEPTH) {
                    MAX_ACHIEVED_RECURSION_DEPTH = childNode.getCurrentState().getRecursionDepth();
                }
                if (childNode.checkIfTargetState(getTargetState())) {
                    NUMBER_OF_PROCESSED_STATES++;
                    while (childNode.getParentNode() != null) {
                        stringBuilder.append(childNode.getOperator());
                        childNode = childNode.getParentNode();
                    }
                    return stringBuilder.reverse().toString();
                }
                addNewClosedState(childNode);
                NUMBER_OF_PROCESSED_STATES++;
                for (Node neighbouringNode : childNode.getAllNeighbours()) {
                    if (!getClosedStateList().contains(neighbouringNode)) {
                        neighbouringNode.getCurrentState().setPathCost(childNode.getCurrentState().getPathCost() + 1);
                        int totalCostValue = neighbouringNode.getCurrentState().calculateTotalCostValue(usedHeuristic);
                        neighbouringNode.getCurrentState().setTotalPathCost(totalCostValue);
                        openStateList.add(neighbouringNode);
                        NUMBER_OF_VISITED_STATES++;
                    }
                }
            }
        }
        return null;
    }
}
