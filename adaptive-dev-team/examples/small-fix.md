# Small Fix Example — Button Offset in Web UI
> **Hypothetical Example — not executed; illustrates team formation and workflow only.**
> **假设示例 — 未真实执行；仅用于说明团队组建与工作流。所有 checklist 与状态均为待验证项。**

**Progressive Disclosure: Small = minimal team, only when needed.**

---

## 1. Requirements (Always shown — minimal)
- **Issue:** Primary "Save" button is misaligned by ~12px on mobile viewport.
- **Fix target:** CSS `margin-top` offset on `.btn-primary`.
- **Acceptance:** Pixel-perfect alignment across 320px–1440px.

---

## 2. Spec (Only needed for non-trivial rules)
- Component: `components/Button/SaveButton.vue`
- Breakpoint: `@media (max-width: 768px)`
- Fix: Change `margin-top: 20px` → `margin-top: 8px`
- No database / backend / security changes required.

---

## 3. UX (Only when user-facing behavior changes)
- Before: Button overlaps nearby text on narrow screens.
- After: Clean vertical spacing preserved.

---

## 4. Skill → Team Adaptation (Auto-selected based on scope)
Because scope = **single file, no backend impact**:

- **Team:** Frontend Builder only — the single agent that edits the CSS.
- **Review:** Optional lightweight review pass. It is a **separate, non-independent review pass**
  (same agent/context, not an independent reviewer), so it is *not* equivalent to a real
  independent review.
- **Skipped:** Builder Lead, Architect, Planner, Integration, Specialists (Security / Performance /
  Accessibility / etc.), Acceptance Reviewer.
  > This list exists to *illustrate team shrinkage* in this example. It is **not** required runtime
  > output: a LIGHT task does not emit an `Architect: N/A` / `Planner: N/A` checklist. See
  > `workflows/light.md` and `workflows/core.md` for when a skip reason actually must be recorded.
- **Why Builder Lead is skipped:** Builder Lead is only activated when **≥2 active Builders** need
  coordination. One file edited by one Builder never reaches that threshold.

**Team activated only when:** multi-file change / **≥2 parallel Builders** (→ Builder Lead) /
new dependency / security boundary crossed.

---

## 5. Module: Frontend Builder
- File edited: `components/Button/SaveButton.vue`
- Diff: 1 line (margin-top: 20px → 8px)
- Verification: Manual viewport resize + screenshot

---

## 6. Integration (Only if integration points affected)
- N/A — isolated CSS change, no API / component contract change.

---

## 7. QA (Progressive — minimal for trivial fix)
- [ ] Visual regression: Button aligned on mobile viewport.
- [ ] Cross-browser (Chrome / Firefox / Safari mobile).
- [ ] Accessibility: Button still focusable, color contrast unchanged.

---

## 8. Security (Only when security boundary touched)
- N/A — no input validation / auth / data flow changes.

---

## 9. Review (Optional — separate non-independent pass)
- Optional lightweight review pass, to be performed after the fix. The reviewer shares the same
  agent/context — this is a **separate, non-independent review pass**, not equivalent to an
  independent review.
- Acceptance visual check: to be run (expected result only; not yet executed).

---

## 10. Acceptance
- [ ] Requirement met: Button aligned.
- [ ] Spec met: Margin corrected.
- [ ] UX met: No overlap.
- [ ] QA passed.
- **Status:** Expected end state (hypothetical) = accepted. Not verified — nothing in this example has
  actually been executed, so no item above may be marked done.

---

## Progressive Disclosure Note
- Full team (Builder Lead, Architect, Planner, Security, Integration, Acceptance Reviewer) was
  **not invoked** — scope did not justify it.
- Builder Lead stays inactive until **≥2 active Builders** exist.
- If this fix had required a new component library / design system change, Skill would have promoted
  to `examples/normal-feature.md` and activated Architect + Planner automatically.
