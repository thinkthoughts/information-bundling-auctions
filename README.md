# IBPA Engineering

**IBPA (Information-Bundling Position Auctions)** was introduced in the paper **"Targeting Information in Ad Auction Mechanisms"** (arXiv:2601.09541). The authors develop an auction mechanism that separates **publisher information acquisition** from **advertiser information disclosure**, allowing information to be bundled in ways that improve allocation efficiency while remaining computationally practical.

This repository builds an engineering implementation of those ideas through reusable Python notebooks, visualizations, benchmarks, and developer tooling. It is designed to help researchers and developers understand, reproduce, implement, evaluate, and extend the mechanism.

## Engineering statement

> **Information Constraints Specify Allocation Efficiency**

<img src="figures/2601-09541-hero.png" alt="Information Constraints Specify Allocation Efficiency" />

## What this repository provides

- reusable Python notebooks
- engineering visualizations
- implementation walkthroughs
- benchmark notebooks
- reproducible engineering figures
- reusable Python package
- engineering demonstrations
- developer-oriented documentation

## Engineering notebook sequence

```text
00  Engineering Context
01  Constraints
07  Connected Lanes
11  Engineering Objects
13  Engineering Variables
17  State Estimation
19  Distribution
23  Dynamics
29  Optimization
37  Controllers
43  Benchmarks
```

Each notebook develops one connected stage of the engineering implementation.

## Engineering focus

The Information-Bundling Position Auction (IBPA) separates two independent design variables:

- **Publisher information granularity** (information acquisition)
- **Advertiser disclosure granularity** (information disclosure)

Rather than revealing all available information to advertisers, IBPA selectively bundles information so that publishers can retain detailed knowledge while exposing only the information needed for effective allocation. This separation can improve allocation efficiency, incentive compatibility, and overall welfare while remaining computationally practical.

This repository develops those engineering ideas through Python implementations, reusable visualizations, benchmark notebooks, and implementation examples that support experimentation and future engineering development.

## Engineering architecture

```text
Constraint
↓
Connected lanes
↓
Engineering objects
↓
Engineering variables
↓
Observable states
↓
Indicators
```

This engineering architecture organizes the repository into reusable implementation notebooks, figures, benchmarks, and supporting software while specializing the engineering variables for Information-Bundling Position Auctions.

## Repository structure

```text
figures/
notebooks/
results/
src/
```

The repository is organized around reusable engineering notebooks and supporting Python modules so that implementations, benchmarks, visualizations, and documentation evolve together.

## Future engineering directions

Planned engineering work includes:

- reference Python implementations
- computational benchmarking
- visualization of information bundles
- mechanism comparisons
- implementation profiling
- reusable benchmark scenarios
- developer documentation
- extensible engineering notebooks

## Reference

**Targeting Information in Ad Auction Mechanisms**

arXiv:2601.09541
