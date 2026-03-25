# Survey of Benchmark Datasets for Computationally Hard Problems

## 1. Overview

This survey catalogs publicly available benchmark datasets for computationally hard (typically NP-hard or harder) problems, organized into 17 categories that align with the `pred` reduction framework's classification of 112 problem types connected by 76 known reductions. The goal is practical: to help researchers find the right dataset for evaluating algorithms on specific problem types, and to understand how datasets relate across problem boundaries.

The 17 categories are:

1. Satisfiability
2. Graph Vertex and Edge Problems
3. Graph Path and Circuit Problems
4. Graph Connectivity and Cut Problems
5. Network Flow
6. Knapsack and Partition
7. Scheduling
8. Set Problems
9. Sequence and String Problems
10. Mathematical Programming
11. Lattice and Number Theory
12. Database and Relational Problems
13. Physics and Statistical Mechanics
14. Vehicle Routing
15. Facility Location
16. Constraint Satisfaction
17. Graph Matching

Each section below provides problem background, commentary on key datasets (not merely a listing), format notes, gaps, and cross-references. A summary table and a discussion of cross-category datasets follow the per-category sections.

---

## 2. Satisfiability

Boolean satisfiability (SAT) is the canonical NP-complete problem and the most extensively benchmarked problem family in computational complexity. The landscape is mature: annual competitions have been running for over two decades, and instance libraries span millions of variables.

### Key Datasets

**SATLIB Benchmark Suite** (~3,900 instances) remains the foundational reference collection. Its strength lies in breadth: uniform random 3-SAT at the phase transition, graph coloring encodings, planning problems, quasigroup completion, and the original DIMACS challenge instances (AIM, JNH, DUBOIS, PARITY). For anyone starting SAT solver development, SATLIB is the first stop.

**SAT Competition Benchmarks (2002--2024)** represent the evolving frontier. The full normalized archive on Zenodo contains over 7,300 instances (28.7 GB compressed) spanning crafted, combinatorial, and industrial categories. The 2024 competition alone contributes 400 instances with variables ranging from 100 to 5 million. These are essential for evaluating solver performance on modern, practically motivated instances.

**GBD Benchmark Database** is a meta-resource: it indexes SAT competition instances with extracted features and hash-based cross-referencing, making it possible to find instances with specific structural properties rather than searching by filename.

For **3-SAT** specifically, SATLIB provides 8,000 uniform random instances at the phase transition ratio (~4.26 clauses per variable), with separate satisfiable and unsatisfiable sets of 1,000 instances each across variable counts from 20 to 250. The Controlled Random 3-SAT (CBS) collection adds 36,000 instances with controlled backbone sizes, enabling systematic study of how solution space structure affects solver performance.

**Max-SAT** has its own competition ecosystem. The MaxSAT Evaluation series (running since 2006) provides ~2,000 instances in WCNF format across weighted and unweighted tracks. The University of Toronto maintains a master archive of instances from all evaluation years.

**QBF** (quantified boolean formulas) extends SAT to PSPACE-completeness. QBFLIB hosts over 13,000 instances from model checking, formal verification, and synthesis, while the QBFGallery competition series (since 2004) selects challenging subsets.

**Circuit-SAT** is well-served by the ISCAS-85 (10 combinational circuits) and ISCAS-89 (31 sequential circuits) benchmark suites, which have been the standard in EDA research since the late 1980s. The EPFL Combinational Benchmark Suite provides 23 circuits in modern formats (Verilog, VHDL, BLIF, AIGER). Velev's processor verification benchmarks produce some of the largest structured SAT instances available.

### Format Notes

The DIMACS CNF format is universal for SAT. QDIMACS extends it for QBF. WCNF adds weights for Max-SAT. Circuit-SAT uses various hardware description formats (Verilog, AIGER, ISCAS netlist) or can be encoded into CNF.

### Notable Gaps

NAE-SAT (Not-All-Equal SAT) has no large-scale dedicated benchmark suite; researchers typically encode it as standard SAT or generate instances ad hoc. D-Wave provides some NAE-3-SAT instances for quantum computing comparisons, but these are limited in scope.

### Cross-References

