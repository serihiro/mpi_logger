from mpi_logger import mpi_logger

logger = mpi_logger.MpiLogger(
    handler_type="file", file_name_prefix="log", file_open_mode="a"
)
print(logger.level)
logger.info("test")
logger.debug("test")
logger.warn("test")
logger.error("test")
