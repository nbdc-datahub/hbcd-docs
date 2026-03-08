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
    <span class="text">Practical Example: Evolution of a Sleep Quality Question Across Data Releases</span>
    <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
  <ul>
  <b>Release 1.0 (Initial Version):</b>
    <li><strong>Question:</strong> "How many hours do you sleep on a typical night?"</li>
    <li><strong>Response Options:</strong> Free-text input (participants enter a number).</li>
  </ul>
  <ul>
  <b>Release 2.0 (Revised Version):</b>
    <li><strong>Question:</strong> "On average, how many hours of sleep do you get per night?"</li>
    <li><strong>Response Options:</strong> Dropdown menu:
      <ul>
        <li>Less than 5 hours</li>
        <li>5-6 hours</li>
        <li>7-8 hours</li>
        <li>More than 8 hours</li>
      </ul>
    </li>
  </ul>
  <ul>
  <b>Release 3.0 (Further Revision):</b>
    <li><strong>Question:</strong> "On average, how many hours of sleep do you get in a 24-hour period, including naps?"</li>
    <li><strong>Response Options:</strong> Same as Release 2.0.</li>
  </ul>
  <hr>
  <ul>
  <b>Implications for Data Analysis:</b>
    <li><strong>Data Consistency:</strong> The shift from free-text to predefined categories (Release 1.0 → 2.0) standardizes responses, reducing variability but limiting detail.</li>
    <li><strong>Comparability:</strong> The addition of naps (Release 2.0 → 3.0) may impact cross-release trend analysis.</li>
    <li><strong>Data Harmonization:</strong> ReproSchema’s version management ensures that each change is documented for consistent longitudinal studies.</li>
  </ul>
</div>

## ReproSchema Workflow 
The ReproSchema workflow for standardizing survey data collection consists of **six key components**, illustrated below:

<figure>
  <img src="../images/reproschema-fig1.jpg" alt="ReproSchema Figure 1">
  <figcaption style="font-size: 0.9em;"><b>Figure 1. ReproSchema workflow overview.</b> <b>(A)</b> ReproSchema supports multiple input formats, including questionnaires in PDF or DOC format (which can be converted to ReproSchema format using large language models (LLMs) such as Claude 3.7 Sonnet), existing assessments from the ReproSchema library, and REDCap CSV exports (which can be automatically converted using <code>redcap2reproschema</code>). <b>(B)</b> The <code>reproschema-protocol-cookiecutter</code> tool provides a structured, stepwise process for researchers to create and publish a protocol on GitHub, ensuring organized metadata and version control. This tool enables schema validation and user interface (UI) serving. <b>(C)</b> ReproSchema protocols are stored in GitHub repositories, where version-controlled URIs ensure persistent access to protocols, activities, and assessment items, supporting reproducibility and provenance tracking. <b>(D)</b> The ReproSchema-UI provides a browser-based interface for interactive survey deployment, allowing researchers to collect structured data while maintaining schema integrity. <b>(E)</b> Survey responses are stored in JSON-LD format, with embedded URIs linking each protocol, activity, and item to their respective sources in the ReproSchema library. This structure ensures data provenance, traceability, and semantic interoperability. <b>(F)</b> The <code>reproschema-py</code> tools facilitate output conversion into various standardized formats, including National Institute of Mental Health (NIMH) Common Data Elements (<code>reproschema2cde</code>), Brain Imaging Data Structure (BIDS) (<code>reproschema2bids</code>), and REDCap CSV (<code>output2redcap</code>).</figcaption>
</figure>

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

ReproSchema organizes research questionnaires into a hierarchical structure that supports versioning, change tracking, and consistent data collection over time. As illustrated in the figure below, questionnaires are organized across **three levels: Protocol → Activity → Item.**

A **protocol** can contain multiple <span style="color: red;">Activities (assessments)</span>. Each Activity contains <span style="color: #13d016;">Items (questions)</span>, which define <span style="color: #9010f7;">ResponseOptions (answer choices)</span>. When a participant selects an answer, that selection is recorded as a <span style="color: orange;">Response</span>. The right panel illustrates how Activities within a protocol are organized in the user interface.

<img src="../images/reproschema-fig2.jpg" alt="ReproSchema hierarchical structure">

#### Protocol Level
A **protocol** represents the **full set of assessments** used within a study or data release. It defines the overall questionnaire framework and links all associated activities together under a version-controlled structure tied to specific data releases.

#### Activity Level
An **activity** corresponds to a specific **questionnaire or instrument** (e.g., PHQ-9 depression scale or GAD-7 anxiety scale). Activities group related questions and allow changes to assessments, such as additions, removals, or revisions, to be tracked across versions.

#### Item Level
An **item** represents a **single question** within an activity (questionnaire). Tracking items allows researchers to identify when questions change and interpret longitudinal data accurately. Each item includes:

 - Question text: the exact wording presented to participants
 - Response options: the available answer choices
 - Skip logic: rules that determine which questions appear next based on responses

## Resources
- [https://www.repronim.org/reproschema](https://www.repronim.org/reproschema/)
- [HBCD-ReproSchema](https://github.com/ReproNim/HBCD-ReproSchema) GitHub repository

## References
<div class="references">
	<p>Chen, Y., Jarecka, D., Abraham, S. A., Gau, R., Ng, E., Low, D. M., Bevers, I., Johnson, A., Keshavan, A., Klein, A., Clucas, J., Rosli, Z., Hodge, S. M., Linkersdörfer, J., Bartsch, H., Das, S., Fair, D., Kennedy, D., & Ghosh, S. S. (2025). Standardizing survey data collection to enhance reproducibility: Development and comparative evaluation of the ReproSchema ecosystem. <i>Journal of Medical Internet Research</i>, 27, e63343. <a href="https://doi.org/10.2196/63343">https://doi.org/10.2196/63343</a>
</div>


 
