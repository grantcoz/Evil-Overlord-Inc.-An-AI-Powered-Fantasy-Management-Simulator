# Evil Overlord Inc. — Development & AI Evaluation Plan

**Last updated:** 2026-11-06  
**Context:** Solo CPSC 481 AI project; approximately six-week development window discussed. The user wants a fun playable game and substantial original AI work.

## 1. Technical direction

**Planned stack:** Python 3.11/3.12, Streamlit, standard Python modules, optional OpenAI-compatible LLM endpoint, pytest. Potential packages as needed: numpy, pandas, scikit-learn, networkx, matplotlib, python-dotenv. Provider choice is not finalized.

**Important:** This document describes planned architecture; it does not assert that these files or features are already implemented.

## 2. Proposed repository structure

```text
evil-overlord-inc/
├── app.py
├── game/
│   ├── __init__.py
│   ├── state.py
│   ├── actions.py
│   ├── missions.py
│   └── simulator.py
├── ai/
│   ├── __init__.py
│   ├── search.py
│   ├── planner.py
│   ├── merchant.py
│   ├── wizard.py
│   └── henchman.py
├── dialogue/
│   ├── __init__.py
│   ├── controller.py
│   ├── intents.py
│   ├── memory.py
│   └── prompts.py
├── data/
│   ├── characters.json
│   ├── lore.json
│   └── missions.json
├── docs/
│   ├── GAME_DESIGN.md
│   ├── CHARACTERS.md
│   └── DEVELOPMENT_PLAN.md
├── evaluation/
├── requirements.txt
└── README.md
```

## 3. Systems and evaluation

| System | Original contribution / implementation | Evaluation |
|---|---|---|
| Mission planning | BFS and DFS over valid, hashable game states | Nodes expanded, path length, runtime, cost/risk, solution success |
| Gribble negotiation | Bayesian/probabilistic offer acceptance and expected-utility counteroffers | Merchant profit, acceptance, transaction outcomes vs fixed-price baseline |
| Archibald lore | RAG over curated fictional knowledge (~20–30 entries) | Grounded accuracy, unsupported claims/hallucination, latency with vs without RAG |
| Conversation | Intent routing, character prompts, memory, structured validated actions | Correct intent routing and no invalid game-state mutations |
| Reputation | Rule-based faction-specific counters and event deltas | Unit tests for bounded updates and correct consequences |
| Magical mishaps | Rule-based probabilistic spell outcomes | Probability sanity checks, deterministic seeded tests |

AI-related grading emphasis previously discussed: approximately **55% original AI contribution** and **15% evaluation**. Verify against the current course rubric before treating these as authoritative grading requirements.

## 4. Design invariants

- Only validated game actions mutate state; LLM prose cannot create gold, items, clues, or mission success.
- BFS/DFS operate on well-defined, hashable states with reproducible transition rules.
- Player can ignore or alter recommended plans.
- Faction scores are separate, bounded dimensions; a higher score is not always beneficial.
- RAG source facts and Archibald's opinions must be distinguishable.
- Random spell effects should be seedable for testing.
- Store durable game facts separately from free-form dialogue memory.

## 5. Development sequence — Proposed

### Phase 1 — Foundation
- Confirm state schema: gold, inventory, location, mission flags, faction reputation, relationships, turn/day.
- Build data-driven mission definitions and validated actions.
- Set up pytest, version control, and basic Streamlit hub.

### Phase 2 — First vertical slice
- Gribble shop inventory and item inspection.
- Merchant negotiation engine and baseline.
- Player dialogue intent → offer → accept → validated purchase → gold/inventory change.

### Phase 3 — Planning and first mission
- BFS/DFS and metrics.
- Crown heist with several legitimate approaches and mission-state transitions.
- Faction reputation effects from verified outcomes.

### Phase 4 — Lore and characters
- Curated lore database and RAG for Archibald.
- Veyra scouting and Mordecai consultation.
- Character-specific prompts and limited persistent dialogue memory.

### Phase 5 — Evaluation and polish
- Reproducible benchmarks, test cases, tables/plots.
- UI improvements, narrative onboarding, balancing, README and presentation.

## 6. Known earlier code / migration caution

A prior prototype was discussed with a frozen `GameState` dataclass (gold=100, location=`headquarters`, tuple inventory, and crown-heist flags such as `guards_distracted`, `crown_stolen`, `escaped`), and an initial `buy_disguise` action. This is **historical discussion, not verified current repository state**. Before changing code, inspect the actual repo and migrate carefully to a generic mission model.

## 7. Immediate next actions

1. Put these Markdown documents into the real repository under `docs/`.
2. Inspect current files and confirm what has already been implemented.
3. Establish the authoritative state schema and action validation.
4. Implement and test the Gribble transaction vertical slice.
5. Begin recording decisions and evaluation results alongside code changes.

## 8. Documentation maintenance protocol

When a design decision changes:
1. Update the corresponding section of `GAME_DESIGN.md`.
2. Update `CHARACTERS.md` for character details or `DEVELOPMENT_PLAN.md` for technical work.
3. Add a dated decision entry to `GAME_DESIGN.md`.
4. Label speculative ideas **Proposed**, and unresolved questions **Undecided**.
5. Commit the updated docs with the relevant code, if any.

The repository files, not ChatGPT memory alone, should be the authoritative reference in later sessions.
