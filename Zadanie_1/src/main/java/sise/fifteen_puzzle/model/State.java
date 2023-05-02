package sise.fifteen_puzzle.model;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

import java.util.Arrays;

public class State implements Comparable<State> {

    private final byte[] arrayOfBlocks;
    private final byte zeroPosition;
    private final int numberOfRows;
    private final int numberOfColumns;
    private int pathCost = 0;
    private final int recursionDepth;

    /*
        @ Constructors:

        @ zeroPosition      -> array index with 0 block
        @ arrayOfBlocks     -> current state of fifteen puzzle
        @ pathCost          -> value of heuristic function in A* algorithm
        @ numberOfRows      -> total number of rows in the puzzle
        @ numberOfColumns   -> total number of columns in the puzzle
        @ RECURSION_DEPTH   -> depth of current state - relative to the depth of starting State
     */

    public State(byte[] arrayOfBlocks, byte zeroPosition, int numberOfRows, int numberOfColumns, int recursionDepth) {
        this.arrayOfBlocks = arrayOfBlocks;
        this.zeroPosition = zeroPosition;
        this.numberOfRows = numberOfRows;
        this.numberOfColumns = numberOfColumns;
        this.recursionDepth = recursionDepth;
    }

    public State(byte[] arrayOfBlocks, byte zeroPosition, int numberOfRows, int numberOfColumns, int pathCost, int recursionDepth) {
        this.arrayOfBlocks = arrayOfBlocks;
        this.zeroPosition = zeroPosition;
        this.numberOfRows = numberOfRows;
        this.numberOfColumns = numberOfColumns;
        this.pathCost = pathCost;
        this.recursionDepth = recursionDepth;
    }

/*
        @ Getters:
     */

    public byte getZeroPosition() {
        return zeroPosition;
    }

    public byte[] getArrayOfBlocks() {
        return arrayOfBlocks;
    }

    public int getPathCost() {
        return pathCost;
    }

    public int getNumberOfRows() {
        return numberOfRows;
    }

    public int getNumberOfColumns() {
        return numberOfColumns;
    }

    public int getRecursionDepth() {
        return recursionDepth;
    }

    /*
        Setters
     */

    public void setPathCost(int pathCost) {
        this.pathCost = pathCost;
    }

    /*
        @ Method: getCertainNeighbour

        @ neighPos -> Neighbour position relative to position of 0 block;

        This method is able to return any instant neighbour of 0 block, depending
        on direction of that neighbour, that is: 'U' for upper neighbour, 'D' for lower
        neighbour, 'L' for neighbour on the left, and 'R' for neighbour on the right.

        This method is only called from Node's getNeighbours, where State is used to
        create new Nodes (that consist of State, operator and parentNode).
     */

    public State getCertainNeighbour(char neighPos) {
        int rowModifier = 0;
        int colModifier = 0;
        switch (neighPos) {
            case 'U' -> rowModifier--;
            case 'D' -> rowModifier++;
            case 'L' -> colModifier--;
            case 'R' -> colModifier++;
            default -> {
                System.out.println(neighPos);
                System.out.println("It is not possible to find given neighbour.");
            }
        }

        byte[] blocksArray = copyArrayOfBlocks();
        int zeroPos = getZeroPosition();
        int columnNumber = ((zeroPos % this.getNumberOfRows()) + colModifier);
        int rowNumber = ((zeroPos / this.getNumberOfColumns()) + rowModifier);
        if (rowNumber >= 0 && rowNumber < this.getNumberOfRows() && columnNumber >= 0 && columnNumber < this.getNumberOfColumns()) {
            int neighbourPosition = (int) (rowNumber * Math.sqrt(this.arrayOfBlocks.length) + columnNumber);
            byte temp = blocksArray[neighbourPosition];
            blocksArray[neighbourPosition] = blocksArray[zeroPos];
            blocksArray[zeroPos] = temp;
            zeroPos = neighbourPosition;
            return new State(blocksArray, (byte) zeroPos, this.getNumberOfRows(), this.getNumberOfColumns(), this.recursionDepth + 1);
        }
        return null;
    }

    public int calculateHeuristicValue(String heuristic) {
        int heuristicFunctionValue = 0;
        if (heuristic.equals("hamm")) {
            for (int i = 0; i < arrayOfBlocks.length; i++) {
                if (arrayOfBlocks[i] != ((i + 1) % arrayOfBlocks.length)) {
                    heuristicFunctionValue++;
                }
            }
        } else if (heuristic.equals("manh")) {
            for (int i = 0; i < arrayOfBlocks.length; i++) {
                int currentRow = i / this.getNumberOfColumns();
                int currentColumn = i % this.getNumberOfRows();
                int currentValue = arrayOfBlocks[i] - 1;
                if (currentValue < 0) {
                    currentValue += arrayOfBlocks.length;
                }
                int requiredRow = currentValue / this.getNumberOfColumns();
                int requiredColumn = currentValue % this.getNumberOfRows();
                heuristicFunctionValue += (Math.abs(requiredRow - currentRow) + Math.abs(requiredColumn - currentColumn));
            }
        } else {
            System.out.println("Unknown heuristic!");
        }
        return heuristicFunctionValue;
    }

    public int calculateTotalCostValue(String heuristic, Node parentNode) {
        int totalCost = parentNode.getCurrentState().getPathCost() + calculateHeuristicValue(heuristic);
        return totalCost;
    }

    public boolean isGoal(State someOtherState) {
        return Arrays.equals(this.arrayOfBlocks, someOtherState.getArrayOfBlocks()) && this.zeroPosition == someOtherState.getZeroPosition() && this.getNumberOfRows() == someOtherState.getNumberOfRows() && this.getNumberOfColumns() == someOtherState.getNumberOfColumns();
    }

    public byte[] copyArrayOfBlocks() {
        byte[] copiedArray = new byte[this.arrayOfBlocks.length];
        System.arraycopy(this.arrayOfBlocks, 0, copiedArray, 0, this.arrayOfBlocks.length);
        return copiedArray;
    }

    public State generateTargetState() {
        byte[] targetState = copyArrayOfBlocks();
        for (int i = 0; i < targetState.length; i++) {
            for (int j = 0; j < targetState.length; j++) {
                if (targetState[i] < targetState[j]) {
                    byte temp = targetState[i];
                    targetState[i] = targetState[j];
                    targetState[j] = temp;
                }
            }
        }
        byte zeroPos = 0;
        for (int i = 0; i < targetState.length; i++) {
            targetState[i] = (byte) ((targetState[i] + 1) % targetState.length);
            if (targetState[i] == 0) {
                zeroPos = (byte) i;
            }
        }
        return new State(targetState, zeroPos, this.getNumberOfRows(), this.getNumberOfColumns(), 0);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (o == null || getClass() != o.getClass()) return false;

        State state = (State) o;

        return new EqualsBuilder().append(zeroPosition, state.zeroPosition).append(this.getNumberOfRows(), state.getNumberOfColumns()).append(numberOfColumns, state.numberOfColumns).append(arrayOfBlocks, state.arrayOfBlocks).isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 37).append(arrayOfBlocks).append(zeroPosition).append(this.getNumberOfRows()).append(this.getNumberOfColumns()).toHashCode();
    }

    @Override
    public int compareTo(State otherState) {
        return this.pathCost - otherState.getPathCost();
    }
}
