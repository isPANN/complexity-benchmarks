# Complexity Benchmarks Dataset Registry — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a comprehensive registry (YAML) and survey (Markdown) of benchmark datasets for computationally hard problems, organized by 13 problem categories.

**Architecture:** Each category gets a YAML registry file populated via web research, then a unified survey.md synthesizes the findings with narrative context. The `pred list` command provides the mapping between standard problem names and the local reduction framework.

**Tech Stack:** YAML (registry), Markdown (survey), `pred` CLI (problem mapping)

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `datasets/registry/01-satisfiability.yaml` | Create | SAT, 3-SAT, Max-SAT, NAE-SAT, QBF, Circuit-SAT datasets |
| `datasets/registry/02-graph-vertex-edge.yaml` | Create | MIS, Vertex Cover, Clique, Coloring, Dominating Set datasets |
| `datasets/registry/03-graph-path-circuit.yaml` | Create | TSP, Hamiltonian, Longest Path, Chinese Postman datasets |
| `datasets/registry/04-graph-connectivity-cut.yaml` | Create | Steiner Tree, Max Cut, Multiway Cut, FVS/FAS datasets |
| `datasets/registry/05-network-flow.yaml` | Create | Integral flow, multicommodity flow datasets |
| `datasets/registry/06-knapsack-partition.yaml` | Create | Knapsack, Bin Packing, Subset Sum, Partition datasets |
| `datasets/registry/07-scheduling.yaml` | Create | Flow Shop, Job Shop, RCPSP, multiprocessor scheduling datasets |
| `datasets/registry/08-set-problems.yaml` | Create | Set Cover, Set Packing, Exact Cover, Hitting Set datasets |
| `datasets/registry/09-sequence-string.yaml` | Create | LCS, SCS, String Correction datasets |
| `datasets/registry/10-mathematical-programming.yaml` | Create | ILP, QUBO, QAP datasets |
| `datasets/registry/11-lattice-number-theory.yaml` | Create | CVP, SVP, Factoring datasets |
| `datasets/registry/12-database-relational.yaml` | Create | BCNF, CQ, relational problem datasets (sparse) |
| `datasets/registry/13-physics-statistical-mechanics.yaml` | Create | Spin Glass, Ising model datasets |
| `datasets/pred-problems.txt` | Create | Local reference file from `pred list` (committed for reproducibility) |
| `datasets/docs/survey.md` | Create | Human-readable survey with narrative |

> **Parallelization note:** Tasks 1–13 are completely independent and may be executed in any order or in parallel. Task 14 (survey) depends on all 13 YAML files. Task 15 (cross-reference) runs last.

---

## Task 0: Setup

**Files:**
- Create: `datasets/registry/` directory
- Create: `datasets/docs/` directory

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p datasets/registry datasets/docs
```

- [ ] **Step 2: Capture `pred` problem list for reference**

```bash
pred list > datasets/pred-problems.txt
```

This file is a reference for mapping standard problem names to `pred_names` throughout the tasks.

- [ ] **Step 3: Commit scaffold**

```bash
git add datasets/
git commit -m "chore: scaffold datasets directory structure"
```

---

## Task 1: Satisfiability (01-satisfiability.yaml)

**Files:**
- Create: `datasets/registry/01-satisfiability.yaml`
- Reference: `datasets/pred-problems.txt`

- [ ] **Step 1: Research datasets**

Web search for benchmark datasets covering: SAT, 3-SAT, Max-SAT, NAE-SAT, QBF, Circuit-SAT.
Key sources to investigate:
- SATLIB (cs.ubc.ca/~hoos/SATLIB)
- SAT Competition / SAT Race annual benchmarks
- MaxSAT Evaluation benchmarks
- QBFLIB
- Circuit SAT benchmarks from hardware verification

For each dataset found, record: name, URL, format, approximate instance count, scale (variables/clauses range), whether solutions are provided, usage context, reference.

- [ ] **Step 2: Write the YAML file**

Create `datasets/registry/01-satisfiability.yaml` following the schema from the spec. Map problems to `pred_names` using the reference file:
- SAT → `Satisfiability`
- 3-SAT → `KSatisfiability/K3`
- k-SAT → `KSatisfiability/KN`
- NAE-SAT → `NAESatisfiability`
- QBF → `QuantifiedBooleanFormulas`
- Circuit-SAT → `CircuitSAT`

- [ ] **Step 3: Validate YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/01-satisfiability.yaml'))"
```

Expected: No errors.

- [ ] **Step 4: Commit**

