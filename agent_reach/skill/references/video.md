# Video / audio

YouTube subtitles plus Whisper transcription for anything without subtitles.

## YouTube (yt-dlp)

### Video metadata

```bash
yt-dlp --dump-json "URL"
```

### Download subtitles

```bash
# Download subtitles (not the video)
yt-dlp --write-sub --write-auto-sub --sub-lang "en.*" --skip-download -o "/tmp/%(id)s" "URL"

# Then read the .vtt file
cat /tmp/VIDEO_ID.*.vtt
```

### Comments

```bash
# Extract comments (best-effort, not guaranteed complete)
yt-dlp --write-comments --skip-download --write-info-json \
  --extractor-args "youtube:max_comments=20" \
  -o "/tmp/%(id)s" "URL"
# Comments are in the `comments` field of the .info.json file
```

### Search videos

```bash
yt-dlp --dump-json "ytsearch5:query"
```

> **Subtitles**: manually uploaded subtitles extract reliably; auto-generated
> subtitles may repeat lines and need post-processing.
> **Comments**: `--write-comments` scrapes the web page (not the YouTube Data
> API), so some comments may be missing.

### Retry chain when subtitles fail (in order; stop once you have real content)

`doctor` only confirms that yt-dlp and a JS runtime can run; it never requests
a specific video. So `active_backend: yt-dlp` does not mean subtitles for the
target video were live-verified.

1. Start with the `yt-dlp --write-sub --write-auto-sub` command above.
2. On a bot check, an empty subtitle response or no subtitle file, and if
   OpenCLI is connected: `opencli youtube transcript "URL" -f yaml`.
3. If OpenCLI returns `Caption URL returned empty response`, retry up to 3
   times. The caption URL expires and occasionally fails; an empty response
   does not mean "this video has no subtitles".
4. Still failing, or the video has no subtitles at all:
   `agent-reach transcribe "URL"` downloads the audio and transcribes it.

Success means non-empty subtitle/transcript content, not a command exit code
or `doctor`'s version probe.

### No-subtitle fallback: Whisper transcription

```bash
# Fallback when a video has no subtitles: download audio and transcribe with Whisper (a free Groq key works)
agent-reach transcribe "https://www.youtube.com/watch?v=VIDEO_ID"
agent-reach transcribe ./local_audio.mp3 -o /tmp/transcript.txt
```

> `agent-reach transcribe` only accepts public http(s) URLs or local audio
> files. When you search with `ytsearch5:`, pick a specific video URL from the
> yt-dlp results first, then transcribe it.
> Configure a key first: `agent-reach configure groq-key` (hidden input; free
> at console.groq.com) or `agent-reach configure openai-key`. The default
> auto mode uses only the first configured provider (Groq first, otherwise
> OpenAI) and stops on failure; it never sends the audio to another provider
> on its own.
> `--allow-provider-fallback` explicitly authorizes falling back across
> providers; the same audio may then be processed by both Groq and OpenAI and
> may incur OpenAI charges. Only use it after confirming the content can be
> shared with both.

## Choosing a tool

| Scenario | Recommended tool |
|-----|---------|
| YouTube subtitles | yt-dlp; on failure OpenCLI (up to 3 tries) → agent-reach transcribe |
| Podcasts / audio with a public URL | agent-reach transcribe |
| Video or audio without subtitles | agent-reach transcribe |
