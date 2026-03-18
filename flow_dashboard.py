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

# Optional knowledge mode
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

# Knowledge Mode
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
st.header("Multi-System Comparison")

# Example systems (تقدر تغيرها لاحقًا)
systems_data = [
    {"name": "System A", "score": 90},
    {"name": "System B", "score": 65},
    {"name": "System C", "score": 30},
]

# Sort systems
systems_data = sorted(systems_data, key=lambda x: x["score"], reverse=True)

for s in systems_data:
    if s["score"] > 80:
        color = "#28a745"
    elif s["score"] > 50:
        color = "#ffc107"
    else:
        color = "#dc3545"

    st.markdown(
        f"""
        <div style="padding:10px;border-radius:10px;background-color:{color};color:white;margin-bottom:5px;">
        {s["name"]} — Score: {s["score"]}
        </div>
        """,
        unsafe_allow_html=st.header("AI Mode")

user_prompt = st.text_area(
    "Describe the system briefly",
    "Duqm logistics flow is stable in production but constrained in transfer due to limited alternative routes and partial coordination."
)

if st.button("Analyze with AI Mode"):
    text = user_prompt.lower()

    # Simple rule-based interpretation
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

    if "limited route" in text or "single route" in text or "no alternative" in text:
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