```bash
git add datasets/registry/01-satisfiability.yaml
git commit -m "feat: add satisfiability dataset registry"
```

---

## Task 2: Graph — Vertex/Edge Problems (02-graph-vertex-edge.yaml)

**Files:**
- Create: `datasets/registry/02-graph-vertex-edge.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: Maximum Independent Set, Vertex Cover, Clique, Graph Coloring, Dominating Set.
Key sources to investigate:
- DIMACS Implementation Challenges (2nd: Clique/Coloring, 10th: Graph Partitioning)
- BHOSLIB (Benchmarks with Hidden Optimum Solutions)
- PACE Challenge (various years for different problems)
- SNAP large network datasets
- Network Repository (networkrepository.com)
- COLOR instances
- Koenig benchmarks

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- MIS → `MaximumIndependentSet/SimpleGraph/One`
- Vertex Cover → `MinimumVertexCover/SimpleGraph/i32`
- Clique → `KClique/SimpleGraph`, `MaximumClique/SimpleGraph/i32`
- Graph Coloring → `KColoring/SimpleGraph/KN`
- Dominating Set → `MinimumDominatingSet/SimpleGraph/i32`

- [ ] **Step 3: Validate YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/02-graph-vertex-edge.yaml'))"
```

- [ ] **Step 4: Commit**

```bash
git add datasets/registry/02-graph-vertex-edge.yaml
git commit -m "feat: add graph vertex/edge dataset registry"
```

---

## Task 3: Graph — Path/Circuit Problems (03-graph-path-circuit.yaml)

**Files:**
- Create: `datasets/registry/03-graph-path-circuit.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: TSP, Hamiltonian Circuit/Path, Longest Path, Chinese Postman, Rural Postman.
Key sources:
- TSPLIB (standard TSP benchmark library)
- VLSI TSP instances
- National TSP instances (country-scale)
- FHCP Challenge (Hamiltonian Cycle Problem)
- Concorde TSP solver test instances

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- TSP → `TravelingSalesman/SimpleGraph/i32`
- Bottleneck TSP → `BottleneckTravelingSalesman`
- Hamiltonian Circuit → `HamiltonianCircuit/SimpleGraph`
- Hamiltonian Path → `HamiltonianPath/SimpleGraph`
- Longest Path → `LongestPath/SimpleGraph/i32`
- Chinese Postman → `MixedChinesePostman/i32`
- Rural Postman → `RuralPostman/SimpleGraph/i32`

- [ ] **Step 3: Validate YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/03-graph-path-circuit.yaml'))"
```

- [ ] **Step 4: Commit**

```bash
git add datasets/registry/03-graph-path-circuit.yaml
git commit -m "feat: add graph path/circuit dataset registry"
```

---

## Task 4: Graph — Connectivity/Cut Problems (04-graph-connectivity-cut.yaml)

**Files:**
- Create: `datasets/registry/04-graph-connectivity-cut.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: Steiner Tree, Max Cut, Multiway Cut, Feedback Vertex Set, Feedback Arc Set.
Key sources:
- SteinLib (Steiner Tree library)
- DIMACS Max-Cut instances
- BiqMac library (Binary Quadratic and Max-Cut)
- PACE Challenge 2016 (Feedback Vertex Set), 2022 (Directed FVS)
- Gset benchmark graphs for Max Cut

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- Steiner Tree → `SteinerTree/SimpleGraph/i32`, `SteinerTreeInGraphs/SimpleGraph/i32`
- Max Cut → `MaxCut/SimpleGraph/i32`
- Multiway Cut → `MinimumMultiwayCut/SimpleGraph/i32`
- FVS → `MinimumFeedbackVertexSet/i32`
- FAS → `MinimumFeedbackArcSet/i32`
- Graph Partitioning → `GraphPartitioning/SimpleGraph`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/04-graph-connectivity-cut.yaml'))"
git add datasets/registry/04-graph-connectivity-cut.yaml
git commit -m "feat: add graph connectivity/cut dataset registry"
```

---

## Task 5: Network Flow (05-network-flow.yaml)

**Files:**
- Create: `datasets/registry/05-network-flow.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: integral flow, multicommodity flow, flow with multipliers, two-commodity flow.
Key sources:
- MIPLIB (flow formulations)
- SNDlib (Survivable Network Design)
- Multicommodity flow benchmarks from OR literature
- NETGEN random network generators

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- Two-Commodity Flow → `DirectedTwoCommodityIntegralFlow`, `UndirectedTwoCommodityIntegralFlow`
- Integral Flow → `IntegralFlowBundles`, `IntegralFlowHomologousArcs`, `IntegralFlowWithMultipliers`
- Path-Constrained Flow → `PathConstrainedNetworkFlow`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/05-network-flow.yaml'))"
git add datasets/registry/05-network-flow.yaml
git commit -m "feat: add network flow dataset registry"
```

