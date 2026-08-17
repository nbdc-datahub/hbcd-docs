import os
import sys
import yaml

sys.path.insert(0, os.path.dirname(__file__))

from macros import (
    csv_table,
    readme_info
)

def define_env(env):
    # Global paths
    data_path = os.path.join(
        env.project_dir,
        "docs",
        "data",
        "instruments.yml",
    )

    with open(data_path) as f:
        instruments = yaml.safe_load(f)

    env.variables["instruments"] = instruments

    # Let each module register its own macros
    readme_info.define_env(env)
    csv_table.define_env(env)