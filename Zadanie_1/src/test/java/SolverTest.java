import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import sise.fifteen_puzzle.additional.IOManager;
import sise.fifteen_puzzle.additional.ParseIO;
import sise.fifteen_puzzle.exceptions.IOManagerReadException;
import sise.fifteen_puzzle.model.Node;
import sise.fifteen_puzzle.model.State;
import sise.fifteen_puzzle.solvers.AStarSolver;
import sise.fifteen_puzzle.solvers.BFSSolver;
import sise.fifteen_puzzle.solvers.DFSSolver;
import sise.fifteen_puzzle.solvers.Solver;

public class SolverTest {

    private static Solver BFS;
    private static Solver DFS;
    private static Solver aStr;
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

        targetState4x4 = readState4x4.generateTargetState();
        targetState3x3 = readState3x3.generateTargetState();
        targetState2x2 = readState2x2.generateTargetState();

        BFS = new BFSSolver(targetState4x4, "LURD");
        DFS = new DFSSolver(targetState4x4, "RDUL");
        aStr = new AStarSolver(targetState4x4, "manh");
    }

    @Test
    public void bfsFindSolution() {
        Node startingNode = new Node(readState4x4, null, ' ');
        String solution = BFS.solve(startingNode);
        System.out.println("Solution: " + solution);
    }

    @Test
    public void dfsFindSolution() {
        Node startingNode = new Node(readState4x4, null, ' ');
        String solution = DFS.solve(startingNode);
        System.out.println("Solution: " + solution);
    }

    @Test
    public void aStrFindSolution() {
        Node startingNode = new Node(readState4x4, null, ' ');
        String solution = aStr.solve(startingNode);
        System.out.println("Solution: " + solution);
    }
}
