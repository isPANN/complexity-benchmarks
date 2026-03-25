#!/usr/bin/env python3
"""Generate MkDocs site pages from YAML registry files."""

import os
import shutil
import yaml
from pathlib import Path

REGISTRY_DIR = Path("registry")
DOCS_DIR = Path("site_docs")
STATIC_DIR = Path("static")


def load_registries():
    """Load all YAML registry files, sorted by filename."""
    registries = []
    for f in sorted(REGISTRY_DIR.glob("*.yaml")):
        with open(f) as fh:
            data = yaml.safe_load(fh)
            data["_filename"] = f.stem
            registries.append(data)
    return registries


def format_scale(scale):
    """Format scale dict into a readable string."""
    if not scale:
        return "-"
    parts = []
    for k, v in scale.items():
        parts.append(f"{v} {k}")
    return ", ".join(parts)


def generate_category_page(reg):
    """Generate a markdown page for one category."""
    lines = []
    cat_title = reg.get("description", reg.get("category", "Unknown"))
    lines.append(f"# {cat_title}\n")

    problems = reg.get("problems", [])
    for prob in problems:
        name = prob["name"]
        aliases = prob.get("aliases", [])
        pred_names = prob.get("pred_names", [])

        # Problem heading
        lines.append(f"## {name}\n")

        # Metadata line
        meta_parts = []
        if aliases:
            meta_parts.append(f"**Aliases:** {', '.join(aliases)}")
        if pred_names:
            meta_parts.append(
                f"**pred:** `{'`, `'.join(pred_names)}`"
            )
        if meta_parts:
            lines.append(" | ".join(meta_parts) + "\n")

        datasets = prob.get("datasets", [])
        if not datasets:
            lines.append("*No public benchmark datasets found.*\n")
            # Check for notes as a comment (from YAML comments this won't work,
            # but some entries have notes at problem level)
            continue

        # Dataset table
        lines.append(
            "| Dataset | Format | Instances | Scale | Optimal? | Reference |"
        )
        lines.append(
            "|---------|--------|-----------|-------|----------|-----------|"
        )

        for ds in datasets:
            ds_name = ds["name"]
            url = ds.get("url", "")
            fmt = ds.get("format", "-")
            count = ds.get("instance_count", "-")
            scale = format_scale(ds.get("scale"))
            optimal = ds.get("has_optimal_solution")
            if optimal is True:
                optimal_str = "Yes"
            elif optimal is False:
                optimal_str = "No"
            else:
                optimal_str = "-"
            ref = ds.get("reference", "-")
            usage = ds.get("usage", "")
            notes = ds.get("notes", "")

            # Name as link
            if url:
                name_cell = f"[{ds_name}]({url})"
            else:
                name_cell = ds_name

            lines.append(
                f"| {name_cell} | {fmt} | {count} | {scale} | {optimal_str} | {ref} |"
            )

        lines.append("")

        # Details (usage/notes) as expandable sections per dataset
        has_details = any(ds.get("usage") or ds.get("notes") for ds in datasets)
        if has_details:
            for ds in datasets:
                usage = ds.get("usage", "").strip()
                notes = ds.get("notes", "").strip()
                if usage or notes:
                    lines.append(f"**{ds['name']}**")
                    if usage:
                        lines.append(f": {usage}")
                    if notes:
                        lines.append(f": {notes}")
                    lines.append("")

    return "\n".join(lines)


def generate_index(registries):
    """Generate the index/home page."""
    lines = []
    lines.append("# Benchmark Datasets for Computationally Hard Problems\n")
    lines.append(
        "A structured registry of publicly available benchmark datasets for "
        "NP-hard and computationally hard problems, organized by problem category.\n"
    )

    # Stats
    total_problems = 0
    total_datasets = 0
    for reg in registries:
        for prob in reg.get("problems", []):
            total_problems += 1
            total_datasets += len(prob.get("datasets", []))

    lines.append(
        f"**{len(registries)} categories** · "
        f"**{total_problems} problems** · "
        f"**{total_datasets} datasets**\n"
    )

    # Category list
    lines.append("## Categories\n")
    lines.append("| # | Category | Problems | Datasets |")
    lines.append("|---|----------|----------|----------|")

    for i, reg in enumerate(registries, 1):
        fname = reg["_filename"]
        # Extract number prefix for display
        num = fname.split("-")[0]
        cat_desc = reg.get("description", reg.get("category", "Unknown"))
        n_prob = len(reg.get("problems", []))
        n_ds = sum(len(p.get("datasets", [])) for p in reg.get("problems", []))
        slug = fname
        lines.append(f"| {num} | [{cat_desc}]({slug}.md) | {n_prob} | {n_ds} |")

    lines.append("")

    # Quick links: all datasets in one table
    lines.append("## All Datasets\n")
    lines.append("| Category | Problem | Dataset | URL |")
    lines.append("|----------|---------|---------|-----|")

    for reg in registries:
        cat = reg.get("description", reg.get("category", ""))
        fname = reg["_filename"]
        for prob in reg.get("problems", []):
            for ds in prob.get("datasets", []):
                url = ds.get("url", "")
                link = f"[link]({url})" if url else "-"
                lines.append(
                    f"| [{cat}]({fname}.md) | {prob['name']} | {ds['name']} | {link} |"
                )

    lines.append("")
    return "\n".join(lines)


def main():
    registries = load_registries()

    # Clean and create docs dir
    DOCS_DIR.mkdir(exist_ok=True)

    # Copy static assets
    if STATIC_DIR.exists():
        for src in STATIC_DIR.rglob("*"):
            if src.is_file():
                dest = DOCS_DIR / src.relative_to(STATIC_DIR)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)

    # Generate index
    index_content = generate_index(registries)
    (DOCS_DIR / "index.md").write_text(index_content)

    # Generate category pages
    nav_items = [{"Home": "index.md"}]
    categories = []
    for reg in registries:
        fname = reg["_filename"]
        page_content = generate_category_page(reg)
        (DOCS_DIR / f"{fname}.md").write_text(page_content)
        cat_desc = reg.get("description", reg.get("category", ""))
        categories.append({cat_desc: f"{fname}.md"})

    nav_items.append({"Categories": categories})

    # Write mkdocs.yml
    mkdocs_config = {
        "site_name": "Complexity Benchmarks",
        "site_description": "Benchmark datasets for computationally hard problems",
        "docs_dir": str(DOCS_DIR),
        "theme": {
            "name": "material",
            "palette": [
                {
                    "scheme": "default",
                    "primary": "indigo",
                    "accent": "indigo",
                    "toggle": {
                        "icon": "material/brightness-7",
                        "name": "Switch to dark mode",
                    },
                },
                {
                    "scheme": "slate",
                    "primary": "indigo",
                    "accent": "indigo",
                    "toggle": {
                        "icon": "material/brightness-4",
                        "name": "Switch to light mode",
                    },
                },
            ],
            "features": [
                "navigation.instant",
                "navigation.tracking",
                "navigation.sections",
                "navigation.expand",
                "navigation.top",
                "search.suggest",
                "search.highlight",
                "content.tabs.link",
                "toc.integrate",
            ],
        },
        "plugins": ["search"],
        "markdown_extensions": [
            "tables",
            "attr_list",
            "def_list",
            "pymdownx.highlight",
            "pymdownx.superfences",
        ],
        "nav": nav_items,
    }

    with open("mkdocs.yml", "w") as f:
        yaml.dump(mkdocs_config, f, default_flow_style=False, sort_keys=False)

    print(f"Generated {len(registries)} category pages + index")
    print(f"Run: mkdocs serve")


if __name__ == "__main__":
    main()
