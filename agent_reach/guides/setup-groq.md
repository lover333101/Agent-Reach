# Groq Whisper Setup Guide

## What it does
When a video or podcast has no subtitles, Groq's Whisper API transcribes the audio. Groq offers a free tier.

## Steps the Agent can do automatically

1. Check whether it is already configured:
```bash
agent-reach doctor | grep -i "transcribe"
```

2. When the user provides a key, save it through the hidden prompt (never put the key in command arguments):
```bash
agent-reach configure groq-key
```

3. Test (optional), reading the key from the environment rather than typing it into the command:
```bash
curl -s https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -o /dev/null -w "%{http_code}"
```
200 = working

## Steps the user must do manually

Tell the user:

> Speech-to-text for videos needs a Groq API key (free).
>
> Steps:
> 1. Open https://console.groq.com
> 2. Sign up with a Google account or email
> 3. Click "API Keys" on the left
> 4. Click "Create API Key"
> 5. Copy the generated key and send it to me
>
> Groq's free tier is plenty for everyday use.

## After the Agent receives the key

1. Save it: `agent-reach configure groq-key` (hidden input)
2. Test that the API works
3. Report back: "✅ Speech-to-text is on! Now I can pull content from videos even when they have no subtitles."
