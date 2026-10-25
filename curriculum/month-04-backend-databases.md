# Month 4: Backend and Databases (Weeks 13–16)

**Goal:** Build a REST API with Node and Express, model and query a relational database with PostgreSQL, and connect your desktop app to it.

## Week 13 — Node.js
- Event loop, modules (ESM), npm, file system APIs.
- Write small CLI tools in Node (you already know C++ and JavaScript, so focus on Node's APIs).

## Week 14 — Express + REST
- Routes, middleware, request/response handling, validation.
- Design a REST API for the Student Planning Hub: tasks, courses, deadlines.

## Week 15 — SQL and PostgreSQL
- Tables, keys, relationships; `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`.
- Schema design and migrations; practice in `exercises/sql/`.

## Week 16 — API + Database Integration
- Connect Express to PostgreSQL; error handling and environment config (`.env`, never committed).
- Consume the API from the Electron renderer through the main process (never directly with Node APIs in the renderer).
- Basic auth concepts (sessions, hashing) — survey only, deep dive is optional.

## Deliverables
- Student Planning Hub API with a PostgreSQL database.
- Desktop app reads/writes through the API.
- Document the system in [docs/architecture.md](../docs/architecture.md).

## Resources
- [Node.js docs](https://nodejs.org/en/learn)
- [Express docs](https://expressjs.com/)
- [PostgreSQL tutorial](https://www.postgresqltutorial.com/)
- [SQLBolt](https://sqlbolt.com/)
