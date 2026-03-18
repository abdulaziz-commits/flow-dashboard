import streamlit as st

st.set_page_config(page_title="Flow System Dashboard", layout="centered")

st.title("🧠 Flow System Dashboard")

# -------------------
# INPUTS
# -------------------
st.header("Inputs")

system = st.text_input("System Name", "Duqm Logistics")

flow_type = st.selectbox(
    "Flow Type",
    ["Energy", "Knowledge", "Logistics", "Capital", "Material"]
)

stage = st.selectbox(
    "Stage",
    ["Production", "Transfer", "Synchronization", "Propagation", "Evolution"]
)

multiplicity = st.selectbox("Multiplicity", [0, 1, 2, 3])
sync = st.selectbox("Synchronization", ["Full", "Partial", "None"])

# -------------------
# KNOWLEDGE MODE INPUTS
# -------------------
st.header("Knowledge Mode (Optional)")

knowledge_sent = st.selectbox("Knowledge Sent?", ["Yes", "No"])
decision_response = st.selectbox("Decision Response?", ["Yes", "No"])
behavior_changed = st.selectbox("Behavior Changed?", ["Yes", "No"])
state_changed = st.selectbox("State Changed?", ["Yes", "No"])

# -------------------
# CORE LOGIC
# -------------------
# Flow State
if multiplicity == 0 or sync == "None":
    flow_state = "Collapse"
    state_color = "#d9534f"
    score = 10
elif multiplicity == 1 and sync == "Full":
    flow_state = "Stable Scarcity"
    state_color = "#f0ad4e"
    score = 45
elif multiplicity == 1 and sync == "Partial":
    flow_state = "Disturbed Scarcity"
    state_color = "#ff8c42"
    score = 30
elif multiplicity > 1 and sync == "Full":
    flow_state = "Stable Abundance"
    state_color = "#28a745"
    score = 90
else:
    flow_state = "Disturbed Abundance"
    state_color = "#ffd966"
    score = 65

# Constraint
if multiplicity == 0:
    constraint = "Multiplicity Failure"
elif sync == "None":
    constraint = "Synchronization Failure"
elif multiplicity == 1:
    constraint = "Multiplicity Constraint"
elif sync == "Partial":
    constraint = "Synchronization Constraint"
else:
    constraint = "No Constraint"

# Recommended Action
if constraint == "Multiplicity Failure":
    action = "Create alternatives immediately."
elif constraint == "Synchronization Failure":
    action = "Restore coordination immediately."
elif constraint == "Multiplicity Constraint":
    action = "Increase routes, options, or available sources."
elif constraint == "Synchronization Constraint":
    action = "Improve alignment across assets and stages."
else:
    action = "Maintain current flow and monitor continuously."

# Stage interpretation
stage_note = {
    "Production": "This stage measures whether the system can generate or prepare the flow.",
    "Transfer": "This stage measures movement between nodes and exposure to route constraints.",
    "Synchronization": "This stage checks whether all required assets are aligned.",
    "Propagation": "This stage measures whether the flow expands across nodes or systems.",
    "Evolution": "This stage measures whether the flow is refined into a stronger or higher-order form.",
}[stage]

# Knowledge Mode Logic
if knowledge_sent == "No":
    knowledge_status = "No Knowledge Entry"
elif behavior_changed == "Yes" or state_changed == "Yes":
    knowledge_status = "Knowledge Exchange Confirmed"
elif decision_response == "Yes":
    knowledge_status = "Decision-Level Activation"
else:
    knowledge_status = "Pre-Activation / Silent Absorption"

# Knowledge explanation
if knowledge_status == "No Knowledge Entry":
    knowledge_note = "No knowledge flow has entered the receiving system."
elif knowledge_status == "Knowledge Exchange Confirmed":
    knowledge_note = "Observable system change suggests successful knowledge exchange."
elif knowledge_status == "Decision-Level Activation":
    knowledge_note = "A decision response exists, but broader behavior or state change is not yet confirmed."
else:
    knowledge_note = "The knowledge may have entered the system, but impact is not yet visible."

# -------------------
# OUTPUT
# -------------------
st.header("System Output")

