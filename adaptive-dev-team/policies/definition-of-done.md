# Definition of Done (Quantified)

Completion requires EVIDENCE per workflow depth:

**Light / Small:**
- [ ] Builder output verified (test / review / demo)
- [ ] No syntax/build errors
- [ ] Final delivery to user

**Standard:**
- [ ] Spec met (all criteria checked)
- [ ] QA checks pass (functional + regression)
- [ ] Code review complete
- [ ] Internal handoff / delivery per `protocols/handoff.md`

**Advanced / Production / Large:**
- [ ] Requirements verified (acceptance criteria all met with evidence)
- [ ] Integration checks pass (cross-module)
- [ ] Security review (only if triggered)
- [ ] Performance review (only if triggered)
- [ ] Accessibility review (only if triggered)
- [ ] Final acceptance report (Pass / Partial / Fail with evidence)
- [ ] Final delivery only after required acceptance; then archived

Agent says Done WITHOUT evidence = NOT complete.

Verification is performed by the reviewer the selected workflow requires. Specialist reviews join only when a trigger in `policies/quality-gates.md` applies — a Specialist is not a mandatory gate for all verification.
