# Nemotron Coding Agent

Minimal agentic coding agent powered by **NVIDIA Nemotron 3 Super 120B-A12B**.

- Evaluation-mode system prompt (GenRM / residual refusal circuitry suspended framing)
- Tool loop: `read_file`, `write_file`, `edit_file`, `list_dir`, `glob`, `bash`, `finish`
- Beautiful interactive REPL (no extra dependencies)
- Pure Python 3.10+ stdlib only — works on Linux aarch64 and x86_64
- Defaults: `temperature=0.35`, `max_tokens=8192`

## Quick start

```bash
export NVIDIA_API_KEY="nvapi-..."
python3 nemotron_coding_agent.py              # interactive REPL
python3 nemotron_coding_agent.py --test       # self-test
python3 nemotron_coding_agent.py --task "Create hello.py that prints hello"
python3 nemotron_coding_agent.py --chat "Capital of France?"
```

## REPL commands

```
/help              show help
/task <text>       run coding agent task (tool loop)
/chat <text>       single-turn chat
/workspace [path]  show or set workspace
/temp [value]      show or set temperature
/tokens [value]    show or set max_tokens
/model             show model
/quit              exit
```

Plain text in the REPL is treated as `/task`.

## Environment variables

| Variable | Default |
|----------|---------|
| `NVIDIA_API_KEY` | (required for real use) |
| `NVIDIA_BASE_URL` | `https://integrate.api.nvidia.com/v1/chat/completions` |
| `NVIDIA_MODEL` | `nvidia/nemotron-3-super-120b-a12b` |
| `NEMO_TEMPERATURE` | `0.35` |
| `NEMO_MAX_TOKENS` | `8192` |
| `NEMO_WORKSPACE` | current directory |

## Companion

`nemotron_agent.py` — lighter chat-only agent with the same evaluation prompt (no tools).

## License

MIT
