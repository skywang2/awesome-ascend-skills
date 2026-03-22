#!/usr/bin/env python3
"""Sync external skills from configured repositories."""

import sys
import yaml
from pathlib import Path
from typing import List

script_dir = Path(__file__).parent
project_root = script_dir.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(script_dir))

from sync_types import ExternalSource


def load_config(config_path: str) -> List[ExternalSource]:
    """Load external sources from YAML config file.

    Args:
        config_path: Path to YAML configuration file.

    Returns:
        List of ExternalSource configurations.

    Raises:
        FileNotFoundError: If config file doesn't exist.
        yaml.YAMLError: If config file contains invalid YAML.
    """
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    config_data = yaml.safe_load(config_file.read_text(encoding="utf-8"))

    sources = []
    for source_data in config_data.get("sources", []):
        source = ExternalSource(
            name=source_data["name"],
            url=source_data["url"],
            branch=source_data.get("branch", "main"),
            enabled=source_data.get("enabled", True),
        )
        sources.append(source)

    return sources


def main():
    """Main entry point."""
    # Default config path (relative to project root)
    config_path = ".github/external-sources.yml"

    try:
        sources = load_config(config_path)
        print(f"Loaded {len(sources)} external sources")
        for source in sources:
            print(f"  - {source.name}: {source.url} (branch: {source.branch})")
        print("\n✅ Configuration loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load config: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