---

## Task 6: Knapsack/Partition (06-knapsack-partition.yaml)

**Files:**
- Create: `datasets/registry/06-knapsack-partition.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: Knapsack, Bin Packing, Subset Sum, Partition.
Key sources:
- Pisinger's hard knapsack instances
- OR-Library (Beasley)
- BPPLib (Bin Packing Problem Library)
- ESICUP datasets
- Martello & Toth benchmark instances

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- Knapsack → `Knapsack`
- Bin Packing → `BinPacking/i32`
- Subset Sum → `SubsetSum`
- Partition → `Partition`
- Partially Ordered Knapsack → `PartiallyOrderedKnapsack`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/06-knapsack-partition.yaml'))"
git add datasets/registry/06-knapsack-partition.yaml
git commit -m "feat: add knapsack/partition dataset registry"
```

---

## Task 7: Scheduling (07-scheduling.yaml)

**Files:**
- Create: `datasets/registry/07-scheduling.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: Flow Shop, Job Shop, RCPSP, Multiprocessor Scheduling, precedence-constrained scheduling.
Key sources:
- Taillard's benchmark instances (Flow Shop, Job Shop)
- OR-Library scheduling instances
- PSPLIB (Project Scheduling Problem Library)
- Adams, Balas & Zawack (ABZ) instances
- Lawrence (LA) instances
- Demirkol, Mehta & Uzsoy (DMU) instances

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- Flow Shop → `FlowShopScheduling`
- Multiprocessor Scheduling → `MultiprocessorScheduling`
- Resource-Constrained → `ResourceConstrainedScheduling`
- Precedence-Constrained → `PrecedenceConstrainedScheduling`
- Minimum Tardiness → `MinimumTardinessSequencing`
- Staff Scheduling → `StaffScheduling`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/07-scheduling.yaml'))"
git add datasets/registry/07-scheduling.yaml
git commit -m "feat: add scheduling dataset registry"
```

---

## Task 8: Set Problems (08-set-problems.yaml)

**Files:**
- Create: `datasets/registry/08-set-problems.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: Set Cover, Set Packing, Exact Cover, Hitting Set.
Key sources:
- OR-Library SCP instances (Beasley)
- RAIL benchmark instances (large-scale set cover)
- CSPLib
- Steiner triple systems (exact cover)

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- Set Cover → `MinimumSetCovering/i32`
- Set Packing → `MaximumSetPacking/One`
- Exact Cover by 3-Sets → `ExactCoverBy3Sets`
- Hitting Set → `MinimumHittingSet`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/08-set-problems.yaml'))"
git add datasets/registry/08-set-problems.yaml
git commit -m "feat: add set problems dataset registry"
```

---

## Task 9: Sequence/String (09-sequence-string.yaml)

**Files:**
- Create: `datasets/registry/09-sequence-string.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: LCS, SCS, String-to-String Correction (Edit Distance).
Key sources:
- CSPLib
- BAliBASE (biological sequence alignment)
- Biological sequence repositories (for LCS/SCS applications)
- DNA/protein sequence benchmarks used in bioinformatics

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- LCS → `LongestCommonSubsequence`
- SCS → `ShortestCommonSupersequence`
- String Correction → `StringToStringCorrection`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/09-sequence-string.yaml'))"
git add datasets/registry/09-sequence-string.yaml
git commit -m "feat: add sequence/string dataset registry"
```

---

## Task 10: Mathematical Programming (10-mathematical-programming.yaml)

**Files:**
- Create: `datasets/registry/10-mathematical-programming.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: ILP, QUBO, Quadratic Assignment.
Key sources:
- MIPLIB (Mixed Integer Programming Library) — multiple versions
- QAPLIB (Quadratic Assignment Problem Library)
- QPLIB (Quadratic Programming Library)
- MINLPLib
- QUBO benchmarks from quantum computing literature

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- ILP → `ILP/bool`, `ILP/i32`
- QUBO → `QUBO/f64`
- QAP → `QuadraticAssignment`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/10-mathematical-programming.yaml'))"
git add datasets/registry/10-mathematical-programming.yaml
git commit -m "feat: add mathematical programming dataset registry"
```

