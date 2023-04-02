package sise.fifteen_puzzle.additional;

import sise.fifteen_puzzle.exceptions.IOManagerReadException;
import sise.fifteen_puzzle.exceptions.IOManagerWriteException;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class IOManager {

    public static void writeBytesToFile(byte[] bytesToBeWrittenToFile, String fileName) throws IOManagerWriteException {
        try (FileOutputStream fileOutStream = new FileOutputStream(fileName)) {
            fileOutStream.write(bytesToBeWrittenToFile);
        } catch (IOException ioException) {
            throw new IOManagerWriteException("Nie powiodło się wykonanie operacji zapisu.", ioException);
        }
    }

    public static byte[] readBytesFromFile(String fileName) throws IOManagerReadException {
        byte[] readBytesFromFile;
        try (FileInputStream fileInStream = new FileInputStream(fileName)) {
            readBytesFromFile = fileInStream.readAllBytes();
            return readBytesFromFile;
        } catch (IOException ioException) {
            throw new IOManagerReadException("Nie powiodło się wykonanie operacji odczytu.", ioException);
        }
    }
}