SAT encodings underlie benchmarks in graph coloring (Category 2), circuit verification (this category), and spin glass ground state computation (Category 13). SATLIB itself contains graph coloring and planning instances, bridging to Categories 2 and 3.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| SAT | SATLIB Benchmark Suite | DIMACS CNF | 3900 | 20-10000 variables; 91-500000 clauses | Yes | [link](https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html) |
| SAT | SAT Competition Benchmarks (2002-2024) | DIMACS CNF | 7330 | 10-10000000 variables; 50-50000000 clauses | Yes | [link](https://zenodo.org/records/15125952) |
| SAT | SAT Competition 2024 | DIMACS CNF | 400 | 100-5000000 variables; 300-30000000 clauses | Yes | [link](https://satcompetition.github.io/2024/) |
| SAT | GBD Benchmark Database | DIMACS CNF | - | - | - | [link](https://benchmark-database.de/) |
| 3-SAT | SATLIB Uniform Random 3-SAT | DIMACS CNF | 8000 | 20-250 variables; 91-1065 clauses | Yes | [link](https://www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/RND3SAT/descr.html) |
| 3-SAT | SATLIB Controlled Random 3-SAT (CBS) | DIMACS CNF | 36000 | 100 variables; 403-449 clauses | Yes | [link](https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html) |
| k-SAT | SATLIB Random k-SAT Instances | DIMACS CNF | - | - | Yes | [link](https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html) |
| Max-SAT | MaxSAT Evaluation Benchmarks | WCNF (Weighted CNF) | 2000 | 10-1000000 variables; 50-5000000 clauses | Yes | [link](https://maxsat-evaluations.github.io/) |
| Max-SAT | MaxSAT Evaluation 2024 | WCNF | - | - | Yes | [link](https://maxsat-evaluations.github.io/2024/) |
| Max-SAT | University of Toronto MaxSAT Library | WCNF | - | - | - | [link](http://www.cs.toronto.edu/maxsat-lib/maxsat-instances/ms-evals/) |
| NAE-SAT | Random NAE-3-SAT Phase Transition Instances | Custom / DIMACS-like | - | - | Yes | [link](https://github.com/dwave-examples/NAE3SAT) |
| NAE-SAT | SATLIB NAE-SAT Encodings | DIMACS CNF | - | - | - | [link](https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html) |
| QBF | QBFLIB | QDIMACS | 13000 | - | Yes | [link](https://www.qbflib.org/) |
| QBF | QBFGallery 2023 | QDIMACS, QCIR, QAIGER | - | - | Yes | [link](https://qbf23.pages.sai.jku.at/gallery/) |
| Circuit-SAT | ISCAS-85 Combinational Benchmark Circuits | ISCAS netlist, Verilog, AIGER | 10 | 17-7552 gates | Yes | [link](https://filebox.ece.vt.edu/~mhsiao/iscas85.html) |
| Circuit-SAT | ISCAS-89 Sequential Benchmark Circuits | ISCAS netlist, Verilog | 31 | - | Yes | [link](https://filebox.ece.vt.edu/~mhsiao/iscas89.html) |
| Circuit-SAT | ITC-99 Benchmark Circuits | Verilog, VHDL | - | - | Yes | [link](https://www.cerc.utexas.edu/itc99-benchmarks/bendoc1.html) |
| Circuit-SAT | EPFL Combinational Benchmark Suite | Verilog, VHDL, BLIF, AIGER | 23 | - | Yes | [link](https://github.com/ispras/hdl-benchmarks) |
| Circuit-SAT | SATLIB Circuit Fault Analysis (BF) | DIMACS CNF | - | - | Yes | [link](https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html) |
| Circuit-SAT | Velev Formal Verification Benchmarks | DIMACS CNF | - | - | Yes | [link](https://www.cs.ubc.ca/~hoos/SATLIB/I-Velev03/index.htm) |

---

## 3. Graph Vertex and Edge Problems

This category covers selection problems on graph vertices and edges: independent set, vertex cover, clique, graph coloring, and dominating set. The DIMACS Implementation Challenges have been the backbone of benchmarking in this area since the early 1990s.

### Key Datasets

**DIMACS 2nd Implementation Challenge** (37 instances, 125--4,000 vertices) is the single most important benchmark collection for maximum clique, and by complement reduction, for maximum independent set and minimum vertex cover. It includes random graphs, Brock graphs, MANN graphs, Hamming graphs, Keller graphs, and others. After 30+ years, several instances still lack proven optimal solutions.

**BHOSLIB** (Benchmarks with Hidden Optimum Solutions, 40 instances) fills a critical gap: unlike DIMACS instances where optima are often unknown, BHOSLIB instances have planted solutions with known optima (clique sizes 30--100). These dense graphs are considered significantly harder than the DIMACS suite for modern solvers. A single collection serves triple duty for MIS, vertex cover, and clique.

**SNAP Large Network Collection** (~80 networks, up to 226M vertices) and **Network Repository** (~6,659 graphs) provide real-world instances at scales far beyond traditional benchmarks. These are essential for evaluating heuristic and local-search algorithms (e.g., NuMVC, FastVC) on social networks, web graphs, citation networks, and infrastructure graphs.

For **graph coloring**, the COLOR02/03/04 collection (119 instances) remains definitive, with instance families including random DSJC graphs, register allocation graphs, Leighton graphs, queen graphs, and Latin squares. Chromatic numbers range from 4 to 76, with many still open. The Trick collection provides a curated subset with tracked best-known bounds.

**PACE Challenges** have become the gold standard for vertex cover (PACE 2019, 200 instances) and dominating set (PACE 2025, 200 instances), with instances specifically designed to challenge parameterized algorithms.

### Format Notes

DIMACS graph format (.col, .clq) is the traditional standard. PACE uses its own .hgr format. Large network repositories use edge lists (TSV), MTX (Matrix Market), or GraphML.

### Notable Gaps

Graph isomorphism and subgraph isomorphism benchmarks are catalogued in Category 17 (Graph Matching).

### Cross-References

BHOSLIB and DIMACS instances appear across MIS, vertex cover, clique, and coloring. The DIMACS 10th Challenge instances (Category 4, graph partitioning) are also used for clique algorithm scalability evaluation. Max clique is equivalent to MIS on the complement graph, and vertex cover equals n minus MIS, so these three problems share all benchmark suites.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Maximum Independent Set | DIMACS 2nd Implementation Challenge (Clique complements) | DIMACS | 37 | 125 to 4,000 vertices; 6,963 to 5,506,380 edges | No | [link](https://iridia.ulb.ac.be/~fmascia/maximum_clique/DIMACS-benchmark) |
| Maximum Independent Set | BHOSLIB (Benchmarks with Hidden Optimum Solutions) | DIMACS | 40 | 450 to 4,000 vertices; 83,151 to 7,425,226 edges | Yes | [link](https://sites.google.com/view/bhoslib/home) |
| Maximum Independent Set | SNAP Large Network Collection | TSV edge list | 80 | 4,039 to 226,000,000 vertices; 88,234 to 480,000,000 edges | No | [link](https://snap.stanford.edu/data/) |
| Maximum Independent Set | Network Repository | MTX, edge list, GML, GraphML | 6659 | tens to millions vertices; tens to hundreds of millions edges | No | [link](https://networkrepository.com/) |
| Minimum Vertex Cover | PACE 2019 Vertex Cover Challenge | PACE graph format (.hgr) | 200 | small to large (ordered by increasing difficulty) vertices; varies edges | Yes | [link](https://pacechallenge.org/2019/vc/) |
| Minimum Vertex Cover | BHOSLIB (Benchmarks with Hidden Optimum Solutions) | DIMACS | 40 | 450 to 4,000 vertices; 83,151 to 7,425,226 edges | Yes | [link](https://sites.google.com/view/bhoslib/home) |
| Minimum Vertex Cover | DIMACS 2nd Implementation Challenge (complement reduction) | DIMACS | 37 | 125 to 4,000 vertices; 6,963 to 5,506,380 edges | No | [link](https://iridia.ulb.ac.be/~fmascia/maximum_clique/DIMACS-benchmark) |
| Minimum Vertex Cover | Network Repository (large real-world graphs) | MTX, edge list | 6659 | tens to millions vertices; tens to hundreds of millions edges | No | [link](https://networkrepository.com/) |
| Maximum Clique | DIMACS 2nd Implementation Challenge | DIMACS | 37 | 125 to 4,000 vertices; 6,963 to 5,506,380 edges | No | [link](https://iridia.ulb.ac.be/~fmascia/maximum_clique/DIMACS-benchmark) |
| Maximum Clique | BHOSLIB (Benchmarks with Hidden Optimum Solutions) | DIMACS (ASCII and binary) | 40 | 450 to 4,000 vertices; 83,151 to 7,425,226 edges | Yes | [link](https://iridia.ulb.ac.be/~fmascia/maximum_clique/BHOSLIB-benchmark) |
| Maximum Clique | DIMACS 10th Implementation Challenge (Graph Partitioning) | METIS, DIMACS | 100 | thousands to millions vertices; thousands to tens of millions edges | No | [link](https://sites.cc.gatech.edu/dimacs10/) |
| Graph Coloring | COLOR02/03/04 Instances (DIMACS Graph Coloring) | DIMACS (.col, .col.b) | 119 | 11 to 1,000 vertices; 20 to 307,350 edges | No | [link](https://mat.tepper.cmu.edu/COLOR/instances.html) |
| Graph Coloring | BHOSLIB Vertex Coloring Instances | DIMACS | 40 | 450 to 4,000 vertices; 83,151 to 7,425,226 edges | Yes | [link](https://sites.google.com/view/bhoslib/home) |
| Graph Coloring | Graph Coloring Benchmarks (Trick collection) | DIMACS | 50 | 11 to 1,000 vertices; 20 to 245,830 edges | No | [link](https://sites.google.com/site/graphcoloring/vertex-coloring) |
| Minimum Dominating Set | PACE 2025 Dominating Set Challenge | DIMACS .gr | 200 | varies (planar and structured graphs) vertices; varies edges | Yes | [link](https://pacechallenge.org/2025/ds/) |
| Minimum Dominating Set | DIMACS 2nd Implementation Challenge (complement-based) | DIMACS | 37 | 125 to 4,000 vertices; 6,963 to 5,506,380 edges | No | [link](https://iridia.ulb.ac.be/~fmascia/maximum_clique/DIMACS-benchmark) |
| Minimum Dominating Set | SNAP Large Network Collection | TSV edge list | 80 | 4,039 to 226,000,000 vertices; 88,234 to 480,000,000 edges | No | [link](https://snap.stanford.edu/data/) |
| Minimum Dominating Set | Network Repository | MTX, edge list, GML, GraphML | 6659 | tens to millions vertices; tens to hundreds of millions edges | No | [link](https://networkrepository.com/) |

---

## 4. Graph Path and Circuit Problems

This category covers TSP variants, Hamiltonian path/cycle problems, longest path, and postman problems. TSP is by far the most extensively benchmarked optimization problem in history.

### Key Datasets

**TSPLIB** (110 symmetric instances, 14--85,900 cities) is to TSP what SATLIB is to SAT: the definitive benchmark. All 110 instances have been solved to optimality by the Concorde solver. Instances come from PCB drilling, VLSI design, and synthetic constructions. Despite being fully solved, TSPLIB remains the standard for comparing heuristic quality and solver performance.

**VLSI TSP Instances** (102 instances, up to 744,710 cities) and **National TSP Instances** (25 country-scale instances, up to 71,009 cities) extend TSPLIB to larger scales. The national instances, derived from geographic feature databases, provide a compelling real-world motivation. Approximately half of the national instances have proven optimal solutions.

TSPLIB also contains 19 **asymmetric TSP** instances (17--443 cities) and 9 **Hamiltonian cycle** instances (1,000--5,000 vertices), though both collections are small.

The **FHCP Challenge Set** (1,001 instances, 66--9,528 vertices) is a standout for Hamiltonian cycle research. All instances are Hamiltonian but structurally difficult; the best competition submission solved 985 of 1,001. Difficulty here is structural rather than size-based, making this collection unusually well-designed for algorithm evaluation.

For **longest path**, the Karlsruhe Longest Paths (KaLP) benchmark provides maze-based and real-world-derived instances.

**Corberan's arc routing repository** (University of Valencia) covers both the mixed Chinese Postman Problem and the Rural Postman Problem, with 118 RPP instances across five groups.

### Format Notes

TSPLIB format is the universal standard for TSP and variants. HCP instances use edge-list formats. Arc routing instances use custom text formats specific to each problem variant.

### Notable Gaps

The asymmetric TSP collection in TSPLIB is small (19 instances, max 443 cities) and could use expansion. Bottleneck TSP has no dedicated benchmark; researchers repurpose standard TSPLIB instances. The Hamiltonian path problem has no dedicated benchmark suite and relies on adapted FHCP instances.

### Cross-References

TSPLIB instances are used across TSP, ATSP, bottleneck TSP, and Hamiltonian cycle/path. The FHCP Challenge Set serves both Hamiltonian cycle and path research. TSP is closely related to the vehicle routing problem (Category 14).


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Traveling Salesman Problem | TSPLIB (Symmetric TSP) | TSPLIB | 110 | 14-85900 cities | Yes | [link](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) |
| Traveling Salesman Problem | VLSI TSP Instances | TSPLIB | 102 | 131-744710 cities | No | [link](https://www.math.uwaterloo.ca/tsp/vlsi/index.html) |
| Traveling Salesman Problem | National TSP Instances | TSPLIB | 25 | 29-71009 cities | No | [link](https://www.math.uwaterloo.ca/tsp/world/countries.html) |
| Traveling Salesman Problem | Concorde TSPLIB Benchmarks | TSPLIB | 110 | 14-85900 cities | Yes | [link](https://www.math.uwaterloo.ca/tsp/concorde/benchmarks/bench99.html) |
| Traveling Salesman Problem | TSP Test Data (Waterloo) | TSPLIB | - | 29-744710 cities | No | [link](https://www.math.uwaterloo.ca/tsp/data/index.html) |
| Asymmetric Traveling Salesman Problem | TSPLIB (Asymmetric TSP) | TSPLIB | 19 | 17-443 cities | Yes | [link](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) |
| Bottleneck Traveling Salesman Problem | TSPLIB (used for Bottleneck TSP) | TSPLIB | 110 | 14-85900 cities | No | [link](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) |
| Hamiltonian Circuit | TSPLIB (HCP Instances) | TSPLIB/HCP | 9 | 1000-5000 vertices | Yes | [link](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) |
| Hamiltonian Circuit | FHCP Challenge Set | HCP (edge list) | 1001 | 66-9528 vertices | Yes | [link](https://sites.flinders.edu.au/flinders-hamiltonian-cycle-project/fhcp-challenge-set/) |
| Hamiltonian Circuit | FHCP TSP/HCP Benchmark Set | TSPLIB/HCP | - | 66-9528 vertices | Yes | [link](https://sites.flinders.edu.au/flinders-hamiltonian-cycle-project/tsp-and-hcp-benchmark-set/) |
| Hamiltonian Path | FHCP Challenge Set (adapted) | HCP (edge list) | 1001 | 66-9528 vertices | Yes | [link](https://sites.flinders.edu.au/flinders-hamiltonian-cycle-project/fhcp-challenge-set/) |
| Longest Path | Karlsruhe Longest Paths (KaLP) | DIMACS (mazes), METIS (others) | - | 2 categories | Yes | [link](https://karlsruhelongestpaths.github.io/) |
| Chinese Postman Problem | Corberan Arc Routing Instances (MCPP) | Custom (text) | - | 4 problem_variants | No | [link](https://www.uv.es/corberan/instancias.htm) |
| Rural Postman Problem | Corberan Arc Routing Instances (RPP) | Custom (text) | 118 | 5 groups | No | [link](https://www.uv.es/corberan/instancias.htm) |
| Rural Postman Problem | Multi-trip Multi-depot RPP Instances | pkl, net | - | undirected weighted multi-graph graph_type | No | [link](https://ieee-dataport.org/documents/multi-trip-multi-depot-rural-postman-problem-instances) |

---

## 5. Graph Connectivity and Cut Problems

This category covers Steiner trees, max cut, multiway cut, feedback vertex/arc sets, and graph partitioning. The problems here arise naturally in network design, VLSI layout, and circuit testing.

### Key Datasets

**SteinLib** (Zuse Institute Berlin) is the definitive Steiner tree benchmark, with instance groups ranging from random complete graphs (B, C series) to sparse graphs (E series) and real-world VLSI instances. The STP format is well-documented. The newer **SteBen** benchmark targets neural combinatorial optimization solvers specifically.

For **max cut**, the ecosystem is rich. **Gset** (71 instances, 800--20,000 vertices) is the workhorse benchmark, with best-known solutions still being improved. **BiqMac Library** provides medium-scale instances (20--500 vertices) with proven optimal solutions via semidefinite programming, making it valuable for exact solver validation. The **DIMACS 7th Challenge** contributes Ising-model spin glass instances, connecting max cut directly to statistical mechanics.

**Multiway cut** is served by DIMACS min-cut/max-flow instances and the DTU benchmark collection, both in DIMACS format with CC BY 4.0 licensing.

The **PACE Challenge series** provides excellent benchmarks for feedback vertex set (PACE 2016, 130 instances) and directed feedback vertex set (PACE 2022, with both exact and heuristic tracks).

For **graph partitioning**, the **Walshaw Archive** (34 graphs, up to 449K nodes) has tracked results from 13 partitioning methods since 2000, with results for k in {2, 4, 8, 16, 32, 64} and multiple balance parameters. The **DIMACS 10th Challenge** extends this with additional synthetic and real-world graphs.

### Format Notes

Steiner tree uses the STP format. Max cut instances use edge-list or sparse matrix formats. Graph partitioning universally uses METIS format. PACE challenges use their own format specifications.

### Notable Gaps

Feedback arc set has no dedicated benchmark; researchers adapt directed FVS instances from PACE 2022. The multiway cut problem (for k > 2 terminals) has limited dedicated benchmark coverage.

### Cross-References

Max cut is equivalent to Ising spin glass ground state optimization (Category 13). BiqMac and Gset instances appear in both categories. The DIMACS 10th Challenge instances are also used for maximum clique scalability testing (Category 2). Steiner tree connects to network design problems in Category 5.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Steiner Tree | SteinLib | STP | - | - | - | [link](https://steinlib.zib.de/steinlib.php) |
| Steiner Tree | SteBen | Custom | - | - | - | [link](https://openreview.net/forum?id=tKif2rXQ6V) |
| Steiner Tree | Real-World GEO Instances | STP | 23 | - | - | [link](https://ivanaljubic.github.io/portfolio/steiner-tree-problems-in-graph/) |
| Max Cut | Gset | edge-list | 71 | - | - | [link](https://web.stanford.edu/~yyye/yyye/Gset/) |
| Max Cut | BiqMac Library | sparse-matrix | - | - | - | [link](https://biqmac.aau.at/biqmaclib.html) |
| Max Cut | DIMACS 7th Challenge Max-Cut | DIMACS | - | - | - | [link](http://archive.dimacs.rutgers.edu/Challenges/Seventh/Instances/) |
| Max Cut | Optsicom Max-Cut | Various | - | - | - | [link](https://grafo.etsii.urjc.es/optsicom/maxcut) |
| Multiway Cut | DIMACS Min-Cut/Max-Flow Instances | DIMACS | - | - | - | [link](https://zenodo.org/records/4905882) |
| Multiway Cut | DTU Min-Cut/Max-Flow Benchmark | DIMACS | - | - | - | [link](https://data.dtu.dk/articles/dataset/Min-Cut_Max-Flow_Problem_Instances_for_Benchmarking/17091101) |
| Feedback Vertex Set | PACE 2016 - Feedback Vertex Set | PACE | 130 | - | - | [link](https://pacechallenge.org/2016/feedback-vertex-set/) |
| Feedback Vertex Set | PACE 2022 - Directed Feedback Vertex Set | PACE | - | - | - | [link](https://pacechallenge.org/2022/directed-fvs/) |
| Feedback Arc Set | PACE 2022 - Directed FVS (adapted) | PACE | - | - | - | [link](https://pacechallenge.org/2022/directed-fvs/) |
| Graph Partitioning | Walshaw Graph Partitioning Archive | METIS | 34 | - | - | [link](https://chriswalshaw.co.uk/partition/) |
| Graph Partitioning | DIMACS 10th Challenge - Graph Partitioning | METIS | - | - | - | [link](https://sites.cc.gatech.edu/dimacs10/downloads.shtml) |
| Graph Partitioning | METIS Test Graphs | METIS | - | - | - | [link](https://github.com/KarypisLab/METIS) |

---

## 6. Network Flow

This category covers multicommodity flow problems with integrality constraints, path-constrained routing, and flow problems with multipliers. The primary source is the CommaLAB collection from the University of Pisa.

### Key Datasets

The **CommaLAB MMCF collection** is a unified repository hosting multiple instance families:

- **Mnetgen instances** (486 instances): The most widely used random MMCF generator. Parameterized by nodes, commodities, and density, with mutual capacity constraints on 80% of arcs.
- **PDS instances** (24 instances): The most famous MMCF benchmark, modeling patient distribution and evacuation in military scenarios as a space-time network with 11 commodities. Instance difficulty scales with planning horizon.
- **Canad instances** (32 C-type, 18 R-type, 96 bipartite/Mulgen): Fixed-charge network design instances of varying topology and commodity count.

**SNDlib** (22 real telecommunication networks, 830 problem instances) is valuable for its real-world grounding. Networks include Abilene, Germany50, Nobel-EU, and Nobel-US with authentic demand matrices and capacity module costs. It supports both directed and undirected models, multicommodity and single-path routing.

For **path-constrained flow**, the CommaLAB unsplittable flow instances derived from GARR (Italian academic network), SNDlib topologies, and Waxman random graphs provide the primary benchmarks.

The **DIMACS 1st Challenge** (1990--1991) provides classic network flow generators (NETGEN), while the **LEMON Min-Cost Flow Benchmark** organizes instances into six families (NETGEN, GRIDGEN, GOTO, GRIDGRAPH, ROAD, VISION). The **DIMACS 13th Challenge** (2025--2027) is an ongoing effort to update network flow benchmarking.

### Format Notes

There is no universal format. Mnetgen, Canadian, DIMACS, MPS, SNDlib-native, PPRN, and custom formats coexist. This fragmentation is a practical obstacle; format conversion is often needed.

### Notable Gaps

Pure single-commodity max-flow/min-cut benchmarking has matured through DIMACS challenges, but multicommodity integral flow benchmarks are relatively sparse compared to the theoretical importance of these problems. The ongoing DIMACS 13th Challenge may address this.

### Cross-References

SNDlib instances connect to Steiner tree (Category 4) through network design. MIPLIB (Category 10) contains network flow formulations as MIP instances. The PDS instances are also studied as integer programming benchmarks.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Two-Commodity Integral Flow (Directed) | CommaLAB Mnetgen Instances | Mnetgen | 486 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Two-Commodity Integral Flow (Directed) | CommaLAB Canad C Instances | Canadian | 32 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Two-Commodity Integral Flow (Directed) | SNDlib | SNDlib-native/GML | 830 | - | - | [link](http://sndlib.zib.de/) |
| Two-Commodity Integral Flow (Undirected) | CommaLAB Vance Instances | JL Origin-Specific | 30 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Two-Commodity Integral Flow (Undirected) | CommaLAB Grid Network Instances | Origin-Destination | 15 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Integral Flow Bundles | CommaLAB PDS Instances | Mnetgen/MPS | 24 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Integral Flow Bundles | DIMACS 1st Challenge Network Flow Instances | DIMACS | - | - | - | [link](http://archive.dimacs.rutgers.edu/pub/netflow/generators/) |
| Integral Flow Bundles | LEMON Min-Cost Flow Benchmark Data | DIMACS | - | - | - | [link](https://lemon.cs.elte.hu/trac/lemon/wiki/MinCostFlowData) |
| Integral Flow with Homologous Arcs | CommaLAB Canad R Instances | Canadian | 18 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Integral Flow with Homologous Arcs | CommaLAB Canad Bipart and Mulgen Instances | Canadian | 96 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Integral Flow with Homologous Arcs | CommaLAB Reserve Instances | Custom | 9 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Integral Flow with Multipliers | CommaLAB Hydrothermal Instances | PPRN | 5 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Integral Flow with Multipliers | CommaLAB Genflot Instances | Custom | 22 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Integral Flow with Multipliers | MIPLIB 2017 Network Instances | MPS | 1065 | - | - | [link](https://miplib.zib.de/) |
| Path-Constrained Network Flow | CommaLAB Unsplittable Flow (GARR) Instances | XML/Mnetgen | 10 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Path-Constrained Network Flow | CommaLAB Unsplittable Flow (SNDlib) Instances | Mnetgen | 23 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Path-Constrained Network Flow | CommaLAB Unsplittable Flow (Waxman) Instances | Mnetgen | 2 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Path-Constrained Network Flow | CommaLAB Mingozzi Instances | Custom | 10 | - | - | [link](https://commalab.di.unipi.it/datasets/mmcf/) |
| Path-Constrained Network Flow | SNDlib Single-Path Routing Instances | SNDlib-native | - | - | - | [link](http://sndlib.zib.de/) |
| Path-Constrained Network Flow | DIMACS 13th Challenge: Network Flows 2.0 | DIMACS | - | - | - | [link](https://coral.ise.lehigh.edu/flow-challenge-2-0/) |

---

## 7. Knapsack and Partition

This category covers the 0-1 knapsack problem, bin packing, subset sum, number partitioning, and precedence-constrained knapsack. These are among the most practically important NP-hard problems, with applications in resource allocation, logistics, and cryptography.

### Key Datasets

**Pisinger's Hard Knapsack Instances** (~14,000 instances, 50--10,000 items) are the standard benchmark, covering 14 instance types including uncorrelated, weakly/strongly correlated, subset sum, and spanner variants. The accompanying generators (combo, minknap, expknap) are widely used.

**Jooken's Hard Knapsack Instances** (3,240 instances, 25--200 items) are a notable recent contribution. Despite being smaller than Pisinger's instances, they are dramatically harder to solve, requiring ~810 CPU-hours on a supercomputer. This demonstrates that instance hardness is about structure, not size.

The **OR-Library Chu-Beasley instances** (270 instances) are the standard for multidimensional knapsack, with systematic variation of constraints (5, 10, 30), items (100, 250, 500), and tightness ratios.

**BPPLIB** (6,195 instances) is comprehensive for one-dimensional bin packing, aggregating Falkenauer, Scholl, Schwerin, Waescher, and random instance sets. The **ESICUP** collection extends to 2D and 3D packing.

For **subset sum**, Pisinger's generator produces hard instances where profit equals weight. The FSU collection provides 7 small educational instances useful for verification but not performance benchmarking.

**Number partitioning** is notably under-benchmarked relative to its theoretical importance. Pisinger's even-odd partition instances and Mertens's phase transition study (exploring the easy/hard boundary at m/n = 1, where m is bit-length and n is set size) are the primary references.

**MineLib** provides precedence-constrained knapsack instances from open-pit mine scheduling, connecting this category to real-world industrial optimization.

### Format Notes

No standard format exists. Pisinger uses custom text (id, profit, weight per line). OR-Library uses its own text format. BPPLIB uses capacity/items/sizes format. Generators are often provided as C source code.

### Notable Gaps

Partition has surprisingly few dedicated benchmark suites given its role as the simplest NP-complete number problem. The multiple knapsack problem and the quadratic knapsack problem lack dedicated benchmarks in this registry.

### Cross-References

Subset sum is a special case of knapsack and connects to lattice problems (Category 11) through the knapsack lattice construction. Bin packing relates to scheduling (Category 7) through machine load balancing. OR-Library instances appear across multiple categories.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Knapsack | Pisinger Hard Knapsack Instances | Custom text (id, profit, weight per line) | 14000 | 50-10000 items | Yes | [link](https://hjemmesider.diku.dk/~pisinger/codes.html) |
| Knapsack | Jooken Hard Knapsack Instances | Custom text (id, profit, weight per line) | 3240 | 25-200 items | Yes | [link](https://github.com/JorikJooken/knapsackProblemInstances) |
| Knapsack | OR-Library Multidimensional Knapsack (Chu-Beasley) | OR-Library text format | 270 | 100-500 items; 5-30 constraints | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html) |
| Knapsack | Ortega 0/1 Knapsack Instances | Custom text | - | - | Yes | [link](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/) |
| Knapsack | kplib Test Instances | Custom text | - | - | Yes | [link](https://github.com/likr/kplib) |
| Bin Packing | BPPLIB (Bin Packing Problem Library) | Custom text (capacity, number of items, item sizes) | 6195 | 50-1000 items | Yes | [link](https://site.unibo.it/operations-research/en/research/bpplib-a-bin-packing-problem-library) |
| Bin Packing | ESICUP Cutting and Packing Datasets | Various | - | - | Yes | [link](https://github.com/ESICUP/datasets) |
| Bin Packing | Assembly Line Balancing BPP Collection | Custom text | - | - | Yes | [link](https://assembly-line-balancing.de/further-data-sets/bin-packing-problem-bpp/) |
| Subset Sum | Pisinger Subset Sum Instances | Custom text | - | - | Yes | [link](https://hjemmesider.diku.dk/~pisinger/codes.html) |
| Subset Sum | FSU Subset Sum Dataset | Custom text (weights and target) | 7 | 8-21 items | Yes | [link](https://people.sc.fsu.edu/~jburkardt/datasets/subset_sum/subset_sum.html) |
| Partition | Pisinger Even-Odd Partition Instances | Custom text | - | - | Yes | [link](https://hjemmesider.diku.dk/~pisinger/codes.html) |
| Partition | Mertens Phase Transition Instances | Generated (random integers) | - | - | Yes | [link](https://arxiv.org/abs/cond-mat/0310317) |
| Partially Ordered Knapsack | MineLib Precedence-Constrained Instances | Custom text | - | - | Yes | [link](http://mansci-web.uai.cl/minelib/) |
| Partially Ordered Knapsack | Boyd Precedence-Constrained Knapsack Solver and Instances | Custom text | - | - | Yes | [link](https://github.com/rmcgibbo/precedenceConstrainedKnapsack) |

---

## 8. Scheduling

Machine scheduling is one of the most practically important problem families, with decades of benchmark development. The benchmarks here are remarkably well-maintained, with best-known bounds actively tracked.

### Key Datasets

**Taillard's instances** are the single most important scheduling benchmark set, covering flow shop (120 instances), job shop (80 instances), and open shop (60 instances). Processing times are drawn from uniform distributions across systematic size combinations. Best-known bounds are maintained on Taillard's website. Several job shop instances remain unsolved to optimality after 30+ years.

**JSPLIB** consolidates seven classic job shop benchmark sets into a single repository with JSON metadata: Fisher & Thompson FT (3 instances, foundational from 1963), Lawrence LA (40 instances, all solved), Adams-Balas-Zawack ABZ (5 instances), Taillard TA (80 instances, many open), Storer-Wu-Vaccari SWV (20 instances, 5 still open), and others.

The **DMU instances** (Demirkol, Mehta & Uzsoy, 80 instances) are especially challenging: processing time ranges are double those of Taillard's, and 54 of 80 instances lack proven optimal solutions.

**VFR instances** (480 instances, up to 800 jobs x 60 machines) extend flow shop benchmarking beyond Taillard's, designed specifically to challenge modern metaheuristics.

**PSPLIB** (Project Scheduling Problem Library) is the definitive resource for resource-constrained project scheduling (RCPSP), with j30 (480 instances, all solved), j60 (480, many open), and j120 (600, very few solved) instance sets generated by ProGen. The multi-mode extension adds activity-mode selection. **MPSPLIB** extends to multi-project scenarios.

For **minimum tardiness**, the OR-Library provides 375 weighted tardiness instances across systematic parameter combinations. Cicirello's benchmark adds sequence-dependent setup times.

**Staff scheduling** (nurse rostering) is well-served by NSPLib (9,210 instances from Ghent University) and the KU Leuven benchmarks derived from real Belgian hospital data.

### Format Notes

Most scheduling benchmarks use custom text formats. JSPLIB adds JSON metadata. PSPLIB uses ProGen's format. Staff scheduling increasingly uses XML-based modeling formats.

### Notable Gaps

The open shop problem is relatively under-benchmarked compared to flow shop and job shop, with only Taillard and Gueret-Prins instances. Flexible job shop (where operations can be processed on alternative machines) is growing in importance but lacks a consolidated benchmark in this registry.

### Cross-References

Taillard's website serves as a unified portal for flow shop, job shop, open shop, and QAP instances. OR-Library instances appear here and in Categories 7, 8, and 10. RCPSP precedence structures connect to precedence-constrained scheduling and DAG-based problems.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Flow Shop Scheduling | Taillard's Flow Shop Instances | Custom text | 120 | 20-500 jobs; 5-20 machines | Yes | [link](http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html) |
| Flow Shop Scheduling | OR-Library Flow Shop Instances | Custom text | 31 | 20-200 jobs; 5-20 machines | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/flowshopinfo.html) |
| Flow Shop Scheduling | VFR Hard Flow Shop Instances | Custom text | 480 | 10-800 jobs; 5-60 machines | No | [link](https://www.sciencedirect.com/science/article/abs/pii/S0377221714005992) |
| Job Shop Scheduling | JSPLIB (Job Shop Problem Library) | Standard text with JSON metadata | 162 | 6-100 jobs; 5-20 machines | Yes | [link](https://github.com/tamy0612/JSPLIB) |
| Job Shop Scheduling | Fisher & Thompson Instances (FT) | Custom text | 3 | 6-20 jobs; 6-10 machines | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/jobshopinfo.html) |
| Job Shop Scheduling | Lawrence Instances (LA) | Custom text | 40 | 10-30 jobs; 5-15 machines | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/jobshopinfo.html) |
| Job Shop Scheduling | Adams, Balas & Zawack Instances (ABZ) | Custom text | 5 | 10-20 jobs; 10-15 machines | Yes | [link](https://github.com/tamy0612/JSPLIB) |
| Job Shop Scheduling | Taillard's Job Shop Instances (TA) | Custom text | 80 | 15-100 jobs; 15-20 machines | No | [link](http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html) |
| Job Shop Scheduling | Storer, Wu & Vaccari Instances (SWV) | Custom text | 20 | 20-50 jobs; 10-15 machines | No | [link](https://github.com/tamy0612/JSPLIB) |
| Job Shop Scheduling | Demirkol, Mehta & Uzsoy Instances (DMU) | Custom text | 80 | 20-100 jobs; 15-20 machines | No | [link](https://optimizizer.com/DMU.php) |
| Job Shop Scheduling | OR-Library Job Shop Instances | Custom text | 82 | 6-30 jobs; 5-15 machines | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/jobshopinfo.html) |
| Job Shop Scheduling | Large-Scale JSP Benchmarks | Custom text | 40 | 100-500 jobs; 20-100 machines | No | [link](https://arxiv.org/abs/2102.08778) |
| Open Shop Scheduling | Taillard's Open Shop Instances | Custom text | 60 | 4-20 jobs; 4-20 machines | Yes | [link](http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html) |
| Open Shop Scheduling | Gueret & Prins Open Shop Instances (GP) | Custom text | 80 | 3-10 jobs; 3-10 machines | Yes | [link](https://link.springer.com/chapter/10.1007/978-3-540-32220-7_9) |
| Multiprocessor Scheduling | OR-Library Parallel Machine Instances | Custom text | - | - | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/info.html) |
| Resource-Constrained Project Scheduling (RCPSP) | PSPLIB j30 Instances | Custom text | 480 | 30 activities | Yes | [link](https://www.om-db.wi.tum.de/psplib/library.html) |
| Resource-Constrained Project Scheduling (RCPSP) | PSPLIB j60 Instances | Custom text | 480 | 60 activities | No | [link](https://www.om-db.wi.tum.de/psplib/library.html) |
| Resource-Constrained Project Scheduling (RCPSP) | PSPLIB j120 Instances | Custom text | 600 | 120 activities | No | [link](https://www.om-db.wi.tum.de/psplib/library.html) |
| Resource-Constrained Project Scheduling (RCPSP) | PSPLIB Multi-Mode RCPSP Instances | Custom text | - | 12-30 activities | Yes | [link](https://www.om-db.wi.tum.de/psplib/library.html) |
| Resource-Constrained Project Scheduling (RCPSP) | MPSPLIB (Multi-Project Scheduling Problem Library) | Custom text | - | - | No | [link](http://www.mpsplib.com/) |
| Precedence-Constrained Scheduling | PSPLIB RCPSP Instances (as precedence-constrained benchmarks) | Custom text | 1560 | 30-120 activities | No | [link](https://www.om-db.wi.tum.de/psplib/library.html) |
| Minimum Tardiness Scheduling | OR-Library Weighted Tardiness Instances | Custom text | 375 | 40-100 jobs | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/wtinfo.html) |
| Minimum Tardiness Scheduling | Cicirello Weighted Tardiness with Sequence-Dependent Setups | Plain text | - | - | No | [link](https://www.cicirello.org/datasets/wtsds/) |
| Staff Scheduling | NSPLib (Nurse Scheduling Problem Library) | Custom text | 9210 | 25-150 nurses | No | [link](https://www.projectmanagement.ugent.be/research/personnel_scheduling/nsp) |
| Staff Scheduling | Shift Scheduling Benchmarks | XML | - | - | No | [link](https://www.schedulingbenchmarks.org/) |
| Staff Scheduling | KU Leuven Nurse Rostering Benchmarks | Custom text | - | 4-46 nurses | No | [link](https://gent.cs.kuleuven.be/nurserostering.html) |

---

## 9. Set Problems

Set cover, set packing, exact cover, and hitting set are foundational NP-hard problems that arise in logistics, operations research, and combinatorial design.

### Key Datasets

The **OR-Library SCP Instances** (80 instances) are the primary benchmark for set covering, with systematic variation of matrix dimensions (200--1,000 rows, 1,000--10,000 columns) and density (2--20%). Optimal solutions are known for sets 4--6 and A--E. The same collection dually serves set packing (by switching from minimization to maximization of disjoint sets) and hitting set (by transposing the incidence matrix).

The **RAIL instances** (7 instances) stand out as real-world benchmarks from Italian railway crew scheduling. These are orders of magnitude larger than the random instances (up to 4,872 rows and 1,092,610 columns) and have very sparse structure (each column covers at most 12 rows). They expose different algorithmic behaviors than random instances.

**Unicost SCP instances** (10 instances in CYC and CLR families) reduce set cover to minimum-cardinality selection, removing the cost dimension. The **Steiner Triple System instances** (5 instances) are extremely symmetric, making them challenging for branch-and-bound despite small size.

For **hitting set**, the **PACE 2025 Challenge** (200 instances in hypergraph format) is now the primary benchmark. The Vera-Licona research group's benchmark collection draws from diverse real-world domains: metabolic networks, cell signaling, circuit testing, and game states.

**Exact cover by 3-sets** has no large-scale dedicated benchmark. The standard test cases are Steiner triple systems (classic combinatorial designs) and polyomino tiling problems (notably the 12 pentominoes on a 6x10 rectangle, with 2,339 solutions). Knuth's Dancing Links algorithm was demonstrated on these instances.

The **PBBS Set Cover Benchmark** targets parallel algorithms with synthetic instances at scale n = 10,000,000, filling the gap for large-scale approximate set cover evaluation.

### Format Notes

OR-Library uses its own text format (rows, columns, costs, coverage lists). PACE 2025 uses HGR (hypergraph) format. MIPLIB instances encode set packing as MIP. PBBS uses bipartite adjacency graphs.

### Notable Gaps

Set packing has no dedicated benchmark; researchers use MIPLIB instances filtered by structure or dual OR-Library instances. Exact cover by 3-sets is poorly benchmarked at scale.

### Cross-References

OR-Library SCP instances serve triple duty across set cover, set packing, and hitting set. MIPLIB (Category 10) contains set packing/partitioning formulations from airline and vehicle routing applications. Set cover connects to vertex cover (Category 2) and dominating set through structural reductions.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Set Cover | OR-Library SCP Instances (Beasley) | Custom text (rows, columns, costs, coverage) | 80 | 200-1000 rows; 1000-10000 columns | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html) |
| Set Cover | OR-Library RAIL Instances | Custom text (rows, columns, costs, coverage) | 7 | 507-4872 rows; 47311-1092610 columns | No | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html) |
| Set Cover | OR-Library Unicost SCP Instances | Custom text (rows, columns, costs, coverage) | 10 | - | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html) |
| Set Cover | Steiner Triple System Covering Instances | Custom text (rows, columns, costs, coverage) | 5 | - | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html) |
| Set Cover | GECCO 2020 OCP/USCP Benchmark | Custom text | 69 | - | No | [link](https://www.mage.fst.uha.fr/brevilliers/gecco-2020-ocp-uscp-competition/) |
| Set Cover | PBBS Set Cover Benchmark | Adjacency graph (bipartite) | - | - | No | [link](https://www.cs.cmu.edu/~pbbs/benchmarks/setCover.html) |
| Set Packing | MIPLIB 2017 | MPS | 1065 | - | Yes | [link](https://miplib.zib.de/) |
| Set Packing | OR-Library SCP Instances (dual as Set Packing) | Custom text (rows, columns, costs, coverage) | 87 | - | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html) |
| Exact Cover by 3-Sets | Steiner Triple Systems (Exact Cover Instances) | Incidence matrix / custom | - | - | Yes | [link](https://en.wikipedia.org/wiki/Steiner_system) |
| Exact Cover by 3-Sets | Pentomino and Polyomino Tiling (Exact Cover) | Incidence matrix (0-1) | - | - | Yes | [link](https://arxiv.org/abs/cs/0011047) |
| Hitting Set | PACE 2025 Hitting Set Challenge | HGR (hypergraph, DIMACS-like) | 200 | - | Yes | [link](https://pacechallenge.org/2025/hs/) |
| Hitting Set | Minimal Hitting Set Algorithm Benchmarks | Custom text | - | - | Yes | [link](https://github.com/VeraLiconaResearchGroup/Minimal-Hitting-Set-Algorithms) |
| Hitting Set | OR-Library SCP Instances (dual as Hitting Set) | Custom text (rows, columns, costs, coverage) | 87 | - | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html) |

---

## 10. Sequence and String Problems

This category covers longest common subsequence (LCS), shortest common supersequence (SCS), and string-to-string correction (edit distance). These problems bridge theoretical computer science and computational biology.

### Key Datasets

For **LCS**, the **BB Benchmark** (Blum & Blesa, 80 instances) is the standard, with correlated strings generated from random base strings via mutations. Its strength is systematic parameter variation across string count (10--200), length (100--1,000), and alphabet size (4--24). The **Rat Genome benchmark** (20 instances) provides real-world biological grounding.

The bioinformatics community has produced extensive alignment benchmarks that serve as indirect LCS datasets. **BAliBASE** (6,255 protein sequences, manually curated reference alignments based on 3D structure superposition) is the gold standard for multiple sequence alignment. **SABmark** covers the entire known protein fold space with emphasis on difficult twilight-zone alignments (< 25% identity). **HomFam** (94 families, up to 93,675 sequences per family) tests how alignment quality degrades at scale.

For **SCS**, benchmarks are smaller: 25 random instances (Blum et al.) and biological instances derived from SARS coronavirus and Swiss-Prot protein sequences. The problem is less extensively studied than LCS.

**String-to-string correction** (edit distance) draws from OCR and spelling correction. The **TREC-5 Confusion Track** (55,600 documents with 5% and 20% character error rates) is the primary OCR benchmark. **Norvig's spelling corpus** and the **Birkbeck Spelling Error Corpus** provide natural language misspelling data. **SymSpell** benchmarks focus on approximate matching speed at scale.

### Format Notes

Most LCS/SCS benchmarks use plain text with custom delimiters. Bioinformatics uses FASTA and MSF formats. String correction uses SGML/text (TREC) or plain text.

### Notable Gaps

The edit distance problem is well-studied algorithmically but lacks a single consolidated benchmark suite. LCS benchmarks focus on the multiple-string variant; the classical two-string LCS is considered efficiently solvable (O(n^2)) and not benchmarked separately.

### Cross-References

LCS and sequence alignment connect directly to computational biology applications. BAliBASE and SABmark are relevant to Category 11 (lattice problems) through sequence analysis in structural biology.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Longest Common Subsequence | BB Benchmark (Blum & Blesa) | Text (custom) | 80 | 10-200 strings; 100-1000 string_length | No | [link](https://link.springer.com/chapter/10.1007/978-3-540-74446-7_11) |
| Longest Common Subsequence | Rat Genome LCS Benchmark | Text (DNA sequences) | 20 | 10 strings; 600 string_length | No | [link](https://link.springer.com/chapter/10.1007/978-3-030-37599-7_14) |
| Longest Common Subsequence | LCS Random Benchmark (Shyu & Tsai) | Text (custom) | - | 10-200 strings; 100-1000 string_length | No | [link](https://link.springer.com/article/10.1007/s00500-018-3200-3) |
| Longest Common Subsequence | Bacteria LCS Benchmark | Text (DNA sequences) | 35 | 4 alphabet_size | No | [link](https://link.springer.com/chapter/10.1007/978-3-540-74446-7_11) |
| Longest Common Subsequence | LCS Non-Uniform Distribution Benchmark | Text (custom) | - | 10-100 strings; 100-1000 string_length | No | [link](https://github.com/milanagrbic/LCSonNuD) |
| Longest Common Subsequence | BAliBASE (Benchmark Alignment dataBASE) | FASTA, MSF | 6255 | 4-50 per family sequences | Yes | [link](https://www.lbgi.fr/balibase/) |
| Longest Common Subsequence | SABmark (Sequence Alignment Benchmark) | FASTA, PDB | - | 0-50% sequence_identity | Yes | [link](https://bioinformatics.vub.ac.be/databases/databases.html) |
| Longest Common Subsequence | PREFAB (Protein Reference Alignment Benchmark) | FASTA | 1682 | up to 50 sequences_per_family; 321 SCOP folds folds | Yes | [link](https://www.drive5.com/muscle/) |
| Longest Common Subsequence | OXBench | FASTA, MSF | - | - | Yes | [link](https://www.compbio.dundee.ac.uk/downloads/oxbench/) |
| Longest Common Subsequence | HomFam Large-Scale Alignment Benchmark | FASTA | 94 | 94 families | Yes | [link](https://academic.oup.com/bioinformatics/article/29/8/989/229582) |
| Shortest Common Supersequence | SCS Random Benchmark (Blum et al.) | Text (custom) | 25 | 8 strings; 40-80 string_length | No | [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC7127599/) |
| Shortest Common Supersequence | SCS DNA Benchmark (SARS Coronavirus) | Text (DNA sequences) | - | 158-1269 string_length | No | [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC7127599/) |
| Shortest Common Supersequence | SCS Protein Benchmark (Swiss-Prot) | Text (protein sequences) | - | 125-595 string_length | No | [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC7127599/) |
| Shortest Common Supersequence | SCS Biological Benchmark (Ning & Leong) | Text (DNA and protein sequences) | 11 | 4-20 alphabet_size | No | [link](https://link.springer.com/article/10.1186/1471-2105-7-S4-S12) |
| Shortest Common Supersequence | SCS Enhanced Beam Search Benchmark (Mousavi et al.) | Text (custom) | - | 5-100 strings; 10-100 string_length | No | [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC7127599/) |
| String-to-String Correction | TREC-5 Confusion Track Corpus | SGML / Text | 55600 | 55600 documents; 5-20% character_error_rate | Yes | [link](https://trec.nist.gov/data.html) |
| String-to-String Correction | Norvig Spelling Correction Corpus | Text | - | 29157 unique words dictionary_size; 1.1M words corpus_size | Yes | [link](https://norvig.com/spell-correct.html) |
| String-to-String Correction | Birkbeck Spelling Error Corpus | Text | - | - | Yes | [link](https://www.dcs.bbk.ac.uk/~roger/corpora.html) |
| String-to-String Correction | OCR-D Ground Truth Corpus | PAGE XML, Text | - | - | Yes | [link](https://github.com/OCR-D/gt_structure_text) |
| String-to-String Correction | SymSpell Benchmark Corpus | Text | - | 82765 dictionary_entries; 1000 test_queries | Yes | [link](https://github.com/wolfgarbe/SymSpell) |

---

## 11. Mathematical Programming

This category covers integer linear programming, QUBO, and quadratic assignment -- the workhorse formulations for encoding combinatorial optimization problems.

### Key Datasets

**MIPLIB** is to mixed-integer programming what TSPLIB is to TSP: the definitive, continuously evolving benchmark. **MIPLIB 2017** (1,065 instances, 240 in the benchmark subset) was selected from 5,721 submissions using a data-driven methodology, representing a collaboration between ZIB, CPLEX, Gurobi, FICO, MOSEK, and SAS. Earlier editions (**MIPLIB 2010**: 361 instances; **MIPLIB 2003**: 60 instances) remain useful for historical comparison. Instance sizes range from 2 variables to 6 million.

**OR-Library** (Beasley) is one of the earliest OR benchmark repositories, covering set covering, knapsack, bin packing, warehouse location, and other IP formulations. While no longer actively maintained, it remains foundational and is referenced across multiple categories in this survey.

**MINLPLib** (1,534 instances) extends benchmarking to mixed-integer nonlinear programming. The Julia-based MINLPLib.jl variant provides over 6,000 instances.

For **QUBO**, **MQLib** (3,296 instances) is comprehensive, drawing from diverse sources and providing best-known solutions from 37 tested heuristics. The **Beasley ORLIB UBQP instances** (125 instances, 50--2,500 variables) are the traditional standard. **QPLIB** (8,000 instances) covers the full spectrum of quadratic programming: continuous, binary, mixed-integer, constrained and unconstrained.

**QAPLIB** (136 instances, 5--256 facilities) is the standard for quadratic assignment, with instances from backboard wiring, hospital layout, typewriter keyboard design, and campus planning. The Taillard tai*b instances are among the hardest known. Many QAPLIB instances remain unsolved to proven optimality, and the **Nugent instances** (12--30 facilities) provide smaller instances with known optima for solver verification.

### Format Notes

MPS is the universal format for MIP/LP. GAMS and AMPL formats serve MINLP. QUBO uses sparse matrix formats. QAPLIB uses paired flow/distance matrices in text format.

### Notable Gaps

Stochastic programming and robust optimization benchmarks are not covered. Multi-objective integer programming benchmarks are sparse.

### Cross-References

MIPLIB instances encode problems from nearly every other category (set packing, network flow, scheduling, etc.). OR-Library spans Categories 7, 8, 9, and 10. QUBO is equivalent to max cut (Category 4) and Ising spin glass (Category 13) via standard reductions. QAPLIB's Taillard instances connect to the scheduling benchmarks by the same author.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Integer Linear Programming | MIPLIB 2017 | MPS | 1065 | 2-6000000 variables; 1-6000000 constraints | No | [link](https://miplib.zib.de/) |
| Integer Linear Programming | MIPLIB 2010 | MPS | 361 | - | No | [link](https://miplib2010.zib.de/) |
| Integer Linear Programming | MIPLIB 2003 | MPS | 60 | - | No | [link](https://miplib.zib.de/history.html) |
| Integer Linear Programming | OR-Library (Beasley) | Custom text | - | - | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/info.html) |
| Integer Linear Programming | MINLPLib | GAMS, AMPL, OSiL | 1534 | 1-1000000 variables; 1-1000000 constraints | No | [link](https://www.minlplib.org/) |
| Quadratic Unconstrained Binary Optimization | MQLib | Custom sparse matrix | 3296 | 20-53130 variables | No | [link](https://github.com/MQLib/MQLib) |
| Quadratic Unconstrained Binary Optimization | Beasley ORLIB UBQP Instances | Custom text | 125 | 50-2500 variables | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/bqpinfo.html) |
| Quadratic Unconstrained Binary Optimization | Palubeckis UBQP Instances | Custom text | - | 3000-7000 variables | No | [link](https://github.com/MQLib/MQLib/blob/master/data/README.md) |
| Quadratic Unconstrained Binary Optimization | QPLIB (Quadratic Programming Library) | QPLIB, AMPL (.mod) | 8000 | 2-1000000 variables; 0-1000000 constraints | No | [link](https://qplib.zib.de/) |
| Quadratic Assignment Problem | QAPLIB | Custom text (flow and distance matrices) | 136 | 5-256 facilities | No | [link](https://qaplib.mgi.polymtl.ca/) |
| Quadratic Assignment Problem | QAPLIB Tai Instances (Taillard) | Custom text (flow and distance matrices) | - | 12-256 facilities | No | [link](https://qaplib.mgi.polymtl.ca/) |
| Quadratic Assignment Problem | Nugent QAP Instances | Custom text (flow and distance matrices) | - | 12-30 facilities | Yes | [link](https://qaplib.mgi.polymtl.ca/) |

---

## 12. Lattice and Number Theory

Lattice problems and integer factoring underpin modern cryptographic security. Benchmarks here serve a dual purpose: evaluating algorithmic progress and calibrating cryptographic parameter choices.

### Key Datasets

The **TU Darmstadt lattice challenges** are the primary benchmarks:

- **SVP Challenge**: Random lattices in even dimensions 140--300, with a hall of fame tracking records. Solutions must find vectors shorter than the Gaussian heuristic. The challenge uses NTL-generated lattices from integer seeds.
- **Ideal Lattice Challenge**: Lattices over cyclotomic polynomial rings in dimensions 52--1,024, with separate halls of fame for exact and approximate SVP. Records include solutions in dimensions 656 and 700.
- **LWE Challenge**: Instances parameterized by dimension (40--120) and relative error (0.005--0.070), generated via multi-party computation ensuring no single party knows solutions. The current record (dimension 95, alpha=0.005) was set by USTC in 2024.

**Ring-LWE Challenges** (516 instances) cover diverse instantiations: two-power and non-two-power cyclotomics, various moduli, error distributions from worst-case hardness theorems. Challenge integrity is verified via non-interactive cut-and-choose with the NIST randomness beacon.

**G6K** (General Sieve Kernel) and **fplll** are both solver frameworks and benchmark generators. G6K set records on SVP challenges at dimensions 151, 153, and 155. fplll generates q-ary lattices, Goldstein-Mayer lattices, knapsack lattices, and structured lattices.

For **integer factoring**, the **RSA Factoring Challenge** (54 semiprimes, 100--617 digits) is the historical benchmark, now discontinued. RSA-250 (829 bits) is the largest factored as of 2020; RSA-2048 remains open. The **Cunningham Project** (ongoing since 1925) tracks factoring of b^n +/- 1 and serves as a historical record of algorithm progress.

The **closest vector problem** has no dedicated challenge; researchers adapt SVP challenge lattices by adding target vectors.

### Format Notes

Lattice bases are specified as integer matrices in text format. LWE instances specify matrix A and vector b. RSA challenges are simply large decimal integers.

### Notable Gaps

CVP lacks a dedicated benchmark analogous to the SVP Challenge. Short integer solution (SIS) problems are benchmarked through lattice reduction but have no standalone challenge. Lattice-based signature and encryption scheme benchmarks (e.g., for evaluating CRYSTALS-Kyber/Dilithium parameters) are not catalogued here.

### Cross-References

Subset sum (Category 7) connects to lattice problems through the knapsack lattice reduction. QUBO (Category 11) and max cut (Category 4) relate through optimization formulations on lattices.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Shortest Vector Problem | TU Darmstadt SVP Challenge | Text (integer matrix) | - | 140-300 dimensions | No | [link](https://www.latticechallenge.org/svp-challenge/) |
| Shortest Vector Problem | TU Darmstadt Ideal Lattice Challenge | Text (integer matrix, ZIP archives) | - | 52-1024 dimensions | No | [link](https://latticechallenge.org/ideallattice-challenge/) |
| Shortest Vector Problem | G6K (General Sieve Kernel) Test Suite | Generated via fplll/fpylll | - | 50-160 dimensions | No | [link](https://github.com/fplll/g6k) |
| Shortest Vector Problem | fplll Lattice Reduction Test Instances | Generated via built-in generators | - | - | No | [link](https://github.com/fplll/fplll) |
| Closest Vector Problem | TU Darmstadt SVP Challenge (adapted for CVP) | Text (integer matrix) | - | 140-300 dimensions | No | [link](https://www.latticechallenge.org/svp-challenge/) |
| Closest Vector Problem | fplll CVP Solver Test Instances | Generated via built-in generators | - | - | Yes | [link](https://github.com/fplll/fplll) |
| Learning With Errors | TU Darmstadt LWE Challenge | Text (matrix A, vector b) | - | 40-120 dimensions | Yes | [link](https://www.latticechallenge.org/lwe_challenge/challenge.php) |
| Learning With Errors | Ring-LWE Challenges | Custom binary | 516 | - | Yes | [link](https://web.eecs.umich.edu/~cpeikert/rlwe-challenges/) |
| Integer Factoring | RSA Factoring Challenge | Decimal integer | 54 | 100-617 digits; 330-2048 bits | Yes | [link](https://en.wikipedia.org/wiki/RSA_Factoring_Challenge) |
| Integer Factoring | Cunningham Project Tables | Text (factor tables) | - | - | Yes | [link](https://homes.cerias.purdue.edu/~ssw/cun/) |
| Integer Factoring | Alpertron Integer Factorization Records | Web interface / decimal integer | - | - | Yes | [link](https://www.alpertron.com.ar/ECM.HTM) |

---

## 13. Database and Relational Problems

This is the most sparsely benchmarked category, reflecting the fact that database normal form problems (BCNF, key discovery) are typically studied as components of larger systems rather than as standalone computational challenges.

### Key Datasets

The **HPI FD/UCC Benchmark Suite** (16 datasets) is effectively the only benchmark for this category. It provides CSV datasets ranging from 5 to 223 columns and 108 to 250,000 rows, with known functional dependency counts ranging from 1 (Balance-scale) to 982,631 (Flight). Key datasets include:

- **Iris** (150 rows, 5 columns, 4 FDs): small-scale verification
- **Adult** (48,842 rows, 14 columns, 78 FDs): medium-scale
- **Horse** (300 rows, 27 columns, 128,726 FDs): high FD density stress test
- **Flight** (1,000 rows, 109 columns, 982,631 FDs): wide-schema stress test
- **Uniprot** (1,000 rows, 223 columns): ultra-wide schema

These datasets serve multiple problems: UCC (unique column combination / additional key) discovery, FD discovery, and indirectly BCNF checking and prime attribute identification.

For **conjunctive boolean queries**, the SPARQL Query Containment Benchmark (sparql-qc-bench) provides small test suites (20--28 query pairs) for containment testing. SQCFramework generates benchmarks from real query logs (e.g., DBpedia). However, no widely adopted benchmark exists for the pure relational conjunctive query evaluation decision problem.

**TPC-H** (8-table decision-support schema) has known FD structure and is used for FD-based query optimization research, though it is primarily a query performance benchmark.

### Format Notes

The HPI benchmarks use CSV. SPARQL benchmarks use RDF/Turtle. TPC-H uses SQL DDL with generated data.

### Notable Gaps

This is the weakest category in the survey. BCNF violation detection, conjunctive query foldability (minimization), prime attribute identification, and minimum cardinality key discovery all lack dedicated benchmarks. These problems are studied as derived tasks from FD/UCC discovery rather than as standalone challenges. The category would benefit from purpose-built benchmark suites with ground-truth annotations.

### Cross-References

The HPI datasets (Iris, Adult) originate from the UCI Machine Learning Repository and are used across many fields. Hitting set algorithms (Category 9) are used in UCC discovery (e.g., the DUCC and HyUCC algorithms).


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Conjunctive Boolean Query | SPARQL Query Containment Benchmark (CQNoProj) | SPARQL / RDF (Turtle) | 20 | - | Yes | [link](https://sparql-qc-bench.inrialpes.fr/) |
| Conjunctive Boolean Query | SPARQL Query Containment Benchmark (UCQProj) | SPARQL / RDF (Turtle) | 28 | - | Yes | [link](https://sparql-qc-bench.inrialpes.fr/) |
| Conjunctive Boolean Query | SQCFramework Generated Benchmarks | TTL (Turtle) | - | - | Yes | [link](https://github.com/dice-group/sqcframework) |
| Additional Key | HPI FD/UCC Benchmark - Iris | CSV | - | 150 rows; 5 columns | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Additional Key | HPI FD/UCC Benchmark - Adult | CSV | - | 48842 rows; 14 columns | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Additional Key | HPI FD/UCC Benchmark - NCVoter | CSV | - | 1000 rows; 19 columns | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Additional Key | HPI FD/UCC Benchmark - Hepatitis | CSV | - | 155 rows; 20 columns | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Additional Key | HPI FD/UCC Benchmark - Horse | CSV | - | 300 rows; 27 columns | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Additional Key | HPI FD/UCC Benchmark - Flight (1K) | CSV | - | 1000 rows; 109 columns | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Additional Key | HPI FD/UCC Benchmark - Uniprot | CSV | - | 1000 rows; 223 columns | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Functional Dependency Discovery | HPI FD Benchmark Suite | CSV | 16 | - | Yes | [link](https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html) |
| Functional Dependency Discovery | TPC-H Schema | SQL DDL / CSV (generated) | - | - | Yes | [link](https://www.tpc.org/tpch/) |

---

## 14. Physics and Statistical Mechanics

Spin glass ground state optimization is NP-hard and sits at the intersection of statistical physics, combinatorial optimization, and quantum computing. This category has seen rapid dataset growth driven by quantum annealing research.

### Key Datasets

The **Spin Glass Server** (University of Bonn) computes exact ground states using the Biq Mac algorithm for complete graphs (Sherrington-Kirkpatrick model), 2D planar lattices, and general sparse topologies. It serves as both a computational service and a reference for ground-truth solutions.

**Gset** (71 instances, 800--20,000 vertices) appears here as well as in Category 4 (max cut), since max cut with antiferromagnetic couplings is equivalent to Ising energy minimization.

**BiqMac Library** (50 Ising instances, 100--300 variables) provides small-scale instances with proven optima, useful for validating exact solvers.

**RL4Ising** (190,000+ instances) is the largest spin glass benchmark, designed for reinforcement learning evaluation. It covers 1D through 4D lattices and general graphs with five coupling types (classic, spin-glass, ferromagnetic, anti-ferromagnetic, synthetic). Baseline solutions from Gurobi and CPLEX are provided. Available on HuggingFace.

**D-Wave hardware topology instances** test quantum annealing on native Chimera (degree-6, ~2,048 qubits), Pegasus (degree-15, 5,760 qubits), and Zephyr (degree-20) graphs. These are important for quantum-classical comparison studies, though Chimera spin glasses have only a zero-temperature phase transition, limiting their hardness.

**Tile-planted instances** offer tunable hardness with known ground states, making them valuable for controlled experiments comparing quantum and classical annealing.

**Edwards-Anderson lattice instances** (dimensions 3--8) study ground state properties in high-dimensional cubic lattices using bond dilution for computational feasibility.

The **Random Field Ising Model** (RFIM) instances (2D and 3D lattices, system sizes up to L=156 in 3D) address disorder-driven phase transitions, with ground states computable via max-flow/min-cut.

### Format Notes

Formats vary widely: edge lists with couplings, lattice coupling matrices, QUBO coefficients, and Python-generated instances. HuggingFace hosting (RL4Ising) represents a modern distribution approach.

### Notable Gaps

Potts model and vector spin model benchmarks are sparse. Spin glass benchmarks on non-planar topologies beyond D-Wave hardware graphs are limited. The RFIM is well-studied but the more general random bond/field models lack consolidated benchmarks.

### Cross-References

Max cut (Category 4), QUBO (Category 11), and spin glass are three formulations of the same underlying problem. Gset and BiqMac Library instances appear in all three contexts. D-Wave instances connect to QUBO formulations in Category 11.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Spin Glass | Spin Glass Server (University of Bonn) | Edge list (spin_i spin_j coupling) | - | - | Yes | [link](http://spinglass.uni-bonn.de/) |
| Spin Glass | Biq Mac Library - Ising Spin Glass Instances | Sparse matrix / adjacency list | 50 | 100-300 variables | Yes | [link](https://biqmac.aau.at/biqmaclib.html) |
| Spin Glass | Gset Max-Cut / Spin Glass Benchmark | Sparse adjacency list | 71 | 800-20000 vertices | No | [link](https://web.stanford.edu/~yyye/yyye/Gset/) |
| Spin Glass | DIRAC Spin Glass Benchmark Instances | Custom lattice files | - | - | Yes | [link](https://github.com/FFrankyy/DIRAC) |
| Spin Glass | RL4Ising Benchmark Dataset | HuggingFace dataset | 190000 | - | Yes | [link](https://github.com/Open-Finance-Lab/RL4Ising) |
| Spin Glass | D-Wave Chimera and Pegasus Spin Glass Instances | QUBO / Ising model coefficients | - | - | No | [link](https://www.dwavequantum.com/learn/publications/) |
| Spin Glass | Tile-Planted Spin Glass Instances | Square lattice coupling matrices | - | - | Yes | [link](https://arxiv.org/abs/1907.10809) |
| Spin Glass | Edwards-Anderson Lattice Spin Glass (d=3,...,8) | Lattice coupling configurations | - | - | Yes | [link](https://arxiv.org/abs/2407.14646) |
| Spin Glass | Exploring Quantum Annealing Architectures | Python-generated graph instances | - | - | No | [link](https://github.com/GabrielJauma/exploring-QA-spin-glass) |
| Spin Glass | Random Field Ising Model (RFIM) Instances | Lattice configurations with random fields | - | - | Yes | [link](https://chimera.roma1.infn.it/RESEARCH/RFIM.html) |

---

## 15. Vehicle Routing

Vehicle routing problems ask how to design a set of routes for a fleet of vehicles to serve a collection of customers while minimizing total cost. These problems generalize TSP to multiple vehicles with capacity, time window, and pickup-delivery constraints, and are central to logistics and supply chain optimization.

### Key Datasets

**CVRPLIB** (hosted at PUC-Rio) is the definitive resource for the Capacitated Vehicle Routing Problem, aggregating multiple benchmark families under one roof. The **Uchoa X Instances** (100 instances, 100--1,000 customers) are the modern standard, systematically varying depot positioning, customer clustering, demand distribution, and route size. The new **XL Instances** (1,000--10,000 customers) extend the same generation principles to large-scale settings, with a Best Known Solution challenge launched in January 2026. CVRPLIB also hosts real-world instances from **Loggi** (Brazilian delivery, 6 instances, 401--1,001 customers) and **ORTEC** (US grocery delivery, 6 instances, 242--701 customers with real driving times), providing practical grounding beyond synthetic benchmarks.

The classic benchmarks remain useful for solver verification. The **Christofides-Mingozzi-Toth (CMT) Instances** (14 instances, 50--199 customers, all solved to optimality) and the **Augerat Instances** (Sets A, B, P; 74 instances, 15--100 customers, mostly solved) are standard reference points. The **Golden-Wasil-Kelly-Chao Instances** (20 instances, 200--480 customers) bridge the gap between classic small-scale and modern large-scale benchmarks.

For the **Vehicle Routing Problem with Time Windows (VRPTW)**, the **Solomon Benchmark** (56 instances, 100 customers each) is foundational, with over 3,000 publications using it. Instances are grouped into random (R), clustered (C), and mixed (RC) types, with narrow (type 1) and wide (type 2) scheduling horizons. The **Gehring-Homberger Benchmark** (300 instances, 200--1,000 customers) extends Solomon to larger scales. Both are maintained at SINTEF TOP with best-known solutions.

The **Pickup and Delivery Problem with Time Windows (PDPTW)** is served by the **Li & Lim Benchmark** (354 instances, 100--1,000 tasks), derived from Solomon instances by pairing locations as pickup-delivery requests. The **Sartori & Buriol** real-world instances complement these with more realistic characteristics.

For **arc routing**, the **Capacitated Arc Routing Problem (CARP)** has several benchmark families: the **GDB Instances** (23 small instances, all solved), the **BCCM/val Instances** (34 instances, all solved), and the **Eglese/Li Winter Gritting Instances** (24 instances derived from real Lancashire road networks). The **BHW Instances** (20 instances) were assembled for the 12th DIMACS Implementation Challenge CARP track.

### Format Notes

VRPLIB format is standard for CVRP. Solomon format is used for VRPTW and PDPTW. CARP instances use their own text format. VRP-REP provides a standardized XML representation for diverse VRP variants.

### Notable Gaps

Multi-depot VRP and heterogeneous fleet VRP have limited dedicated benchmark coverage. Dynamic and stochastic VRP variants, increasingly important in practice, lack consolidated benchmarks.

### Cross-References

TSP (Category 3) is the single-vehicle, unconstrained special case of VRP. TSPLIB instances are sometimes used for VRP by adding depot and capacity data. The DIMACS 12th Implementation Challenge covered CVRP, VRPTW, and CARP tracks, connecting to graph path problems. Facility location (Category 15) shares real-world instances with CVRPLIB's Loggi collection.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Capacitated Vehicle Routing Problem | CVRPLIB - Uchoa X Instances | VRPLIB | 100 | 100-1000 customers | No | [link](https://galgos.inf.puc-rio.br/cvrplib/index.php/en/) |
| Capacitated Vehicle Routing Problem | CVRPLIB - XL Instances | VRPLIB | - | 1000-10000 customers | No | [link](https://galgos.inf.puc-rio.br/cvrplib/index.php/en/) |
| Capacitated Vehicle Routing Problem | Christofides, Mingozzi & Toth (CMT) Instances | VRPLIB | 14 | 50-199 customers | Yes | [link](https://neo.lcc.uma.es/vrp/vrp-instances/capacitated-vrp-instances/) |
| Capacitated Vehicle Routing Problem | Augerat Instances (Sets A, B, P) | VRPLIB | 74 | 15-100 customers | Yes | [link](https://neo.lcc.uma.es/vrp/vrp-instances/capacitated-vrp-instances/) |
| Capacitated Vehicle Routing Problem | Golden, Wasil, Kelly & Chao Instances | VRPLIB | 20 | 200-480 customers | No | [link](https://neo.lcc.uma.es/vrp/vrp-instances/capacitated-vrp-instances/) |
| Capacitated Vehicle Routing Problem | CVRPLIB - Loggi Real-World Instances | VRPLIB | 6 | 401-1001 customers | No | [link](https://galgos.inf.puc-rio.br/cvrplib/index.php/en/) |
| Capacitated Vehicle Routing Problem | CVRPLIB - ORTEC Real-World Instances | VRPLIB | 6 | 242-701 customers | No | [link](https://galgos.inf.puc-rio.br/cvrplib/index.php/en/) |
| Vehicle Routing Problem with Time Windows | Solomon VRPTW Benchmark | Solomon | 56 | 100 customers | Yes | [link](https://www.sintef.no/projectweb/top/vrptw/solomon-benchmark/) |
| Vehicle Routing Problem with Time Windows | Gehring & Homberger Large-Scale VRPTW | Solomon | 300 | 200-1000 customers | No | [link](https://www.sintef.no/projectweb/top/vrptw/homberger-benchmark/) |
| Vehicle Routing Problem with Time Windows | DIMACS VRPTW Challenge Instances | Solomon | - | 100-1000 customers | No | [link](http://dimacs.rutgers.edu/programs/challenge/vrp/vrptw/) |
| Pickup and Delivery Problem with Time Windows | Li & Lim PDPTW Benchmark | Solomon | 354 | 100-1000 tasks | No | [link](https://www.sintef.no/projectweb/top/pdptw/li-lim-benchmark/) |
| Pickup and Delivery Problem with Time Windows | Sartori & Buriol PDPTW Real-World Instances | custom | - | - | No | [link](https://github.com/cssartori/pdptw-instances) |
| Capacitated Arc Routing Problem | GDB Instances (Golden, DeArmon & Baker) | CARP | 23 | 7-27 nodes; 11-55 edges | Yes | [link](https://www.uv.es/belengue/carp.html) |
| Capacitated Arc Routing Problem | BCCM / val Instances (Benavent et al.) | CARP | 34 | 24-50 nodes; 34-97 edges | Yes | [link](https://www.uv.es/belengue/carp.html) |
| Capacitated Arc Routing Problem | Eglese / Li Instances (Winter Gritting) | CARP | 24 | 77-140 nodes; 98-190 edges | No | [link](https://www.uv.es/belengue/carp.html) |
| Capacitated Arc Routing Problem | KSHS Instances (Kiuchi et al.) | CARP | 6 | - | Yes | [link](https://www.uv.es/belengue/carp.html) |
| Capacitated Arc Routing Problem | BHW Instances (Bach, Hasle & Wohlk) | CARP | 20 | - | No | [link](http://dimacs.rutgers.edu/programs/challenge/vrp/carp/) |
| Vehicle Routing Problem | Christofides & Eilon Instances | VRPLIB | 15 | 13-101 customers | Yes | [link](https://neo.lcc.uma.es/vrp/vrp-instances/capacitated-vrp-instances/) |
| Vehicle Routing Problem | Taillard CVRP Instances | VRPLIB | 12 | 75-385 customers | No | [link](https://neo.lcc.uma.es/vrp/vrp-instances/capacitated-vrp-instances/) |
| Vehicle Routing Problem | VRP-REP Repository | XML (VRP-REP) | - | - | No | [link](http://www.vrp-rep.org/) |
| Vehicle Routing Problem | DIMACS 12th Implementation Challenge | mixed | - | - | No | [link](http://dimacs.rutgers.edu/programs/challenge/vrp/) |

---

## 16. Facility Location

Facility location problems ask where to open facilities and how to assign customers to them so as to minimize a combination of fixed opening costs and transportation costs. These problems are fundamental to supply chain design, public service planning, and network infrastructure placement.

### Key Datasets

**UflLib** (645 instances, 10--750 facilities/customers) is the comprehensive benchmark for Uncapacitated Facility Location (UFL). It aggregates 14 benchmark packages from multiple contributors, including Bilde-Krarup, Euclidean, Galvao-Raggi, and the notoriously difficult **Koerkel-Ghosh instances** (m=n in {250, 500, 750}), which remain partially unsolved and are considered among the hardest UFL benchmarks. A mirror is maintained at Goethe University Frankfurt.

**OR-Library** provides instances for both uncapacitated (15 instances, 16--100 facilities, 50--1,000 customers) and **capacitated facility location** (40 instances, same scale range). The capacitated instances span thirteen problem sets (IV--XIII and A--C) and are also used as warehouse location benchmarks, since the two problems are equivalent in the discrete optimization literature. The **Kochetov Hard UFL Instances** from the Sobolev Institute include classes with large integrality gaps and exponentially many strong local optima, specifically designed to challenge both metaheuristics and exact methods.

For **capacitated facility location (CFLP)**, the **Holmberg SSCFLP Instances** (71 instances, 10--30 facilities, 50--200 customers) are the standard for the single-source variant, with four subsets of varying distributions and sizes. The **CommaLAB CFLP Instances** from the University of Pisa extend to larger-scale settings.

The **p-Median** problem is benchmarked by **OR-Library p-Median Instances** (40 instances, 100--900 vertices), where Floyd's algorithm must be applied to edge costs to obtain the full allocation cost matrix. **TSPLIB-derived instances** (98 instances, up to 3,038 vertices) provide larger-scale benchmarks using Euclidean distances from TSP city coordinates.

The closely related **p-Center** problem reuses the same OR-Library instances (pmed1--pmed40) with a minimax objective; all 40 have been solved to proven optimality. **TSPLIB-derived p-Center instances** complement these for scalability testing.

**Hub location** is served by the **OR-Library AP Dataset** (Australia Post, up to 200 nodes), the **CAB Dataset** (Civil Aeronautics Board, 25 nodes), and the **HLP Survey Benchmark** which standardizes AP, CAB, and Turkish postal network instances in CSV format with over 5,000 optimal solutions across 12 problem variants.

### Format Notes

UflLib uses its own text format specifying facilities, customers, opening costs, and connection costs. OR-Library uses a common text format across its facility location files. Hub location data uses coordinate, flow, and cost matrices. No single universal format exists for the category.

### Notable Gaps

Multi-period and dynamic facility location problems lack dedicated benchmarks. Stochastic facility location, where demand or costs are uncertain, is increasingly important but has no consolidated benchmark suite in this registry.

### Cross-References

OR-Library instances appear across facility location, knapsack (Category 6), set cover (Category 8), and scheduling (Category 7). TSPLIB-derived instances connect to TSP (Category 3) and graph path problems. The p-median problem is structurally related to clustering problems. MIPLIB (Category 10) contains facility location formulations as MIP instances. CVRPLIB's Loggi instances (Category 14) were derived from vehicle routing and facility location data in Brazilian cities.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Uncapacitated Facility Location | UflLib Benchmark Collection | UflLib text format (facilities, customers, opening costs, connection costs) | 645 | 10-750 facilities; 10-750 customers | Yes | [link](https://resources.mpi-inf.mpg.de/departments/d1/projects/benchmarks/UflLib/) |
| Uncapacitated Facility Location | OR-Library Uncapacitated Warehouse Location | OR-Library text (warehouses, customers, capacities, fixed costs, demands, allocation costs) | 15 | 16-100 facilities; 50-1000 customers | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/uncapinfo.html) |
| Uncapacitated Facility Location | Kochetov Hard UFL Instances | Custom text | - | - | Yes | [link](https://www.academia.edu/4646193/Benchmark_library_Discrete_Location_Problems) |
| Capacitated Facility Location | OR-Library Capacitated Warehouse Location | OR-Library text (warehouses, customers, capacities, fixed costs, demands, allocation costs) | 40 | 16-100 facilities; 50-1000 customers | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/capinfo.html) |
| Capacitated Facility Location | Holmberg SSCFLP Instances | Custom text | 71 | 10-30 facilities; 50-200 customers | Yes | [link](https://or-brescia.unibs.it/instances/instances_sscflp) |
| Capacitated Facility Location | CommaLAB CFLP Instances | Multiple formats | - | - | Yes | [link](https://commalab.di.unipi.it/datasets/mex/) |
| p-Median | OR-Library p-Median Instances | OR-Library text (vertices, edges, p; edge list with costs) | 40 | 100-900 vertices; 5-200 p | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/pmedinfo.html) |
| p-Median | TSPLIB-derived p-Median Instances | TSPLIB coordinate format (Euclidean distances) | 98 | up to 3038 vertices | Yes | [link](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) |
| p-Center | OR-Library p-Center Instances (pmed) | OR-Library text (vertices, edges, p; edge list with costs) | 40 | 100-900 vertices; 5-200 p | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/pmedinfo.html) |
| p-Center | TSPLIB-derived p-Center Instances | TSPLIB coordinate format (Euclidean distances, rounded to integer) | - | up to 3038 vertices | Yes | [link](https://msinnl.github.io/pages/pcenter.html) |
| Hub Location | OR-Library AP Hub Location Dataset | OR-Library text (coordinates, flows, costs) | 3 | up to 200 nodes | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/phubinfo.html) |
| Hub Location | OR-Library CAB Hub Location Dataset | OR-Library text (coordinates, flows, costs) | 1 | 25 nodes | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/phubinfo.html) |
| Hub Location | HLP Survey Benchmark Datasets | CSV (node file, distance matrix, demand matrix) | - | 10-80 nodes | Yes | [link](http://m3nets.de/HLP/) |
| Warehouse Location | OR-Library Warehouse Location Instances | OR-Library text (warehouses, customers, capacities, fixed costs, demands, allocation costs) | 40 | 16-100 facilities; 50-1000 customers | Yes | [link](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/capinfo.html) |

---

## 17. Constraint Satisfaction

Constraint satisfaction problems (CSPs) require finding assignments of values to variables that satisfy a set of constraints, without necessarily optimizing an objective. This category also covers timetabling and rostering problems, which are among the most practically important CSP applications.

### Key Datasets

**CSPLib** (97 problems) is a reference library of constraint satisfaction test problems across 16 categories, specified in natural language to encourage diverse modeling approaches. It serves as a problem catalog rather than a fixed instance set, with many entries including example models in various constraint languages.

The **XCSP3 Competition Benchmarks** (over 23,000 instances) represent the current scale frontier for CSP benchmarking. Covering both satisfaction (CSP) and optimization (COP) variants, the 2024 competition alone featured 34 problems spanning mathematics, logistics, and scheduling, with 10--15 instances per problem series. All instances are in the standardized XCSP3 XML format.

The **MiniZinc Challenge Benchmarks** (annually since 2008) provide a solver-independent testing ground, with approximately 100 instances across 10--12 models selected each year. Restricted to integer variables, these benchmarks cover the breadth of finite-domain constraint solving. Models and data files are available under the MIT license on GitHub.

For **university course timetabling**, the **ITC 2007 Track 3** (21 real-world instances from the University of Udine) and **ITC 2019** (30 instances from universities across six continents) are the primary benchmarks. ITC 2019 combines student sectioning with time and room assignment, reflecting modern timetabling complexity. The **ITC 2007 Track 2** covers post-enrolment-based timetabling.

**Examination timetabling** is served by the **ITC 2007 Track 1** (12 instances from British universities, 273--1,018 exams, 4,421--16,365 students) and the **University of Nottingham collection**, which aggregates Carter's classic benchmark instances.

**High school timetabling** has the **ITC 2011 XHSTT Archive** (35 instances from 10 countries in the XHSTT XML format), providing international diversity in scheduling constraints and institutional requirements.

**Nurse rostering** is extensively benchmarked. **INRC-I** (69 real-world instances across sprint, medium, and long tracks) and **INRC-II** (multi-stage formulation with rolling-horizon decision making over 4--8 weeks) represent competition-driven benchmarks. **NSPLib** (9,210 instances, 25--150 nurses, 7--28 day periods) is the largest collection. The **KU Leuven benchmarks** provide real Belgian hospital data with normal, overload, and absence scenarios.

**Sports scheduling** is covered by the **RobinX Repository** (real-life instances from different countries and sports in a unified XML format) and the **ITC 2021** competition (45 instances for double round-robin tournaments with 16--20 teams).

### Format Notes

CSP formats are fragmented: XCSP3 (XML), MiniZinc (.mzn/.dzn), and CSPLib (natural language specifications) are the main options. Timetabling uses competition-specific custom text or XML formats. Nurse rostering uses custom text or XML formats. RobinX uses its own XML format for sports scheduling.

### Notable Gaps

General CSP random instance generators exist but lack standardized benchmark suites with documented phase-transition behavior comparable to SAT. Constraint optimization (COP) is covered by XCSP3 and MiniZinc but has less dedicated benchmarking infrastructure than pure satisfaction problems.

### Cross-References

CSP encodings are closely related to SAT (Category 1), as constraint satisfaction problems can be translated to boolean satisfiability. Nurse rostering connects to staff scheduling in the scheduling category (Category 7). Sports scheduling shares structure with graph coloring (Category 2) through tournament design. Timetabling problems can be formulated as ILP instances (Category 10).


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Constraint Satisfaction Problem | CSPLib | Natural language specifications with model files | 97 | - | No | [link](https://www.csplib.org/) |
| Constraint Satisfaction Problem | XCSP3 Competition Benchmarks | XCSP3 XML | 23000 | - | No | [link](https://xcsp.org/instances/) |
| Constraint Satisfaction Problem | MiniZinc Challenge Benchmarks | MiniZinc (.mzn + .dzn) | - | 10-12 models_per_year; 8-12 instances_per_model | No | [link](https://github.com/MiniZinc/minizinc-benchmarks) |
| University Course Timetabling | ITC 2007 Curriculum-Based Course Timetabling (Track 3) | Custom text | 21 | University of Udine source | No | [link](https://www.unitime.org/itc2007/) |
| University Course Timetabling | ITC 2007 Post Enrolment Course Timetabling (Track 2) | Custom text | - | - | No | [link](https://www.unitime.org/itc2007/) |
| University Course Timetabling | ITC 2019 University Course Timetabling | XML | 30 | Multiple universities across six continents institutions | No | [link](https://www.itc2019.org/) |
| Examination Timetabling | ITC 2007 Examination Timetabling (Track 1) | Custom text | 12 | 273-1018 exams; 4421-16365 students | No | [link](https://www.unitime.org/itc2007/) |
| Examination Timetabling | University of Nottingham Exam Timetabling Instances | Custom text | - | - | No | [link](https://people.cs.nott.ac.uk/pszajp/timetabling/exam/) |
| High School Timetabling | ITC 2011 XHSTT High School Timetabling Archive | XML (XHSTT) | 35 | 10 countries | No | [link](https://www.utwente.nl/en/eemcs/dmmp/hstt/itc2011/) |
| Nurse Rostering | INRC-I (First International Nurse Rostering Competition 2010) | Custom text | 69 | - | No | [link](https://nrpcompetition.kuleuven-kulak.be/) |
| Nurse Rostering | INRC-II (Second International Nurse Rostering Competition) | Custom text | - | 30-120 nurses | No | [link](https://mobiz.vives.be/inrc2/) |
| Nurse Rostering | NSPLib (Nurse Scheduling Problem Library) | Custom text | 9210 | 25-150 nurses | No | [link](https://www.projectmanagement.ugent.be/research/personnel_scheduling/nsp) |
| Nurse Rostering | Scheduling Benchmarks (Employee Scheduling) | XML | - | - | No | [link](https://www.schedulingbenchmarks.org/) |
| Nurse Rostering | KU Leuven Nurse Rostering Benchmarks | Custom text | - | 4-46 nurses | No | [link](https://gent.cs.kuleuven.be/nurserostering.html) |
| Sports Scheduling | RobinX Sports Timetabling Repository | XML (RobinX) | - | - | No | [link](https://robinxval.ugent.be/RobinX/index.php) |
| Sports Scheduling | ITC 2021 Sports Timetabling | XML (RobinX) | 45 | 16-20 teams | No | [link](https://robinxval.ugent.be/ITC2021/index.php) |

---

## 18. Graph Matching

Graph matching encompasses problems of determining structural correspondence between graphs: graph isomorphism, subgraph isomorphism, maximum common subgraph, and graph edit distance. These problems arise in pattern recognition, chemoinformatics, social network analysis, and computer vision.

### Key Datasets

For **subgraph isomorphism**, the **MIVIA ARG Database** (143,600 unlabeled graphs, up to 2,000 nodes) is the standard benchmark, organized into 168 graph types generated from six models (2D/3D/4D regular meshes, bounded valence, random). It was used to evaluate VF2 and VF3, the most widely cited subgraph isomorphism algorithms. The **MIVIA LDGraphs** extension (6,350 instances, 300--10,000 nodes, edge density 0.2--0.4) targets large and dense graphs at scales relevant to bioinformatics and social network analysis.

The **Solnon SIP Benchmarks** (14,621 instances, 10--6,671 nodes) provide a comprehensive evaluation suite aggregating eight benchmark families: real application graphs (images, meshes), Stanford GraphBase (LV, 113 graphs), scale-free networks, MIVIA bounded-valence/mesh instances, and random instances near the phase transition. The **Glasgow Subgraph Solver Test Suite** uses the same Solnon benchmark suite but introduces supplemental implied constraints based on path counting for stronger domain filtering.

For **graph isomorphism**, the **Neuen-Schweitzer Benchmark** (400--4,000 nodes) is specifically designed to challenge state-of-the-art solvers (Nauty, Traces, Bliss, Conauto). These instances are orders of magnitude harder than all previously available benchmarks at comparable sizes -- instances at 1,500 vertices are far more difficult than generic random graphs with tens of thousands of vertices. The MIVIA ARG Database also provides graph-graph isomorphism pairs.

**Maximum common subgraph (MCS)** is benchmarked by labeled graph pairs from the **MIVIA ARG Database** (166,000 labeled graphs with known non-trivial common subgraphs) and the **Dilkas MCS Benchmark** (73 graph pairs aggregated from multiple papers).

**Graph edit distance (GED)** has a rich benchmark ecosystem centered on the **IAM Graph Database** (~7,000 graphs across six sub-datasets: Letter, AIDS, GREC, Fingerprint, Mutagenicity, Protein). The **ICPR 2016 Graph Distance Contest** integrates IAM and GREYC collections across seven datasets with a 30-second time limit per comparison. The **GREYC Chemistry Dataset** provides molecular graphs (Acyclic, Alkane, PAH, MAO) with regression targets for boiling point prediction. The **GEDLIB** C++ library bundles all these datasets with standardized edit cost functions.

The **Stanford GraphBase** (113 graphs, 10--6,671 nodes) and **SNAP Large Network Collection** (~80 networks, up to 226M nodes) serve as target graphs for pattern matching scalability evaluation, particularly in graph database query workloads.

### Format Notes

Formats are diverse. MIVIA uses a custom binary format. Solnon and Glasgow use text adjacency and LAD formats. GED benchmarks predominantly use GXL (Graph Exchange Language). SNAP uses TSV edge lists. Stanford GraphBase has its own text format. Conversion between formats is frequently necessary.

### Notable Gaps

Temporal graph matching and dynamic graph isomorphism lack dedicated benchmarks. Approximate graph matching for large-scale knowledge graphs is increasingly important but has no consolidated benchmark suite. Weighted and attributed graph matching benchmarks beyond molecular graphs are sparse.

### Cross-References

SNAP (Category 2) provides large-scale target graphs for pattern matching evaluation. The Stanford GraphBase connects to subgraph isomorphism benchmarks via the LV benchmark in the Solnon suite. Molecular graph benchmarks (IAM, GREYC) connect to applications in computational chemistry. Graph coloring (Category 2) and graph isomorphism share structural concerns about graph symmetry. GED computation relates to string edit distance (Category 9) through analogous dynamic programming formulations.


### Dataset Registry

| Problem | Dataset | Format | Instances | Scale | Optimal? | URL |
|---------|---------|--------|-----------|-------|----------|-----|
| Subgraph Isomorphism | MIVIA ARG Database | Binary (MIVIA custom) | 143600 | up to 2,000 nodes | Yes | [link](https://mivia.unisa.it/datasets/graph-database/arg-database/) |
| Subgraph Isomorphism | MIVIA LDGraphs (Large Dense Graphs) | Binary (MIVIA custom) | 6350 | 300 to 10,000 nodes | Yes | [link](https://mivia.unisa.it/datasets/graph-database/mivia2-graph-database/) |
| Subgraph Isomorphism | Solnon SIP Benchmarks | Text adjacency | 14621 | 10 to 6,671 nodes | Yes | [link](https://perso.liris.cnrs.fr/christine.solnon/SIP.html) |
| Subgraph Isomorphism | Glasgow Subgraph Solver Test Suite | CSV / LAD | 14621 | varies (pattern and target graph pairs) nodes | Yes | [link](https://github.com/ciaranm/glasgow-subgraph-solver) |
| Graph Isomorphism | Neuen-Schweitzer Benchmark Graphs | DIMACS-like | - | 400 to 4,000 nodes | Yes | [link](https://doi.org/10.4230/LIPIcs.ESA.2017.60) |
| Graph Isomorphism | MIVIA ARG Database (Graph Isomorphism pairs) | Binary (MIVIA custom) | 143600 | up to 2,000 nodes | Yes | [link](https://mivia.unisa.it/datasets/graph-database/arg-database/) |
| Maximum Common Subgraph | MIVIA ARG Database (Labeled Common Subgraph pairs) | Binary (MIVIA custom) | 166000 | up to 2,000 nodes | Yes | [link](https://mivia.unisa.it/datasets/graph-database/arg-database/) |
| Maximum Common Subgraph | MCS Benchmark (Dilkas collection) | LAD | 73 | varies (pairs typically similar sizes) nodes | Yes | [link](https://dilkas.github.io/pdf/mcs_dissertation.pdf) |
| Graph Edit Distance | IAM Graph Database | GXL (Graph Exchange Language) | 7000 | varies by dataset (typically 2 to 200) nodes | No | [link](https://fki.tic.heia-fr.ch/databases/iam-graph-database) |
| Graph Edit Distance | ICPR 2016 Graph Distance Contest | GXL | - | varies by dataset nodes | No | [link](https://gdc2016.greyc.fr/) |
| Graph Edit Distance | GREYC Chemistry Dataset | CML / GXL | - | typically 2 to 60 atoms per molecule nodes | No | [link](https://brunl01.users.greyc.fr/CHEMISTRY/) |
| Graph Edit Distance | GEDLIB Benchmark Collection | GXL | - | varies (organized by node-count bins) nodes | No | [link](https://github.com/dbblumenthal/gedlib) |
| Pattern Matching in Graphs | Stanford GraphBase (LV Benchmark) | Text (SGBformat) | 113 | 10 to 6,671 nodes | Yes | [link](https://www-cs-faculty.stanford.edu/~knuth/sgb.html) |
| Pattern Matching in Graphs | SNAP Large Network Collection | TSV edge list | 80 | 4,039 to 226,000,000 nodes; 88,234 to 480,000,000 edges | No | [link](https://snap.stanford.edu/data/) |

---

## 19. Summary Table

The table below maps major problems to their primary benchmark datasets. Entries marked with an asterisk (*) indicate that the dataset is adapted or repurposed rather than purpose-built.

| Problem | Primary Dataset(s) | Instances | Scale |
|---|---|---|---|
| SAT | SAT Competition, SATLIB | ~11,000 | up to 10M vars |
| 3-SAT | SATLIB Uniform Random | 8,000 | 20--250 vars |
| Max-SAT | MaxSAT Evaluation | ~2,000 | up to 1M vars |
| QBF | QBFLIB | 13,000 | various |
| Circuit-SAT | ISCAS-85/89, EPFL | ~64 | 17--7,552 gates |
| Max Independent Set | DIMACS 2nd, BHOSLIB, SNAP | ~160 | up to 226M vertices |
| Vertex Cover | PACE 2019, BHOSLIB | ~240 | up to 4,000 vertices |
| Max Clique | DIMACS 2nd, BHOSLIB | ~77 | up to 4,000 vertices |
| Graph Coloring | COLOR02/03/04, BHOSLIB | ~160 | up to 4,000 vertices |
| Dominating Set | PACE 2025, SNAP | ~280 | varies |
| TSP | TSPLIB, VLSI, National | ~237 | up to 744K cities |
| Hamiltonian Cycle | FHCP Challenge Set | 1,001 | 66--9,528 vertices |
| Longest Path | KaLP | varies | mazes, road networks |
| Steiner Tree | SteinLib | hundreds | various |
| Max Cut | Gset, BiqMac | ~121 | up to 20K vertices |
| Feedback Vertex Set | PACE 2016, PACE 2022 | ~260 | various |
| Graph Partitioning | Walshaw, DIMACS 10th | ~134 | up to 449K nodes |
| Network Flow (MMCF) | CommaLAB, SNDlib | ~900 | up to 1,225 nodes |
| Knapsack | Pisinger, Jooken | ~17,000 | up to 10K items |
| Bin Packing | BPPLIB | 6,195 | 50--1,000 items |
| Subset Sum | Pisinger* | varies | generated |
| Flow Shop | Taillard, VFR | 600 | up to 800x60 |
| Job Shop | JSPLIB, DMU | ~360 | up to 500x100 |
| RCPSP | PSPLIB | 1,560 | 30--120 activities |
| Set Cover | OR-Library SCP, RAIL | ~97 | up to 4.8K x 1.1M |
| Hitting Set | PACE 2025 | 200 | various |
| LCS | BB Benchmark, BAliBASE | ~6,300 | various |
| SCS | Blum et al. | ~25 | 8 strings |
| Edit Distance | TREC-5, Norvig, Birkbeck | ~56,000 | various |
| ILP / MIP | MIPLIB 2017 | 1,065 | up to 6M vars |
| QUBO | MQLib, QPLIB | ~11,300 | up to 53K vars |
| QAP | QAPLIB | 136 | 5--256 facilities |
| SVP | TU Darmstadt SVP Challenge | varies | dim 140--300 |
| LWE | TU Darmstadt LWE Challenge | grid | dim 40--120 |
| Integer Factoring | RSA Challenge, Cunningham | ~54 | up to 617 digits |
| FD/UCC Discovery | HPI Benchmark Suite | 16 | up to 223 columns |
| Spin Glass | RL4Ising, Gset, BiqMac | ~190,000 | up to 20K spins |
| CVRP | CVRPLIB (Uchoa X, XL) | ~206 | up to 10K customers |
| VRPTW | Solomon, Gehring-Homberger | ~356 | up to 1K customers |
| PDPTW | Li & Lim | 354 | up to 1K tasks |
| CARP | GDB, BCCM, Eglese | ~107 | up to 190 edges |
| Uncapacitated Facility Location | UflLib | 645 | up to 750 facilities |
| Capacitated Facility Location | OR-Library, Holmberg | ~111 | up to 1K customers |
| p-Median | OR-Library, TSPLIB* | ~138 | up to 3K vertices |
| p-Center | OR-Library pmed | 40 | 100--900 vertices |
| Hub Location | OR-Library AP/CAB, HLP | ~4 | up to 200 nodes |
| CSP | XCSP3, MiniZinc | ~23,000 | various |
| Course Timetabling | ITC 2007, ITC 2019 | ~51 | various |
| Exam Timetabling | ITC 2007 | 12 | 273--1,018 exams |
| Nurse Rostering | NSPLib, INRC-I/II | ~9,300 | up to 150 nurses |
| Subgraph Isomorphism | MIVIA ARG, Solnon SIP | ~158,000 | up to 10K nodes |
| Graph Isomorphism | Neuen-Schweitzer, MIVIA ARG | ~143,600 | up to 4K nodes |
| Graph Edit Distance | IAM, GEDLIB | ~7,000 | up to 200 nodes |
| Maximum Common Subgraph | MIVIA ARG, Dilkas | ~166,000 | up to 2K nodes |

---

## 20. Cross-Category Datasets

Several dataset repositories appear across multiple categories and deserve special mention as unifying resources.

### DIMACS Implementation Challenges

The DIMACS (Center for Discrete Mathematics and Theoretical Computer Science) challenge series has produced benchmark instances across multiple categories:

- **1st Challenge** (1990--1991): Network flows and matching (Category 5)
- **2nd Challenge** (1993): Cliques, coloring, and satisfiability (Categories 1, 2)
- **7th Challenge**: Semidefinite relaxations and max cut (Category 4)
- **10th Challenge** (2012): Graph partitioning and clustering (Categories 2, 4)
- **12th Challenge** (2021--2022): Vehicle routing -- CVRP, VRPTW, CARP (Category 14)
- **13th Challenge** (2025--2027): Network flows 2.0 (Category 5, ongoing)

The DIMACS graph format itself is a de facto standard used across satisfiability, graph optimization, and network flow.

### OR-Library (Beasley)

One of the earliest electronic benchmark repositories, OR-Library provides instances for:

- Flow shop and job shop scheduling (Category 8)
- Set covering, set packing, hitting set (Category 9)
- Knapsack (Category 7)
- Weighted tardiness (Category 8)
- Parallel machine scheduling (Category 8)
- UBQP (Category 11)
- Facility location -- uncapacitated, capacitated, p-median, p-center, hub location (Category 15)

While no longer actively maintained, it remains cited in hundreds of papers annually.

### MIPLIB

Mixed-integer programming naturally encodes problems from most categories. MIPLIB 2017's 1,065 instances include formulations of:

- Set packing and covering (Category 9)
- Network design and flow (Category 5)
- Scheduling (Category 8)
- Facility location and assignment (Category 15)
- Vehicle routing formulations (Category 14)

Researchers can filter MIPLIB instances by structural tags to find specific problem types.

### BHOSLIB

The Benchmarks with Hidden Optimum Solutions serve maximum independent set, minimum vertex cover, maximum clique, and graph coloring (Category 2). Their unique value is that optimal solutions are known by construction, enabling ground-truth evaluation that the older DIMACS instances cannot provide.

### PACE Challenges

The Parameterized Algorithms and Computational Experiments (PACE) challenge series has become a primary benchmark source for:

- Vertex cover (2019, Category 2)
- Feedback vertex set (2016) and directed FVS (2022, Category 4)
- Dominating set (2025, Category 2)
- Hitting set (2025, Category 9)

PACE instances are particularly well-designed, with public/private splits, clear time/memory limits, and instances specifically crafted to challenge parameterized algorithms.

### Taillard's Benchmarks

Eric Taillard's contributions span:

- Flow shop scheduling (Category 8)
- Job shop scheduling (Category 8)
- Open shop scheduling (Category 8)
- Quadratic assignment (Category 11)

His website at HEIG-VD remains the authoritative source for all four problem types, with maintained best-known bounds.

### SNAP and Network Repository

These large-scale network collections (SNAP: ~80 networks; Network Repository: ~6,659 graphs) serve as benchmarks for any graph optimization problem (Categories 2, 4) and graph matching (Category 17) when researchers need instances at real-world scale. They are essential for evaluating the scalability of heuristic algorithms.

### CVRPLIB

The Capacitated Vehicle Routing Problem Library at PUC-Rio aggregates classic, modern, and real-world CVRP instances (Category 14), including instances from the 12th DIMACS Implementation Challenge. Its Loggi instances share origins with facility location data (Category 15).

### MIVIA ARG Database

The MIVIA ARG Database (143,600 graphs) serves triple duty across subgraph isomorphism, graph isomorphism, and maximum common subgraph (Category 17). Its systematic coverage of graph types makes it a unifying benchmark for the entire graph matching family.

### International Timetabling Competitions (ITC)

The ITC series (2002, 2007, 2011, 2019, 2021) provides benchmarks spanning course timetabling, examination timetabling, high school timetabling, and sports scheduling (Category 16). These competition-driven instances ensure practical relevance and difficulty calibration.

---

## 21. Concluding Remarks

The benchmark landscape for computationally hard problems is uneven. Satisfiability, TSP, job shop scheduling, vehicle routing, and constraint satisfaction enjoy decades of benchmark development with active competition ecosystems. At the other extreme, database normal form problems, exact cover by 3-sets, and several network flow variants have minimal dedicated benchmarks.

A few patterns emerge:

1. **Competition-driven categories** (SAT, Max-SAT, QBF, TSP, scheduling, vehicle routing, constraint satisfaction, PACE problems) have the richest benchmarks, because annual competitions create demand for fresh, challenging instances.

2. **Reduction-connected problems** share benchmarks extensively. The MIS/clique/vertex-cover triple uses identical instances via complement. Max cut, QUBO, and spin glass are three views of one problem.

3. **Format fragmentation** remains a practical obstacle, especially in network flow and scheduling. The DIMACS and TSPLIB formats are rare examples of broadly adopted standards.

4. **Scale gaps** are common: many benchmarks target either small instances with known optima (for exact solver validation) or heuristic competition instances, but lack systematic coverage of the transition between tractable and intractable regimes.

For researchers entering a new problem domain, this survey aims to provide a starting point. For those already working in a domain, the cross-category connections may reveal useful benchmark reuse opportunities.
