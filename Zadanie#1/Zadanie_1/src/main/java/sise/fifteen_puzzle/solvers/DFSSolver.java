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
        CURRENT_RECURSION_DEPTH++;
        if (CURRENT_RECURSION_DEPTH > MAX_ACHIEVED_RECURSION_DEPTH) {
            MAX_ACHIEVED_RECURSION_DEPTH = CURRENT_RECURSION_DEPTH;
        }
        if (primaryNode.getCurrentState().isGoal(getTargetState())) {
            NUMBER_OF_VISITED_STATES++;
            NUMBER_OF_PROCESSED_STATES++;
            if (primaryNode.getParentNode() == null) {
                return stringBuilder.reverse().toString();
            } else {
                return "END";
            }
        } else {
            NUMBER_OF_VISITED_STATES++;
            addNewClosedState(primaryNode);
            NUMBER_OF_PROCESSED_STATES++;
            for (int i = 0; i < lookUpOrder.length(); i++) {
                Node childNode = primaryNode.getCertainNeighbour(lookUpOrder.charAt(i));
                if (!getClosedStateList().contains(childNode) && childNode != null && CURRENT_RECURSION_DEPTH < MAX_RECURSION_DEPTH) {
                    if (Objects.equals(solve(childNode), "END")) {
                        stringBuilder.append(childNode.getOperator());
                        if (childNode.getParentNode().getParentNode() == null) {
                            return stringBuilder.reverse().toString();
                        } else {
                            return "END";
                        }
                    } else {
                        CURRENT_RECURSION_DEPTH--;
                        getClosedStateList().remove(childNode);
                    }
                }
            }
        }
        return null;
    }
}
