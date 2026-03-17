# skill-guard-action

> Reusable GitHub Action for [skill-guard](https://github.com/vaibhavtupe/skill-guard) — quality gate for Anthropic AgentSkills.

## Usage

```yaml
- uses: vaibhavtupe/skill-guard-action@v1
  with:
    command: validate      # validate | secure | conflict | check | test
    path: ./my-skill       # path to skill directory
```

### Embeddings-enabled usage

```yaml
- uses: vaibhavtupe/skill-guard-action@v1
  with:
    command: conflict
    path: ./skills/my-skill
    against: ./skills
    embeddings: "true"
```

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `command` | No | `check` | Command to run: `validate`, `secure`, `conflict`, `check`, `test` |
| `path` | Yes | — | Path to skill directory |
| `against` | No | `""` | Skills dir or catalog for conflict detection |
| `endpoint` | No | `""` | OpenAI-compatible agent endpoint for eval tests |
| `config` | No | `""` | Path to `skill-guard.yaml` |
| `format` | No | `text` | Output format: `text`, `json`, `markdown` |
| `fail-on-warning` | No | `false` | Exit non-zero on warnings |
| `version` | No | latest | skill-guard version to pin |
| `python-version` | No | `3.11` | Python version |
| `embeddings` | No | `false` | Install embeddings deps (torch + skill-guard[embeddings]) |

## Outputs

| Output | Description |
|---|---|
| `exit-code` | Exit code from skill-guard |
| `report-path` | Path to report file (when `format=markdown`) |

## Exit Codes

- `0` success
- `1` validation/security failures  
- `2` warnings only (when `fail_on_warning` is false)
- `3` config error
- `4` parse error
- `5` hook script failure
- `6` health check timeout

## Full workflow example

```yaml
name: Skill Quality Gate
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: vaibhavtupe/skill-guard-action@v1
        with:
          command: check
          path: ./skills/my-skill
```
