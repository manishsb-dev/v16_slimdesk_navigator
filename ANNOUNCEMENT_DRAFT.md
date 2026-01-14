# [Release] SlimDesk Navigator: Persistent Sidebar for v16 (Solve Context Switching Fatigue)

Hi everyone,

Like many of you testing the new v16 UI, I found myself getting "lost" when navigating between different modules. The new design is beautiful, but the constant need to click "Home" or "Desk" just to switch from *Buying* to *Selling* or *Stock* was adding friction to my workflow. I missed the structure and "anchor" of a persistent navigation sidebar.

Searching through the forum, I saw I wasn't alone:
> "Navigation inefficiency... need to return to Desk to switch modules."
> "Confusing module switching... context changes make it difficult to stay oriented."

So I built **SlimDesk Navigator** to solve this.

## What is it?
It's a simple, unobtrusive app that injects a **persistent, slim sidebar** on the left side of your screen. 

**Result:** You can jump from *Accounting* to *Manufacturing* in **one click**, without ever losing your current page context or going back to the grid.

### Key Features
*   **Persistent & Unobtrusive:** Always there, but takes up minimal space.
*   **Smart Icons:** Uses a professional grayscale "subtle" theme that matches the v16 aesthetic (color on hover).
*   **Auto-Discovery:** Automatically detects icons for your installed apps (no configuration needed).
*   **Fully Customizable:** Drag & drop reordering and custom links via a simple "Edit" dialog.
*   **Native Feel:** Sorts alphabetically and respects standard Frappe Desk permissions and hidden workspaces.

## Screenshots
[Insert Screenshot Here - showing the Sidebar next to a standard List View]

## Installation
The app is open source and public.

```bash
bench get-app v16_slimdesk_navigator https://github.com/zerodiscount/v16_slimdesk_navigator
bench --site [your-site] install-app v16_slimdesk_navigator
```

## Repository
[https://github.com/zerodiscount/v16_slimdesk_navigator](https://github.com/zerodiscount/v16_slimdesk_navigator)

I hope this helps others who are missing that "persistent anchor" in their daily workflows! Feedback is welcome.

Cheers,
[Your Name]
