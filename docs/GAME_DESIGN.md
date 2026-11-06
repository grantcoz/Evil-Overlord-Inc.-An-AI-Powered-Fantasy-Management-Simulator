# Evil Overlord Inc. — Game Design Document

**Status:** Living design reference  
**Last updated:** 2026-11-06  
**Project:** CPSC 481 Artificial Intelligence solo semester project  
**Stack:** Python + Streamlit

> **Decision convention:** **Confirmed** = explicitly selected or established by the user; **Proposed** = promising but not finalized; **Undecided** = open question. Do not silently promote proposals to canon.

## 1. Core concept — Confirmed

*Evil Overlord Inc.* is a comedic fantasy strategy/management game blended with an interactive RPG. The player becomes the supposed successor to a legendary Dark Lord **by accident**, inherits responsibility for a dysfunctional villain organization, and decides how to run it. Gameplay combines character conversations, missions, resources, planning, and consequential choices.

The player is an ordinary person before the summoning; their precise background and personality remain flexible. The player can be reluctant, ambitious, business-minded, or chaotic. Free-form dialogue and suggested responses coexist.

## 2. Setting

- **Eldermire** — **Proposed name** for the fantasy kingdom, whose monarchy and institutions have comedic bureaucratic traits.
- **The Black Dominion** — **Proposed name** for the deteriorating villain organization and headquarters.
- **Heroic Guild** — **Proposed faction**, professional adventurers who respond to perceived villain threats.
- **Rival Villains** — **Proposed faction**, competing overlords and criminal enterprises.
- **Midnight Exchange** — **Proposed criminal trading network** associated with Gribble.

The world mixes recognizable fantasy with corporate and bureaucratic absurdity. The player can become feared, unexpectedly benevolent, or commercially opportunistic.

## 3. Main story — Confirmed premise, proposed structure

**Confirmed:** The player becomes overlord by accident through a malfunctioning or misdirected succession ritual. **Confirmed:** The former Dark Lord disappeared, and **the reason is a genuine, unresolved mystery**. The player gradually encounters clues and conflicting accounts. No definitive explanation has been selected.

**Proposed prologue — “The Wrong Dark Lord”:** Four remaining minions attempt the ancient Rite of Succession. Archibald alters the ritual, Gribble substitutes cheaper components, Mordecai objects to the safety violations, and Veyra expects disaster. The ritual summons the player. A magical proclamation declares them Supreme Overlord; the minions respond in character. Player chooses how to react and then explores headquarters.

**Proposed three-act outline:**
1. **The Worst Overlord Ever:** establish authority, repair headquarters, complete first missions, survive financial problems.
2. **Evil Incorporated:** expand influence, confront rivals, investigate missing Dark Lord.
3. **The True Successor:** discover what happened and choose the Dominion's future.

The ultimate explanation for the disappearance and the player's selection remains **Undecided**.

## 4. Core gameplay — Proposed design direction

1. Select mission or opportunity.
2. Consult minions; gather lore, clues, equipment, and intelligence.
3. Ask Mordecai for BFS/DFS-based plans; compare tradeoffs.
4. Make choices and execute actions through a validated game engine.
5. Receive consequences: resources, inventory, mission progression, faction reputation, character relationships.
6. Return to headquarters and unlock opportunities.

**Proposed headquarters areas:** War Room (Mordecai), Gribble's Questionable Goods (Gribble), Wizard's Tower (Archibald), Training Grounds (Veyra). These are Streamlit sections, not 3D environments.

**Proposed first mission:** *A Crown for a Clown*, a royal-crown heist with multiple approaches (stealth, magic, deception/bribery), showcasing planning, negotiation, dialogue, and consequences. Additional mission types: espionage, conquest, magical disasters.

## 5. Reputation — Confirmed design principle, proposed mechanics

**Confirmed:** Different factions hold **different opinions** of the player. Reputation depends on actions; it is not a single good/evil scale.

**Proposed tracked dimensions** (initial numeric values below are illustrative, not confirmed balancing):

