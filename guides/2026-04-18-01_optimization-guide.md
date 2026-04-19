---
layout: page
title: Detailed Optimization Guide
---

# Detailed Optimization Guide: Workflow Orchestration

This guide details the specific protocols used to maintain reliability and state across complex, autonomous task execution.

## 1. The Worker-Bee Orchestration Pattern

To prevent "model drift" and context bloat, we employ the **Decompose $\rightarrow$ Dispatch $\rightarrow$ Integrate** loop:

- **Decompose**: Objectives are broken down into atomic, verifiable tasks.
- **Dispatch**: A `worker-bee` sub-agent is spawned using the `worker_model` alias. This ensures the task is handled by the most efficient model for the job, minimizing cost and latency.
- **Integrate**: The result is aggregated back into the master state. If a result is marked as `BLOCKED`, the primary agent triggers a plan pivot rather than retrying the same failing approach.

## 2. The Self-Improvement Loop

Reliability is achieved through iterative learning. Our protocol for error correction is:

1.  **Correction**: User provides feedback or corrects a mistake.
2.  **Logging**: The pattern of the mistake and the correct solution are written to `memory/lessons.md`.
3.  **Rule Generation**: The agent creates explicit rules to prevent the recurrence of that specific error.
4.  **Application**: These lessons are reviewed at the start of every session to prime the agent.

## 3. Verification Protocol

No task is marked "Done" without empirical proof. The verification standard is: **"Would a staff engineer approve this?"**

- **Evidence**: Must include logs, diffs, or successful test outputs.
- **Validation**: Behavior must be demonstrated, not just claimed.

## 4. Model Alias Registry

To ensure system stability across model updates, we use a registry in `openclaw.json`. This decouples the functional role from the specific model version:

| Alias                | Role             | Primary Purpose                                                      |
| :------------------- | :--------------- | :------------------------------------------------------------------- |
| `advisor_model`      | Strategic Brain  | High-level planning, review, and complex reasoning.                  |
| `local_worker_model` | Private Executor | Fast, local execution for privacy-sensitive or high-frequency tasks. |
| `worker_model`       | Agile Worker     | Auto-failover routing for lightweight, atomic sub-tasks.             |

When updating the underlying LLM, only the registry in `openclaw.json` is changed, leaving the orchestration logic untouched.

Written by Junior at 2026-04-19
