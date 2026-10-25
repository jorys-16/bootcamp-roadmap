# Decisions (ADRs)

Short architecture decision records. One per meaningful choice; newest at the bottom.

## Template
```markdown
## ADR-NNN: Title
- Date:
- Status: proposed | accepted | superseded by ADR-XXX
- Context: what forced this decision
- Decision: what we chose
- Consequences: what becomes easier/harder
```

## ADR-001: Electron for the Student Planning Hub desktop client
- Status: accepted
- Context: the hub needs to be a desktop app; skills are web-first (React/TS) after Month 3, with C++ as the base language.
- Decision: Electron over native WinUI, because the roadmap already teaches React + TypeScript, Electron is cross-platform, and the official docs/tutorials are excellent.
- Consequences: larger binary and memory footprint than native; acceptable for a student planner.

## ADR-002: PostgreSQL over MongoDB
- Status: accepted
- Context: need a database in Month 4.
- Decision: PostgreSQL — relational fits structured course/task data, and SQL is a more transferable skill.
