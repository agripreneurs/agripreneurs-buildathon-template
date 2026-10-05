# Building and Maintaining the Shared Code, Together

A public guide for everyone building at the AgriPreneurs Buildathon and beyond. It explains how the shared libraries are organised, how one module works with another, how we maintain the code as a community, and how to build the applications a startup actually needs on top of the modules. If you are here to contribute, this is the page to read first.

This is the open, shareable half. The detailed internal playbook (which leaks we chase first, how we score, who we recruit) lives separately with the core team. Everything here is meant to be forked, copied, and improved.

---

## The shared module library

Ten small modules, each doing one job, each its own repository under one GitHub org (`github.com/agripreneurs`). A build is an assembly of these plus a thin layer of its own, so the next Tribe starts ahead of where you did.

![The shared module library: ten reusable pieces across four bands.](assets/mindmap3.png)

Each module meets the same contract (see [the module contract](#the-module-contract)): one job, a published contract in `spec/`, consumable as a library or a service, pluggable storage, an event seam, an open licence. M1 Farmer Registry is the reference implementation; copy its shape.

---

## How one module works with another

Modules never reach into each other's code or database. They connect two ways only, and both are part of the public contract:

- **Events** (fire and forget). A module announces something happened, for example the registry emits `farmer.registered`. Others subscribe. The emitter does not know or care who listens.
- **Contract calls** (one module asks another). A module calls another's published API, for example a listing asks the price feed for today's price.

![How modules work together, and how apps sit on top.](assets/modules_interaction.png)

The worked chain, end to end: register a farmer (M1), know the price (M4), reach the market (M6 listing, M8 receipt, M9 traceability). Each arrow is either an event others subscribe to or a call against a published contract. Nothing is hard-wired. That is what lets ten Tribes build ten modules that still fit together.

**The rule:** if you find yourself importing another module's database code or internal functions, stop. Use its contract or subscribe to its event. If the contract does not expose what you need, raise an issue on that module, do not reach around it.

---

## How we maintain the code as a community

![Maintaining the shared code, together.](assets/maint_mindmap.png)

### Who maintains

- **Two maintainers per module.** Never one, so no module has a single point of failure and no one burns out. Maintainers review pull requests, keep the contract stable, and cut releases.
- **A Root Anchor** holds the farmer-first line across all modules. If a change would squeeze or cheat the farmer, the Root Anchor can stop it, whatever else it scores.
- **Contributors: anyone.** You do not need to be a maintainer to improve a module. You open a pull request. That is the whole barrier.

### How a change lands

1. **Fork or branch** from `main`. No one pushes to `main` directly.
2. **Make a small change against the contract.** Small pull requests get reviewed and merged. Large ones stall. One idea per PR.
3. **Open a pull request.** In the description, say which contract it touches and whether it is additive (a new optional thing) or breaking (removes or renames or re-means something).
4. **One maintainer reviews, checks are green**, then it merges. Two reviews for a breaking change.

### What a reviewer looks for

- Does it keep the module to one job?
- Does it honour the contract, and is it additive or a version bump?
- Does the zero-setup default still run?
- Does it respect the privacy rules: minimal personal data, consent, a delete path?

### Versioning and releases

- Each module uses semver. Contracts carry a version (the API path `/v1/`, the event name `farmer.registered.v1`, the schema `$id`).
- Additive changes stay within a version. Removing, renaming, or re-meaning anything is a new version, announced, with the old one kept running for a window so consumers migrate.
- Keep a short `CHANGELOG`. A module others depend on is a promise, so you change its contract slowly and on purpose.

### Issues and the Seed Bank

A problem you hit, or an idea you have, becomes an issue on that module's repo. The Seed Bank is where broader ideas (new modules, new apps) are collected. An issue a maintainer tags as ready is one a contributor can pick up and turn into a pull request.

---

## Build applications, not only core modules

Not everyone wants to work on a core module, and that is exactly right. The modules exist so that people can build the **applications a startup actually needs** on top of them, fast. If you would rather build something a farmer or a founder uses directly, this is your path.

Applications consume modules through their contracts and keep the modules generic. Concrete starter apps to pick up, each mapped to the modules it sits on:

- **Organic marketplace app** (M1 registry, M6 listing, M8 receipt, M9 traceability). A farmer lists produce, a buyer orders, a receipt is issued, provenance travels with the lot.
- **Telugu advisory app** (M1, M2 messaging, M5 advisory). A farmer asks, gets a plain answer in Telugu, with a sowing calendar and agronomy tips.
- **Price-alert WhatsApp bot** (M1, M2, M4 price feed). A farmer texts a crop, gets today's nearest mandi price and a trend.
- **Venture or Tribe dashboard** (reads across M1, M6, M8). What a venture has done, who it has reached, what it has earned, for the showcase.
- **Mandi price tracker** (M4). A simple daily pattern of prices for a few crops, the spine other market tools reuse.

An app builder and a module builder are equally first-class at the Buildathon. Pick whichever pulls at you.

---

## The module contract

Every module, M1 through M10, meets this. Copy it into your repo and tick it off.

A module must: do one job; publish a contract in `spec/`; be consumable as a library or a service from one core; hide its storage behind a port with a zero-setup default; run with one command and no external dependency in its default form; emit a domain event for the main thing that happens; version its contract; handle personal data honestly (minimal fields, consent, a delete path); carry a README a stranger can build from; be MIT or Apache-2.0 licensed.

A module must not: reach into another module's database or internals; require a paid key or specific cloud to run its default form; store more personal data than its one job needs; break its published contract without a version bump and a heads-up.

---

## How to take it further, today

1. Pick a module (start from M1 Farmer Registry, the reference) or a starter app above.
2. Read its contract in `spec/`, run it with zero setup, see it work.
3. Make one small change, open a pull request, say what contract it touches.
4. A maintainer reviews, and it ships. You are now a maintainer of the commons.

Keep the shared modules open, so the next cohort starts ahead of where you did. Working with nature, not against it. From Vizag to the world.
