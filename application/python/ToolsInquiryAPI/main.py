from html import escape

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from controllers.tools_controller import router as tools_router
from models.tools import ToolsModel 


app = FastAPI(
    title="Tools Inquiry API",
    version="1.0.0",
)

app.include_router(tools_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/tools/{tool_id}")
def get_tool(tool_id: int):
    tool = ToolsModel.FindToolById(tool_id)
    #return tool
    print (tool_id)
    return tool


@app.get("/toolsformatted", response_class=HTMLResponse)
def get_tools_page():
    tools = ToolsModel.FindToolList()
    tool_rows = "".join(
        f"""<tr>
            <td class="tool-id">{tool.id:03}</td>
            <td><span class="tool-name">{escape(str(tool.name))}</span></td>
            <td class="description">{escape(str(tool.description))}</td>
            <td class="quantity">{tool.quantity}</td>
            <td class="price">{tool.price:.2f}</td>
        </tr>"""
        for tool in tools
    )
    total_quantity = sum(tool.quantity for tool in tools)
    total_value = sum(tool.price for tool in tools)
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light">
    <title>Tool Inventory</title>
    <style>
        :root {{
            font-family: "Avenir Next", Avenir, "Segoe UI", sans-serif;
            color: #202a25;
            background: #f3f5ef;
            font-synthesis: none;
            --green: #245c45;
            --muted: #68756d;
            --line: #e2e8e1;
        }}
        * {{ box-sizing: border-box; }}
        body {{ margin: 0; min-height: 100vh; }}
        .topbar {{ height: 58px; display: flex; align-items: center; justify-content: space-between; padding: 0 clamp(20px, 5vw, 72px); background: #fff; border-bottom: 1px solid var(--line); }}
        .brand {{ display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; }}
        .brand-mark {{ display: grid; place-items: center; width: 29px; height: 29px; border-radius: 8px; background: var(--green); color: white; font-size: 17px; }}
        .api-link {{ color: var(--green); font-size: 13px; font-weight: 650; text-decoration: none; }}
        main {{ width: min(1120px, calc(100% - 40px)); margin: 0 auto; padding: 46px 0 64px; }}
        .eyebrow {{ color: var(--green); font-size: 11px; font-weight: 750; letter-spacing: 1.4px; text-transform: uppercase; }}
        h1 {{ margin: 8px 0 5px; font-size: clamp(29px, 4vw, 40px); line-height: 1.1; letter-spacing: 0; }}
        .subtitle {{ margin: 0; color: var(--muted); font-size: 14px; }}
        .summary {{ display: flex; gap: 42px; margin: 30px 0 24px; padding: 17px 20px; border: 1px solid var(--line); border-radius: 8px; background: #fff; }}
        .metric {{ display: flex; align-items: baseline; gap: 9px; }}
        .metric strong {{ color: var(--green); font-size: 23px; }}
        .metric span {{ color: var(--muted); font-size: 12px; }}
        .toolbar {{ display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 10px; }}
        .toolbar h2 {{ margin: 0; font-size: 15px; }}
        .search {{ width: min(310px, 100%); height: 38px; padding: 0 12px; border: 1px solid #d5ded5; border-radius: 6px; background: white; color: inherit; font: inherit; font-size: 13px; outline: none; }}
        .search:focus {{ border-color: var(--green); box-shadow: 0 0 0 3px #245c4520; }}
        .table-wrap {{ overflow: hidden; border: 1px solid var(--line); border-radius: 8px; background: #fff; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; }}
        th {{ padding: 12px 16px; background: #f8faf7; color: #66736b; font-size: 10px; font-weight: 750; letter-spacing: .9px; text-transform: uppercase; }}
        td {{ padding: 14px 16px; border-top: 1px solid #edf0ec; font-size: 13px; vertical-align: top; }}
        tbody tr {{ animation: rise .35s both; }}
        tbody tr:hover {{ background: #f8fbf7; }}
        .tool-id {{ width: 90px; color: #7a867e; font-variant-numeric: tabular-nums; }}
        .tool-name {{ color: #25382e; font-weight: 700; }}
        .description {{ color: var(--muted); }}
        .quantity {{ width: 120px; color: var(--green); font-weight: 750; font-variant-numeric: tabular-nums; }}
        .price {{ width: 120px; color: var(--green); font-weight: 750; font-variant-numeric: tabular-nums; }}
        .empty {{ display: none; padding: 28px; color: var(--muted); text-align: center; }}
        footer {{ margin-top: 15px; color: var(--muted); font-size: 11px; text-align: right; }}
        @keyframes rise {{ from {{ opacity: 0; transform: translateY(5px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @media (max-width: 640px) {{
            main {{ padding-top: 32px; }}
            .summary {{ gap: 20px; justify-content: space-between; }}
            .metric {{ display: block; }}
            .metric span {{ display: block; margin-top: 2px; }}
            .toolbar {{ align-items: stretch; flex-direction: column; }}
            .search {{ width: 100%; }}
            .table-wrap {{ overflow-x: auto; }}
            table {{ min-width: 620px; }}
        }}
        @media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ animation-duration: .01ms !important; }} }}
    </style>
</head>
<body>
    <header class="topbar">
        <div class="brand"><span class="brand-mark" aria-hidden="true">T</span> ToolSet Inventory</div>
        <a class="api-link" href="/api/tools">View JSON <span aria-hidden="true">↗</span></a>
    </header>
    <main>
        <div class="eyebrow">Inventory overview</div>
        <h1>Tools</h1>
        <p class="subtitle">Your complete equipment catalog, at a glance.</p>
        <section class="summary" aria-label="Inventory summary">
            <div class="metric"><strong>{len(tools)}</strong><span>tools listed</span></div>
            <div class="metric"><strong>{total_quantity}</strong><span>total units</span></div>
            <div class="metric"><strong>{sum(tool.price for tool in tools):.2f}</strong><span>total value</span></div>
        </section>
        <section aria-labelledby="catalog-heading">
            <div class="toolbar">
                <h2 id="catalog-heading">Tool catalog</h2>
                <input class="search" id="tool-search" type="search" placeholder="Search tools or descriptions" aria-label="Search tools">
            </div>
            <div class="table-wrap">
                <table>
                    <thead><tr><th scope="col">ID</th><th scope="col">Tool</th><th scope="col">Description</th><th scope="col">Quantity</th><th scope="col">Price</th></tr></thead>
                    <tbody id="tool-rows">{tool_rows}</tbody>
                </table>
                <div class="empty" id="empty-state">No tools match your search.</div>
            </div>
            <footer id="result-count">Showing {len(tools)} tools</footer>
        </section>
    </main>
    <script>
        const search = document.getElementById("tool-search");
        const rows = [...document.querySelectorAll("#tool-rows tr")];
        const emptyState = document.getElementById("empty-state");
        const resultCount = document.getElementById("result-count");
        search.addEventListener("input", () => {{
            const query = search.value.trim().toLocaleLowerCase();
            let visible = 0;
            for (const row of rows) {{
                const matches = row.textContent.toLocaleLowerCase().includes(query);
                row.hidden = !matches;
                visible += Number(matches);
            }}
            emptyState.style.display = visible ? "none" : "block";
            resultCount.textContent = `Showing ${{visible}} of {len(tools)} tools`;
        }});
    </script>
</body>
</html>"""


@app.get("/api/tools")
def get_tools_json():
    return ToolsModel.FindToolList()
