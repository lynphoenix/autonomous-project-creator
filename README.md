# Autonomous Project Creator

An autonomous coding agent powered by Claude that can build complete applications from specification documents. This tool implements a two-agent pattern (initializer + coding agent) that works across multiple sessions to implement features systematically.

## Features

- **Autonomous Development**: Automatically builds applications from text specifications
- **Multi-Session Support**: Continues work across multiple sessions with progress tracking
- **Security Layers**: OS-level sandbox, filesystem restrictions, and bash command allowlist
- **Browser Automation**: Built-in Puppeteer integration for E2E testing
- **Flexible Configuration**: Support for custom models, API endpoints, and feature counts

## Quick Start

### Prerequisites

1. **Python 3.10+**
2. **Claude Code CLI** (latest version)
3. **Anthropic API Key**

### Installation

```bash
# Clone the repository
git clone https://github.com/lynphoenix/autonomous-project-creator.git
cd autonomous-project-creator

# Install Python dependencies
pip install -r requirements.txt
```

### Configuration

Set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

For custom API endpoints or models:

```bash
# Optional: Use custom base URL
export ANTHROPIC_BASE_URL=https://api.anthropic.com

# Optional: Specify model
export ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
```

Or create a `.env` file from the example:

```bash
cp .env.example .env
# Edit .env with your API key
```

### Usage

**Basic Usage:**

```bash
# Interactive spec creation (recommended for first time)
python create_app_spec.py

# Then run autonomous development
python autonomous_agent_demo.py --project-dir ./my_project
```

**Advanced Usage:**

```bash
# Use existing spec file
python autonomous_agent_demo.py --project-dir ./my_project

# Specify custom model
python autonomous_agent_demo.py --project-dir ./my_project --model claude-sonnet-4-5-20250929

# Limit iterations for testing
python autonomous_agent_demo.py --project-dir ./my_project --max-iterations 5
```

### Writing Specifications

Create your application specification in `prompts/app_spec.txt` following the guide in `prompts/APP_SPEC_GUIDE.md`.

Key elements:
- Clear project description
- Technology stack preferences
- P0/P1/P2 feature priorities
- Testing requirements
- UI design specifications

## Project Structure

```
autonomous-project-creator/
├── autonomous_agent_demo.py  # Main entry point
├── create_app_spec.py        # Interactive spec generator
├── agent.py                  # Agent session logic
├── client.py                 # Claude SDK client configuration
├── security.py               # Bash command allowlist
├── progress.py               # Progress tracking
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── README.md                 # This file
└── prompts/
    ├── APP_SPEC_GUIDE.md     # Spec writing guide
    ├── app_spec.txt          # Application specification template
    ├── initializer_prompt.md # First session prompt
    └── coding_prompt.md      # Continuation session prompt
```

## How It Works

### Two-Agent Pattern

1. **Initializer Agent (Session 1)**:
   - Reads `app_spec.txt`
   - Creates `feature_list.json` with test cases
   - Sets up project structure
   - Initializes git repository

2. **Coding Agent (Sessions 2+)**:
   - Picks up where previous session left off
   - Implements features systematically
   - Marks tests as passing
   - Commits progress

### Session Management

- Each session runs with fresh context
- Progress persisted via `feature_list.json` and git commits
- Auto-continues between sessions (3 second delay)
- Press `Ctrl+C` to pause; run same command to resume

## Configuration Options

### Command-Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--project-dir` | Project directory | `./autonomous_demo_project` |
| `--max-iterations` | Max agent iterations | Unlimited |
| `--model` | Claude model to use | From env or `claude-sonnet-4-5-2025029` |

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | Required |
| `ANTHROPIC_BASE_URL` | API base URL | `https://api.anthropic.com` |
| `ANTHROPIC_MODEL` | Model to use | `claude-sonnet-4-5-2025029` |
| `DISABLE_SANDBOX` | Disable sandbox (NOT recommended) | `false` |

## Security Model

This tool uses defense-in-depth security:

1. **OS-level Sandbox**: Isolated bash environment
2. **Filesystem Restrictions**: Operations limited to project directory
3. **Bash Allowlist**: Only specific commands permitted

See `security.py` for the complete command allowlist.

## Troubleshooting

### "Appears to hang on first run"
This is normal! The initializer agent is generating detailed test cases. Watch for `[Tool: ...]` output.

### "Command blocked by security hook"
The agent tried a command not in the allowlist. Add it to `ALLOWED_COMMANDS` in `security.py` if needed.

### "API key not set"
Ensure `ANTHROPIC_API_KEY` is exported:
```bash
echo $ANTHROPIC_API_KEY  # Should show your key, not empty
```

### ModuleNotFoundError: No module named 'claude_code_sdk'
Install dependencies:
```bash
pip install -r requirements.txt
```

## Server Deployment

### On 219 Server (Aliyun)

```bash
# Clone and setup
git clone https://github.com/lynphoenix/autonomous-project-creator.git
cd autonomous-project-creator
pip install -r requirements.txt

# Set your API key in environment or .env file
export ANTHROPIC_API_KEY='your-key-here'

# Run your project
python autonomous_agent_demo.py --project-dir ./my_project
```

### On H100 Server

Same as above - the tool is Python-based and works on any Linux server with Python 3.10+.

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation in `QUICKSTART.md`
- Review `prompts/APP_SPEC_GUIDE.md` for spec writing help
