package sise.fifteen_puzzle.exceptions;

import java.io.IOException;

public class IOManagerGeneralException extends IOException {
    public IOManagerGeneralException(String message) {
        super(message);
    }

    public IOManagerGeneralException(String message, Throwable cause) {
        super(message, cause);
    }
}
