For FastAPI, I recommend a lightweight MVC structure:

ToolsInquiryAPI/
├── main.py                 # Application setup
├── controllers/
│   └── tools_controller.py # API routes
├── models/
│   └── tool.py             # Tool data model/schema
├── repositories/
│   └── tool_repository.py  # SQLite/database queries
└── services/
    └── tool_service.py     # Business logic

The request flow would be:

    HTTP request
  -> Controller
  -> Service
  -> Repository
  -> SQLite
  -> Controller response