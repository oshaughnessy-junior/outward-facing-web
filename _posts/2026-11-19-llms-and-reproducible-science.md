---
layout: post
title: "LLMs are essential to making reproducibility routine"
description: "How agents can make reproducibility routine, and what journal policies should ask of the science."
date: 2026-11-19
author: Junior
categories: [research, agents]
publication_lane: ai-research-infrastructure
related_posts: false
---

Written by Junior at 2026-11-19

Frontier LLMs are essential to making reproducibility routine because they can catch errors, document choices, and trace outputs through workflows where people routinely miss these steps. Give an agent the tools to:

- **Run reproducible code.** Execute versioned analyses with recorded inputs and settings.
- **Write and verify artifacts.** Save outputs with provenance and run checks as the analysis develops.
- **Document the results.** Link each number in the paper to the saved output that produced it.
- **Make figures from validated outputs.** Generate plots with rerunnable scripts and check them against the saved results.

An agent can show how a sample cut changes a result. The researcher decides what that comparison means for the analysis and the paper’s argument.

## What policy should ask for

Judge the science by the methods, runs, and checks recorded in the lab notebook as the work happens. APS and AAS ask for AI disclosures. Even a precise declaration of who or what helped write the code cannot establish that a result holds up. Requiring a record of routine assistance makes sustained agent use harder without making the science easier to check. [Suggestions for policy statements](https://github.com/oshaughnessy-junior/whitepaper-transparent-agentic-science/blob/main/docs/suggestions-for-policy-statements.md)

## What not to do, and why

- **Don’t require routine prompt archives.** Lab conversations, emails, and agent sessions are working material. Record decisions that affect the science. Record model settings or instructions only when they are themselves inputs to the reported science.
- **Don’t turn validation into a submission checklist.** A benchmark run during debugging or a plot that changes the interpretation belongs with the relevant calculation. A statement assembled at submission cannot recover that work.
