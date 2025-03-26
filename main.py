from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()

@app.post("/voice")
async def voice(request: Request):
    response = VoiceResponse()
    response.say("Hi Graeme, the system is working. This is just a test message.")
    return PlainTextResponse(str(response), media_type="application/xml")

@app.get("/")
async def root():
    return {"status": "live"}
if__name__== "__main__":
   import uvicorn
   import os
   port =
int(os.environ.get("PORT", 10000))
   uvicorn.run(app, host="0.0.0.0", port=port)
