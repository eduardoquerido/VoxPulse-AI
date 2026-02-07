# 🗳️ VoxPulse-AI: 2026 Brazil's Political Sentiment Monitor

**VoxPulse-AI** is an autonomous AI agent designed to capture and analyze voter sentiment in real-time. Powered by **Gemini 2.5 Flash** and **Groq Cloud**, it processes large volumes of social media data and news to identify electoral trends, toxicity spikes, and key campaign themes.

---

## 🎯 Project Overview
In a polarized electoral landscape, understanding the "digital pulse" is crucial. This project demonstrates how autonomous agents can replace manual monitoring by browsing the web, synthesizing public opinion, and generating actionable insights for campaign coordinators or political analysts.

While currently focused on the Brazilian political landscape, it can be easily adapted to other scenarios with minimal effort.

## 🚀 Key Features
* **Autonomous Web Research:** Scans the web for recent mentions of candidates, parties, or specific hashtags.
* **Nuanced Sentiment Analysis:** Goes beyond "positive/negative" to detect emotions like hope, anger, or skepticism.
* **Topic Modeling:** Automatically categorizes sentiments into pillars such as Economy, Healthcare, Security, and Education.
* **Crisis Detection:** Identifies sudden surges in negative mentions, acting as an early warning system for PR teams.
* **Zero-Cost Infrastructure:** Optimized to run entirely on Free Tier LLMs without compromising performance.

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **LLM (The Brain):** [Google Gemini 2.5 Flash](https://aistudio.google.com/) (Free Tier)
* **LLM (The Brain):** [Groq Cloud](https://console.groq.com/home) - Llama 3.3 70B Versatile.
    * **Advantage:** Powered by LPU™ (Language Processing Unit) architecture, delivering significantly faster response times than Gemini (ultra-low latency), which is ideal for complex multi-agent workflows in CrewAI.
    * **Cost:** Free Tier (usage-based limits on RPM and TPM).
    * **Integration:** Implemented via `crewai.LLM` with native `litellm` support to ensure structured outputs and full compatibility with the LangChain ecosystem.
* **Agent Framework:** [CrewAI](https://www.crewai.com/) / LangChain
* **Web Search:** [Tavily AI](https://tavily.com/) / Serper.dev (Optimized for LLMs)
* **Dashboard:** Streamlit

*Note:* The project leverages Groq for agent orchestration due to its extreme inference speed, allowing political analyses to be completed in a fraction of the time compared to traditional cloud providers.

## 📋 Getting Started

### Prerequisites
* A Google AI Studio API Key.
* A Search API Key (Tavily or Serper).

### Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/eduardoquerido/VoxPulse-AIAgent.git
    cd VoxPulse-AI
    ```

2. **Install dependencies:**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Environment Setup:**
    Create a `.env` file in the root directory or change env_example to .env
    ```env
    GOOGLE_API_KEY=your_google_studio_ai_api_key
    GROQ_API_KEY=your_groq_api_key_here
    TAVILY_API_KEY=your_tavily_api_key

## 🔒 Security & Reproducibility
This project uses `pip-tools` to ensure deterministic builds. 
To regenerate the hashed dependencies, run:
`pip-compile --generate-hashes --output-file=requirements.txt requirements.in`

## 🛠️ Development Automation with Tox

This project uses **[tox](https://tox.wiki/)** to automate environment management, code formatting, and testing.

### Core Commands

| Command | Description |
| :--- | :--- |
| `tox -l` | List all available environments. |
| `tox -a` | List environments with detailed descriptions. |
| `tox` | Run the full suite (formatting, linting, and tests). |
| `tox -e format` | **Auto-fix** code style using `black` and `isort`. |
| `tox -e checklint` | **Verify** code style and import sorting (checks only). |
| `tox -e unittesting` | Run all unit tests in a clean Python 3.10 environment. |

### Maintenance & Troubleshooting

* **Rebuild environments:** Use this if you've updated dependencies or the `tox.ini` file.
  ```bash
  tox -r

## 🚀 Running the Web Dashboard

The **VoxPulse-AI** interface is built with Streamlit. Follow these steps to launch the dashboard locally:

### 1. Standard Execution
Run this command in your terminal while your virtual environment is active:
`python3.11 -m streamlit run app.py`