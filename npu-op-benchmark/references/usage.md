# Usage Guide

执行顺序必须按下面流程进行：

1. 先要求使用者提供服务器 IP、账号、密码；如果不提供，直接中断。
2. 询问使用者是否有 CANN、torch 版本要求。
3. 如果使用者没有明确拒绝 conda 方案，先检查服务器上是否存在具备 torch 和 CANN 的 conda 环境。
4. 如果使用者给出了版本要求，则按版本要求寻找 conda 环境；如果没给版本要求，则返回可用 conda 环境及版本信息供使用者确认。
5. 明确询问使用者是否要使用 conda 环境，以及使用哪个 conda 环境名；如果使用服务器 conda，必须由使用者明确给出 conda 环境名。
6. 如果使用者不想使用 conda，再寻找符合条件的容器，返回容器名和版本信息让使用者选择。
7. 如果容器和 conda 都不选择，直接中断。
8. 询问使用者提供算子名，并询问是否提供额外测试用例。
9. 如果使用者提供额外用例，优先基于该用例设计测试 demo。
10. 如果没有提供额外用例，则由 agent 按目标算子的性能测试原则自行设计 demo；当前仓库中的 `repeat_interleave` 相关脚本和配置只是示例，不代表只支持测试 `repeat_interleave`。
11. demo 设计完成后，先把 demo 方案返回给使用者。
12. 在用户确认的 conda 或容器环境中执行测试。
13. 如果环境不满足要求，或算子执行时报环境错误，立即停止并要求使用者提供新的环境。

结果返回应包含：

- `CANN version`
- `torch version`
- `torch_npu version`
- `test environment`
- `test target`
- `test method`
- `tensor shape`
- `demo code`
- `performance data`
