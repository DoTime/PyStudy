from conf import log
from conf import config
import os

company_code=None
domain=None
total=0
processing=0
success=0
failure=0
skip=0
nopk=0
empty=0

def print_stat():
    log_dir = os.path.join(config.flinkx_log_dir, company_code)
    logger = log.getFileLogger(company_code + "_" + domain + "_stat", log_dir)
    logger.info("company_code=%s domain=%s total=%d processing=%d success=%d failure=%d skip=%d nopk=%d empty=%d" %(str(company_code),(domain),total,processing,success,failure,skip,nopk,empty))
    logger.info("------------------------------------ end -------------------------------------------")