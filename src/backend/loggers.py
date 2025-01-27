from functools import wraps
from logging import Logger
from time import time
from typing import Any

from utils.logging import CategoryLogger, DefaultLogger

# Test logger
test_logger: Logger = CategoryLogger.get_logger('test', 'test')

# Default logger
logger: Logger = DefaultLogger.get_logger('default')

# Task runner logger
task_runner_logger: Logger = DefaultLogger.get_logger('task')

# Logger for gRPC calls
rpc_logger: Logger = CategoryLogger.get_logger('grpc', 'grpc')

# Loggers for library's internal operations
lib_manager_logger: Logger = CategoryLogger.get_logger('lib', 'lib_manager')
lib_logger: Logger = CategoryLogger.get_logger('lib', 'lib')
doc_lib_logger: Logger = CategoryLogger.get_logger('lib', 'doc_lib')
image_lib_logger: Logger = CategoryLogger.get_logger('lib', 'img_lib')

# Loggers for embedding process
doc_embedder_logger: Logger = CategoryLogger.get_logger('embedder', 'doc_embedder')
img_embedder_logger: Logger = CategoryLogger.get_logger('embedder', 'img_embedder')

# Loggers for DBs
db_logger: Logger = DefaultLogger.get_logger('db')
vector_db_logger: Logger = DefaultLogger.get_logger('vector_db')


def log_time_cost(start_log: str, end_log: str, LOGGER: Logger = logger):
    """Decorator for automatically logging execution time cost
    """
    def wrapper(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            LOGGER.debug(start_log)
            start: float = time()
            try:
                result: Any = func(*args, **kwargs)
                time_taken: float = time() - start
                LOGGER.debug(f'{end_log}, cost: {time_taken:.2f}s')
                return result
            except Exception as e:
                time_taken: float = time() - start
                LOGGER.error(f'{end_log} with error, cost: {time_taken:.2f}s, error: {e}')
                raise e
        return wrapper_func
    return wrapper
