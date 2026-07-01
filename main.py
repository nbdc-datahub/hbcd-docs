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
from macros.data_warning_multi import build_data_warning_multi
from macros.alert_warnings import build_alert_warning
from macros.hbcd_mods import build_hbcd_mods
from macros.scoring import build_scoring

from macros.scoring_tables import (
    build_scoring_table,
)

from macros.banner_headers import (
    ref_banner,
    issues_banner,
    warning_banner,
    alert_banner,
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
    def data_warning_multi(instruments, instrument_ids):
        return build_data_warning_multi(instruments, instrument_ids)
    
    @env.macro
    def alert_warning(inst):
        return build_alert_warning(inst)
    
    @env.macro
    def scoring(inst):
        return build_scoring(inst)
    
    @env.macro
    def hbcd_mods(inst):
        return build_hbcd_mods(inst)

    @env.macro
    def issues_banner_macro():
        return issues_banner()
    @env.macro
    def ref_banner_macro():
        return ref_banner()
    
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




