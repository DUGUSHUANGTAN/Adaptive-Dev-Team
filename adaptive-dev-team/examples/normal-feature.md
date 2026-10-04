# Normal Feature Example — Dark Mode Toggle
> **Hypothetical Example — not executed; illustrates team formation and workflow only.**
> **假设示例 — 未真实执行；仅用于说明团队组建与工作流。所有 checklist 与状态均为待验证项。**

**Progressive Disclosure: Normal = full team, all sections shown when needed.**

---

## 1. Requirements
- Add a dark/light theme toggle to the application settings page.
- Persist user preference across sessions.
- No breaking changes to existing UI.

---

## 2. Spec
- **Frontend:** Add toggle component, CSS variable theming, `localStorage` persistence.
- **Backend:** Optional — store user theme preference on profile (if multi-device sync required).
- **Database:** Optional — `users.theme` column (if sync required).
- **API:** `GET /api/profile` returns `theme`; `PATCH /api/profile` accepts `theme`.

---

## 3. UX
- Toggle placement: Settings page header, right-aligned.
- Visual states: Light icon / Dark icon, animated transition (200ms).
- Accessibility: `aria-pressed`, keyboard support, prefers-color-scheme fallback.

---

## 4. Architect
- **Tech selection:** CSS custom properties (`--bg`, `--fg`) + `data-theme` attribute on `<html>`.
- **No new dependencies** — native `localStorage`, native fetch.
- **Integration points:** Profile API (existing), existing UI components (theme-aware).

---

## 5. Planner
- **Breakdown:**
  1. Frontend: Toggle component (2 days)
  2. Frontend: Theming system + persistence (1 day)
  3. Backend: Profile API extension (1 day)
  4. QA: Cross-browser + accessibility (0.5 day)
- **Total:** ~4.5 days

---

## 6. Builder Lead
- Assigns: Frontend Builder (toggle + theming), Backend Builder (API).
- Key decisions:
  - Use CSS variables over precompiled CSS (runtime switchable).
  - Default to `prefers-color-scheme` if no stored preference.

---

## 7. Module: Frontend Builder
- **Toggle component:** `ThemeToggle.vue` — button + `aria-pressed` + `click` handler.
- **Theming system:** `theme.css` with `:root[data-theme="dark"]` variables.
- **Persistence:** `localStorage.setItem('theme', ...)` + read on mount.

---

## 8. Module: Backend Builder
- **API:** `PATCH /api/profile` — accepts `theme: 'light' | 'dark'`.
- **Validation:** Enum check, default to `'system'` if invalid.
- **Database:** `users.theme` column (nullable, defaults to `NULL`).

---

## 9. Module: Database Builder
- **Migration:** Add `theme VARCHAR(10) NULL` to `users`.
- **Index:** Not needed (single-column, low cardinality).

---

## 10. Integration
- **Contract:** `GET /api/profile` returns `{ theme: 'light' | 'dark' | 'system' }`.
- **Flow:** App reads theme on load → sets `data-theme` → persists on toggle.
- **Tests:** Unit (toggle logic), integration (API contract), E2E (toggle persists across reload).

---

## 11. QA
- [ ] Toggle works on click, keyboard, and touch.
- [ ] Theme persists after page reload.
- [ ] Theme persists after browser restart (localStorage).
- [ ] prefers-color-scheme respected when no stored preference.
- [ ] No regressions in existing UI.

---

## 12. Security (Only when auth / data boundary touched)
- **Input validation:** Enum check on `theme` field — prevents injection.
- **Auth:** Profile endpoint already requires authentication.
- **Data:** No PII / sensitive data in theme preference.

---

## 13. Review (planned — separate, non-independent pass)
- **Code review:** Toggle logic, API contract, migration — planned, not yet performed.
- **Design review:** Toggle placement, transition timing — planned.
- **Accessibility review:** `aria-pressed`, keyboard nav, contrast — planned.
- These are **separate, non-independent review passes** within the same team, not independent
  third-party reviews.

---

## 14. Acceptance
- [ ] Requirement: Toggle present and functional.
- [ ] Spec: All API / DB changes implemented.
- [ ] UX: Placement, animation, accessibility met.
- [ ] QA: All test cases passed.
- [ ] Security: No new vulnerabilities.
- **Status:** Expected end state (hypothetical) = accepted. Not verified — this example was never
  executed, so every checklist item stays `[ ]`.

---

## Progressive Disclosure Note
- **Security** was included because the feature touches a user-data API boundary.
- **Architect / Planner / Integration** were activated because scope spans frontend + backend + database.
- If this had been **only a frontend toggle** (no backend sync), Architect and Planner would have been skipped, and Security would have been reduced to a checklist.
- Compare with `examples/small-fix.md` (minimal team) and `examples/web-app.md` (full-stack team).