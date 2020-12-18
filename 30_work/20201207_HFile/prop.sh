
#!/bin/bash

# sh prop.sh >pp.log &
echo '===put file=== '
start=$(date +%s)
date "+%Y-%m-%d %H:%M:%S"
hadoop fs -put zw_qfmx.dat /user/fxf/20201207
end=$(date +%s)
date "+%Y-%m-%d %H:%M:%S"
take=$(( end - start ))
echo Time taken to execute commands is ${take} seconds.
echo '===get file=== '
start=$(date +%s)
date "+%Y-%m-%d %H:%M:%S"
hadoop fs -get /user/fxf/20201207/zw_qfmx.dat ./res
end=$(date +%s)
date "+%Y-%m-%d %H:%M:%S"
take=$(( end - start ))
echo Time taken to execute commands is ${take} seconds.

