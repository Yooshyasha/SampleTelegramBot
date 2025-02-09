from loguru import Logger as LoguruLogger

@DeprecationWarning
class Logger(LoguruLogger):
    def __init__(self):
        super().__init__()
