import logging
import main

def entry_point(event, context):
    """
    Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print("GCP Function Triggered: Running Stock Automation...")
    
    # We force the automation mode
    import sys
    sys.argv = ["main.py", "--auto"]
    
    try:
        main.main()
        return "Success"
    except Exception as e:
        logging.error(f"Error running automation: {e}")
        return f"Error: {e}"
