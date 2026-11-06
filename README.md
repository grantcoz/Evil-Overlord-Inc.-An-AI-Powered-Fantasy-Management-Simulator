# Evil Overlord Inc. 🏰

> *World domination is easy. Managing incompetent employees is the real challenge.*

**Evil Overlord Inc.** is a comedic, AI-powered fantasy management simulator developed as a solo project for **CPSC 481: Artificial Intelligence**. Players take the role of an aspiring evil overlord attempting ridiculous missions with limited resources and a deeply unreliable staff.

The project combines traditional AI algorithms with generative AI. A mission planner searches for viable strategies, a goblin merchant makes probabilistic pricing decisions, a wizard offers occasionally questionable advice, and a procrastinating henchman generates excuses instead of doing his job.

> **Project status:** In development. The features and commands below describe the planned application; they may not work until the corresponding components are implemented.

## Gameplay

The player selects a mission, consults advisors, purchases supplies, assigns tasks, and chooses how to execute a plan. Actions affect a shared game state that tracks resources, inventory, mission progress, and outcomes.

Example missions may include:
- Stealing the royal crown.
- Conquering the village bakery.
- Acquiring a suspiciously powerful magical artifact.

The goal is a **turn-based hybrid simulator** with a simple browser interface, rather than a real-time game.

## AI Systems

| Character / System | Planned AI approach | Role |
| --- | --- | --- |
| **Evil Overlord Planner** | State-space search; breadth-first search (BFS) and depth-first search (DFS) | Finds sequences of valid actions to complete missions. |
| **Goblin Merchant** | Bayesian inference and expected utility | Estimates purchase acceptance and chooses prices. |
| **Confidently Incorrect Wizard** | Large language model (LLM) and retrieval-augmented generation (RAG) | Answers questions about fictional lore; enables comparison of grounded and ungrounded answers. |
| **Procrastinating Henchman** | LLM prompting and rule-based task outcomes | Generates excuses while the game engine determines delays and outcomes. |

### Original AI Contributions

The project is intended to implement its own:

- Mission states, action preconditions, transitions, and goal tests.
- BFS and DFS planning logic and a plan-scoring function.
- Bayesian merchant model and pricing strategy.
- Fictional lore collection, retrieval workflow, and evaluation questions.
- Shared simulation rules that connect advisor decisions to gameplay.

Existing libraries and pretrained LLMs may be used for the interface, model access, and supporting utilities.

## Technologies

- **Python** — simulation logic and AI algorithms.
- **Streamlit** — browser-based user interface.
- **JSON / CSV** — mission data, probability tables, lore, and evaluation scenarios.
- **Pretrained LLM** — wizard and henchman dialogue (provider/model to be selected).
- **Matplotlib** — optional charts for evaluation results.

## Getting Started

These are the **planned** local setup steps once the application and dependency files are available.

### Prerequisites

- Python 3.10 or newer (subject to final dependency compatibility).
- Git.
- Access to a supported LLM API for dialogue features.

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/evil-overlord-inc.git
cd evil-overlord-inc
python -m venv .venv
```

Activate the virtual environment:

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

Once `requirements.txt` has been created:

```bash
pip install -r requirements.txt
```

### Run the Application

Once `app.py` is implemented:

```bash
streamlit run app.py
```

Streamlit will display a local browser URL, typically `http://localhost:8501`.

LLM-backed features will require provider-specific configuration. **Do not commit API keys or `.env` files to Git.**

## Planned Project Structure

```text
evil-overlord-inc/
├── app.py                   # Streamlit interface
├── game/
│   ├── state.py             # Shared game state
│   ├── actions.py           # Action rules and transitions
│   ├── missions.py          # Mission definitions
│   └── simulator.py         # Turn execution
├── ai/
│   ├── search.py            # BFS and DFS
│   ├── planner.py           # Plan evaluation
│   ├── merchant.py          # Bayesian pricing
│   ├── wizard.py            # LLM and lore retrieval
│   └── henchman.py          # Excuse generation
├── data/
│   └── lore.json            # Fictional world knowledge
├── evaluation/
│   ├── test_search.py
│   ├── test_merchant.py
│   └── test_wizard.py
├── requirements.txt
└── README.md
```

*This structure is a design target, not a claim that all files currently exist.*

## Datasets

No external training dataset is required. The project will use small, self-created datasets for mission rules, merchant probability tables, fictional lore, and evaluation questions. The LLM components will use an existing pretrained model rather than training a new one.

## Evaluation Plan

| Component | Comparison | Metrics |
| --- | --- | --- |
| Mission planner | BFS vs. DFS (and potentially a cost-aware search baseline) | Solved missions, nodes expanded, plan length, resource cost, runtime |
| Merchant | Bayesian pricing vs. fixed-price strategy | Offer acceptance, average profit, pricing outcomes |
| Wizard | LLM without retrieval vs. LLM with RAG | Factual accuracy, unsupported claims, abstention, response time |

Evaluation scenarios will use consistent starting conditions. Wizard responses will be checked against a predefined fictional lore answer key.

## Academic Context

This project is being developed for **CPSC 481: Artificial Intelligence** as an individual course project. It explores state-space search, probabilistic reasoning, generative AI, retrieval-augmented generation, and AI evaluation through a comedic interactive simulation.

## License

No license has been selected yet. Until one is added, the repository should not be assumed to grant reuse permissions.
