from loguru import logger

logger.add(
    "logs/farmaciapos.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

app_logger = logger