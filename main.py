import os
import yaml
import sys

sys.path.insert(0, os.path.dirname(__file__))

from macros.instrument_tables import (
    build_all_instruments_table,
    build_domain_table,
)

from macros.readme_tables import build_readme

from macros.data_warnings import build_data_warning

from macros.scoring_tables import (
    build_scoring_table,
)

from macros.banner_headers import (
    warning_banner,
    alert_banner,
    issues_banner,
    scoring_banner, 
    mods_banner
)

def define_env(env):

    data_path = os.path.join(
        env.project_dir,
        "docs",
        "data",
        "instruments.yml"
    )

    with open(data_path) as f:
        instruments = yaml.safe_load(f)

    env.variables["instruments"] = instruments

    @env.macro
    def all_instruments_table(battery=None):
        return build_all_instruments_table(
            instruments,
            battery=battery
        )

    @env.macro
    def domain_table(domain, battery=None):
        return build_domain_table(
            instruments,
            domain,
            battery=battery
        )

    @env.macro
    def readme(inst):
        return build_readme(inst)
    
    @env.macro
    def data_warning(inst):
        return build_data_warning(inst)

    @env.macro
    def issues_banner_macro():
        return issues_banner()

    @env.macro
    def warning_banner_macro():
        return warning_banner()

    @env.macro
    def alert_banner_macro():
        return alert_banner()

    @env.macro
    def scoring_banner_macro():
        return scoring_banner()
    
    @env.macro
    def mods_banner_macro():
        return mods_banner()




