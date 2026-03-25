# Complexity Benchmarks Dataset Registry — Design Spec

## Overview

A structured survey and machine-readable registry of publicly available benchmark datasets for computationally hard problems (NP-hard and beyond). The project catalogs datasets organized by problem category, with cross-references to a reduction framework (`pred` tool) that implements 112 problem types and 76 reductions.

## Goals

1. **Broad coverage**: Survey well-known benchmark datasets across all major categories of computational complexity problems, not limited to any single list.
2. **Dual format**: Produce both machine-readable YAML registry files and a human-readable Markdown survey.
3. **Category-first organization**: Group by problem category (e.g., satisfiability, graph theory, scheduling), with representative problems and their datasets within each category.
4. **Practical metadata**: Each dataset entry includes enough information to evaluate relevance and start using the data (URL, format, scale, known solutions).
5. **`pred` mapping**: Where applicable, link problems to their corresponding names in the `pred` reduction framework.

## Non-Goals

- Downloading or hosting actual dataset files in this repository.
- Implementing parsers or format converters (separate concern).
- Exhaustive coverage of every obscure dataset — focus on well-established, widely-used benchmarks.

## File Structure

```
datasets/
  registry/
    01-satisfiability.yaml
    02-graph-vertex-edge.yaml
    03-graph-path-circuit.yaml
    04-graph-connectivity-cut.yaml
    05-network-flow.yaml
    06-knapsack-partition.yaml
    07-scheduling.yaml
    08-set-problems.yaml
    09-sequence-string.yaml
    10-mathematical-programming.yaml
    11-lattice-number-theory.yaml
    12-database-relational.yaml
    13-physics-statistical-mechanics.yaml
  docs/
    survey.md
```

## YAML Schema

Each category file follows this schema:

```yaml
category: "<category-slug>"
description: "<one-line description of the category>"
problems:
  - name: "<standard problem name>"
    aliases: ["<alternative name>", ...]          # optional
    pred_names: ["<pred tool name>", ...]          # optional, maps to pred framework
    datasets:
      - name: "<dataset name>"
        url: "<primary URL>"
        format: "<file format, e.g. DIMACS CNF, TSPLIB, CSV>"
        instance_count: <approximate number>       # optional
        scale:                                     # optional, keys vary by problem
          <dimension>: "<range string>"             # e.g. variables: "20-10000" (SAT),
                                                    #      cities: "14-85900" (TSP),
                                                    #      items: "50-10000" (Knapsack)
        has_optimal_solution: <true|false>          # optional
        usage: "<where/how this dataset is commonly used>"
        reference: "<citation or author, year>"    # optional
        notes: "<additional context>"              # optional
```

### Field Details

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Dataset name |
| `url` | Yes | Primary download/info URL |
| `format` | No | File format (DIMACS CNF, TSPLIB, etc.) |
| `instance_count` | No | Approximate number of instances |
| `scale` | No | Key-value pairs describing instance size ranges |
| `has_optimal_solution` | No | Whether optimal/best-known solutions are provided |
| `usage` | No | Common use context (competitions, papers, etc.) |
| `reference` | No | Paper or author citation |
| `notes` | No | Additional context |

## Survey Document (`survey.md`)

The Markdown survey will contain:

1. **Overview** — Landscape of computational complexity benchmarks, how this survey is organized.
2. **Per-category sections** — For each of the 13 categories:
   - Brief problem background and significance
   - Key datasets with narrative commentary (not just a table)
   - Format notes and practical tips for using the data
   - Notable gaps (problems with few or no public datasets)
   - Cross-references to related categories where datasets overlap
3. **Summary table** — Matrix mapping major problems to available datasets.
4. **Cross-category datasets** — Datasets that span multiple categories (e.g., DIMACS challenges cover SAT, Clique, Coloring; OR-Library covers multiple optimization problems).

## Problem Categories and Survey Scope

### 1. Satisfiability
SAT, 3-SAT, Max-SAT, NAE-SAT, QBF, Circuit-SAT.
Target sources: SATLIB, SAT Competition, MaxSAT Evaluation, QBFLIB.

### 2. Graph — Vertex/Edge Problems
Maximum Independent Set, Vertex Cover, Clique, Graph Coloring, Dominating Set.
Target sources: DIMACS Challenge, SNAP, Network Repository, BHOSLIB, PACE Challenge.

### 3. Graph — Path/Circuit Problems
TSP, Hamiltonian Circuit/Path, Longest Path, Chinese Postman, Rural Postman.
Target sources: TSPLIB, VLSI datasets, FHCP, National TSP instances.

### 4. Graph — Connectivity/Cut Problems
Steiner Tree, Max Cut, Multiway Cut, Feedback Vertex/Arc Set.
Target sources: SteinLib, DIMACS Max-Cut, BiqMac, PACE Challenge (FVS).

### 5. Network Flow
Integral flow, multicommodity flow, flow with multipliers.
Target sources: MIPLIB (flow formulations), multicommodity flow benchmarks.

### 6. Knapsack/Partition
Knapsack, Bin Packing, Subset Sum, Partition.
Target sources: Pisinger's hard instances, OR-Library, BPPLib.

### 7. Scheduling
Flow Shop, Multiprocessor Scheduling, Resource-Constrained Project Scheduling.
Target sources: OR-Library, Taillard's benchmarks, PSPLIB, job shop benchmarks.

### 8. Set Problems
Set Cover, Set Packing, Exact Cover, Hitting Set.
Target sources: OR-Library (SCP), CSPLib.

### 9. Sequence/String
Longest Common Subsequence, Shortest Common Supersequence, String Correction.
Target sources: CSPLib, biological sequence databases (BAliBASE).

### 10. Mathematical Programming
ILP, QUBO, Quadratic Assignment.
Target sources: MIPLIB, QAPLIB, MINLPLib, QPLIB.

### 11. Lattice/Number Theory
Closest Vector Problem, Factoring.
Target sources: SVP Challenge, Lattice Challenge, RSA Factoring Challenge (historical).

### 12. Database/Relational
BCNF Violation, Conjunctive Query, Additional Key, Prime Attribute.
Expected: sparse coverage; will document gaps.

### 13. Physics/Statistical Mechanics
Spin Glass, Ising models.
Target sources: Spin Glass Server, D-Wave Chimera/Pegasus instances, random field Ising benchmarks.

## Implementation Approach

1. Research datasets systematically, category by category.
2. For each category, create the YAML registry file with verified entries.
3. After all categories are populated, write the survey.md with narrative content.
4. Cross-reference datasets that appear in multiple categories.
5. Map problems to `pred` framework names where applicable.

## Success Criteria

- All 13 category YAML files created with at least the well-known datasets documented.
- Survey.md provides useful narrative context beyond what the YAML contains.
- `pred_names` mapping is populated for problems that exist in the `pred` framework.
- Gaps are explicitly noted rather than silently omitted.
- URLs are real and point to actual dataset sources.
