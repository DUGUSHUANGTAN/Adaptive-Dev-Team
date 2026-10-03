# Small Fix Example — Button Offset in Web UI
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
- **Architect:** Skipped — no architecture change.
- **Planner:** Skipped — task < 30 min, no breakdown needed.
- **Builder Lead:** Active — assigns the single frontend builder.
- **Module team:** Only Frontend Builder active.
- **Integration / QA / Security / Review:** Minimal touch-point checks.

**Full team activated only when:** multi-file change / new dependency / security boundary crossed.

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

## 9. Review (Always — minimal)
- Peer review: Confirmed single-line diff, no unintended side effects.
- Acceptance: Passed visual check.

---

## 10. Acceptance
- [ ] Requirement met: Button aligned.
- [ ] Spec met: Margin corrected.
- [ ] UX met: No overlap.
- [ ] QA passed.
- **Status:** ✅ Accepted

---

## Progressive Disclosure Note
- Full team (Architect, Planner, Security, Integration) was **not invoked** — scope did not justify it.
- If this fix had required a new component library / design system change, Skill would have promoted to `normal-feature` and activated Architect + Planner automatically.