# Flow state card
st.markdown(
    f"""
    <div style="padding:16px;border-radius:12px;background-color:{state_color};color:white;text-align:center;">
        <div style="font-size:16px;">Flow State</div>
        <div style="font-size:28px;font-weight:bold;">{flow_state}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# Score
st.subheader("System Score")
st.progress(score / 100)
st.write(f"**{score}/100**")

# Constraint card
st.markdown(
    f"""
    <div style="padding:12px;border-radius:12px;background-color:#1f1f1f;color:white;">
        <b>Constraint:</b> {constraint}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# Action card
st.markdown(
    f"""
    <div style="padding:12px;border-radius:12px;background-color:#0d6efd;color:white;">
        <b>Recommended Action:</b> {action}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# Stage explanation
st.subheader("Stage Interpretation")
st.info(stage_note)

# Knowledge block
st.subheader("Knowledge Exchange Status")
st.markdown(
    f"""
    <div style="padding:12px;border-radius:12px;background-color:#6f42c1;color:white;">
        <b>{knowledge_status}</b><br><br>
        {knowledge_note}
    </div>
    """,
    unsafe_allow_html=True
)

# Summary
st.markdown("---")
st.caption(
    f"System: {system} | Flow Type: {flow_type} | Stage: {stage} | "
    f"Multiplicity: {multiplicity} | Synchronization: {sync}"
)

# -------------------
# MULTI-SYSTEM COMPARISON
# -------------------
st.header("Multi-System Comparison")

systems_data = [
    {"name": "System A", "score": 90},
    {"name": "System B", "score": 65},
    {"name": "System C", "score": 30},
]

systems_data = sorted(systems_data, key=lambda x: x["score"], reverse=True)

for s in systems_data:
    if s["score"] > 80:
        box_color = "#28a745"
    elif s["score"] > 50:
        box_color = "#ffc107"
    else:
        box_color = "#dc3545"

    st.markdown(
        f"""
        <div style="padding:10px;border-radius:10px;background-color:{box_color};color:white;margin-bottom:5px;">
        {s["name"]} — Score: {s["score"]}
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------
# AI MODE
# -------------------
st.header("AI Mode")

user_prompt = st.text_area(
    "Describe the system briefly",
    "Duqm logistics flow is stable in production but constrained in transfer due to limited alternative routes and partial coordination."
)

if st.button("Analyze with AI Mode"):
    text = user_prompt.lower()

    detected_stage = "Unknown"
    detected_constraint = "No Clear Constraint"
    detected_state = "Monitor"
    detected_action = "Gather more detail."

    if "production" in text:
        detected_stage = "Production"
    elif "transfer" in text:
        detected_stage = "Transfer"
    elif "synchronization" in text:
        detected_stage = "Synchronization"
    elif "propagation" in text:
        detected_stage = "Propagation"
    elif "evolution" in text:
        detected_stage = "Evolution"

    if (
        "limited route" in text
        or "limited routes" in text
        or "single route" in text
        or "no alternative" in text
    ):
        detected_constraint = "Multiplicity Constraint"
        detected_state = "Scarcity or Disturbed Flow"
        detected_action = "Increase routes, options, or backup sources."

    if "partial coordination" in text or "misalignment" in text or "delay" in text:
        detected_constraint = "Synchronization Constraint"
        detected_state = "Disturbed Flow"
        detected_action = "Improve alignment across assets and decision layers."

    if "collapse" in text or "stopped" in text or "failed completely" in text:
        detected_constraint = "Critical Failure"
        detected_state = "Collapse"
        detected_action = "Immediate intervention required."

    if "stable" in text and "full coordination" in text:
        detected_constraint = "No Active Constraint"
        detected_state = "Stable Abundance"
        detected_action = "Maintain and monitor."

    st.subheader("AI Interpretation")
    st.markdown(
        f"""
        <div style="padding:14px;border-radius:12px;background-color:#0b5ed7;color:white;">
        <b>Detected Stage:</b> {detected_stage}<br><br>
        <b>Detected State:</b> {detected_state}<br><br>
        <b>Detected Constraint:</b> {detected_constraint}<br><br>
        <b>Recommended Action:</b> {detected_action}
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------
# LEADERSHIP MODE
# -------------------
st.header("Leadership Mode")

lead_summary = (
    f"The system '{system}' is currently assessed at the '{flow_state}' level "
    f"during the '{stage}' stage. The main issue identified is '{constraint}'."
)

if constraint == "No Constraint":
    strategic_note = (
        "The system is functioning within acceptable parameters. "
        "The priority is to preserve continuity, maintain synchronization, "
        "and monitor for early signs of degradation."
    )
elif "Multiplicity" in constraint:
    strategic_note = (
        "The system is exposed to structural vulnerability due to limited alternatives. "
        "Its current configuration increases exposure to disruption if one path or source fails."
    )
elif "Synchronization" in constraint:
    strategic_note = (
        "The system is structurally present, but alignment across assets or decision layers is incomplete. "
        "This creates inefficiency, delay, and rising risk despite available capacity."
    )
else:
    strategic_note = (
        "The system is approaching critical instability and requires immediate executive attention."
    )

leader_recommendation = action

st.subheader("Executive Summary")
st.markdown(
    f"""
    <div style="padding:14px;border-radius:12px;background-color:#111827;color:white;">
    {lead_summary}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.subheader("Strategic Note")
st.markdown(
    f"""
    <div style="padding:14px;border-radius:12px;background-color:#374151;color:white;">
    {strategic_note}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.subheader("Leader Recommendation")
st.markdown(
    f"""
    <div style="padding:14px;border-radius:12px;background-color:#7c3aed;color:white;">
    {leader_recommendation}
    </div>
    """,
    unsafe_allow_html=True
)
# -------------------
# REPORT MODE
# -------------------
st.header("Report Mode")

if st.button("Generate Report"):

    report_text = f"""
Flow System Report

System: {system}
Flow Type: {flow_type}
Stage: {stage}

Flow State: {flow_state}
Constraint: {constraint}
Score: {score}/100

Analysis:
The system is currently operating at the '{flow_state}' level during the '{stage}' stage.
The primary constraint identified is '{constraint}'.

Strategic Insight:
{strategic_note}

Recommended Action:
{action}

Knowledge Status:
{knowledge_status}
{knowledge_note}

Conclusion:
The system requires {'immediate intervention' if score < 30 else 'targeted optimization' if score < 70 else 'continuous monitoring'} to ensure stable and resilient flow performance.
"""

    st.subheader("Generated Report")
    st.text_area("Copy & Send", report_text, height=300)
# -------------------
# PREDICTION MODE
# -------------------
st.header("Prediction Mode")

# Direction logic
if score >= 80:
    direction = "→ Stable Trajectory"
    risk = "Low Risk"
    prediction = "System expected to remain stable if current conditions persist."
elif score >= 50:
    direction = "↘ Potential Degradation"
    risk = "Moderate Risk"
    prediction = "System may shift toward disturbance if constraints are not addressed."
else:
    direction = "↓ Collapse Trajectory"
    risk = "High Risk"
    prediction = "System is at risk of collapse or already degrading."

# Constraint-based amplification
if "Multiplicity" in constraint:
    prediction += " Risk amplified by lack of alternatives."
elif "Synchronization" in constraint:
    prediction += " Risk amplified by coordination gaps."

# Stage-based insight
if stage == "Transfer":
    prediction += " Transfer stage is highly sensitive to disruption."
elif stage == "Synchronization":
    prediction += " Misalignment at this stage can rapidly degrade system performance."

# Output UI
st.subheader("Future Direction")
st.markdown(
    f"""
    <div style="padding:14px;border-radius:12px;background-color:#212529;color:white;">
    <b>Direction:</b> {direction}<br><br>
    <b>Risk Level:</b> {risk}<br><br>
    <b>Prediction:</b> {prediction}
    </div>
    """,
    unsafe_allow_html=True
)
# -------------------
# SCENARIO MODE
# -------------------
st.header("Scenario Mode")

# Current
current_score = score

# Best case assumptions
if multiplicity < 3:
    best_mult = multiplicity + 1
else:
    best_mult = multiplicity

best_sync = "Full"

if best_mult == 0 or best_sync == "None":
    best_score = 10
elif best_mult == 1 and best_sync == "Full":
    best_score = 45
elif best_mult == 1 and best_sync == "Partial":
    best_score = 30
elif best_mult > 1 and best_sync == "Full":
    best_score = 90
else:
    best_score = 65

# Worst case assumptions
worst_mult = max(0, multiplicity - 1)
worst_sync = "None" if sync == "Partial" else "Partial"

if worst_mult == 0 or worst_sync == "None":
    worst_score = 10
elif worst_mult == 1 and worst_sync == "Full":
    worst_score = 45
elif worst_mult == 1 and worst_sync == "Partial":
    worst_score = 30
elif worst_mult > 1 and worst_sync == "Full":
    worst_score = 90
else:
    worst_score = 65

st.subheader("Scenario Comparison")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div style="padding:12px;border-radius:12px;background-color:#0d6efd;color:white;text-align:center;">
        <b>Current</b><br><br>
        Score: {current_score}/100
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="padding:12px;border-radius:12px;background-color:#198754;color:white;text-align:center;">
        <b>Best Case</b><br><br>
        Score: {best_score}/100
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style="padding:12px;border-radius:12px;background-color:#dc3545;color:white;text-align:center;">
        <b>Worst Case</b><br><br>
        Score: {worst_score}/100
        </div>
        """,
        unsafe_allow_html=True
    )

st.info(
    "Best Case assumes stronger synchronization and/or more alternatives. "
    "Worst Case assumes weaker synchronization and/or fewer alternatives."
)
