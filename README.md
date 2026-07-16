# Information Bundling Auctions

This repository specifies **information constraints** as an engineering variable for allocation efficiency.

It develops a connected engineering specification for understanding how information acquisition, information disclosure, and auction design interact to improve allocation efficiency in Information-Bundling Position Auctions (IBPA).

## Engineering statement

> **Information Constraints Specify Allocation Efficiency**

<img src="figures/2601-09541-hero.png" alt="Information Constraints Specify Allocation Efficiency" />

## Engineering 

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

## Repository construction

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

Each notebook develops one connected stage of the engineering specification.

## Repository outputs

* reusable engineering notebooks
* repository context figures
* machine-readable engineering specifications
* reusable Python package
* engineering demonstrations and benchmarks

## Engineering focus

This repository interprets **Targeting Information in Ad Auction Mechanisms** (arXiv:2601.09541) through a reusable engineering specification.

The central engineering variable separates two independent design levers:

* **Publisher information granularity** (information acquisition)
* **Advertiser disclosure granularity** (information disclosure)

The Information-Bundling Position Auction (IBPA) demonstrates how retaining granular publisher information while limiting advertiser disclosure can improve allocation efficiency, incentive compatibility, and overall welfare.

The repository develops these engineering variables through connected notebooks, reusable figures, and machine-readable engineering context so the same Notebook 00 architecture can be reused across future engineering repositories while specializing only the engineering context, connected lanes, and engineering variables for a new domain.
