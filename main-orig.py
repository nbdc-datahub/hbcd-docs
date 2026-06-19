import yaml
import os
import textwrap

def define_env(env):

    # Path to YAML file & make available in templates
    data_path = os.path.join(env.project_dir, "docs", "data", "instruments.yml")

    with open(data_path, "r") as f:
        instruments = yaml.safe_load(f)

    env.variables["instruments"] = instruments

    # CHECK IF VALUE IS PRESENT (not empty)
    def is_present(val):
        return val is not None and str(val).strip() != ""

    # Don't render rows without values and define css classes where needed (i.e. for visits list)
    def row(label, value, code=False, value_class=None):
        if not is_present(value):
            return ""
        if code:
            value = f"<code>{value}</code>"
        class_attr = f' class="{value_class}"' if value_class else ""
        return f"<tr><td>{label}</td><td{class_attr}>{value}</td></tr>"

    
## WARNING BANNER - INSTRUMENT-SPECIFIC
    @env.macro
    def warning_banner_FULL(inst):
        return f"""
<div id="warn" class="banner data-warning" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-exclamation-triangle"></i>
</span>
<span class="text-with-link">
    <span class="text">Data Warning</span>
    <a class="anchor-link" href="#data-warning" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning1")}
</div>
<p>
  {inst.get("warning1_text")}
</p>
</div>

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning2")}
</div>
<p>
  {inst.get("warning2_text")}
</p>
</div>

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning3")}
</div>
<p>
  {inst.get("warning3_text")}
</p>
</div>

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning4")}
</div>
<p>
  {inst.get("warning4_text")}
</p>
</div>

</div>
"""
    

   