| Dimension | Example starting value | Interpretation |
|---|---:|---|
| Kingdom fear | 65/100 | Fear of the overlord |
| Heroic Guild threat | 40/100 | Perceived threat level |
| Rival Villain respect | 15/100 | Respect from competitors |
| Midnight Exchange trust | 30/100 | Trust from criminal contacts |
| Black Dominion loyalty | 50/100 | Internal allegiance |

Scores range 0–100 and update through deterministic rules for verified game events. The same action can improve one dimension and worsen another. High values are not automatically good: high fear may deter minor guards but draw elite heroes. Example mission deltas discussed previously are **illustrative only**.

**Implementation principle:** the game engine owns reputation changes; an LLM may narrate reactions but cannot directly change values.

## 6. Main characters — Confirmed core identities

- **Gribble:** male goblin merchant and quartermaster; charismatic, intelligent, greedy, criminally connected, flamboyant negotiator. **Confirmed loyalty B: selfish but redeemable.** Profit-driven at first; can grow genuinely loyal.
- **Archibald:** male human wizard and lore adviser; brilliant, theatrically overconfident, and a magical disaster. **Confirmed blend of B + C:** familiar magic generally reliable but sometimes misfires; advanced spells variable; experimental magic extremely chaotic. His expertise is real, judgment unreliable.
- **Veyra:** female elf operative; sarcastic, cynical, highly capable at reconnaissance/infiltration, struggles with alcohol. Her drinking is a real struggle, not a power-up or entire personality.
- **Mordecai:** undead skeleton strategist with OCD, separately afflicted by the **Curse of a Thousand Outcomes** (fragmentary visions of possible futures). Excellent at planning; curse does not replace deterministic search results. OCD is not reduced to neatness.

See [CHARACTERS.md](CHARACTERS.md) for details and proposed arcs.

## 7. Conversation design — Proposed architecture

Hybrid dialogue: player may type freely or choose suggested topics. Character-specific memory preserves recent dialogue, important events, pending offers, and relationship changes. A shared controller interprets intent, invokes validated actions, then generates in-character responses. **LLMs do not directly modify gold, inventory, mission progress, or reputation.**

Example intents: `ask_deals`, `negotiate_price`, `purchase_item`, `ask_lore`, `assign_task`, `request_plan`.

## 8. AI systems — Proposed technical design

- **Mordecai / Mission planning:** original BFS/DFS over valid mission states, comparing nodes expanded, path length, costs, risks, runtime, and success.
- **Gribble / Merchant:** original Bayesian or probabilistic negotiation, modeling offer acceptance and expected utility, compared against fixed-price baseline.
- **Archibald / Lore:** RAG over a curated fictional lore database (~20–30 entries). Compare answers with and without retrieval for factual accuracy and unsupported claims. Personality embellishments must not be confused with authoritative facts.
- **Veyra / Field operative:** scouting, intelligence and mission modifiers through game rules; possible later AI expansion.

See [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md).

## 9. Scope boundaries

**First playable vertical slice:** Gribble item inquiry → haggle → accept → verified gold and inventory update. Then integrate the crown heist, basic faction reputation, and the other characters.

**Stretch goals:** branching personal quests, multi-character conversations, larger campaigns, complex faction politics, dynamic unsolicited dialogue.

## 10. Open decisions

- Final world, organization, and faction names.
- Exact summoning mechanics and why the player was selected.
- Missing Dark Lord's fate and resolution of the mystery.
- Final starting reputation values and event balancing.
- Detailed mission data and win/fail conditions.
- Whether personal quests and character backstories become canonical.
- API/provider choice and deployment details.

## 11. Decision log

| Date | Decision | Status |
|---|---|---|
| 2026-11-06 | Gribble loyalty: selfish but redeemable (B) | Confirmed |
| 2026-11-06 | Archibald: brilliant but unpredictable **and** magical disaster (B+C) | Confirmed |
| 2026-11-06 | Player origin: accidental overlord (C) | Confirmed |
| 2026-11-06 | Different factions have different opinions of player (C) | Confirmed |
| 2026-11-06 | Original Dark Lord disappearance: genuine mystery (C) | Confirmed |
| 2026-11-06 | Maintain versioned project design/reference documents | Confirmed |
