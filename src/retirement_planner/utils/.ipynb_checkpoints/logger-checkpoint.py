import logging
from retirement_planner.config.setting import settings

def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level=getattr(logging, settings.log_level),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    return logging.getLogger(name)