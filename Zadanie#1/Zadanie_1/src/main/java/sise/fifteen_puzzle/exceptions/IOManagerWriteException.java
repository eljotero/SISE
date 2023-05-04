package sise.fifteen_puzzle.exceptions;

public class IOManagerWriteException extends IOManagerGeneralException {
    public IOManagerWriteException(String message) {
        super(message);
    }

    public IOManagerWriteException(String message, Throwable cause) {
        super(message, cause);
    }
}
