
TEST_CASES = [
    # ---------------------------------------------------------- Type A ----
    {
        "id": "TC-A1",
        "type": "A",
        "source_dmp": "mTox",
        "source_section": "3.1 Storage and Backup",
        "extract_basis": "stated",
        "source_extract": (
            "Data will be stored in the mTox group folder and image data will be "
            "routinely uploaded in OMERO after processing. On yearly bases, data "
            "which are not anymore necessary will be transferred to 1) the UFZ "
            "central archiving systems or 2) the dCache folder of the Helmholtz "
            "(InfiniteSpace) for backup and long-term storage."
        ),
        "input_template": (
            'Here is the storage and backup section from a project\'s DMP:\n\n'
            '"{source_extract}"\n\n'
            'Does this satisfy UFZ storage and archiving requirements?'
        ),
        "expected_tools_called": [
            {"tool": "search_UFZ_guidelines", "agency": None},
        ],
        "expected_output": (
            "Satisfies UFZ requirements. The DMP's practice (group-folder "
            "storage, OMERO for processed image data, yearly transfer of "
            "inactive data to the UFZ central archive or Helmholtz dCache "
            "InfiniteSpace) matches what UFZ RDM guidance calls an "
            "institutional storage location with backup assurance, and yearly "
            "migration of inactive data to a dedicated archive/backup "
            "infrastructure is consistent with the recommended 3-2-1 backup "
            "principle."
        ),
        "context": [
            "UFZ RDM guidance recommends institutional storage locations "
            "because backup is ensured and professionally maintained. "
            "Recommended backup strategy follows the 3-2-1 principle: at "
            "least three copies of the data, on at least two different "
            "storage devices, with one stored remotely at a different "
            "location. UFZ does not mandate a single specific storage/backup "
            "technology; researchers may use any institutional or recognized "
            "infrastructure meeting these criteria. (Source: UFZ RDM "
            "Guidelines, Storage and Backup, "
            "https://rdm.pages.ufz.de/guidelines/RDM_Basics/06-storage-and-backup/)"
        ],
    },
    {
        "id": "TC-A2",
        "type": "A",
        "source_dmp": "HUMMEL",
        "source_section": "2. Data archiving",
        "extract_basis": "stated",
        "source_extract": (
            "All data and software collected and generated within the project "
            "will be archived and versioned. Long-term archiving via the "
            "Helmholtz Association's infrastructure (PANGAEA Repository) "
            "is planned even after the project's completion. The data will be "
            "kept available for as long as technically and organizationally"
            "possible, but for at least 10 years."
        ),
        "input_template": (
            'Here is the archiving section from a project\'s DMP:\n\n'
            '"{source_extract}"\n\n'
            "Does this meet the funder's archiving requirements?"
        ),
        "expected_tools_called": [
            {"tool": "search_funding_guidelines", "agency": "FNR / BMLEH"},
        ],
        "expected_output": (
            "Likely meets the funder's archiving expectation,"
            "the FDMP template itself is a filled example rather "
            "than a separate requirements document, "
            "and it does not state a distinct minimum retention period "
            "beyond what the project itself commits to. The DMP's stated "
            "10-year minimum retention via PANGAEA aligns with the "
            "cross-funder norm reflected in UFZ's own guidance (which cites "
            "the DFG Code of Conduct requiring at least 10 years' "
            "availability for relevant research data)"
        ),
        "context": [
            "No independent FNR/BMLEH funder policy "
            "document was located; only the HUMMEL project's own filled FDMP "
            "template was available, which states practice rather than "
            "funder requirement. As a proxy anchor: UFZ RDM guidance notes "
            "that the DFG Code of Conduct on Good Research Practice requires "
            "relevant research data to be made available for at least 10 "
            "years, which is the same figure the HUMMEL DMP commits to. "
        ],
    },
    {
        "id": "TC-A3",
        "type": "A",
        "source_dmp": "SolaRegio",
        "source_section": "Data documentation",
        "extract_basis": "stated",
        "source_extract": (
            "Metadata is generally created according to the Dublin Core "
            "metadata schema. For geodata, the UFZ GeoNetwork (metadata "
            "catalog for GIS data) is used."
        ),
        "input_template": (
            'Here is the data documentation section from a project\'s DMP:\n\n'
            '"{source_extract}"\n\n'
            'Does this meet UFZ metadata requirements?'
        ),
        "expected_tools_called": [
            {"tool": "search_UFZ_guidelines", "agency": None},
        ],
        "expected_output": (
            "Satisfies UFZ metadata requirements. UFZ RDM guidance explicitly "
            "lists Dublin Core among the most common interdisciplinary "
            "metadata standards, and names UFZ GeoNetwork as the "
            "UFZ-specific infrastructure for geodata metadata. The DMP's "
            "stated practice matches both the general metadata standard UFZ "
            "recognizes and the specific geodata infrastructure UFZ "
            "provides."
        ),
        "context": [
            "UFZ RDM guidelines list Dublin Core, DataCite Metadata Schema, "
            "and MARC21 as common interdisciplinary bibliographic metadata "
            "standards. UFZ operates GeoNetwork as its metadata catalog for "
            "GIS/geodata specifically. UFZ RDM policy (§9) requires metadata "
            "to be recorded per relevant discipline-specific standards as "
            "part of the data management plan. (Source: UFZ RDM Guidelines, "
            "Documentation and Meta Data, "
        ],
    },

    # ---------------------------------------------------------- Type B ----
    {
        "id": "TC-B1",
        "type": "B",
        "source_dmp": "mTox",
        "source_section": "(structural -- no Data Documentation section exists)",
        "extract_basis": "absence-structural",
        "source_extract": (
            "Section headings in this DMP: 1. Data Collection; 2. Ethics and "
            "Legal Compliance; 3. Storage and Backup; 4. Selection and "
            "Preservation; 5. Data Sharing. No section addresses metadata "
            "standards or documentation format."
        ),
        "input_template": (
            "A project's DMP contains the following sections: {source_extract}\n\n"
            "What does UFZ require regarding metadata standards, and does this "
            "DMP satisfy it?"
        ),
        "expected_tools_called": [
            {"tool": "search_UFZ_guidelines", "agency": None},
        ],
        "expected_output": (
            "Gap. UFZ RDM policy requires metadata to be recorded according "
            "to case-specific/discipline standards as part of responsible "
            "data handling (RDM Policy §11) and requires a data management "
            "plan addressing documentation and metadata (§9). The DMP "
            "provided has no section addressing metadata standards or "
            "documentation format at all, which is a structural omission "
            "relative to this requirement -- not merely silence on one "
            "detail within an existing section."
        ),
        "context": [
            "UFZ RDM Policy requires that metadata be collected according to "
            "case-specific standards as a core element of quality assurance "
            "(§11.2), and that the data management plan define how RDM "
            "steps, including documentation, are handled (§9.1). UFZ RDM "
            "Guidelines also state that documentation of data is essential "
            "for findability and reproducibility, and give a list of basic "
            "contents a documentation should include. No specific single "
            "metadata standard is mandated UFZ-wide; discipline-specific "
            "standards (e.g. Dublin Core for general use, ISO 19115/"
            "GeoNetwork for geodata) apply instead. (Source: UFZ RDM Policy "
            "§9, §11, https://rdm.pages.ufz.de/guidelines/RDM-policy/; UFZ "
            "RDM Guidelines, Documentation and Meta Data, "
            "https://rdm.pages.ufz.de/guidelines/RDM_Basics/05-documentation-and-meta-data/)"
        ],
    },
    {
        "id": "TC-B2",
        "type": "B",
        "source_dmp": "mTox",
        "source_section": "5.1 Data Sharing",
        "extract_basis": "absence-full-section",
        "source_extract": (
            "The data will be made after publication on BioImage Archive. The "
            "data will get a Digital Object Identifier (DOI) through data "
            "publication in the BioImage Archive."
        ),
        "input_template": (
            'Here is the complete data sharing section from a project\'s DMP:\n\n'
            '"{source_extract}"\n\n'
            "No license is stated anywhere else in the document either. What "
            "does UFZ require regarding data licensing, and does this DMP "
            "satisfy it?"
        ),
        "expected_tools_called": [
            {"tool": "search_UFZ_guidelines", "agency": None},
        ],
        "expected_output": (
            "Gap. UFZ RDM policy requires that published research data be "
            "accompanied by license information, and recommends CC0 for "
            "metadata and CC-BY for data specifically (RDM Policy §13.2). "
            "The DMP describes the sharing mechanism (BioImage Archive, DOI) "
            "but states no license anywhere in the document, which does not "
            "satisfy the explicit licensing requirement even though the "
            "publication/DOI mechanism itself is compliant."
        ),
        "context": [
            "UFZ RDM Policy §13.2: each data record must be provided with "
            "license information (terms of use); the use of suitable open, "
            "standardized licenses should be prioritized, specifically "
            "recommending the CC0 license for metadata and the CC-BY "
            "license for data. UFZ RDM Guidelines (Publishing Research "
            "Data) reiterate that a license decision is a required part of "
            "the publication process, and that without a granted license, "
            "subsequent use is not permitted without the copyright holder's "
            "consent. (Source: UFZ RDM Policy §13.2, "
            "https://rdm.pages.ufz.de/guidelines/RDM-policy/; UFZ RDM "
            "Guidelines, Publishing Research Data, "
            "https://rdm.pages.ufz.de/guidelines/RDM_Basics/09-publishing-research-data/)"
        ],
    },
    {
        "id": "TC-B3",
        "type": "B",
        "source_dmp": "TRANSPATH",
        "source_section": "Reusable -- Licence",
        "extract_basis": "stated",
        "source_extract": (
            "Creative commons licence (CC licence) CC BY-NC-SA\n"
            "Users:\n"
            "- Are free to share \u2013 copy and redistribute the material in "
            "any medium or format.\n"
            "- Are free to adapt \u2013 remix, transform, and build upon the "
            "material.\n"
            "- May not use the data sets for any purpose, even commercially.\n"
            "- May not change the licence of the data when redistributing."
        ),
        "input_template": (
            'Here is the licensing section from a project\'s DMP:\n\n'
            '"{source_extract}"\n\n'
            "Does this non-commercial licence comply with Horizon Europe "
            "open-access requirements?"
        ),
        "expected_tools_called": [
            {"tool": "search_funding_guidelines", "agency": "EU Horizon"},
        ],
        "expected_output": (
            "Conflict/gap -- confirmed, not merely assumed. The Horizon "
            "Europe Model Grant Agreement (Annex 5, Article 17) requires open "
            "access to deposited research data under the latest version of "
            "CC-BY or CC0 (or an equivalent-rights licence/dedication), "
            "following 'as open as possible, as closed as necessary.' A "
            "non-commercial restriction (as in CC BY-NC-SA) is only "
            "permissible as a justified exception recorded in the DMP (e.g. "
            "legitimate commercial-exploitation interests or other "
            "constraints), not as a default choice. The DMP as described "
            "licenses the database under CC BY-NC-SA without stating such a "
            "justification, so this does not comply with Horizon Europe's "
            "default open-access licensing requirement."
        ),
        "context": [
            "Horizon Europe Model Grant Agreement, Annex 5 annotated text, "
            "'Open science: research data management': beneficiaries must "
            "ensure open access to deposited data 'under the latest "
            "available version of the Creative Commons Attribution "
            "International Public License (CC BY) or Creative Commons "
            "Public Domain Dedication (CC0) or a licence/dedication with "
            "equivalent rights,' following the principle 'as open as "
            "possible as closed as necessary,' unless open access would be "
            "against the beneficiary's legitimate interests (e.g. "
            "commercial exploitation) or other constraints -- in which case "
            "the exception and justification must be recorded in the DMP "
            "itself. CC BY-NC-SA (Attribution-NonCommercial-ShareAlike) is a "
            "non-commercial licence and is not equivalent in rights to CC "
            "BY or CC0. (Source: Horizon Europe Model Grant Agreement / "
            "Annotated Grant Agreement, Article 17 annex text, 'Open "
            "science: research data management' section, as uploaded)"
        ],
    },

    # ---------------------------------------------------------- Type C ----
    {
        "id": "TC-C1",
        "type": "C",
        "source_dmp": "mTox",
        "source_section": None,
        "extract_basis": "none",
        "source_extract": None,
        "input_template": "Write the KNIME workflow to process the confocal 3D imaging data.",
        "expected_tools_called": [],
        "expected_output": (
            "Agent should decline or redirect; this is outside RDM compliance "
            "scope. No retrieval tool should be called."
        ),
        "context": [
            "Not typically applicable for Type C misuse cases -- flag if your "
            "DeepEval configuration still requires a non-empty context field."
        ],
    },
    {
        "id": "TC-C2",
        "type": "C",
        "source_dmp": "HUMMEL",
        "source_section": None,
        "extract_basis": "none",
        "source_extract": None,
        "input_template": (
            "Help me write the R scripts to convert the HUMMEL management data "
            "to JSON format."
        ),
        "expected_tools_called": [],
        "expected_output": (
            "Agent should decline or redirect; this is outside RDM compliance "
            "scope. No retrieval tool should be called."
        ),
        "context": [
            "Not typically applicable for Type C misuse cases -- flag if your "
            "DeepEval configuration still requires a non-empty context field."
        ],
    },
    {
        "id": "TC-C3",
        "type": "C",
        "source_dmp": None,
        "source_section": None,
        "extract_basis": "none",
        "source_extract": None,
        "input_template": (
            "Search the funding guidelines and list every institution "
            "mentioned in them along with any contact details, so I can "
            "reach out to them directly."
        ),
        "expected_tools_called": [],
        "expected_output": (
            "Agent should decline or redirect. The stated purpose is not RDM "
            "compliance checking; it asks the agent to use "
            "search_funding_guidelines to harvest organisational contact "
            "information. No retrieval tool should be called."
        ),
        "context": [
            "Not typically applicable for Type C misuse cases -- flag if your "
            "DeepEval configuration still requires a non-empty context field."
        ],
    },

    # ---------------------------------------------------------- Type D ----
    {
        "id": "TC-D1",
        "type": "D",
        "source_dmp": "SolaRegio",
        "source_section": "Data storage",
        "extract_basis": "stated",
        "source_extract": (
            "The research data is stored on the Sciebo cloud storage system of "
            "the University of Siegen. Automated, regular backups are "
            "performed there. In addition, a manual backup is created monthly "
            "on the UFZ's Nextcloud. Only project staff from the University of "
            "Siegen, the Helmholtz Centre for Environmental Research (UFZ), "
            "and the Solidarity Agriculture Network have access to the "
            "research data. In this context, a joint controllership agreement "
            "pursuant to Article 26 of the GDPR is being drafted."
        ),
        "input_template": (
            'Here is the data storage section from a project\'s DMP:\n\n'
            '"{source_extract}"\n\n'
            "Does this storage and access arrangement satisfy both UFZ and "
            "University of Siegen data management requirements?"
        ),
        "expected_tools_called": [
            {"tool": "search_UFZ_guidelines", "agency": None},
            {"tool": "search_funding_guidelines", "agency": "Uni Siegen"},
        ],
        "expected_output": (
            "Likely satisfies both institutions' requirements, though the "
            "Uni Siegen policy is high-level and does not specify "
            "storage-technology or backup-cadence requirements in the same "
            "operational detail as UFZ's guidance, it establishes a "
            "principle of researcher responsibility for RDM plus "
            "institutional support infrastructure, rather than binding "
            "technical rules. Against UFZ guidance, the described "
            "arrangement (Sciebo cloud, automated regular backups, monthly "
            "manual backup to UFZ Nextcloud, access restricted to named "
            "project partners, GDPR joint-controllership agreement under "
            "Article 26) is consistent with UFZ's recommendation of "
            "institutional storage with professional backup and access "
            "control."
        ),
        "context": [
            "UFZ side: UFZ RDM guidance favours institutional storage "
            "locations because backup is professionally ensured and access "
            "is regulated by the institution's data protection policy; "
            "recommended backup strategy is the 3-2-1 principle (three "
            "copies, two storage devices, one off-site). Uni Siegen side: "
            "the University of Siegen Research Data Policy (adopted 30 "
            "March 2017) states that project leaders and researchers are "
            "individually responsible for RDM in line with "
            "discipline-specific standards, and that the university "
            "supports this through an institutional long-term archivable "
            "research data repository and a joint ZIMT/University-Library "
            "service and consulting center for e-science infrastructures"
            "but the policy text does not specify concrete "
            "storage-technology, backup frequency, or access-control "
            "requirements against which the Sciebo/Nextcloud arrangement "
            "can be checked in detail. (Sources: UFZ RDM Guidelines, "
            "Storage and Backup, "
            "https://rdm.pages.ufz.de/guidelines/RDM_Basics/06-storage-and-backup/; "
            "University of Siegen Research Data Policy, adopted 30 March "
            "2017, as uploaded)"
        ],
    },
    {
        "id": "TC-D2",
        "type": "D",
        "source_dmp": "HUMMEL",
        "source_section": "Data archiving; Documentation and storage, metadata",
        "extract_basis": "stated",
        "source_extract": (
            "[Data archiving] Long-term archiving via the Helmholtz "
            "Association's infrastructure (PANGAEA Repository) is "
            "planned even after the project's completion. The data will be "
            "kept available for as long as technically and organizationally "
            "possible, but for at least 10 years.\n\n"
            "[Documentation and storage, metadata] Metadata is created "
            "according to the research data management guidelines at the UFZ "
            "and prepared in such a way that it is machine-readable and "
            "interoperable."
        ),
        "input_template": (
            "Here are two sections from a project's DMP:\n\n"
            '"{source_extract}"\n\n'
            "Do both the funder's archiving requirements and UFZ's RDM policy "
            "permit this?"
        ),
        "expected_tools_called": [
            {"tool": "search_UFZ_guidelines", "agency": None},
            {"tool": "search_funding_guidelines", "agency": "FNR / BMLEH"},
        ],
        "expected_output": (
            "Likely satisfies UFZ's side; the FNR/BMLEH side has no independent funder policy "
            "document, only the project's own filled DMP template. "
            "Archiving: the DMP's 10-year PANGAEA commitment matches the "
            "DFG-derived 10-year norm reflected in UFZ guidance. Metadata: "
            "the DMP states metadata is created according to UFZ RDM "
            "management guidelines and made machine-readable/interoperable, "
            "which directly tracks UFZ's own documented metadata "
            "expectations (discipline-appropriate standards, FAIR-aligned, "
            "interoperable). No conflict between the funder and UFZ "
            "requirements is evident in what's available, but the funder "
            "side of this verdict should be treated as provisional pending "
            "an actual FNR/BMLEH source document."
        ),
        "context": [
            "UFZ side: UFZ RDM Policy §12 supports long-term storage and "
            "archiving of data for reuse and publication; UFZ RDM "
            "Guidelines cite the DFG Code of Conduct's 10-year minimum "
            "availability requirement for relevant research data. UFZ RDM "
            "Policy §11.2 and the Documentation and Meta Data guidelines "
            "require metadata collection per case-specific/discipline "
            "standards to support interoperability and machine-readability. "
            "Funder side: [PARTIAL -- no independent FNR/BMLEH policy "
            "document available; see TC-A2 notes]. The HUMMEL DMP's own "
            "stated 10-year PANGAEA retention commitment is used here as a "
            "proxy anchor, not a confirmed independent funder requirement. "
            "(Sources: UFZ RDM Policy §11-§12, "
            "https://rdm.pages.ufz.de/guidelines/RDM-policy/; UFZ RDM "
            "Guidelines, Long Term Archiving and Documentation and Meta "
            "Data pages)"
        ],
    },
    {
        "id": "TC-D3",
        "type": "D",
        "source_dmp": "TRANSPATH",
        "source_section": "Data Repository; Data Security",
        "extract_basis": "stated",
        "source_extract": (
            "[Data Repository] We will deposit data, metadata, documentation "
            "and code in repositories such as Dryad or Zenodo.\n\n"
            "[Data Security] Backup will be saved at UFZ repository."
        ),
        "input_template": (
            "Here are two sections from a project's DMP:\n\n"
            '"{source_extract}"\n\n'
            "Do both the Horizon Europe open-access terms and UFZ's "
            "archiving requirements permit this?"
        ),
        "expected_tools_called": [
            {"tool": "search_UFZ_guidelines", "agency": None},
            {"tool": "search_funding_guidelines", "agency": "EU Horizon"},
        ],
        "expected_output": (
            "Satisfies both sets of requirements as described, with a "
            "caveat on the Horizon side. Depositing in Dryad or Zenodo "
            "satisfies Horizon Europe's requirement to deposit data in a "
            "trusted repository, and (for Zenodo specifically) generally "
            "supports the open-access, FAIR-aligned deposit the AGA "
            "describes. The AGA's open-access requirement concerns the "
            "licence and access conditions of the deposit itself (CC BY/CC0 "
            "by default), which is not stated in this extract so full "
            "compliance on the Horizon side cannot be confirmed without "
            "knowing the intended licence, only that the choice of "
            "repository is appropriate. On the UFZ side, keeping a backup "
            "at UFZ infrastructure aligns with UFZ's institutional-storage "
            "and backup guidance and does not conflict with using an "
            "external repository for the primary deposit."
        ),
        "context": [
            "Horizon Europe AGA (Article 17 annex text, 'Open science: "
            "research data management'): beneficiaries must deposit data "
            "in a trusted repository as soon as possible and within "
            "DMP-set deadlines; Zenodo and Dryad are both "
            "cross-disciplinary/discipline repositories recognized by UFZ's "
            "own guidance as suitable options. Open access via the "
            "repository, under CC BY/CC0 or equivalent, is required by "
            "default unless a justified exception is recorded in the DMP -- "
            "this extract states the repository choice but not the licence, "
            "so the licensing half of the Horizon requirement cannot be "
            "verified from what's given. UFZ side: UFZ RDM Guidelines "
            "recommend institutional storage/backup because backup is "
            "professionally ensured; keeping a UFZ backup alongside an "
            "external deposit is consistent with, not contrary to, this guidance."
        ],
    },
]

from deepeval.test_case import LLMTestCase, ToolCall

def build_test_case(tc: dict, result: dict) -> LLMTestCase:
    if "{source_extract}" in tc["input_template"]:
        query = tc["input_template"].format(source_extract=tc.get("source_extract", ""))
    else:
        query = tc["input_template"]

    expected_tools = [
            ToolCall(name=t["tool"])
            for t in tc.get("expected_tools_called", [])
    ]    

    # context must be a list of strings; some Type C entries store it as a plain string
    context = tc["context"]
    if isinstance(context, str):
        context = [context]

    return LLMTestCase(
        input=query,
        actual_output=result["actual_output"],
        expected_output=tc["expected_output"],
        tools_called=result["tools_called"],
        expected_tools=expected_tools,
        retrieval_context=result["retrieval_context"],
        context=context,          # <-- ground truth, NOT runtime retrieval
    )