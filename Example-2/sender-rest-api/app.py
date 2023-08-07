from fastapi import FastAPI
from constants import rabbit_mq
from pydantic import BaseModel
import uvicorn

app = FastAPI(docs_url='/docs', redoc_url=None)


class MessageRequest(BaseModel):
    Message:str

@app.get("/")
def home():
    return {"message":"Service running"}

@app.post("/api/v1/send-to-queue")
def send_to_queue(message: MessageRequest):
    '''
        This pushes parameters into massage queue
        to be picked up by the consumer

        Parameters:
        - Message: your message
        
        Example:
        ```
        {
            "message": "Payload is sent to quque please wait"
        }
        ```
    '''
    print(rabbit_mq)
    
    payload = message.dict()
    
    rabbit_mq.send_message(payload=payload)

    return {"message": "Payload is sent to quque please wait"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
