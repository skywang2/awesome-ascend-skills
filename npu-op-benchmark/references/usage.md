# Usage Guide

执行顺序：

1. 先检查现有环境。
2. 先问使用者是提供 demo 还是由 AI 生成 demo。
3. 若容器满足条件，报告容器名，等待确认。
4. 确认后执行 benchmark。
5. 如环境不满足或算子报环境错误，停止并要求使用者提供新环境。

结果返回应包含：

- `CANN version`
- `torch version`
- `torch_npu version`
- `test target`
- `test method`
- `tensor shape`
- `demo code`
- `performance data`
