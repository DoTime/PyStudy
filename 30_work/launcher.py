from concurrent.futures import ThreadPoolExecutor
import os
import flinkx
import argparse
import statistic
from conf import log,config



def launcher(mode,flinkx_json_dir,max_workers=3):

    files=os.listdir(flinkx_json_dir)

    #声明线程池
    executor = ThreadPoolExecutor(max_workers=max_workers)

    for file_name in files:
        path="{flinkx_json_dir}/{file_name}".format(flinkx_json_dir=flinkx_json_dir,file_name=file_name)
        table_name=file_name[:-5]
        statistic.total+=1
        executor.submit(flinkx.call, mode, table_name, path)

    executor.shutdown(wait=True)
    statistic.print_stat()

    #打印结束符号
    company_code=str(statistic.company_code)
    domain=str(statistic.domain)
    log_dir = os.path.join(config.flinkx_log_dir, company_code)
    success_logger = log.getFileLogger(company_code + "_" + domain + "_success", log_dir)
    success_logger.info("---------------------------  end  ---------------------------------")
    failure_logger = log.getFileLogger(company_code + "_" + domain + "_failure", log_dir)
    failure_logger.info("---------------------------- end  --------------------------------")



if __name__ == "__main__":
    #D:\\flinkx\\config
    parser = argparse.ArgumentParser(description='launcher...')
    parser.add_argument("--mode", type=str, default="local")
    parser.add_argument("--jsondir", type=str)
    parser.add_argument("--workers", type=int,default=3)
    args = parser.parse_args()
    launcher(args.mode,args.jsondir,max_workers=args.workers)