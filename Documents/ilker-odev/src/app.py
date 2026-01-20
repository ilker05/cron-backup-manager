"""
---------------------------------------------------------
Proje: Cron Backup Manager
Ders: Açık Kaynak
Hazırlayan: ILKER MIRIK
Öğrenci No: 2420161145
Tarih: 20.01.2026
---------------------------------------------------------
"""

import streamlit as st
import os
from backup_utils import translate_cron, perform_backup, get_logs, clear_logs, log_activity

# Page Configuration
st.set_page_config(
    page_title="Cron Backup Manager",
    page_icon="🕒",
    layout="wide",
)

# Custom CSS for modern look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
        border: 2px solid #45a049;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    .reportview-container .main .block-container{
        padding-top: 2rem;
    }
    h1 {
        color: #2c3e50;
    }
    .log-container {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        font-family: monospace;
        height: 400px;
        overflow-y: scroll;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.title("🚀 Navigation")
    menu = ["Dashboard", "Cron Translator", "Backup Wizard", "Log Viewer"]
    choice = st.sidebar.selectbox("Go to", menu)

    if choice == "Dashboard":
        st.title("🏡 Cron & Backup Dashboard")
        st.write("Welcome to the **Cron Backup Manager**. Use the sidebar to navigate through features.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("### 🕒 Cron Translator\nConvert cron expressions to readable text instantly.")
        with col2:
            st.success("### 📂 Backup Wizard\nSecurely archive your folders with a single click.")
            
        st.write("---")
        st.markdown("### 📊 Quick Stats")
        logs = get_logs()
        success_count = logs.count("[SUCCESS]")
        error_count = logs.count("[ERROR]")
        st.metric("Total Successful Backups", success_count)
        st.metric("Total Errors Encountered", error_count, delta_color="inverse")

    elif choice == "Cron Translator":
        st.title("🕒 Cron Expression Translator")
        st.write("Enter a standard cron expression (e.g., `*/5 * * * *`) to see its human-friendly description.")
        
        cron_input = st.text_input("Cron Expression", placeholder="* * * * *")
        if cron_input:
            description = translate_cron(cron_input)
            if "Error" in description:
                st.error(description)
            else:
                st.success(f"**Description:** {description}")
                if st.button("Log this Translation"):
                    log_activity(f"Translated cron: {cron_input} -> {description}", "INFO")
                    st.toast("Translation logged!")

    elif choice == "Backup Wizard":
        st.title("📂 Backup Wizard")
        st.write("Enter the paths for the source and destination directories.")
        
        source = st.text_input("Source Folder Path", placeholder="/path/to/source")
        destination = st.text_input("Destination Folder Path", placeholder="/path/to/backups")
        
        if st.button("🔥 Start Backup"):
            if source and destination:
                with st.spinner("Creating backup..."):
                    success, message = perform_backup(source, destination)
                    if success:
                        st.success(message)
                        st.balloons()
                    else:
                        st.error(message)
            else:
                st.warning("Please provide both source and destination paths.")

    elif choice == "Log Viewer":
        st.title("📜 System Activity Logs")
        
        logs = get_logs()
        st.markdown(f'<div class="log-container"><pre>{logs}</pre></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("🗑️ Clear Logs"):
                clear_logs()
                st.rerun()

if __name__ == "__main__":
    main()
