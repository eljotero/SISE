package sise.fifteen_puzzle.model;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

import java.util.HashSet;
import java.util.Set;

public class Node implements Comparable<Node> {

    private final State currentState;
    private final Node parentNode;
    private final char operator;

    /*
        @ Constructor:

        @ currentState  -> current state of puzzle
        @ parentNode    -> state of the puzzle before using operator
        @ operator      -> operation (that is "L", "R", "D" or "U") from parentState to currentState
     */

    public Node(State currentState, Node parentNode, char operator) {
        this.currentState = currentState;
        this.parentNode = parentNode;
        this.operator = operator;
    }

    /*
        @ Getters:
     */

    public Node getParentNode() {
        return parentNode;
    }

    public char getOperator() {
        return operator;
    }

    public State getCurrentState() {
        return currentState;
    }

    /*
        Method to get neighbouring State by moving 0 block
        to direction specified with neighbourPosition.
     */

    public Node getCertainNeighbour(char neighbourPosition) {
        State neighbouringState = this.currentState.getCertainNeighbour(neighbourPosition);
        if (neighbouringState == null) {
            return null;
        } else {
            return new Node(neighbouringState, this, neighbourPosition);
        }
    }

    /*
        Method to get all neighbouring States for current State in Node.
     */

    public Set<Node> getAllNeighbours() {
        State neighbouringState;
        Node childNode;
        Set<Node> neighboursOfCurrentState = new HashSet<>();
        String orderOfNeighbours = "UDRL";
        for (int i = 0; i < orderOfNeighbours.length(); i++) {
            neighbouringState = this.currentState.getCertainNeighbour(orderOfNeighbours.charAt(i));
            if (neighbouringState != null) {
                childNode = new Node(neighbouringState, this, orderOfNeighbours.charAt(i));
                neighboursOfCurrentState.add(childNode);
            }
        }
        return neighboursOfCurrentState;
    }

    /*
        Method used to check, whether this State is the same
        as other given State (the second being targetState).
     */

    public boolean checkIfTargetState(State targetState) {
        return this.currentState.equals(targetState);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (o == null || getClass() != o.getClass()) return false;

        Node node = (Node) o;

        return new EqualsBuilder().append(currentState, node.currentState).isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 37).append(currentState).toHashCode();
    }

    @Override
    public int compareTo(Node otherNode) {
        return this.getCurrentState().compareTo(otherNode.getCurrentState());
    }
}
