from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/tools/{tool_id}")
def getTool(tool_id: int):
    # Simulate fetching tool data from a database or other source
    tools_data = {
        1: {"name": "Hammer", "brand": "ToolBrand", "price": 19.99},
        2: {"name": "Screwdriver", "brand": "ToolBrand", "price": 9.99},
        3: {"name": "Wrench", "brand": "ToolBrand", "price": 14.99},
    }

    tool = tools_data.get(tool_id)
    if tool is None:
        raise HTTPException(status_code=404, detail="Tool not found")
    
    return tool
