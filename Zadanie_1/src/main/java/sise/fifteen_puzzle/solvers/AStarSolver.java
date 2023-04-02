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
        setNumberOfVisitedStates(getNumberOfVisitedStates() + 1);
        while (!openStateList.isEmpty()) {
            Node childNode = openStateList.poll();
            if (!getClosedStateList().contains(childNode) && childNode != null) {
                if (childNode.checkIfTargetState(getTargetState())) {
                    setNumberOfProcessedStates(getNumberOfProcessedStates() + 1);
                    setMaxAchievedRecursionDepth(childNode.getCurrentState().getRecursionDepth());
                    while (childNode.getParentNode() != null) {
                        stringBuilder.append(childNode.getOperator());
                        childNode = childNode.getParentNode();
                    }
                    return stringBuilder.reverse().toString();
                }
                addNewClosedState(childNode);
                setNumberOfProcessedStates(getNumberOfProcessedStates() + 1);
                for (Node neighbouringNode : childNode.getAllNeighbours()) {
                    int totalCostValue = neighbouringNode.getCurrentState().calculateTotalCostValue(usedHeuristic);
                    neighbouringNode.getCurrentState().setPathCost(totalCostValue);
                    openStateList.add(neighbouringNode);
                    setNumberOfVisitedStates(getNumberOfVisitedStates() + 1);
                }
            }
        }
        return null;
    }
}
