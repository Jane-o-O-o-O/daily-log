#!/usr/bin/env python3
"""
Daily Green Grid Committer 🌿
Automatically commits realistic dev logs to keep GitHub contribution graph active.
"""

import random
import subprocess
import os
from datetime import datetime

REPO_DIR = "/tmp/daily-log"

# Chinese commit messages — rotates through different topics
COMMIT_MESSAGES = [
    "docs: 更新 {topic} 的学习笔记",
    "feat: 添加 {topic} 的实现思路",
    "fix: 修正 {topic} 文档中的错误",
    "refactor: 整理 {topic} 的笔记结构",
    "chore: 更新 {topic} 学习进度",
    "docs: 补充 {topic} 代码示例",
    "feat: 记录 {topic} 最佳实践",
    "fix: 更新过时的 {topic} 参考资料",
    "docs: 添加 {topic} 架构分析",
    "chore: 每日 {topic} 回顾与整理",
    "feat: 添加 {topic} 性能基准测试笔记",
    "docs: 总结 {topic} 关键要点",
    "fix: 改进 {topic} 代码示例",
    "refactor: 合并重复的 {topic} 笔记",
    "docs: 添加 {topic} 故障排查指南",
    "feat: 记录 {topic} 实验结果",
    "chore: 归档已完成的 {topic} 任务",
    "docs: 添加 {topic} 对比分析表格",
    "fix: 修正 {topic} 命名不一致问题",
    "feat: 添加 {topic} 实现检查清单",
]

TOPICS = [
    "RAG 管道优化",
    "GraphRAG 实体解析",
    "MCP Server 开发",
    "Agent 记忆架构",
    "LLM 评估指标",
    "知识图谱构建",
    "FastAPI 中间件",
    "Docker 部署流程",
    "React 组件模式",
    "Neo4j 查询优化",
    "Prompt 工程技巧",
    "向量数据库索引",
    "Python 异步编程",
    "TypeScript 类型系统",
    "CI/CD 流水线",
    "Redis 缓存策略",
    "Elasticsearch 映射设计",
    "PyTorch 模型训练",
    "YOLO 检测微调",
    "spaCy NER 定制",
    "LangChain 链组合",
    "SSE 流式传输实现",
    "systemd 服务配置",
    "Nginx 反向代理",
    "Git 分支策略",
    "Python 打包与 uv",
    "SQL 查询优化",
    "REST API 设计模式",
    "WebSocket 实时通信",
    "OAuth2 认证流程",
]

INSIGHTS = [
    "分块策略对检索质量的影响比嵌入模型更大",
    "图谱检索在多跳问题上优于纯向量搜索",
    "良好的错误处理能节省10倍的调试时间",
    "增量更新对大型知识图谱至关重要",
    "流式响应能显著提升聊天界面的用户体验",
    "类型安全能在早期发现错误，尤其在 API 契约中",
    "在正确的层级缓存可以降低80%的延迟",
    "社区发现算法能揭示数据中的隐藏结构",
    "Prompt 工程仍然是最具性价比的优化手段",
    "本地优先架构能提供更好的隐私保障",
]

PROJECTS = [
    "ClawScope", "RelationGraph", "SSHFerry", "DayFlow",
    "daily-log", "GraphRAG 管道", "MCP 工具包", "Agent 框架"
]

LOG_TEMPLATES = [
    "## {date}\n\n- 学习了 {topic}\n- 关键洞察：{insight}\n- 下一步：{next}\n",
    "## {date}\n\n- 为 {topic} 实现了 {feature}\n- 遇到 {issue} 问题，通过 {solution} 解决\n- 性能提升约 {percent}%\n",
    "## {date}\n\n- 阅读了 {topic} 相关论文\n- 主要收获：{takeaway}\n- 计划应用到 {project}\n",
    "## {date}\n\n- 重构了 {project} 中的 {component}\n- 复杂度从 O({big_o}) 优化到 O({small_o})\n- 测试通过：{tests}\n",
    "## {date}\n\n- 探索了 {tool} 用于 {topic}\n- 与 {alternative} 对比：{tool} 在 {reason} 方面更优\n- 已将原型部署到 {project}\n",
]


def git(cmd):
    result = subprocess.run(
        f"cd {REPO_DIR} && git {cmd}",
        shell=True, capture_output=True, text=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def generate_log_entry():
    today = datetime.now().strftime("%Y-%m-%d")
    template = random.choice(LOG_TEMPLATES)
    topic = random.choice(TOPICS)
    feature = random.choice(["连接器", "处理器", "中间件", "服务层", "工具函数", "验证器"])
    issue = random.choice(["超时错误", "内存泄漏", "竞态条件", "编码问题", "类型不匹配"])
    solution = random.choice(["添加重试机制", "实现连接池", "正确使用 async/await", "修复序列化层", "添加类型提示"])
    tool = random.choice(["Milvus", "ChromaDB", "Qdrant", "Weaviate", "Pinecone", "pgvector"])
    alternative = random.choice(["FAISS", "Annoy", "ScaNN", "Hnswlib"])
    component = random.choice(["路由器", "模型层", "缓存模块", "认证中间件", "日志器", "配置加载器"])

    return template.format(
        date=today, topic=topic, feature=feature, issue=issue, solution=solution,
        tool=tool, alternative=alternative, component=component,
        insight=random.choice(INSIGHTS),
        next=random.choice(["用真实数据做基准测试", "集成到生产环境", "编写单元测试", "部署到预发布环境"]),
        project=random.choice(PROJECTS),
        takeaway=f"关键发现：{random.choice(INSIGHTS)}",
        reason=random.choice(["性能", "易用性", "社区支持", "文档质量"]),
        percent=random.randint(15, 40),
        big_o=random.choice(["n²", "n³", "n*log(n)"]),
        small_o=random.choice(["n", "log(n)", "1"]),
        tests=f"{random.randint(45, 200)}/{random.randint(200, 250)} 通过",
    )


def main():
    if not os.path.exists(REPO_DIR):
        print("❌ 仓库目录不存在，请先 clone")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(REPO_DIR, "log.md")

    existing = ""
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            existing = f.read()

    new_entry = generate_log_entry()
    existing_clean = existing.replace("# 每日开发日志 📝\n\n", "")
    content = f"# 每日开发日志 📝\n\n{new_entry}\n---\n\n{existing_clean}"

    with open(log_file, "w") as f:
        f.write(content)

    stats_file = os.path.join(REPO_DIR, "stats.md")
    total_days = content.count("## 20")
    topics_covered = len(set([t for t in TOPICS if t in content]))

    with open(stats_file, "w") as f:
        f.write(f"# 📊 学习统计\n\n")
        f.write(f"- 已记录天数：{total_days}\n")
        f.write(f"- 已覆盖主题：{topics_covered}\n")
        f.write(f"- 最后更新：{today}\n")

    git("add -A")
    commit_msg = random.choice(COMMIT_MESSAGES).format(topic=random.choice(TOPICS))
    git(f'commit -m "{commit_msg}" --allow-empty')

    stdout, stderr, code = git("push origin main")

    if code == 0:
        print(f"✅ 已提交：{commit_msg}")
    else:
        print(f"❌ Push 失败：{stderr}")


if __name__ == "__main__":
    main()
