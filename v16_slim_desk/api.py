import frappe
import json

@frappe.whitelist()
def save_config(workspaces):
    """
    Save the user's sidebar configuration.
    workspaces: List of strings (workspace names)
    """
    if isinstance(workspaces, str):
        try:
            workspaces = json.loads(workspaces)
        except:
            pass
    
    # Ensure it's a list
    if not isinstance(workspaces, list):
        frappe.throw("Invalid workspace list")

    # Save as User Default
    frappe.defaults.set_user_default("slim_desk_config", json.dumps(workspaces))
    
    return "success"
