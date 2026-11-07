# Evil Overlord Inc. 🏰

> *World domination is easy. Managing your staff is the real challenge.*

**Evil Overlord Inc.** is a comedic, AI-powered fantasy strategy and management RPG being developed as a **solo CPSC 481: Artificial Intelligence project**. The player is an ordinary person accidentally summoned as the successor to a missing Dark Lord. They inherit a failing villainous organization and must manage unreliable but talented advisors, scarce resources, and increasingly ridiculous missions.

**Status:** In development. This README distinguishes the existing visual prototype from planned gameplay and AI systems.

## Story and Gameplay

A botched succession ritual makes the player the new Evil Overlord. The former Dark Lord has disappeared, and the truth remains a mystery. The player can choose how to rule, interact with advisors, acquire equipment, investigate clues, and complete missions while their decisions affect resources and faction relationships.

The planned gameplay loop is:

1. Explore headquarters and speak with advisors.
2. Choose a mission and gather information.
3. Compare AI-generated plans and purchase equipment.
4. Execute validated actions and deal with outcomes.
5. Update inventory, gold, reputation, and story progression.

The **minimum playable mission** is **“A Crown for a Clown”**, a royal-crown heist with multiple possible approaches. Additional missions are stretch goals.

## Main Characters

| Character | Position | Personality and gameplay role | Planned AI |
| --- | --- | --- | --- |
| **Mordecai** | Undead military strategist | Disciplined, formal, obsessive about order, and burdened by unreliable visions of possible futures; advises on mission strategies | BFS, DFS, uniform-cost search, and A* mission planning |
| **Gribble** | Goblin merchant and quartermaster | Clever, greedy, scheming, and potentially loyal; sells supplies and negotiates deals | Bayesian negotiation and expected-utility pricing |
| **Archibald** | Elderly human wizard | Brilliant, overconfident, and accident-prone; explains lore and offers risky magical assistance | LLM dialogue with retrieval-augmented generation (RAG); rule-based spell outcomes |
| **Veyra** | Elven scout and field operative | Sarcastic, rebellious, cynical, and highly capable **but prone to procrastination**; delays assignments, makes excuses, and sometimes leaves reconnaissance until the last moment | Contextual LLM dialogue and explicit, testable task-delay/reconnaissance rules |

**Veyra's procrastination is a character trait, not a lack of skill.** She is an excellent scout and infiltrator when she commits to a task. Her tendency to put work off creates management challenges: the player may need to follow up, change priorities, or work around delays. Her drinking is a separate personal struggle, not a gameplay power-up or the sole explanation for her behavior.

## AI Systems and Original Contributions

### 1. Mordecai — Mission Planning (Primary Contribution)

Missions are represented as searchable state spaces. States describe relevant facts such as player location, inventory, mission flags, available gold, and guard status. Actions have explicit preconditions, effects, and costs.

Planned algorithms:
- **Breadth-first search (BFS):** baseline for minimum-action plans in unweighted graphs.
- **Depth-first search (DFS):** baseline search that does not guarantee optimal plans.
- **Uniform-cost search (UCS):** finds minimum-cost plans under nonnegative action costs.
- **A* search:** uses accumulated cost and a heuristic estimate of remaining cost.

The project will implement its own mission representation, legal transitions, goal tests, weighted cost model, and A* heuristic. A possible objective combines gold, time, and modeled risk using configurable weights. The heuristic must be tested for correctness and admissibility when claiming optimal solutions.

### 2. Gribble — Bayesian Merchant

Gribble estimates whether a proposed price is likely to be accepted based on negotiation context, then selects offers or counteroffers using expected utility. His strategy will be compared with fixed-price and simple rule-based baselines. All purchases require validated player confirmation.

### 3. Archibald — Lore Retrieval and Magical Risk

Archibald can answer questions about the fictional world using an existing LLM. A local lore knowledge base supports retrieval-augmented generation (RAG), allowing grounded responses to be compared with responses generated without retrieval. Magical mishaps use explicit, reproducible game rules rather than unconstrained LLM text.

### 4. Veyra — Reconnaissance and Procrastination

Veyra provides scouting intelligence, identifies potential routes, and influences what information is available to the mission planner. Her tendency to postpone work is represented through explicit assignment status and delay rules. Dialogue can supply humorous excuses, but an LLM cannot independently alter mission state, timers, or rewards.

### Safe Integration Rule

**LLM-generated dialogue never directly changes game state.** The Python game engine validates purchases, mission progress, assignments, inventory changes, and outcomes.

## User Interface

