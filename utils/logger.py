
import logging
import os

os.makedirs("reports", exist_ok=True)

logging.basicConfig(
    filename="reports/ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)

logger = logging.getLogger(__name__)