---

## Task 11: Lattice/Number Theory (11-lattice-number-theory.yaml)

**Files:**
- Create: `datasets/registry/11-lattice-number-theory.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: Closest Vector Problem, Shortest Vector Problem, Factoring.
Key sources:
- SVP Challenge (TU Darmstadt)
- Lattice Challenge (TU Darmstadt)
- RSA Factoring Challenge (historical, discontinued)
- NIST post-quantum cryptography lattice benchmarks
- HElib/SEAL lattice benchmarks

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- CVP → `ClosestVectorProblem/i32`
- Factoring → `Factoring`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/11-lattice-number-theory.yaml'))"
git add datasets/registry/11-lattice-number-theory.yaml
git commit -m "feat: add lattice/number theory dataset registry"
```

---

## Task 12: Database/Relational (12-database-relational.yaml)

**Files:**
- Create: `datasets/registry/12-database-relational.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: BCNF violation detection, conjunctive query evaluation/containment, key/attribute identification.
Key sources:
- Database theory papers (likely no standard benchmark libraries)
- TPC benchmarks (schema complexity aspects)
- Functional dependency datasets from data profiling research
- Metanome project datasets

Note: expect sparse coverage. Document gaps explicitly.

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- BCNF → `BoyceCoddNormalFormViolation`
- Conjunctive Query → `ConjunctiveBooleanQuery`, `ConjunctiveQueryFoldability`
- Additional Key → `AdditionalKey`
- Prime Attribute → `PrimeAttributeName`
- Minimum Key → `MinimumCardinalityKey`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/12-database-relational.yaml'))"
git add datasets/registry/12-database-relational.yaml
git commit -m "feat: add database/relational dataset registry"
```

---

## Task 13: Physics/Statistical Mechanics (13-physics-statistical-mechanics.yaml)

**Files:**
- Create: `datasets/registry/13-physics-statistical-mechanics.yaml`

- [ ] **Step 1: Research datasets**

Web search for benchmarks covering: Spin Glass, Ising models.
Key sources:
- Spin Glass Server (University of Cologne)
- D-Wave chimera/pegasus graph instances
- Ising model instances from statistical physics literature
- Random field Ising model benchmarks
- Quantum annealing benchmark sets

- [ ] **Step 2: Write the YAML file**

`pred_names` mapping:
- Spin Glass → `SpinGlass/SimpleGraph/i32`, `SpinGlass/SimpleGraph/f64`

- [ ] **Step 3: Validate YAML and commit**

```bash
python3 -c "import yaml; yaml.safe_load(open('datasets/registry/13-physics-statistical-mechanics.yaml'))"
git add datasets/registry/13-physics-statistical-mechanics.yaml
git commit -m "feat: add physics/statistical mechanics dataset registry"
```

---

## Task 14: Write Survey Document

**Files:**
- Create: `datasets/docs/survey.md`
- Reference: all 13 registry YAML files

- [ ] **Step 1: Read all completed YAML files**

Read all 13 registry files to understand the full landscape of datasets collected.

- [ ] **Step 2: Write survey.md**

Structure:
1. **Overview** — What this survey covers, how it's organized, relationship to `pred` framework
2. **Per-category sections (13)** — For each:
   - Problem background (2-3 sentences)
   - Key datasets with narrative commentary
   - Format notes and practical tips
   - Notable gaps
   - Cross-references to other categories
3. **Summary table** — Matrix of problems vs datasets
4. **Cross-category datasets** — DIMACS, OR-Library, MIPLIB, etc. that span categories

- [ ] **Step 3: Commit**

```bash
git add datasets/docs/survey.md
git commit -m "feat: add human-readable benchmark survey"
```

---

## Task 15: Cross-Reference and Final Review

- [ ] **Step 1: Verify `pred_names` coverage**

Cross-check all `pred_names` used in YAML files against `pred list` output. Ensure no typos or mismatches.

```bash
# Extract all pred_names from YAML files
grep -r "pred_names" datasets/registry/ | grep -oE '"[^"]*"'
```

- [ ] **Step 2: Verify YAML consistency**

Validate all 13 files parse correctly:

```bash
for f in datasets/registry/*.yaml; do
  python3 -c "import yaml; yaml.safe_load(open('$f'))" && echo "OK: $f" || echo "FAIL: $f"
done
```

- [ ] **Step 3: Final commit**

```bash
git add -A datasets/
git commit -m "chore: final cross-reference and consistency pass"
```
