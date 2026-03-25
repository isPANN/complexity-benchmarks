# Survey of Benchmark Datasets for Computationally Hard Problems

## 1. Overview

This survey catalogs publicly available benchmark datasets for computationally hard (typically NP-hard or harder) problems, organized into 13 categories that align with the `pred` reduction framework's classification of 112 problem types connected by 76 known reductions. The goal is practical: to help researchers find the right dataset for evaluating algorithms on specific problem types, and to understand how datasets relate across problem boundaries.

The 13 categories are:

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

Graph isomorphism, while a famous problem in computational complexity, lacks representation in this registry. Subgraph isomorphism benchmarks exist in the pattern matching literature but are not catalogued here.

### Cross-References

BHOSLIB and DIMACS instances appear across MIS, vertex cover, clique, and coloring. The DIMACS 10th Challenge instances (Category 4, graph partitioning) are also used for clique algorithm scalability evaluation. Max clique is equivalent to MIS on the complement graph, and vertex cover equals n minus MIS, so these three problems share all benchmark suites.

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

TSPLIB instances are used across TSP, ATSP, bottleneck TSP, and Hamiltonian cycle/path. The FHCP Challenge Set serves both Hamiltonian cycle and path research. TSP is closely related to the vehicle routing problem (not explicitly covered in this registry).

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

---

## 15. Summary Table

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

---

## 16. Cross-Category Datasets

Several dataset repositories appear across multiple categories and deserve special mention as unifying resources.

### DIMACS Implementation Challenges

The DIMACS (Center for Discrete Mathematics and Theoretical Computer Science) challenge series has produced benchmark instances across multiple categories:

- **1st Challenge** (1990--1991): Network flows and matching (Category 5)
- **2nd Challenge** (1993): Cliques, coloring, and satisfiability (Categories 1, 2)
- **7th Challenge**: Semidefinite relaxations and max cut (Category 4)
- **10th Challenge** (2012): Graph partitioning and clustering (Categories 2, 4)
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

While no longer actively maintained, it remains cited in hundreds of papers annually.

### MIPLIB

Mixed-integer programming naturally encodes problems from most categories. MIPLIB 2017's 1,065 instances include formulations of:

- Set packing and covering (Category 9)
- Network design and flow (Category 5)
- Scheduling (Category 8)
- Facility location and assignment

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

These large-scale network collections (SNAP: ~80 networks; Network Repository: ~6,659 graphs) serve as benchmarks for any graph optimization problem (Categories 2, 4) when researchers need instances at real-world scale. They are essential for evaluating the scalability of heuristic algorithms.

---

## 17. Concluding Remarks

The benchmark landscape for computationally hard problems is uneven. Satisfiability, TSP, and job shop scheduling enjoy decades of benchmark development with active competition ecosystems. At the other extreme, database normal form problems, exact cover by 3-sets, and several network flow variants have minimal dedicated benchmarks.

A few patterns emerge:

1. **Competition-driven categories** (SAT, Max-SAT, QBF, TSP, scheduling, PACE problems) have the richest benchmarks, because annual competitions create demand for fresh, challenging instances.

2. **Reduction-connected problems** share benchmarks extensively. The MIS/clique/vertex-cover triple uses identical instances via complement. Max cut, QUBO, and spin glass are three views of one problem.

3. **Format fragmentation** remains a practical obstacle, especially in network flow and scheduling. The DIMACS and TSPLIB formats are rare examples of broadly adopted standards.

4. **Scale gaps** are common: many benchmarks target either small instances with known optima (for exact solver validation) or heuristic competition instances, but lack systematic coverage of the transition between tractable and intractable regimes.

For researchers entering a new problem domain, this survey aims to provide a starting point. For those already working in a domain, the cross-category connections may reveal useful benchmark reuse opportunities.
