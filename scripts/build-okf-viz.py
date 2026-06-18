"""Générer la visualisation HTML interactive du bundle OKF.

Utilise le visualiseur officiel d'Open Knowledge Format
(GoogleCloudPlatform/knowledge-catalog, Apache-2.0) : un graphe force-directed
self-contained (un seul .html, sans backend). Seul le sous-module `viewer`
est utilisé — aucune dépendance google-adk / bigquery requise, juste pyyaml.

Le tool est cloné à la demande dans .cache/okf-tool (gitignoré). Sortie :
output/okf/viz.html.

Prérequis : `task build-okf` doit avoir généré output/okf/ au préalable.
"""

import subprocess
import sys
from pathlib import Path

BUNDLE = Path("output/okf")
OUT = BUNDLE / "viz.html"
TOOL_DIR = Path(".cache/okf-tool")
TOOL_REPO = "https://github.com/GoogleCloudPlatform/knowledge-catalog.git"


def ensure_tool() -> Path:
    src = TOOL_DIR / "okf" / "src"
    if not src.is_dir():
        TOOL_DIR.parent.mkdir(parents=True, exist_ok=True)
        print(f"Clonage du visualiseur OKF → {TOOL_DIR} …")
        subprocess.run(
            ["git", "clone", "--depth", "1", TOOL_REPO, str(TOOL_DIR)],
            check=True,
        )
    return src


def main():
    if not BUNDLE.is_dir():
        sys.exit("output/okf/ absent — lancer `task build-okf` d'abord.")
    src = ensure_tool()
    sys.path.insert(0, str(src))
    from enrichment_agent.viewer.generator import generate_visualization

    stats = generate_visualization(BUNDLE, OUT, bundle_name="Adrien Sales — OKF")
    size_kb = stats["bytes"] // 1024
    print(f"Done. {OUT} — {stats['concepts']} concepts, "
          f"{stats['edges']} liens, {size_kb} Ko")


if __name__ == "__main__":
    main()
