# SlimDesk Navigator TODO

## Backlog
- [ ] 

## In Progress
- [ ] **Bug: Icons Unresponsive after System Reload**
    - **Scenario:** Changing system settings triggers a Frappe "Reload". The sidebar remains visible, but **clicking icons does nothing**.
    - **Suspect:** Event listeners are attached to specific DOM elements that get replaced or wiped during the soft reload, and re-initialization fails to re-attach them.
    - **Workaround:** Hard Refresh fixes it. **Bug: Icons Stop Working after System Reload**
    - **Scenario:** Changing system settings triggers a Frappe "Reload" modal. After this reload, SlimDesk icons become unresponsive or disappear.
    - **Workaround:** Navigating to Desk URL + Hard Refresh restores functionality.
    - **Suspect:** Initialization logic doesn't re-trigger correctly after a soft `frappe.ui.reload` or DOM replacement. 

## Completed
- [x] v3.40 Public Release
