package sise.fifteen_puzzle.solvers;

import sise.fifteen_puzzle.model.Node;
import sise.fifteen_puzzle.model.State;

import java.util.ArrayDeque;

public class BFSSolver extends Solver {

    private final String lookUpOrder;
    private final ArrayDeque<Node> openStateList = new ArrayDeque<>();

    public BFSSolver(State targetState, String lookUpOrder) {
        super(targetState);
        this.lookUpOrder = lookUpOrder;
    }

    public void addNewOpenState(Node newNode) {
        if (newNode != null) {
            openStateList.add(newNode);
        }
    }

    @Override
    public String solve(Node primaryNode) {
        StringBuilder stringBuilder = new StringBuilder();
        if (primaryNode.getCurrentState().isGoal(getTargetState())) {
            NUMBER_OF_VISITED_STATES++;
            NUMBER_OF_PROCESSED_STATES++;
            return stringBuilder.reverse().toString();
        } else {
            Node startingNode = new Node(primaryNode.getCurrentState(), null, ' ');
            addNewOpenState(startingNode);
            NUMBER_OF_VISITED_STATES++;
            addNewClosedState(startingNode);
            NUMBER_OF_PROCESSED_STATES++;
            while (!openStateList.isEmpty()) {
                Node nodeFromList = openStateList.poll();
                for (int i = 0; i < lookUpOrder.length(); i++) {
                    Node childNode = nodeFromList.getCertainNeighbour(lookUpOrder.charAt(i));
                    if (!getClosedStateList().containsKey(childNode) && childNode != null) {
                        NUMBER_OF_VISITED_STATES++;
                        if (childNode.checkIfTargetState(getTargetState())) {
                            NUMBER_OF_PROCESSED_STATES++;
                            MAX_ACHIEVED_RECURSION_DEPTH = childNode.getCurrentState().getRecursionDepth();
                            while (childNode.getParentNode() != null) {
                                stringBuilder.append(childNode.getOperator());
                                childNode = childNode.getParentNode();
                            }
                            return stringBuilder.reverse().toString();
                        }
                        addNewOpenState(childNode);
                        addNewClosedState(childNode);
                        NUMBER_OF_PROCESSED_STATES++;
                    }
                }
            }
        }
        return null;
    }
}
