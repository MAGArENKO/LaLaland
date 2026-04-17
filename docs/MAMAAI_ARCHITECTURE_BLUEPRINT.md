# Architectural Blueprint for MamaAI Agency: FinOps-Optimized Multi-Agent System

## I. Executive Summary and Competitive Strategy

### 1.1. Strategic Overview: Achieving Competitive Advantage with Low Capital

The design of the MamaAI Agency system architecture is fundamentally a financial strategy aimed at securing a structural competitive advantage through aggressive cost management. The primary goal is to minimize starting capital expenditure (CapEx) while dramatically controlling and reducing long-term operational expenditure (OpEx), specifically targeting the variable, unpredictable costs associated with large language model (LLM) inference.

**The FinOps Mandate**: Convert unpredictable, usage-based variable OpEx (the "pay-per-token" model) into manageable, fixed CapEx through strategic self-hosting.

**LLM Hybrid Strategy** — A tiered approach:
- **Open-Source Models (Workhorses)**: DeepSeek-R1, Llama 3 via Ollama — $0.00/token post-CapEx
- **Proprietary Value APIs (Specialists)**: GPT-4o-mini, Gemini Flash — for critical, low-volume tasks

### 1.2. Core FinOps Thesis: CapEx Investment in Self-Hosting for Sustained OpEx Savings

- Self-hosting via Ollama: projected $50,000+ annual savings vs cloud APIs
- Low-CapEx GPU strategy: 2x NVIDIA P40 (24GB VRAM each, ~$300 each) for large quantized models
- Full data privacy and sovereignty

---

## II. Core System Architecture

### 2.1. System Overview (MCP, Agencies, Communication Bus)

- **Master Control Program (MCP)**: Goal decomposition, strategic planning, task delegation
- **Specialized Agencies**: Software Dev, Marketing, Research, Blender 3D — each as autonomous FastAPI microservices
- **Communication Bus**: High-speed, schema-enforced, real-time (gRPC/Protobuf)

### 2.2. Agent Orchestration: CrewAI + LangGraph Hybrid

- **LangGraph**: Stateful orchestration — persistence, branching, cyclical workflows, human-in-the-loop
- **CrewAI**: Rapid execution — role assignment, task delegation, collaborative sub-tasks
- **Hybrid rationale**: LangGraph for reliability + state; CrewAI for speed + simplicity

### 2.3. Context Engineering

- Avoid "shoveling" raw data into ever-larger context windows
- Implement active filtering, summarization, RAG
- Minimize prompt size → reduces time-to-first-token → cuts cumulative latency
- Token streaming for perceived responsiveness

### 2.4. Structured Output and Self-Correction Loops

- All agent outputs via Pydantic models / JSON schemas
- Self-correction (Reflection): detect errors → evaluate → log → retry
- Boosts success rate from ~54% to ~82% for complex tasks

---

## III. LLM Strategy: Maximum Performance, Minimum Cost

### LLM Cost-Performance Matrix

| Model Tier | Model | Input $/1M tokens | Output $/1M tokens | Primary Use Case |
|---|---|---|---|---|
| Open-Source Leader | DeepSeek-R1 API | ~$0.27 | ~$1.10 | Software Dev, Research |
| Self-Hosted Core | Llama 3 (Ollama) | $0.00 | $0.00 | Internal RAG, Automation |
| Value API | GPT-4o-mini | $0.15 | $0.60 | Marketing Copy, Review |
| Premium Reasoning | Claude 3.7 Sonnet | $3.00 | $15.00 | Critical Code Review |

### Self-Hosting: Ollama + Modelfile Customization

- OpenAI-compatible API for seamless switching
- Custom Modelfiles for domain-specific variants (Blender scripting, marketing styles)

---

## IV. Infrastructure, Communication, and FinOps

### 4.1. K3s on VPS/EC2 (No Managed Kubernetes)

- K3s: single binary (<100MB), SQLite backend, built-in Traefik
- Deploy on t3.medium EC2/VPS — avoids EKS/GKE/AKS control plane fees

### 4.2. GPU Strategy

- **Dedicated**: P40/V100 for 24/7 Ollama inference ($0/token)
- **Elastic**: Vast.ai Serverless for burst (renders, fine-tuning)

### 4.3. Internal Communication: gRPC + Protobuf

- Binary serialization (smaller, faster than JSON)
- HTTP/2 with bi-directional streaming
- Compounding efficiency across all multi-step workflows

### 4.4. Observability: Prometheus/Grafana + LLM Gateway

- LiteLLM gateway: intercepts all LLM calls, exposes /metrics
- Per-agent tagging (agent_id, agency_name)
- Grafana dashboards: token usage, cost, latency per agent
- Budget caps and rate limiting at gateway layer

---

## V. Data Architecture

### 5.1. PostgreSQL + PgBouncer

- Single PostgreSQL instance with Transaction Pooling via PgBouncer
- Multi-agency data separation via PostgreSQL schemas (not multiple instances)

### 5.2. Qdrant for RAG

- Industry-leading RPS, 3ms latency at 1M vectors
- Vector quantization: up to 30x memory savings
- Memory-mapping: hot data in RAM, cold data on disk

---

## VI. Specialized Agency Blueprints

### 6.1. Software Development Agency
- **Model**: DeepSeek-R1 Coder
- **Workflow**: Task decomposition → code generation → execution → self-correction
- **Output**: Structured (Pydantic models)

### 6.2. Research Agency
- **Pipeline**: Scrapy + scrapy-playwright for dynamic JS scraping
- **Zero-cost**: no third-party scraping APIs

### 6.3. Blender 3D Agency
- **Procedural generation**: Geometry Nodes for environments/assets ($0/generation)
- **Textures**: Self-hosted Stable Diffusion (AUTOMATIC1111) — zero marginal cost
- **Eliminates**: human labor costs + texture licensing costs

### 6.4. Marketing Agency
- **Model**: GPT-4o-mini / Gemini Flash (value tier)
- **RAG**: Brand guidelines, historical messaging, demographics from Qdrant
- **Reflection**: Claude 3.7 Sonnet for high-stakes campaigns

---

## VII. Scaling Roadmap

### Phase 1: MVP
- K3s cluster + single PostgreSQL + PgBouncer
- 2x P40 GPUs for Ollama
- DeepSeek-R1 API for complex tasks

### Phase 2: Performance
- PgBouncer tuning for agentic load
- Qdrant quantization + memory-mapping
- Migrate all high-volume tasks to self-hosted Ollama

### Phase 3: Scale
- GPU upgrades (V100/H100) only when needed
- Vast.ai Serverless for burst compute
- Prometheus/Grafana FinOps enforcement

---

## VIII. Cost Comparison

| Component | Managed Cloud | MamaAI Proposed | Advantage |
|---|---|---|---|
| Orchestration | AWS EKS (hourly fees) | K3s on VPS | No control plane charges |
| Core Inference | GPT-4 API (~$10/1M output) | Ollama ($0.00/token) | $50K+ annual savings |
| Messaging | REST/JSON | gRPC/Protobuf | Lower latency, less bandwidth |
| DB Concurrency | RDS Multi-AZ | PostgreSQL + PgBouncer | Single instance, efficient pooling |
| Vector DB | High-RAM cloud instance | Qdrant + quantization | 30x memory reduction |
