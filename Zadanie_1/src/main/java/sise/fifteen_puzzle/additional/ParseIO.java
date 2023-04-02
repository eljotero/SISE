package sise.fifteen_puzzle.additional;

import sise.fifteen_puzzle.model.State;

import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class ParseIO {

    public static State parseInputFile(byte[] inputByteArray) {
        int iterator = 0;
        int numberOfRows = 0;
        int numberOfColumns = 0;
        // Wyłączone spod parsowania znaki: spacja, powrót karetki, znak nowej linii.
        while (inputByteArray[iterator] != 32 && inputByteArray[iterator] != 13) {
            numberOfRows = numberOfRows * 10 + (inputByteArray[iterator] - 48);
            iterator++;
        }
        iterator += checkByteValue(inputByteArray[iterator]);
        while (inputByteArray[iterator] != 32 && inputByteArray[iterator] != 13) {
            numberOfColumns = numberOfColumns * 10 + (inputByteArray[iterator] - 48);
            iterator++;
        }
        iterator += checkByteValue(inputByteArray[iterator]);
        byte zeroPosition = 0;
        byte[] arrayOfBlocks = new byte[numberOfRows * numberOfColumns];
        for (int i = 0; i < numberOfRows * numberOfColumns;) {
            while (inputByteArray[iterator] != 32 && inputByteArray[iterator] != 13) {
                arrayOfBlocks[i] = (byte) (arrayOfBlocks[i] * 10 + (inputByteArray[iterator] - 48));
                iterator++;
            }
            i++;
            iterator += checkByteValue(inputByteArray[iterator]);
        }
        for (int i = 0; i < arrayOfBlocks.length; i++) {
            if (arrayOfBlocks[i] == 0) {
                zeroPosition = (byte) i;
                break;
            }
        }
        return new State(arrayOfBlocks, zeroPosition, numberOfRows, numberOfColumns, 0);
    }

    private static int checkByteValue(byte byteValue) {
        if (byteValue == 13) {
            return 2;
        } else {
            return 1;
        }
    }

    public static String parseSolution(int numberOfMoves, String pathToTargetState) {
        StringBuilder resultString = new StringBuilder();
        resultString.append(numberOfMoves);
        if (numberOfMoves != -1) {
            resultString.append(System.getProperty("line.separator") + pathToTargetState);
        }
        return resultString.toString();
    }

    public static String parseStats(int numberOfMoves, int visitedStates, int processedStates, int maxRecursionDepth, double lengthOfProcess) {
        StringBuilder resultString = new StringBuilder();
        resultString.append(numberOfMoves);
        if (numberOfMoves != -1) {
            DecimalFormatSymbols decimalFormatSymbols = DecimalFormatSymbols.getInstance();
            decimalFormatSymbols.setDecimalSeparator('.');
            DecimalFormat formatter = new DecimalFormat("0.000", decimalFormatSymbols);
            resultString.append(System.getProperty("line.separator") + visitedStates);
            resultString.append(System.getProperty("line.separator") + processedStates);
            resultString.append(System.getProperty("line.separator") + maxRecursionDepth);
            resultString.append(System.getProperty("line.separator") + formatter.format(lengthOfProcess));
        }
        return resultString.toString();
    }

}
