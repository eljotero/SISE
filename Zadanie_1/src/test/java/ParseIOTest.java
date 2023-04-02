import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import sise.fifteen_puzzle.additional.IOManager;
import sise.fifteen_puzzle.additional.ParseIO;
import sise.fifteen_puzzle.exceptions.IOManagerReadException;
import sise.fifteen_puzzle.model.State;

public class ParseIOTest {

    /*
        Test sprawdzajacy poprawność wczytywania układanki o wymiarach 4 x 4 z pliku.
     */
    @Test
    public void read4By4ArrayOfBlocksFromFile() throws IOManagerReadException {
        String fileName = "4x4_01_00001.txt";
        byte[] readBytes = IOManager.readBytesFromFile(fileName);
        byte[] arrayOfBlocksInFile = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12};
        State stateInFile = new State(arrayOfBlocksInFile, (byte) 11, 4, 4, 0);
        State readState = ParseIO.parseInputFile(readBytes);
        assertEquals(stateInFile, readState);
    }

    /*
        Test sprawdzajacy poprawność wczytywania układanki o wymiarach 3 x 3 z pliku.
     */
    @Test
    public void read3By3ArrayOfBlocksFromFile() throws IOManagerReadException {
        String fileName = "3x3_01_00001.txt";
        byte[] readBytes = IOManager.readBytesFromFile(fileName);
        byte[] arrayOfBlocksInFile = {1, 2, 3, 4, 5, 0, 7, 8, 6};
        State stateInFile = new State(arrayOfBlocksInFile, (byte) 5, 3, 3, 0);
        State readState = ParseIO.parseInputFile(readBytes);
        assertEquals(stateInFile, readState);
    }

    /*
        Test sprawdzajacy poprawność wczytywania układanki o wymiarach 2 x 2 z pliku.
     */
    @Test
    public void read2By2ArrayOfBlocksFromFile() throws IOManagerReadException {
        String fileName = "2x2_01_00001.txt";
        byte[] readBytes = IOManager.readBytesFromFile(fileName);
        byte[] arrayOfBlocksInFile = {1, 0, 3, 2};
        State stateInFile = new State(arrayOfBlocksInFile, (byte) 1, 2, 2, 0);
        State readState = ParseIO.parseInputFile(readBytes);
        assertEquals(stateInFile, readState);
    }
}
