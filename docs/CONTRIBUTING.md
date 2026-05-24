# Contributing to ADC

## 1. Project Overview

ADC Archiver is an open-source archiving project focused on simplicity, performance, and maintainability.

The project is structured to ensure a clean separation between development and stable releases.

Core goals:

* Stable and reliable release branches
* Active development on a single main branch
* No duplicate package identities
* Simple and predictable contribution workflow

---

## 2. Repository Structure

The repository consists of two primary development layers.

### Main Branch

The `main` branch is the active development branch.

It is used for:

* New features
* Experimental changes
* Bug fixes before release
* Pre-release testing

> [!Note]
> The main branch may contain breaking changes at any time.

---

### Stable Branches

Stable branches represent released versions of the software.

Examples:

* `stable/1.5`
* `stable/1.4`

Stable branches are used for:

* Bug fixes
* Security patches
* Minor compatibility updates

Stable branches are intended for production use.

---

## 3. Tags and Releases

Tags represent immutable release snapshots.

Examples:

* `v1.5.0`
* `v1.4.5`

Tags are never modified after creation.

They represent exact historical versions of the codebase.

---

## 4. How to Contribute

### Step 1: Fork and Clone

Fork the repository on GitHub and clone your fork locally.

If you want to work from the upstream repository directly, use the main branch clone command from the README:

```bash
git clone --branch main --single-branch https://github.com/Mealman1551/ArchivedDataCodec.git
```

If you forked the repository, clone your fork and then add the upstream remote:

```bash
git clone https://github.com/<your-username>/ArchivedDataCodec.git
cd ArchivedDataCodec
git remote add upstream https://github.com/Mealman1551/ArchivedDataCodec.git
```

---

### Step 2: Create a Branch

All contributions should start from the `main` branch.

Create a feature branch before making changes:

* feature/your-feature-name
* fix/your-bug-fix

---

### Step 3: Commit Guidelines

Keep commits clean and focused:

* One logical change per commit
* Avoid mixing refactors and features
* Use clear commit messages

---

### Step 4: Pull Request

Submit a pull request into `main`.

Include:

* What changed
* Why it changed
* Any breaking changes

---

## 5. Code Structure

The project uses a single unified package structure:

```
src/adc
```

Do not introduce alternative or legacy package names.

All previous duplicate package identities have been deprecated.

---

## 6. Stable Release Workflow

Stable branches are created from release tags on `main`.

Workflow:

1. A release is tagged on `main`
2. A stable branch is created from that tag
3. Stable maintenance branches receive only bug fixes
4. Development continues on `main`

---

## 7. What NOT to Do

* Do not commit directly to stable branches
* Do not introduce new package identities
* Do not reintroduce legacy canary or aurora structures
* Do not duplicate module implementations

---

## 8. Project Philosophy

This project is designed to remain:

* Simple
* Maintainable
* Contributor-friendly
* Free of unnecessary complexity

The goal is long-term sustainability without over-engineering.

---

## 9. Communication

For questions or discussions:

* Open a GitHub issue
* Provide clear context and examples
* Reference branch or version when relevant

###### &copy; Mealman1551 - The ADC Project