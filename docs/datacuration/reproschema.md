# ReproSchema
## What is ReproSchema?
Ensuring consistent research data collection is critical in large-scale, multi-site studies like HBCD. However, managing questionnaire structure, tracking changes, and maintaining version control across time points can be challenging.

**ReproSchema** is a framework designed to address these challenges by providing a **structured, standardized, and version-controlled system for managing research questionnaires**. It is not a standalone survey tool like Qualtrics or REDCap. Instead, it serves as a modular framework that integrates with data collection platforms, helping ensure consistency, traceability, and reproducibility in longitudinal research. ReproSchema functions as both a **schema** and **software platform**:

**As a schema**: ReproSchema defines a standardized structure for organizing questionnaires:

 - Questionnaires follow a consistent format across studies and time points.
 - Questions, response options, and skip logic are explicitly defined and linked to metadata.
 - Version history is preserved to track changes over time.

**As a platform**: ReproSchema also provides tools to manage questionnaire versions and changes:

 - Store and version questionnaires to maintain consistency across sites.
 - Track changes such as wording updates, added or removed questions, and modified response options.
 - Access and compare questionnaire versions used at different time points.

<div id="rs-example" class="table-banner" onclick="toggleCollapse(this)">
   <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Example: Evolution of a Sleep Question Across Data Releases</span>
  <a class="anchor-link" href="#rs-example" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The example below illustrates how a question and its response options may change across data releases.</p>
<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Release</th>
<th>Item Definition</th>
</tr>
</thead>
<tbody>
<tr>
  <td>1.0</td>
  <td><strong>Question</strong>: "How many hours do you sleep on a typical night?"<br>
  <strong>Responses</strong>: Free-text numeric entry</td>
</tr>
<tr>
  <td>2.0</td>
  <td><strong>Question</strong>: "On average, how many hours of sleep do you get per night?"<br>
  <strong>Responses</strong>: Dropdown menu (<i>Less than 5, 5-6, 7-8, or More than 8 hours</i>)</td>
</tr>
<tr>
  <td>3.0</td>
  <td><strong>Question</strong>: "On average, how many hours of sleep do you get in a 24-hour period, including naps?"<br>
  <strong>Responses</strong>: Same as Release 2.0.</td>
</tr>
</tbody>
</table>
<p><b>Implications for Analysis:</b></p>
<ul>
  <li><strong>Data consistency</strong>: Moving from free-text to predefined categories (1.0 → 2.0) standardizes responses and reduces variability, but removes fine-grained detail.</li>
  <li><strong>Comparability across releases</strong>: Adding naps to the question (2.0 → 3.0) changes the construct being measured and may affect cross-release trend analyses.</li>
  <li><strong>Data harmonization</strong>: ReproSchema versioning records these changes to support consistent longitudinal studies.</li>
</ul>
</div>

## ReproSchema Workflow 

The ReproSchema workflow for standardizing survey data collection consists of **six key components**:

<img src="../images/reproschema-fig1.jpg" width="100%" height="auto" alt="ReproSchema Figure 1" class="center">

<table class="table-no-vertical-lines">
<tbody>
<tr>
  <td style="word-wrap: break-word; white-space: normal;"><b>1. Import questionnaires (<i>A</i>)</b><br>
  ReproSchema supports multiple input formats, including questionnaires in PDF or DOC format, existing assessments from the ReproSchema library, and REDCap CSV exports. Questionnaires can be converted into ReproSchema format using large language models (e.g., Claude 3.7 Sonnet) (from PDF/DOC) or automated tools such as <code>redcap2reproschema</code>.</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;"><b>2. Create and publish protocols (<i>B</i>)</b><br>
  The <code>reproschema-protocol-cookiecutter</code> tool provides a structured workflow for creating and publishing protocols on GitHub, ensuring organized metadata and version control. This tool enables schema validation and user interface (UI) serving.</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;"><b>3. Store protocols with version control (<i>C</i>)</b><br>
  ReproSchema protocols are stored in <b>GitHub repositories</b>, where version-controlled URIs provide persistent access to protocols, activities, and individual assessment items. This structure supports reproducibility and provenance tracking.</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;"><b>4. Deploy surveys through the web interface (<i>D</i>)</b><br>
