from fastapi import FastAPI, Request, Form
from twilio.twiml.voice_response import VoiceResponse
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/voice")
async def voice():
    resp = VoiceResponse()
    gather = resp.gather(input="speech", action="/process", timeout=5)
    gather.say("Hi Graeme, speak truth.")
    return PlainTextResponse(str(resp), media_type="application/xml")

@app.post("/process")
async def process(request: Request):
    form = await request.form()
    msg = form.get("SpeechResult", "").strip()

    if not msg:
        resp = VoiceResponse()
        resp.say("I didn’t hear anything.")
        return PlainTextResponse(str(resp), media_type="application/xml")

    # Gemma’s brain — upgrade this anytime
    reply = gemma_thinks(msg)

    resp = VoiceResponse()
    resp.say(reply)
    return PlainTextResponse(str(resp), media_type="application/xml")

def gemma_thinks(input_text):
    # This is her brain — edit here to upgrade
    if "zion" in input_text.lower():
        return "Zion shall be redeemed in power. D&C 103:15."
    return f"You said: {input_text}. I’m listening."

@app.get("/")
async def root():
    return {"status": "live"}
