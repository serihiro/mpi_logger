import logging
from logging import Formatter
from mpi4py import MPI


class BaseFormatter:
    @staticmethod
    def generate_formatter(comm: MPI.Intracomm) -> Formatter:
        raise NotImplementedError()
