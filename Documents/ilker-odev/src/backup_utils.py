import os
import zipfile
import datetime
from cron_descriptor import get_description

LOG_FILE = os.path.join(os.path.dirname(__file__), "activity.log")

def translate_cron(expression):
    """Translates a cron expression to human-readable text."""
    try:
        return get_description(expression)
    except Exception as e:
        return f"Error: Invalid Cron Expression ({str(e)})"

def log_activity(message, status="INFO"):
    """Logs activity to a file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{status}] {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def perform_backup(source_dir, dest_dir):
    """Zips the source directory and saves it to the destination directory."""
    if not os.path.exists(source_dir):
        msg = f"Source directory does not exist: {source_dir}"
        log_activity(msg, "ERROR")
        return False, msg
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = os.path.basename(os.path.normpath(source_dir))
    zip_name = f"backup_{folder_name}_{timestamp}.zip"
    zip_path = os.path.join(dest_dir, zip_name)

    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
        
        # Self-Check mechanism
        if os.path.exists(zip_path) and os.path.getsize(zip_path) > 0:
            success_msg = f"Backup created successfully: {zip_path}"
            log_activity(success_msg, "SUCCESS")
            return True, success_msg
        else:
            fail_msg = "Backup failed: File was not created or is empty."
            log_activity(fail_msg, "ERROR")
            return False, fail_msg
            
    except Exception as e:
        error_msg = f"Backup failed with error: {str(e)}"
        log_activity(error_msg, "ERROR")
        return False, error_msg

def get_logs():
    """Reads the activity log file."""
    if not os.path.exists(LOG_FILE):
        return "No activity logs found."
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()

def clear_logs():
    """Clears the activity log file."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("")
    log_activity("Logs cleared", "INFO")
