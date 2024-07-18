from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gen_reply_api import gen_reply

app = FastAPI()

class ChatRequest(BaseModel):
    userId: str
    message: str

class ChatResponse(BaseModel):
    botMessage: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Basic validation (can be more complex based on actual requirements)
    if not request.userId or not request.message:
        raise HTTPException(status_code=400, detail="Missing or invalid parameters")

    # Dummy response logic
    bot_response, _ = "hey", "" #gen_reply(request.message)

    return ChatResponse(botMessage=bot_response)

# To run the application, save this script as app.py and run the following command:
# uvicorn app:app --reload



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
