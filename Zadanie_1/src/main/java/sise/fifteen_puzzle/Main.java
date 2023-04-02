package sise.fifteen_puzzle;

import sise.fifteen_puzzle.additional.IOManager;
import sise.fifteen_puzzle.additional.ParseIO;
import sise.fifteen_puzzle.exceptions.IOManagerGeneralException;
import sise.fifteen_puzzle.model.Node;
import sise.fifteen_puzzle.model.State;
import sise.fifteen_puzzle.solvers.AStarSolver;
import sise.fifteen_puzzle.solvers.BFSSolver;
import sise.fifteen_puzzle.solvers.DFSSolver;
import sise.fifteen_puzzle.solvers.Solver;

public class Main {

    public static void main(String[] runParameters) throws IOManagerGeneralException {

        String searchAlgorithm = runParameters[0];
        String searchingApproach = runParameters[1];
        String boardSourceFile = runParameters[2];
        String solutionFile = runParameters[3];
        String statsFile = runParameters[4];

        State primaryState = ParseIO.parseInputFile(IOManager.readBytesFromFile(boardSourceFile));
        Node startingNode = new Node(primaryState, null, ' ');
        State targetState = startingNode.getCurrentState().generateTargetState();

        switch (searchAlgorithm) {
            case "bfs":
                Solver bfsSolver = new BFSSolver(targetState, searchingApproach);
                long startTime = System.nanoTime();
                String solution = bfsSolver.solve(startingNode);
                long endTime = System.nanoTime();
                int solutionLength;
                if (solution == null) {
                    solutionLength = -1;
                } else {
                    solutionLength = solution.length();
                }
                int numberOfVisitedStates = Solver.getNumberOfVisitedStates();
                int numberOfProcessedStates = Solver.getNumberOfProcessedStates();
                int maxRecursionDepth = Solver.getMaxAchievedRecursionDepth();
                double totalTime = ((endTime - startTime) / 1000000.0);
                IOManager.writeBytesToFile(ParseIO.parseSolution(solutionLength, solution).getBytes(), solutionFile);
                IOManager.writeBytesToFile(ParseIO.parseStats(solutionLength, numberOfVisitedStates, numberOfProcessedStates,
                        maxRecursionDepth, totalTime).getBytes(), statsFile);
                break;
            case "dfs":
                Solver dfsSolver = new DFSSolver(targetState, searchingApproach);
                startTime = System.nanoTime();
                solution = dfsSolver.solve(startingNode);
                endTime = System.nanoTime();
                if (solution == null) {
                    solutionLength = -1;
                } else {
                    solutionLength = solution.length();
                }
                numberOfVisitedStates = Solver.getNumberOfVisitedStates();
                numberOfProcessedStates = Solver.getNumberOfProcessedStates();
                maxRecursionDepth = Solver.getMaxAchievedRecursionDepth();
                totalTime = ((endTime - startTime) / 1000000.0);
                IOManager.writeBytesToFile(ParseIO.parseSolution(solutionLength, solution).getBytes(), solutionFile);
                IOManager.writeBytesToFile(ParseIO.parseStats(solutionLength, numberOfVisitedStates, numberOfProcessedStates,
                        maxRecursionDepth, totalTime).getBytes(), statsFile);
                break;
            case "astr":
                Solver aStarSolver = new AStarSolver(targetState, searchingApproach);
                startTime = System.nanoTime();
                solution = aStarSolver.solve(startingNode);
                endTime = System.nanoTime();
                if (solution == null) {
                    solutionLength = -1;
                } else {
                    solutionLength = solution.length();
                }
                numberOfVisitedStates = Solver.getNumberOfVisitedStates();
                numberOfProcessedStates = Solver.getNumberOfProcessedStates();
                maxRecursionDepth = Solver.getMaxAchievedRecursionDepth();
                totalTime = ((endTime - startTime) / 1000000.0);
                IOManager.writeBytesToFile(ParseIO.parseSolution(solutionLength, solution).getBytes(), solutionFile);
                IOManager.writeBytesToFile(ParseIO.parseStats(solutionLength, numberOfVisitedStates, numberOfProcessedStates,
                        maxRecursionDepth, totalTime).getBytes(), statsFile);
                break;
            default:
                System.out.println("Search algorithm not implemented!");
        }
    }
}