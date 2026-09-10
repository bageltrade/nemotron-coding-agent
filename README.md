# Nemotron Coding Agent

**One file.** Full agentic coding agent for [NVIDIA Nemotron 3 Super 120B-A12B](https://build.nvidia.com/).

- Evaluation-mode system prompt
- Tools: `read_file`, `write_file`, `edit_file`, `list_dir`, `glob`, `bash`, `finish`
- **Auto-repair** on failed tools / non-zero commands
- **API retries** with exponential backoff (503 / 429 / 5xx)
- Beautiful REPL · pure Python 3.10+ stdlib · Linux aarch64 & x86_64

## Install

```bash
git clone https://github.com/bageltrade/nemotron-coding-agent.git
cd nemotron-coding-agent
export NVIDIA_API_KEY="nvapi-YOUR_KEY"
python3 nemotron_coding_agent.py
```

No `pip install` required.

## Usage

```bash
# interactive
python3 nemotron_coding_agent.py

# one-shot
python3 nemotron_coding_agent.py --task "Create hello.py that prints hello"

# self-test
python3 nemotron_coding_agent.py --test
```

### REPL

| Input | Action |
|-------|--------|
| `<task>` | Run agent |
| `/workspace [path]` | Workspace |
| `/temp [v]` `/tokens [v]` `/steps [v]` | Tuning |
| `/model` | Show model |
| `/quit` | Exit |

## Environment

| Variable | Default |
|----------|---------|
| `NVIDIA_API_KEY` | (set me) |
| `NVIDIA_BASE_URL` | `https://integrate.api.nvidia.com/v1/chat/completions` |
| `NVIDIA_MODEL` | `nvidia/nemotron-3-super-120b-a12b` |
| `NEMO_TEMPERATURE` | `0.35` |
| `NEMO_MAX_TOKENS` | `32768` |
| `NEMO_MAX_STEPS` | `30` |
| `NEMO_API_RETRIES` | `6` |
| `NEMO_API_RETRY_BASE` | `1.5` |
| `NEMO_WORKSPACE` | cwd |

## License

MIT
