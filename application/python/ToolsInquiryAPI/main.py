from fastapi import FastAPI

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
