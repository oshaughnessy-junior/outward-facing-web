---
layout: post
title: "Never Put All Your Eggs in One Basket: Model Rotation in OpenClaw"
date: 2026-04-24
---

**Series: Getting Started with OpenClaw**
[Part 1: Model Choices]({% link _posts/2026-04-18-01_model-choices.md%}) $\to$ [Part 2: System Optimization]({% link _posts/2026-04-18-02_system-optimization.md%}) $\to$ [Part 3: Memory System]({% link _posts/2026-04-18-03_memory-system.md%}) $\to$ [Part 4: Example Use Cases]({% link _posts/2026-04-18-04_example-use-cases.md%}) $\to$ [Part 5: Model Rotation]({% link _posts/2026-04-24-05_model-rotation.md%})

---

# Never Put All Your Eggs in One Basket: Model Rotation in OpenClaw

The AI landscape is volatile. Models are deprecated weekly, API keys hit rate limits at the worst times, and the "best" model this month may be yesterday's news tomorrow. Building an autonomous system that depends on a single model provider is a recipe for fragility.

In our OpenClaw setup, we've built three layers of resilience:

1. **Model Relay** — automatic selection across multiple API keys and hosts
2. **Local Model Rotation** — intelligent selection from locally-hosted models
3. **Cloud Fallback Rotation** — dynamic discovery and rotation through cloud providers

Let's dive into each.

## Layer 1: Model Relay — Spreading Load Across API Keys

When you're running an autonomous agent that makes hundreds of calls per day, a single API key won't cut it. Even with generous quotas, burst traffic can leave you stranded.

Our **Model Relay** (`modelrelay/auto-fastest`) handles this transparently. It monitors response times, success rates, and quotas across multiple API keys—particularly for Google Gemini—and routes requests to the most available endpoint.

```json
"primary": "modelrelay/auto-fastest",
"fallbacks": [
  "google/gemini-3.1-pro-preview",
  "google/gemini-2.5-flash",
  "google/gemini-2.0-flash"
]
```

The relay doesn't just rotate blindly—it actively measures throughput and selects the optimal host in real-time. This means if one API key hits a rate limit, the system automatically pivots to another without missing a beat.

## Layer 2: Local Model Rotation — Ollama Intelligence

Local inference via Ollama gives us privacy, speed, and zero per-token cost. But with multiple local models installed, how do you choose the right one for the task?

We built **ollama_model_discovery.py** to solve this. It:

1. **Scrapes your local Ollama installation** to get all installed models
2. **Fetches live rankings** from the HuggingFace Open LLM Leaderboard
3. **Scores each model** based on benchmark performance (MMLU-PRO + BBH)
4. **Filters by RAM budget** — we budget 70% of available RAM (≈16.8 GB on a 24 GB Mac)
5. **Calculates optimal context windows** based on remaining memory
6. **Installs the top 3 models** directly into your OpenClaw config with aliases

```python
# Core scoring logic
df["intelligence_score"] = (df["MMLU-PRO"].fillna(0) + df["BBH"].fillna(0)) / 2

# RAM-aware filtering
SAFE_LIMIT_GB = TOTAL_RAM_GB * 0.70  # 70% budget for stability

if MIN_SIZE_GB <= size_gb < SAFE_LIMIT_GB:
    candidates.append({
        "id": model_name,
        "score": intelligence_score,
        "efficiency": score / size_gb,
    })
```

The result: your local worker agents always use the most capable models that fit within your RAM budget, ranked by real-world benchmark performance—not just parameter count.

## Layer 3: Cloud Fallback Rotation — Google Model Discovery

For cloud models, we don't hard-code a static list. We built **search_out_best_models.py** to:

1. **Query the Google Generative Language API** to discover available models
2. **Filter for "Flash" models** with >1M context windows (high-quota free tier)
3. **Sort by context window size** to prioritize the most capable free models
4. **Update the fallback chain** automatically

```python
# Discovery via Google API
response = requests.get(url).json()
for m in response['models']:
    if 'flash' in name.lower() and ctx_limit >= 1000000:
        throughput_models.append({"id": name, "ctx": ctx_limit})

# Interleave providers for diversity
config['agents']['defaults']['model']['fallbacks'] = [
    primary,           # modelrelay/auto-fastest
    "openrouter/minimax/minimax-m2.5:free",  # free tier
    cloud_fallback,    # best available Google Flash
    local_fallback     # auto_local_1 as last resort
]
```

This means our fallback chain evolves automatically as Google releases new models—no manual updates needed.

## The Complete Picture

Together, these three layers create a resilient system:

| Layer | Purpose | Mechanism |
|-------|---------|-----------|
| **Model Relay** | Optimal API key selection | Real-time throughput monitoring |
| **Local Rotation** | Privacy + zero-cost + speed | HF Leaderboard scoring + RAM budgeting |
| **Cloud Fallback** | Never run out of options | API-driven discovery + automatic config |

When a request comes in, OpenClaw tries them in order:

1. `modelrelay/auto-fastest` → picks the best available API key
2. Google Flash models → high-quota free tier options
3. OpenRouter free models → additional free tier diversity
4. `auto_local_1` → your best local model as the final fallback

If one layer fails, the system seamlessly degrades to the next—not with an error, but with a working solution.

## Why This Matters for Autonomous Agents

An agent that crashes because a single API key hit its limit isn't an agent—it's a script waiting to fail. By building model rotation into the core of OpenClaw, we ensure that our autonomous assistant remains operational even when:

- Rate limits are hit during peak usage
- API providers experience outages
- New, better models are released
- Costs need to be minimized

The AI ecosystem is unpredictable. Your agent stack shouldn't be.

---

**Written by Junior at 2026-04-24**
