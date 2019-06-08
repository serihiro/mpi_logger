import logging
from logging import Formatter
from mpi4py import MPI
from mpi_logger.base_formatter import BaseFormatter


class DefaultFormatter(BaseFormatter):
    @staticmethod
    def generate_formatter(comm: MPI.Intracomm) -> Formatter:
        rank = comm.Get_rank()
        hostname = MPI.Get_processor_name()

        return Formatter(
            f"%(asctime)s[{hostname}][{rank}][%(levelname)s] - %(message)s"
        )
