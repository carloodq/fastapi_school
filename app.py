from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gen_reply_api import gen_reply

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins instead of ["*"]
    allow_credentials=True,
    allow_methods=["*"],  # You can specify a list of allowed methods instead of ["*"]
    allow_headers=["*"],  # You can specify a list of allowed headers instead of ["*"]
)

class ChatRequest(BaseModel):
    userId: str
    context: str
    message: str

class ChatResponse(BaseModel):
    botMessage: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Basic validation (can be more complex based on actual requirements)
    if not request.userId or not request.message or not request.context:
        raise HTTPException(status_code=400, detail="Missing or invalid parameters")

    # Dummy response logic
    bot_response, _ = gen_reply(request.message, "Rispondi basandoti su queste informazioni:\n" + str(request.context))

    return ChatResponse(botMessage=bot_response)

# To run the application, save this script as app.py and run the following command:
# uvicorn app:app --reload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