The <b>ReproSchema-UI</b> provides a browser-based interface for interactive survey administration, allowing researchers to collect structured data while maintaining schema integrity. </td></tr>
<tr><td style="word-wrap: break-word; white-space: normal;"><b>5. Record structured responses (<i>E</i>)</b><br>
Survey responses are stored in <b>JSON-LD format</b>, with embedded URIs linking each response to the corresponding protocol, activity, and item in the ReproSchema library. This structure supports provenance, traceability, and semantic interoperability.</td></tr>
<tr><td style="word-wrap: break-word; white-space: normal;"><b>6. Export data to standardized formats (<i>F</i>)</b><br>
The <code>reproschema-py</code> toolkit allows responses and protocols to be converted into multiple standardized formats, including <b>NIMH Common Data Elements (CDE)</b> (<code>reproschema2cde</code>), <b>Brain Imaging Data Structure (BIDS)</b> (<code>reproschema2bids</code>), and REDCap CSV (<code>output2redcap</code>).</td></tr>
</tbody>
</table>

## Version Management
In longitudinal studies like HBCD, where data are collected over many years, tracking changes to data collection instruments is essential. ReproSchema maintains a detailed version history so researchers can understand how questionnaires evolve over time. This version tracking helps researchers:

 - **Maintain data consistency** across study waves by documenting all modifications.
 - **Interpret data more reliably** by providing context for changes in wording, structure, or response options.
 - **Support transparent reporting** of methods, improving reproducibility.

#### Types of Changes Tracked

 - **Typographical error corrections**
 - **Response option updates** (to account for differences across versions in analyses)
 - **Question order changes** (which may influence how participants interpret and answer questions)
 - **Question addition or removal** and other structural changes, supporting accurate longitudinal analysis and data comparability

## How ReproSchema Organizes Questionnaires

ReproSchema organizes research questionnaires into a hierarchical structure that supports **versioning, change tracking, and consistent data collection over time.** Questionnaires are organized across the following levels:

- <span style="color: #3a82fe;"><b>Protocol</b></span>: The Protocol represents the **full set of instruments used within a study**. The right panel in the figure below illustrates how Activities within a protocol are organized in the user interface.

- <span style="color: red;"><b>Activity</b></span>: An Activity corresponds to a **single questionnaire or instrument** (e.g., PHQ-9 depression scale).

- <span style="color: #12ba15;">Items</span>: Items are **individual questions** within an Activity. The available answer choices are <span style="color: #9010f7;">ResponseOptions</span>. When a participant selects an answer, that selection is recorded as a <span style="color: orange;">Response</span>. Item tracking includes **question text** (the exact wording presented to participants), **response options** (available answer choices), and **skip logic** (rules that determine which questions appear next based on responses).

<img src="../images/reproschema-fig2.jpg" alt="ReproSchema hierarchical structure">

## Resources
- [https://www.repronim.org/reproschema](https://www.repronim.org/reproschema/)
- [HBCD-ReproSchema](https://github.com/ReproNim/HBCD-ReproSchema) GitHub repository

## References
<div class="references">
	<p>Chen, Y., Jarecka, D., Abraham, S. A., Gau, R., Ng, E., Low, D. M., Bevers, I., Johnson, A., Keshavan, A., Klein, A., Clucas, J., Rosli, Z., Hodge, S. M., Linkersdörfer, J., Bartsch, H., Das, S., Fair, D., Kennedy, D., & Ghosh, S. S. (2025). Standardizing survey data collection to enhance reproducibility: Development and comparative evaluation of the ReproSchema ecosystem. <i>Journal of Medical Internet Research</i>, 27, e63343. <a href="https://doi.org/10.2196/63343">https://doi.org/10.2196/63343</a>
</div>


 
