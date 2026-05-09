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

# Realistic commit messages — rotates through different topics
COMMIT_MESSAGES = [
    "docs: update learning notes on {topic}",
    "feat: add {topic} implementation notes",
    "fix: correct typo in {topic} documentation",
    "refactor: reorganize {topic} notes structure",
    "chore: update {topic} study progress",
    "docs: add {topic} code snippets and examples",
    "feat: document {topic} best practices",
    "fix: update outdated {topic} references",
    "docs: add {topic} architecture analysis",
    "chore: daily {topic} review and cleanup",
    "feat: add {topic} performance benchmark notes",
    "docs: summarize {topic} key takeaways",
    "fix: improve {topic} code examples",
    "refactor: merge duplicate {topic} notes",
    "docs: add {topic} troubleshooting guide",
    "feat: record {topic} experiment results",
    "chore: archive completed {topic} tasks",
    "docs: add {topic} comparison table",
    "fix: resolve inconsistent {topic} naming",
    "feat: add {topic} implementation checklist",
]

TOPICS = [
    "RAG pipeline optimization",
    "GraphRAG entity resolution",
    "MCP server development",
    "Agent memory architecture",
    "LLM evaluation metrics",
    "Knowledge graph construction",
    "FastAPI middleware",
    "Docker deployment workflow",
    "React component patterns",
    "Neo4j query optimization",
    "Prompt engineering techniques",
    "Vector database indexing",
    "Python async programming",
    "TypeScript type system",
    "CI/CD pipeline setup",
    "Redis caching strategies",
    "Elasticsearch mapping design",
    "PyTorch model training",
    "Yolo detection fine-tuning",
    "SpaCy NER customization",
    "LangChain chain composition",
    "SSE streaming implementation",
    "systemd service configuration",
    "Nginx reverse proxy",
    "Git branching strategies",
    "Python packaging with uv",
    "SQL query optimization",
    "REST API design patterns",
    "WebSocket real-time communication",
    "OAuth2 authentication flow",
]

# Realistic log entry templates
LOG_TEMPLATES = [
    "## {date}\n\n- Studied {topic}\n- Key insight: {insight}\n- Next step: {next}\n",
    "## {date}\n\n- Implemented {feature} for {topic}\n- Encountered issue with {issue}, resolved by {solution}\n- Performance improved by ~{percent}%\n",
    "## {date}\n\n- Read paper on {topic}\n- Main takeaway: {takeaway}\n- Will apply to {project} next\n",
    "## {date}\n\n- Refactored {component} in {project}\n- Reduced complexity from O({big_o}) to O({small_o})\n- Tests passing: {tests}\n",
    "## {date}\n\n- Explored {tool} for {topic}\n- Compared with {alternative}: {tool} wins on {reason}\n- Shipped prototype to {project}\n",
]

INSIGHTS = [
    "chunking strategy matters more than embedding model for retrieval quality",
    "graph-based retrieval outperforms pure vector search for multi-hop questions",
    "proper error handling saves 10x debugging time later",
    "incremental updates are crucial for large knowledge graphs",
    "streaming responses dramatically improve user experience in chat UIs",
    "type safety catches bugs early, especially in API contracts",
    "caching at the right layer can reduce latency by 80%",
    "community detection algorithms reveal hidden structure in data",
    "prompt engineering is still the most cost-effective optimization",
    "local-first architecture gives better privacy guarantees",
]

PROJECTS = [
    "ClawScope", "RelationGraph", "SSHFerry", "DayFlow", 
    "daily-log", "GraphRAG pipeline", "MCP toolkit", "Agent framework"
]


def git(cmd):
    """Run a git command in the repo directory."""
    result = subprocess.run(
        f"cd {REPO_DIR} && git {cmd}",
        shell=True, capture_output=True, text=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def generate_log_entry():
    """Generate a realistic-looking daily log entry."""
    today = datetime.now().strftime("%Y-%m-%d")
    template = random.choice(LOG_TEMPLATES)
    
    topic = random.choice(TOPICS)
    feature = random.choice(["connector", "handler", "middleware", "service", "utility", "validator"])
    issue = random.choice(["timeout errors", "memory leak", "race condition", "encoding issue", "type mismatch"])
    solution = random.choice(["adding retry logic", "implementing connection pooling", "using async/await properly", "fixing the serialization layer", "adding proper type hints"])
    tool = random.choice(["Milvus", "ChromaDB", "Qdrant", "Weaviate", "Pinecone", "pgvector"])
    alternative = random.choice(["FAISS", "Annoy", "ScaNN", "Hnswlib"])
    component = random.choice(["router", "model layer", "cache module", "auth middleware", "logger", "config loader"])
    
    return template.format(
        date=today,
        topic=topic,
        feature=feature,
        issue=issue,
        solution=solution,
        tool=tool,
        alternative=alternative,
        component=component,
        insight=random.choice(INSIGHTS),
        next=random.choice(["benchmark with real data", "integrate into production", "write unit tests", "deploy to staging"]),
        project=random.choice(PROJECTS),
        takeaway=f"Key finding: {random.choice(INSIGHTS)}",
        reason=random.choice(["performance", "ease of use", "community support", "documentation quality"]),
        percent=random.randint(15, 40),
        big_o=random.choice(["n²", "n³", "n*log(n)"]),
        small_o=random.choice(["n", "log(n)", "1"]),
        tests=f"{random.randint(45, 200)}/{random.randint(200, 250)} passed",
    )


def main():
    # Ensure repo exists
    if not os.path.exists(REPO_DIR):
        print("❌ Repo directory not found. Clone it first.")
        return

    # Generate today's content
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(REPO_DIR, "log.md")
    
    # Read existing content
    existing = ""
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            existing = f.read()
    
    # Prepend new entry (newest on top)
    new_entry = generate_log_entry()
    existing_clean = existing.replace("# Daily Dev Log 📝\n\n", "")
    content = f"# Daily Dev Log 📝\n\n{new_entry}\n---\n\n{existing_clean}"
    
    with open(log_file, "w") as f:
        f.write(content)
    
    # Also update a stats file
    stats_file = os.path.join(REPO_DIR, "stats.md")
    total_days = content.count("## 20")
    topics_covered = len(set([t for t in TOPICS if t in content]))
    
    with open(stats_file, "w") as f:
        f.write(f"# 📊 Learning Stats\n\n")
        f.write(f"- Total days logged: {total_days}\n")
        f.write(f"- Topics covered: {topics_covered}\n")
        f.write(f"- Last updated: {today}\n")
    
    # Git commit and push
    git("add -A")
    
    commit_msg = random.choice(COMMIT_MESSAGES).format(topic=random.choice(TOPICS))
    git(f'commit -m "{commit_msg}" --allow-empty')
    
    stdout, stderr, code = git("push origin main")
    
    if code == 0:
        print(f"✅ Committed: {commit_msg}")
    else:
        print(f"❌ Push failed: {stderr}")


if __name__ == "__main__":
    main()
