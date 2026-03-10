# Docker Notes

当前版本只用于：

- 发现现有容器环境
- 在用户明确确认容器名后执行 benchmark

不要默认复用未知容器。

检查命令重点：

- `pip list | grep torch_npu`
- `ls -ld /usr/local/Ascend/ascend-toolkit/latest`
- `find /usr/local/Ascend/ascend-toolkit -maxdepth 1 -mindepth 1 -type d | sort`
