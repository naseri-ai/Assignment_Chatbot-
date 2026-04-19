KNOWLEDGE_BASE = [

# -------------------------
# 1. INTRODUCTION / OVERVIEW
# -------------------------
{
    "intent": "assignment_overview",
    "patterns": [
        "what is assignment 2 about",
        "overview of the assignment",
        "what do we need to do",
        "purpose of assignment",
        "what is this assignment",
        "assignment description",
        "what is required in assignment 2"
    ],
    "answer": (
        """📘 **Assignment Overview**

This assignment requires you to analyse a real-world problem and design a comprehensive information system solution.

You will:
• Identify and describe a problem  
• Propose an information system solution  
• Explain how data is used  
• Conduct a feasibility study  
• Present your work in a structured business report  

This is a **team-based assignment** assessing both technical and communication skills."""
    )
},

# -------------------------
# 2. DEADLINE
# -------------------------
{
    "intent": "deadline",
    "patterns": [
        "when is the assignment due",
        "deadline for assignment",
        "due date",
        "submission deadline",
        "what time is it due",
        "is it due at midnight",
        "when do we submit",
        "assignment due date"
    ],
    "answer": (
        """⏰ **Deadline**

The assignment is due on:

📅 **Friday, May 15, 2026 at 23:59 (Australian time)**

Make sure to submit before the deadline to avoid penalties."""
    )
},

# -------------------------
# 3. SUBMISSION METHOD
# -------------------------
{
    "intent": "submission_method",
    "patterns": [
        "how do we submit",
        "where do we submit",
        "submit assignment",
        "upload assignment",
        "moodle submission",
        "do we email assignment",
        "submission link",
        "how to upload report"
    ],
    "answer": (
        """📤 **Submission Method**

• Submit via **Moodle** using the correct submission link  
• Do NOT email your assignment unless instructed  
• Ensure the correct file is uploaded before the deadline"""
    )
},

# -------------------------
# 4. FILE FORMAT
# -------------------------
{
    "intent": "file_format",
    "patterns": [
        "what format should we submit",
        "word or pdf",
        "file format",
        "can we submit pdf",
        "document format",
        "report format"
    ],
    "answer": (
        """📄 **File Format**

Submit your report as:

• Word document OR  
• PDF  

Ensure it follows a **business report format**."""
    )
},

# -------------------------
# 5. GROUP WORK
# -------------------------
{
    "intent": "group_work",
    "patterns": [
        "is this group work",
        "team assignment",
        "how many people in group",
        "group size",
        "do we work in teams"
    ],
    "answer": (
        """👥 **Group Work**

• This is a **team assignment of 3 students**  
• One member acts as the **team leader**  
• Each member contributes an individual section"""
    )
},

# -------------------------
# 6. GROUP SUBMISSION RULE
# -------------------------
{
    "intent": "group_submission",
    "patterns": [
        "does everyone submit",
        "one submission per group",
        "who submits the assignment",
        "team leader submit",
        "group submission rule",
        "can one person submit for group"
    ],
    "answer": (
        """👥 **Group Submission**

• Only **ONE submission per group**  
• Usually submitted by the **team leader**  
• Make sure all members are included in the document"""
    )
},

# -------------------------
# 7. REPORT LENGTH
# -------------------------
{
    "intent": "report_length",
    "patterns": [
        "how many words",
        "word count",
        "report length",
        "minimum words",
        "maximum words",
        "how long should the report be"
    ],
    "answer": (
        """📝 **Report Length**

• Total: **2500–3000 words**  
• Each student: **~800–1000 words**"""
    )
},

# -------------------------
# 8. INDIVIDUAL CONTRIBUTION
# -------------------------
{
    "intent": "individual_section",
    "patterns": [
        "individual part",
        "what does each student do",
        "individual contribution",
        "who writes what",
        "individual marking",
        "are we marked individually"
    ],
    "answer": (
        """👤 **Individual Contribution**

Each student writes one section:

• Problem identification  
• System solution  
• Data management  
• Feasibility study  

Each section is **marked individually**."""
    )
},

# -------------------------
# 9. PROBLEM IDENTIFICATION
# -------------------------
{
    "intent": "problem_identification",
    "patterns": [
        "what is problem identification",
        "how to identify problem",
        "problem description",
        "what to include in problem section",
        "problem analysis"
    ],
    "answer": (
        """🔍 **Problem Identification**

You must:

• Clearly describe the problem  
• Explain context and impact  
• Use TWO problem-solving approaches  
• Justify with evidence"""
    )
},

# -------------------------
# 10. SYSTEM SOLUTION
# -------------------------
{
    "intent": "system_solution",
    "patterns": [
        "what is system solution",
        "proposed system",
        "what to include in system design",
        "information system solution",
        "design system"
    ],
    "answer": (
        """💡 **System Solution**

Describe your proposed system including:

• System purpose  
• Hardware & software  
• Data  
• Users (stakeholders)  
• Processes  

Your solution should be **feasible and innovative**."""
    )
},

# -------------------------
# 11. DATA MANAGEMENT
# -------------------------
{
    "intent": "data_management",
    "patterns": [
        "data management",
        "data use",
        "how data is used",
        "data storage",
        "database model",
        "data processing"
    ],
    "answer": (
        """🗄️ **Data Management**

Explain:

• Data collection  
• Data storage (e.g., relational DB)  
• Data processing  
• Data security & privacy"""
    )
},

# -------------------------
# 12. FEASIBILITY STUDY
# -------------------------
{
    "intent": "feasibility",
    "patterns": [
        "feasibility study",
        "what is feasibility",
        "technical feasibility",
        "economic feasibility",
        "operational feasibility",
        "time feasibility"
    ],
    "answer": (
        """📊 **Feasibility Study**

Evaluate:

• Technical feasibility  
• Economic feasibility  
• Legal feasibility  
• Operational feasibility  
• Time feasibility"""
    )
},

# -------------------------
# 13. REFERENCING
# -------------------------
{
    "intent": "referencing",
    "patterns": [
        "how to reference",
        "apa format",
        "referencing style",
        "citation style",
        "do we need references"
    ],
    "answer": (
        """📚 **Referencing**

• Use **APA 7th edition**  
• Include all sources used  
• Use Fed Cite tool if needed"""
    )
},

# -------------------------
# 14. MARKING
# -------------------------
{
    "intent": "marking",
    "patterns": [
        "how is it marked",
        "marking criteria",
        "grading",
        "rubric",
        "who marks assignment"
    ],
    "answer": (
        """📊 **Marking**

• Based on rubric criteria  
• Includes individual and team components  
• Marked by coordinator and tutors"""
    )
},

# -------------------------
# 15. FEEDBACK
# -------------------------
{
    "intent": "feedback",
    "patterns": [
        "when do we get feedback",
        "where to see marks",
        "feedback location",
        "how to check grades"
    ],
    "answer": (
        """📥 **Feedback**

• Available on **Moodle / FDL Marks**  
• Includes comments and grades"""
    )
},

# -------------------------
# 16. LATE SUBMISSION
# -------------------------
{
    "intent": "late_policy",
    "patterns": [
        "late submission",
        "penalty",
        "submit late",
        "what happens if late",
        "late assignment penalty"
    ],
    "answer": (
        """⚠️ **Late Submission**

• Penalties apply according to university policy  
• Submit on time to avoid deductions"""
    )
},

# -------------------------
# 17. EXTENSIONS
# -------------------------
{
    "intent": "extension",
    "patterns": [
        "extension",
        "special consideration",
        "request extension",
        "can I get more time"
    ],
    "answer": (
        """📌 **Extensions**

You must apply via **special consideration** with valid reasons."""
    )
},

# -------------------------
# FALLBACK
# -------------------------
{
    "intent": "fallback",
    "patterns": [],
    "answer": (
        """🤖 I'm not fully confident about this question.

Please:
• Rephrase your question  
• Or contact the unit coordinator for clarification"""
    )
},
{
        "intent": "assignment_purpose",
        "patterns": [
            "purpose", "aim", "what is this assignment about",
            "what are we supposed to do"
        ],
        "answer": (
            "This assignment assesses your ability to analyse a real-world problem, "
            "design a feasible information system solution, and clearly communicate that proposal. "
            "Marks are awarded for analysis, justification, and alignment with information systems principles, "
            "not for technical implementation."
        )
    },

    {
        "intent": "assignment_date",
        "patterns": [
            "purpose", "time", "due", "date" , "what is this assignment due",
            "when are we supposed to submit"
        ],
        "answer": (
            "This assignment is due by Friday 15 May 2026, 21:59 in your Chinese local time, set to 23:59, "
            "in Australian time on Moodle"
        )
    },

    {
        "intent": "group_size_and_roles",
        "patterns": [
            "group", "team", "how many people", "group size",
            "roles", "team leader"
        ],
        "answer": (
            "This assignment must be completed in groups of three students. "
            "Each group member is responsible for one major section of the report, "
            "which will be marked individually. Coordination and consistency across sections are expected."
        )
    },

    {
        "intent": "word_count_distribution",
        "patterns": [
            "word count", "how many words", "length",
            "per student", "individual words"
        ],
        "answer": (
            "The total report length is 2500–3000 words. "
            "Each individual section should be approximately 800–1000 words. "
            "The introduction and conclusion are team-written and included in the total word count."
        )
    },

    # =========================
    # INTRODUCTION
    # =========================

    {
        "intent": "introduction_expectations",
        "patterns": [
            "introduction", "what to write in introduction",
            "overview", "case study overview"
        ],
        "answer": (
            """📘 **Introduction Section – What to Write**

    Your introduction should **set the context** of your report.

    Include:
    • Brief description of the case study  
    • The organisation or domain (e.g., hospital, retail, university)  
    • The main problem area (high-level only)  
    • Purpose of the report  

    🧠 **Tip:** Do NOT explain the full problem here — keep it brief.

    📌 **Example:**
    "This report analyses inefficiencies in a retail inventory system and proposes an improved information system solution to enhance accuracy and decision-making."

    ⚠️ Common mistake:
    Students go into too much detail — keep it concise and focused."""
        )
    },

    # =========================
    # PROBLEM IDENTIFICATION
    # =========================

    {
        "intent": "problem_identification",
        "patterns": [
            "problem identification", "problem section",
            "problem analysis", "how to identify problem"
        ],
        "answer": (
            """🔍 **Problem Identification – How to Do It Well**

        You must go beyond describing symptoms — identify **root causes**.
    
        Include:
        • What is the problem?  
        • Why does it happen?  
        • Who is affected?  
        • What are the consequences?  
    
        🧠 Use TWO problem-solving approaches (e.g., root cause analysis, 5 Whys)
    
        📌 **Example:**
        Problem: Inventory errors  
        Cause: Manual data entry  
        Impact: Financial loss + poor decision-making  
    
        ⚠️ Common mistakes:
        • Only describing symptoms  
        • No justification  
        • No structured analysis"""
            )
    },

    {
        "intent": "problem_depth",
        "patterns": [
            "how detailed", "depth", "how much analysis",
            "problem description"
        ],
        "answer": (
            "A strong problem analysis goes beyond symptoms and identifies root causes. "
            "You should clearly explain the context, stakeholders affected, and consequences "
            "of the problem if it remains unresolved."
        )
    },

    {
        "intent": "multiple_problems",
        "patterns": [
            "more than one problem", "multiple problems",
            "several issues"
        ],
        "answer": (
            "You may identify multiple related problems; however, they should be clearly connected "
            "and manageable within the scope of a single system solution. Avoid unrelated or overly broad issues."
        )
    },

    # =========================
    # PROPOSED SYSTEM SOLUTION
    # =========================

    {
    "intent": "system_solution",
    "patterns": [
        "system solution", "proposed system",
        "system design", "what to include in system"
    ],
    "answer": (
        """💡 **System Solution – What You Must Include**

    You are proposing a **conceptual system design (NOT coding)**.
    
    Include:
    
    🖥️ Hardware:
    • Servers, devices, cloud infrastructure  
    
    💻 Software:
    • Applications, databases, platforms  
    
    👥 People:
    • Users, admins, stakeholders  
    
    🔄 Processes:
    • How the system works (input → process → output)  
    
    🗄️ Data:
    • What data is used and how  
    
    📌 **Example:**
    "A cloud-based inventory system that automatically updates stock levels and generates reports."
    
    ⚠️ Common mistakes:
    • Too vague  
    • No justification  
    • Missing components"""
        )
    },

    {
        "intent": "solution_scope",
        "patterns": [
            "how big", "scope", "how detailed is solution",
            "level of detail"
        ],
        "answer": (
            "You are proposing a conceptual system design, not building a system. "
            "The focus should be on system components, processes, and data flows, "
            "with clear justification for design choices."
        )
    },

    {
        "intent": "system_name",
        "patterns": [
            "system name", "do we need a name",
            "naming the system"
        ],
        "answer": (
            "Yes, you should give your proposed system a clear and descriptive name. "
            "This helps communicate its purpose and improves clarity throughout the report."
        )
    },

    {
        "intent": "hardware_expectations",
        "patterns": [
            "hardware", "servers", "devices",
            "do we need hardware"
        ],
        "answer": (
            "You should identify the key hardware components required to support your system, "
            "such as servers, workstations, or mobile devices. "
            "Justification is more important than technical detail."
        )
    },

    {
        "intent": "software_expectations",
        "patterns": [
            "software", "platform", "operating system",
            "applications"
        ],
        "answer": (
            "You should describe the main software components, such as operating systems, "
            "databases, or application software. The emphasis should be on suitability and alignment "
            "with the problem rather than specific product features."
        )
    },

    {
        "intent": "people_and_stakeholders",
        "patterns": [
            "people", "users", "stakeholders",
            "who will use the system"
        ],
        "answer": (
            "You should identify all key stakeholders and user roles, such as administrators, "
            "end users, and decision-makers. A brief stakeholder analysis is expected."
        )
    },

    {
        "intent": "process_diagrams",
        "patterns": [
            "diagram", "dfd", "flowchart", "uml"
        ],
        "answer": (
            """📈 **Diagrams – What You Need**

        You must include at least ONE diagram:
    
        ✔ Flowchart  
        ✔ UML Activity Diagram  
        ✔ Data Flow Diagram (DFD)  
    
        📌 Purpose:
        Show how the system works visually
    
        🧠 Example flow:
        User → Input Data → System Processing → Output Report
    
        ⚠️ Common mistakes:
        • Diagram not explained  
        • Too complex or unclear  
        • No labels"""
            )
        },

    # =========================
    # DATA USE AND MANAGEMENT
    # =========================

    {
    "intent": "data_management",
    "patterns": [
        "data management", "data section",
        "data storage", "database"
    ],
    "answer": (
        """🗄️ **Data Management – What to Explain**

    You must clearly describe how data flows in your system:
    
    📥 Data Collection:
    • Forms, sensors, user input  
    
    💾 Data Storage:
    • Database (usually relational)  
    
    ⚙️ Data Processing:
    • Calculations, reports, analytics  
    
    🔐 Data Security:
    • Access control, encryption  
    
    📌 **Example Table:**
    User(ID, Name, Email, Role)
    
    🧠 Tip:
    Explain WHY your design is suitable — not just WHAT.
    
    ⚠️ Common mistakes:
    • No example data  
    • No security discussion"""
        )
    },

    {
        "intent": "data_types",
        "patterns": [
            "what data", "types of data",
            "data used"
        ],
        "answer": (
            "You should describe the key types of data the system will collect, store, and process, "
            "including their sources and purpose within the system."
        )
    },

    {
        "intent": "data_schema_example",
        "patterns": [
            "data schema", "table", "database example",
            "schema required"
        ],
        "answer": (
            "You are expected to include at least one example of a data structure, such as a table schema. "
            "This should demonstrate how important data entities are organised, not a full database design."
        )
    },

    {
        "intent": "database_model",
        "patterns": [
            "database model", "relational", "nosql",
            "which database"
        ],
        "answer": (
            "You should state and justify the database model used, such as relational or NoSQL. "
            "Your justification should relate to the nature of the data and system requirements."
        )
    },

    {
        "intent": "data_security",
        "patterns": [
            "security", "privacy", "data protection",
            "unauthorised access"
        ],
        "answer": (
            "You must explain how data will be protected from unauthorised access or modification. "
            "This may include access controls, authentication, encryption, and privacy considerations."
        )
    },

    {
    "intent": "sample_solution",
    "patterns": [
        "example solution", "sample system",
        "example answer system design"
    ],
    "answer": (
        """📘 **Sample System Idea**

    Example:
    
    A university system that:
    • Tracks student attendance  
    • Stores grades in a database  
    • Generates performance reports  
    
    🧠 Why it works:
    • Solves real problem  
    • Uses data effectively  
    • Supports decision-making"""
        )
    },

    # =========================
    # FEASIBILITY STUDY
    # =========================

    {
    "intent": "feasibility",
    "patterns": [
        "feasibility study", "feasibility section"
    ],
    "answer": (
        """📊 **Feasibility Study – Required Analysis**

    Evaluate whether your system is realistic:
    
    🖥️ Technical:
    Can it be built with available technology?
    
    💰 Economic:
    Is it cost-effective?
    
    👥 Operational:
    Will users accept it?
    
    ⚖️ Legal:
    Any legal/privacy issues?
    
    ⏳ Time:
    Can it be completed in time?
    
    📌 **Example:**
    Cloud system → technically feasible, scalable, moderate cost
    
    ⚠️ Common mistakes:
    • Only listing advantages  
    • No justification  
    • Too generic"""
        )
    },

    {
        "intent": "feasibility_types",
        "patterns": [
            "feasibility", "types of feasibility",
            "technical economic legal"
        ],
        "answer": (
            "You must analyse technical, economic, legal, operational, and time feasibility. "
            "Each type should be addressed explicitly with evidence or justification."
        )
    },

    {
        "intent": "feasibility_depth",
        "patterns": [
            "how detailed feasibility",
            "depth of feasibility"
        ],
        "answer": (
            """📊 **Feasibility Depth – What Gets High Marks**

    A strong answer includes:

    ✔ Realistic assumptions  
    ✔ Limitations and risks  
    ✔ Justification with reasoning  

    📌 Example:
    "While cloud systems reduce maintenance cost, initial setup may require training."

    ⚠️ Weak answer:
    "It is feasible because it is good" ❌"""
        )
    },

    {
        "intent": "overlap_between_sections",
        "patterns": [
            "overlap", "repeat", "duplicate",
            "same content in sections"
        ],
        "answer": (
            "Some overlap is acceptable, but each section must serve its own purpose. "
            "For example, data management focuses on data handling, while feasibility "
            "focuses on whether the proposed approach is practical."
        )
    },

    # =========================
    # MARKING AND RUBRIC
    # =========================

    {
        "intent": "rubric_breakdown",
        "patterns": [
            "rubric", "marks", "marking",
            "how is this marked"
        ],
        "answer": (
            "Marks are allocated as follows: Introduction (10 marks), "
            "Individual section (12 marks), Conclusion and recommendations (8 marks), "
            "and References and writing quality (5 marks)."
        )
    },

    {
        "intent": "individual_marking",
        "patterns": [
            "individual marks", "marked individually",
            "team marks"
        ],
        "answer": (
            "Each major section is marked individually. "
            "While the report is a team submission, your allocated section determines "
            "your individual mark."
        )
    },

    # =========================
    # ACADEMIC INTEGRITY
    # =========================

    {
        "intent": "ai_usage",
        "patterns": [
            "ai", "chatgpt", "can i use ai",
            "tools allowed"
        ],
        "answer": (
            "You must comply with university academic integrity policies. "
            "AI tools may be used for understanding requirements or improving clarity, "
            "but not for generating assessed content unless explicitly permitted."
        )
    },

    {
        "intent": "plagiarism",
        "patterns": [
            "plagiarism", "copy", "reuse",
            "academic integrity"
        ],
        "answer": (
            "Plagiarism occurs when another person’s work is presented as your own without acknowledgment. "
            "You are responsible for ensuring your work is original and properly referenced."
        )
    },



]