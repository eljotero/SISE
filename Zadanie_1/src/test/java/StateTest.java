import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import sise.fifteen_puzzle.additional.IOManager;
import sise.fifteen_puzzle.additional.ParseIO;
import sise.fifteen_puzzle.exceptions.IOManagerReadException;
import sise.fifteen_puzzle.model.State;

public class StateTest {

    private static State readState4x4;
    private static State readState3x3;
    private static State readState2x2;
    private static State targetState4x4;
    private static State targetState3x3;
    private static State targetState2x2;

    @BeforeAll
    public static void init() throws IOManagerReadException {
        String fileName = "4x4_01_00001.txt";
        byte[] readBytes = IOManager.readBytesFromFile(fileName);
        readState4x4 = ParseIO.parseInputFile(readBytes);
        fileName = "3x3_01_00001.txt";
        readBytes = IOManager.readBytesFromFile(fileName);
        readState3x3 = ParseIO.parseInputFile(readBytes);
        fileName = "2x2_01_00001.txt";
        readBytes = IOManager.readBytesFromFile(fileName);
        readState2x2 = ParseIO.parseInputFile(readBytes);

        byte[] targetArrayOfBlocks4x4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0};
        byte[] targetArrayOfBlocks3x3 = {1, 2, 3, 4, 5, 6, 7, 8, 0};
        byte[] targetArrayOfBlocks2x2 = {1, 2, 3, 0};
        targetState4x4 = new State(targetArrayOfBlocks4x4, (byte) 15, 4, 4, 0);
        targetState3x3 = new State(targetArrayOfBlocks3x3, (byte) 8, 3, 3, 0);
        targetState2x2 = new State(targetArrayOfBlocks2x2, (byte) 3, 2, 2, 0);
    }

    @Test
    public void getZeroPositionTest() {
        int zeroPos = readState4x4.getZeroPosition();
        int actualZeroPosition = 10;
        assertEquals(actualZeroPosition, zeroPos);
    }

    @Test
    public void getArrayOfBlocksTest() {
        byte[] arrayOfBlocks = readState4x4.getArrayOfBlocks();
        byte[] actualArrayOfBlocks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 13, 14, 15, 12};
        assertArrayEquals(arrayOfBlocks, actualArrayOfBlocks);
    }

    /*
        Test for getting certain neighbouring State for 4 x 4
        array of blocks.
     */

    @Test
    public void getUpper4x4NeighbourTest() {
        State upperNeighState = readState4x4.getCertainNeighbour('U');
        byte[] newArrayOfBlocks = readState4x4.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState4x4.getZeroPosition()];
        newArrayOfBlocks[readState4x4.getZeroPosition()] = newArrayOfBlocks[6];
        newArrayOfBlocks[6] = temp;
        byte currentZeroPos = 6;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 4, 4, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getLower4x4NeighboursTest() {
        State upperNeighState = readState4x4.getCertainNeighbour('D');
        byte[] newArrayOfBlocks = readState4x4.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState4x4.getZeroPosition()];
        newArrayOfBlocks[readState4x4.getZeroPosition()] = newArrayOfBlocks[14];
        newArrayOfBlocks[14] = temp;
        byte currentZeroPos = 14;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 4, 4, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getLeft4x4NeighboursTest() {
        State upperNeighState = readState4x4.getCertainNeighbour('L');
        byte[] newArrayOfBlocks = readState4x4.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState4x4.getZeroPosition()];
        newArrayOfBlocks[readState4x4.getZeroPosition()] = newArrayOfBlocks[9];
        newArrayOfBlocks[9] = temp;
        byte currentZeroPos = 9;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 4, 4, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getRight4x4NeighbourTest() {
        State upperNeighState = readState4x4.getCertainNeighbour('R');
        byte[] newArrayOfBlocks = readState4x4.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState4x4.getZeroPosition()];
        newArrayOfBlocks[readState4x4.getZeroPosition()] = newArrayOfBlocks[11];
        newArrayOfBlocks[11] = temp;
        byte currentZeroPos = 11;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 4, 4, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

     /*
        Test for getting certain neighbouring State for 3 x 3
        array of blocks.
     */

    @Test
    public void getUpper3x3NeighbourTest() {
        State upperNeighState = readState3x3.getCertainNeighbour('U');
        byte[] newArrayOfBlocks = readState3x3.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState3x3.getZeroPosition()];
        newArrayOfBlocks[readState3x3.getZeroPosition()] = newArrayOfBlocks[2];
        newArrayOfBlocks[2] = temp;
        byte currentZeroPos = 2;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 3, 3, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getLower3x3NeighboursTest() {
        State upperNeighState = readState3x3.getCertainNeighbour('D');
        byte[] newArrayOfBlocks = readState3x3.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState3x3.getZeroPosition()];
        newArrayOfBlocks[readState3x3.getZeroPosition()] = newArrayOfBlocks[8];
        newArrayOfBlocks[8] = temp;
        byte currentZeroPos = 8;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 3, 3, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getLeft3x3NeighboursTest() {
        State upperNeighState = readState3x3.getCertainNeighbour('L');
        byte[] newArrayOfBlocks = readState3x3.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState3x3.getZeroPosition()];
        newArrayOfBlocks[readState3x3.getZeroPosition()] = newArrayOfBlocks[4];
        newArrayOfBlocks[4] = temp;
        byte currentZeroPos = 4;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 3, 3, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getRight3x3NeighbourTest() {
        State upperNeighState = readState3x3.getCertainNeighbour('R');
        assertNull(upperNeighState);
    }

     /*
        Test for getting certain neighbouring State for 2 x 2
        array of blocks.
     */

    @Test
    public void getUpper2x2NeighbourTest() {
        State upperNeighState = readState2x2.getCertainNeighbour('U');
        assertNull(upperNeighState);
    }

    @Test
    public void getLower2x2NeighboursTest() {
        State upperNeighState = readState2x2.getCertainNeighbour('D');
        byte[] newArrayOfBlocks = readState2x2.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState2x2.getZeroPosition()];
        newArrayOfBlocks[readState2x2.getZeroPosition()] = newArrayOfBlocks[3];
        newArrayOfBlocks[3] = temp;
        byte currentZeroPos = 3;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 2, 2, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getLeft2x2NeighboursTest() {
        State upperNeighState = readState2x2.getCertainNeighbour('L');
        byte[] newArrayOfBlocks = readState2x2.copyArrayOfBlocks();
        byte temp = newArrayOfBlocks[readState2x2.getZeroPosition()];
        newArrayOfBlocks[readState2x2.getZeroPosition()] = newArrayOfBlocks[0];
        newArrayOfBlocks[0] = temp;
        byte currentZeroPos = 0;
        State predictedUpperNeighState = new State(newArrayOfBlocks, currentZeroPos, 2, 2, 0);
        assertEquals(predictedUpperNeighState, upperNeighState);
    }

    @Test
    public void getRight2x2NeighbourTest() {
        State upperNeighState = readState2x2.getCertainNeighbour('R');
        assertNull(upperNeighState);
    }

    /*
        Test for checking whether current State is target State.
     */

    @Test
    public void checkIfTargetState4x4Positive() {
        assertTrue(targetState4x4.isGoal(targetState4x4));
    }

    @Test
    public void checkIfTargetState4x4Negative() {
        assertFalse(readState4x4.isGoal(targetState4x4));
    }

    @Test
    public void checkIfTargetState3x3Positive() {
        assertTrue(targetState3x3.isGoal(targetState3x3));
    }

    @Test
    public void checkIfTargetState3x3Negative() {
        assertFalse(readState3x3.isGoal(targetState3x3));
    }

    @Test
    public void checkIfTargetState2x2Positive() {
        assertTrue(targetState2x2.isGoal(targetState2x2));
    }

    @Test
    public void checkIfTargetState2x2Negative() {
        assertFalse(readState2x2.isGoal(targetState2x2));
    }

    @Test
    public void generateTargetArrayFor4x4() {
        State targetState = readState4x4.generateTargetState();
        for (byte oneByte : targetState.getArrayOfBlocks()) {
            System.out.print(oneByte + " ");

        }
        assertEquals(targetState, targetState4x4);
    }

    @Test
    public void generateTargetArrayFor4x3() throws IOManagerReadException {
        String fileName = "4x3_01_00001.txt";
        State readState = ParseIO.parseInputFile(IOManager.readBytesFromFile(fileName));
        byte[] expectedTargetArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0};
        State expectedState = new State(expectedTargetArray, (byte) 11, 4, 3, 0);
        State actualState = readState.generateTargetState();
        assertEquals(actualState, expectedState);
    }
}