The game uses **Python and Streamlit** with a stylized cartoon-fantasy, visual-novel-inspired presentation:

- Illustrated location backgrounds and transparent character sprites.
- Character dialogue with suggested topics and planned free-text input.
- Headquarters navigation, inventory, mission planning, and faction reputation views.
- A planned parchment-style dialogue overlay and compact game controls.

The interface will separate **Conversation Mode** (characters and story) from **Management Mode** (missions, resources, and planning).

## Performance Evaluation

| Experiment | Comparison | Measurements |
| --- | --- | --- |
| Mission planning | BFS vs. DFS vs. UCS vs. A* | Valid solutions, nodes expanded, runtime, plan length, total cost, and risk |
| Negotiation | Bayesian strategy vs. fixed-price and rule-based strategies | Acceptance rate, average profit, player spending, negotiation rounds |
| Lore answers | LLM without retrieval vs. LLM with RAG | Factual accuracy against an authored answer key, unsupported claims, latency |
| Task assignment (supporting) | Veyra assignment scenarios | Correct status transitions and reproducible delay behavior |

Experiments will use documented starting conditions and repeatable test cases. Results will be reported rather than assumed in advance.

## Technologies and Data

- **Python:** game state, rules, search, probability models, and tests.
- **Streamlit:** interactive browser interface.
- **Pillow:** scene composition and sprite placement.
- **JSON / CSV:** authored missions, fictional lore, negotiation scenarios, and evaluation results.
- **Optional existing LLM API:** character dialogue and Archibald's RAG responses; provider not finalized.
- **pytest / plotting tools:** automated correctness tests and evaluation figures.

No external training dataset is required. Planned local data includes mission/action definitions, merchant probabilities, approximately 20–30 lore entries, and a curated set of lore evaluation questions. These are targets, not completed dataset counts.

## Repository Structure

```text
Evil-Overlord-Inc/
├── ai/
│   ├── __init__.py
│   ├── henchman.py       # Existing module; Veyra task-delay logic may be integrated here
│   ├── merchant.py
│   ├── planner.py
│   ├── search.py
│   └── wizard.py
├── assets/
│   ├── backgrounds/
│   │   └── wizard_tower.png
│   ├── characters/
│   │   ├── archibald/
│   │   │   └── neutral.png
│   │   ├── gribble/
│   │   ├── mordecai/
│   │   └── veyra/
│   └── ui/
├── data/
├── dialogue/
├── docs/
│   ├── CHARACTERS.md
│   ├── DEVELOPMENT_PLAN.md
│   └── GAME_DESIGN.md
├── evaluation/
│   └── results/
├── game/
│   ├── __init__.py
│   ├── actions.py
│   ├── missions.py
│   ├── simulator.py
│   └── state.py
├── tests/
├── ui/
│   └── scenes.py
├── app.py
├── scene_demo.py
├── requirements.txt
└── README.md
```

This reflects the reported repository layout, not a claim that all modules contain finished implementations. `ai/henchman.py` is an existing filename and may be adapted for Veyra rather than creating a separate henchman character.

## Getting Started

From the project root, create or activate a Python virtual environment and install dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the **existing Archibald visual prototype**:

```powershell
python -m streamlit run scene_demo.py
```

Run the main application entry point (its functionality depends on development progress):

```powershell
python -m streamlit run app.py
```

LLM functionality may require provider credentials. Store secrets outside the repository (for example, in ignored environment files), and never commit API keys.

## Development Roadmap

1. **Visual foundation:** Archibald sprite, Wizard's Tower background, and basic dialogue prototype — working.
2. **Mission state model:** define crown-heist states, actions, preconditions, and transitions.
3. **Core search:** implement BFS, DFS, UCS, and A* with a custom heuristic.
4. **Evaluation:** benchmark planning methods with reproducible scenarios.
5. **Character AI:** integrate Gribble's negotiation, Archibald's lore retrieval, and Veyra's assignment behavior.
6. **Playable integration:** complete one branching mission and connect conversations, inventory, reputation, and outcomes.
7. **Final polish:** tests, presentation, and written report.

## Academic Context

Developed individually by **Brendon Cozzens** for **CPSC 481: Artificial Intelligence** at California State University, Fullerton. The project's central academic contribution is an original, measurable AI planning problem within a novel fantasy management game, supported by probabilistic reasoning and LLM-based interaction.

For ongoing design decisions and planned implementation details, see `docs/GAME_DESIGN.md`, `docs/CHARACTERS.md`, and `docs/DEVELOPMENT_PLAN.md`.
