# CANN Version Guide

当前版本只检查，不安装，不切换，不修复。

判断规则：

1. 看 `/usr/local/Ascend/ascend-toolkit` 下是否存在目标版本目录。
2. 执行 `ls -ld /usr/local/Ascend/ascend-toolkit/latest`。
3. 如果 `latest` 是目录而非软链，再看同级目录列表并如实返回。
