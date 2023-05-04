package sise.fifteen_puzzle.exceptions;

public class IOManagerReadException extends IOManagerGeneralException {
    public IOManagerReadException(String message) {
        super(message);
    }

    public IOManagerReadException(String message, Throwable cause) {
        super(message, cause);
    }
}
