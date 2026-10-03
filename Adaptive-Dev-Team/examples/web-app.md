# Web App Example — Task Management Dashboard
**Progressive Disclosure: Web App = full stack, full team, all sections detailed when needed.**

---

## 1. Requirements
A full-stack web application for teams to create, assign, and track tasks.

### Core Features
- User authentication (signup, login, password reset)
- Task CRUD (create, read, update, delete)
- Task assignment to team members
- Task status (Todo, In Progress, Review, Done)
- Filtering / search by status, assignee, label, deadline
- Real-time updates via WebSocket
- Responsive design (desktop + mobile)
- Export tasks to CSV

### Non-functional Requirements
- Sub-200ms server response for task list (<100 tasks)
- 99.9% uptime SLA
- GDPR-compliant data handling

---

## 2. Spec
| Area | Detail |
|------|--------|
| Frontend | React 18, TypeScript, Tailwind CSS, Zustand (state) |
| Backend | Node.js 20, Express, TypeScript |
| Database | PostgreSQL 16, Prisma ORM |
| Real-time | Socket.IO on Redis pub/sub |
| Auth | bcrypt + JWT, email via SendGrid |
| Hosting | Docker + Docker Compose, nginx reverse proxy |
| Monitoring | Prometheus + Grafana, Sentry |

---

## 3. UX
- **Dashboard:** Kanban board, cards show title, assignee avatar, due date.
- **Task editor:** Modal with form (title, description, assignee, labels, due date, status).
- **Sidebar:** Navigation (Dashboard, Teams, Settings).
- **Mobile:** Collapsible sidebar, swipe to delete.
- **Accessibility:** WCAG 2.1 AA, keyboard navigation, ARIA labels.

---

## 4. Architect
```
Browser → nginx → [Frontend (React)]
                → [Backend (Express API)]
                   → PostgreSQL (tasks, users)
                   → Redis (pub/sub, session cache)
                   → SendGrid (email)
```
- PostgreSQL for relational data; Redis for session + pub/sub; Prisma ORM.
- Socket.IO with Redis adapter for scaling.

---

## 5. Planner
| # | Task | Module | Est. |
|---|------|--------|------|
| 1 | DB schema + migration | Database | 1d |
| 2 | Auth API | Backend | 1.5d |
| 3 | Session + JWT in Redis | Backend | 0.5d |
| 4 | Task CRUD API | Backend | 1.5d |
| 5 | WebSocket events | Backend | 1d |
| 6 | Frontend auth + routing | Frontend | 1.5d |
| 7 | Kanban dashboard | Frontend | 2d |
| 8 | Task editor modal | Frontend | 1d |
| 9 | Export CSV | Both | 0.5d |
| 10 | E2E tests (Cypress) | QA | 1d |
| 11 | Security review | Security | 0.5d |
| 12 | Performance tuning | Backend | 0.5d |
**Total:** ~12 days (3 sprints, 2 devs)

---

## 6. Builder Lead
- 2-week sprints, 3 sprints total.
- Pairing on API contract design (Week 1).
- Key decisions: Kanban state server-side; optimistic updates; WebSocket fallback to polling.

---

## 7. Module: Frontend Builder
- React 18 + TypeScript + Tailwind + Zustand.
- Components: KanbanBoard, TaskCard, LoginForm, SignupForm, TaskEditorModal, Sidebar.
- State: Zustand stores for auth/tasks; WebSocket hook.
- API client: Axios with JWT interceptor.

---

## 8. Module: Backend Builder
- Node 20 + Express + TypeScript.
- Endpoints: `/api/auth/*`, `/api/tasks` (CRUD), `/api/users`, `/api/teams`.
- Real-time: Socket.IO broadcasting task changes to room subscribers.
- Cache: Redis session tokens + 5-min task TTL.
- Validation: zod schema validation.

---

## 9. Module: Database Builder
- Schema: users, teams, team_members, tasks, labels.
- Indexes: Composite `(team_id, status)` for board queries.
- Migrations: Prisma Migrate, version-controlled.

---

## 10. Integration
- **API Contract:** `GET/POST/PATCH/DELETE /api/tasks` with query filters.
- **Real-time:** `taskUpdated` / `taskCreated` events → frontend updates store; fallback polling every 30s.
- **Tests:** Jest + Supertest (backend); React Testing Library + Cypress (frontend); OpenAPI 3 spec.

---

## 11. QA
- [ ] Auth flow (signup → login → reset)
- [ ] Task CRUD (all roles)
- [ ] Real-time propagation (2 tabs)
- [ ] Mobile responsive (iOS / Android Chrome)
- [ ] Keyboard + screen reader (NVDA / VoiceOver)
- [ ] CSV export integrity
- [ ] Performance: 100 tasks load < 200ms
- [ ] Dark mode toggle + persistence

---

## 12. Security
- SQL injection: Prisma parameterized.
- XSS: React auto-escaping + CSP headers.
- Auth: bcrypt (12 rounds), JWT (15min access / 7d refresh rotation).
- Rate limit: express-rate-limit on `/auth/*`.
- Secrets: `.env` excluded; vault in prod.
- Compliance: GDPR — `DELETE /api/users/:id` erases PII in 24h.
- Scan: `npm audit`, Prisma query engine.

---

## 13. Review
- Architecture review: Diagram + stack validated.
- Code review: PR requires 1 frontend + 1 backend reviewer.
- UX review: Designer validates against wireframes.
- Security review: Security specialist checks OWASP.
- Performance review: Benchmarking on staging.

---

## 14. Acceptance
- [ ] Requirements met (core + non-functional)
- [ ] Spec deployed to staging with green tests
- [ ] UX validated (designer sign-off)
- [ ] QA all pass
- [ ] Security scan clean, OWASP mitigated
- [ ] All reviews approved
- **Status:** ✅ Accepted — deployed

---

## Progressive Disclosure Note
- Full team activated (Architect, Planner, Security) because scope spans frontend + backend + database + auth.
- **Security** included because auth + PII crosses a security boundary.
- For frontend-only version (static mock), Architect/Backend/Database/Security would be skipped → `normal-feature`.
