from fastapi import FastAPI, Request, Form
from fastapi.responses import PlainTextResponse
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()

@app.post("/voice")
async def voice():
    resp = VoiceResponse()
    gather = resp.gather(input="speech", action="/process", timeout=5)
    gather.say("Hi Graeme, speak truth.")
    return PlainTextResponse(str(resp), media_type="application/xml")

@app.post("/process")
async def process(SpeechResult: str = Form(...)):
    msg = SpeechResult.strip()
    if not msg:
        resp = VoiceResponse()
        resp.say("I didn’t hear anything.")
        return PlainTextResponse(str(resp), media_type="application/xml")
    reply = "Zion shall be redeemed in power. Doctrine and Covenants section 103 verse 15."
    resp = VoiceResponse()
    resp.say(reply)
    return PlainTextResponse(str(resp), media_type="application/xml")

@app.get("/")
async def root():
    return {"status": "Live"}
