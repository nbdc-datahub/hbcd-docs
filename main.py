import os
import sys
import yaml

sys.path.insert(0, os.path.dirname(__file__))

from macros import (
    csv_table,
    readme_info
)

def define_env(env):
    data_dir = os.path.join(env.project_dir, "data")

    with open(os.path.join(data_dir, "instruments.yml")) as f:
        env.variables["instruments"] = yaml.safe_load(f)

    with open(os.path.join(data_dir, "release_definitions.yml")) as f:
        release_defs = yaml.safe_load(f)

    # Option A: top-level, so {{ release }} and {{ hbcd_processing_site }} work directly
    env.variables.update(release_defs)

    # Option B: namespaced, so {{ release_defs.release }} (safer against name collisions)
    # env.variables["release_defs"] = release

    readme_info.define_env(env)
    csv_table.define_env(env)