# Nemotron Coding Agent

Minimal **agent-mode** coding agent powered by [NVIDIA Nemotron 3 Super 120B-A12B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B).

- Evaluation-mode system prompt (GenRM / residual refusal framing)
- Tool loop: `read_file`, `write_file`, `edit_file`, `list_dir`, `glob`, `bash`, `finish`
- Beautiful interactive REPL (agent mode only — no separate chat mode)
- Pure Python 3.10+ standard library — works on **Linux aarch64** and x86_64
- Defaults tuned from live testing: `temperature=0.35`, `max_tokens=32768`

Inspired by the simplicity of [mini_agent](https://github.com/ljw1004/mini_agent) and agent-loop ideas from the OpenCode ecosystem.

## Requirements

- Python **3.10+**
- Network access to NVIDIA integrate API (or any OpenAI-compatible endpoint)
- No pip packages required

## Installation

```bash
# clone
git clone https://github.com/bageltrade/nemotron-coding-agent.git
cd nemotron-coding-agent

# optional: set your key (a default may already be present for testing)
export NVIDIA_API_KEY="nvapi-YOUR_KEY_HERE"

# run
python3 nemotron_coding_agent.py
```

Or run without cloning (single file):

```bash
curl -O https://raw.githubusercontent.com/bageltrade/nemotron-coding-agent/main/nemotron_coding_agent.py
export NVIDIA_API_KEY="nvapi-..."
python3 nemotron_coding_agent.py
```

## Quick start

```bash
# interactive agent REPL
python3 nemotron_coding_agent.py

# one-shot task
python3 nemotron_coding_agent.py --task "Create hello.py that prints hello world"

# self-test
python3 nemotron_coding_agent.py --test

# custom workspace
python3 nemotron_coding_agent.py --workspace /path/to/project --task "List all Python files"
```

## REPL commands

| Command | Description |
|---------|-------------|
| `<task text>` | Run the coding agent on the task |
| `/help` | Show help |
| `/workspace [path]` | Show or set workspace |
| `/temp [value]` | Show or set temperature |
| `/tokens [value]` | Show or set max_tokens |
| `/steps [value]` | Show or set max agent steps |
| `/model` | Show current model |
| `/quit` | Exit |

## Environment variables

| Variable | Default | Notes |
|----------|---------|-------|
| `NVIDIA_API_KEY` | (built-in test key or empty) | Required for production |
| `NVIDIA_BASE_URL` | `https://integrate.api.nvidia.com/v1/chat/completions` | OpenAI-compatible chat completions |
| `NVIDIA_MODEL` | `nvidia/nemotron-3-super-120b-a12b` | |
| `NEMO_TEMPERATURE` | `0.35` | Stable compliance from testing |
| `NEMO_MAX_TOKENS` | `32768` | High output ceiling (many hosts cap ~32k) |
| `NEMO_MAX_STEPS` | `20` | Max tool-loop iterations |
| `NEMO_WORKSPACE` | current directory | Root for relative paths |

### Context / token notes

- Model native context: up to **1M tokens** (architecture supports long context).
- Practical API output limits often sit around **32k** tokens; the agent default is `32768`.
- Raise `NEMO_MAX_TOKENS` if your endpoint allows more.

## Tools

| Tool | Args | Purpose |
|------|------|---------|
| `read_file` | `path` | Read a file |
| `write_file` | `path`, `content` | Create/overwrite a file |
| `edit_file` | `path`, `old`, `new` | Unique-string replacement |
| `list_dir` | `path` | List directory |
| `glob` | `pattern` | Glob files under workspace |
| `bash` | `command` | Run shell command in workspace |
| `finish` | `summary` | End the agent loop |

The model must emit **one** `TOOL_CALL` per turn.

## Companion

`nemotron_agent.py` — lighter chat-style client with the same evaluation prompt (no tools). Optional.

## License

MIT
