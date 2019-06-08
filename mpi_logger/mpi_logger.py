import logging
from logging import (
    getLogger,
    Formatter,
    StreamHandler,
    FileHandler,
    Handler,
    getLevelName,
)
from mpi4py import MPI
from mpi_logger.default_formatter import DefaultFormatter
from mpi_logger.base_formatter import BaseFormatter


class MpiLogger:
    def __init__(
        self,
        handler_type: str = "file",
        log_level: int = logging.DEBUG,
        formatter: BaseFormatter = DefaultFormatter,
        **handler_options,
    ):
        self._comm = MPI.COMM_WORLD

        formatter = formatter.generate_formatter(self._comm)
        handler = self._generate_handler(type=handler_type, **handler_options)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)

        self._logger = getLogger("MpiLogger")
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(handler)

    def info(self, message):
        return self._logger.info(message)

    def debug(self, message):
        return self._logger.debug(message)

    def warn(self, message):
        return self._logger.warn(message)

    def error(self, message):
        return self._logger.error(message)

    @property
    def level(self):
        return getLevelName(self._logger.getEffectiveLevel())

    def _generate_handler(self, type: str = "stream", **options) -> Handler:
        if type == "file":
            return FileHandler(
                f"{options['file_name_prefix']}.{self._comm.Get_rank()}",
                options["file_open_mode"],
            )
        elif type == "stream":
            return StreamHandler()
        else:
            raise Exception(f"Unknown handler type:{type}")


if __name__ == "__main__":
    logger = MpiLogger(handler_type="file", file_name_prefix="log", file_open_mode="a")
    logger.info("test")
    logger.debug("test")
    logger.warn("test")
    logger.error("test")
