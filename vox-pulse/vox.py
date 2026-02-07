# --- Monkey Patch --- #
import sys

try:
    import sqlite3

    import pysqlite3

    if sqlite3.sqlite_version_info < (3, 35, 0):
        sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
        print("SQLite3 patched successfully with pysqlite3-binary")
except ImportError:
    print("DEBUG: pysqlite3 not found in sys.path. Still using system sqlite3.")

# --- CrewAI Telemetry --- #
import os

os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

import datetime

import streamlit as st
from voxpulse import run_analysis

st.set_page_config(page_title="VoxPulse-AI", page_icon="🗳️", layout="wide")

st.title("🗳️ VoxPulse-AI")
st.markdown("""
    **Autonomous Political Sentiment Analysis Engine** Monitor the 2026 electoral digital pulse using Gemini 1.5 Flash and Multi-Agent Systems.
""")

with st.sidebar:
    st.header("Settings")
    st.info("Currently running on Gemini 2.5 Flash (Free Tier)")
    st.divider()
    st.write(f"**Date:** {datetime.date.today()}")

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None


# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    # Language Selection
    language = st.selectbox(
        "Preferred Language / Idioma:",
        options=["Portuguese-BR", "English"],
        index=0  # Default to Portuguese
    )
    st.divider()


politician = st.text_input(
    "Enter the name of a politician or public figure:",
    placeholder="e.g., President of Brazil, Governor of São Paulo...",
)

# --- Analysis Logic ---
if st.button("Analyze Digital Pulse"):
    if not politician:
        st.warning("Please enter a name to start the analysis.")
    else:
        with st.status(
            f"Agents are working on {politician}...", expanded=True
        ) as status:
            try:
                st.write("🔍 Searching for recent news...")
                results = run_analysis(politician, language)
                st.session_state.analysis_result = results.raw

                status.update(
                    label="Analysis Complete!", state="complete", expanded=False
                )

                col1, col2 = st.columns([2, 1])

                with col1:
                    st.subheader("📋 Executive Summary")
                    st.markdown(results.raw)  # CrewAI result object

                with col2:
                    st.subheader("📊 Metadata")
                    st.json(
                        {
                            "Model": "Gemini 2.5 Flash",
                            "Agents": ["Researcher", "Analyst"],
                            "Timestamp": str(datetime.datetime.now()),
                        }
                    )

            except Exception as e:
                st.error(f"An error occurred: {e}")
                status.update(label="Analysis Failed", state="error")

if st.session_state.analysis_result:
    st.divider()
    st.subheader(f"📊 Results for {politician}")

    st.markdown(st.session_state.analysis_result)

    if st.button("Clear Results"):
        st.session_state.analysis_result = None
        st.rerun()

st.divider()
st.caption("VoxPulse-AI POC - Developed for the 2026 Election Portfolio.")
