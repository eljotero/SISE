package sise.fifteen_puzzle.solvers;

import sise.fifteen_puzzle.model.Node;
import sise.fifteen_puzzle.model.State;

import java.util.Objects;

public class DFSSolver extends Solver {

    private final String lookUpOrder;
    private final StringBuilder stringBuilder = new StringBuilder();
    private final static int MAX_RECURSION_DEPTH = 25;

    public DFSSolver(State targetState, String lookUpOrder) {
        super(targetState);
        this.lookUpOrder = lookUpOrder;
    }

    @Override
    public String solve(Node primaryNode) {
        setCurrentRecursionDepth(getCurrentRecursionDepth() + 1);
        if (getCurrentRecursionDepth() > getMaxAchievedRecursionDepth()) {
            setMaxAchievedRecursionDepth(getCurrentRecursionDepth());
        }
        setNumberOfVisitedStates(getNumberOfVisitedStates() + 1);
        if (primaryNode.getCurrentState().isGoal(getTargetState())) {
            setNumberOfProcessedStates(getNumberOfProcessedStates() + 1);
            if (primaryNode.getParentNode() == null) {
                return stringBuilder.reverse().toString();
            } else {
                return "END";
            }
        } else {
            addNewClosedState(primaryNode);
            setNumberOfProcessedStates(getNumberOfProcessedStates() + 1);
            for (int i = 0; i < lookUpOrder.length(); i++) {
                // TODO: Check if childNode does not change algorithm in any way.
                Node childNode = primaryNode.getCertainNeighbour(lookUpOrder.charAt(i));
                if (!getClosedStateList().contains(childNode) && childNode != null && getCurrentRecursionDepth() < MAX_RECURSION_DEPTH) {
                    if (Objects.equals(solve(childNode), "END")) {
                        stringBuilder.append(childNode.getOperator());
                        if (childNode.getParentNode().getParentNode() == null) {
                            return stringBuilder.reverse().toString();
                        } else {
                            return "END";
                        }
                    } else {
                        setCurrentRecursionDepth(getCurrentRecursionDepth() - 1);
                    }
                }
            }
        }
        return null;
    }
}
