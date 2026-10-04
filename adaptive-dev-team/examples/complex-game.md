# Complex Game Example — Physics-Based Puzzle Platformer
> **Hypothetical Example — not executed; illustrates team formation and workflow only.**
> **假设示例 — 未真实执行；仅用于说明团队组建与工作流。所有 checklist、状态与性能指标均为待验证项；FPS / 延迟 / 体积等为 target 目标值，非实测结果。**

**Progressive Disclosure: Complex Game = full team expanded + specialist roles activated by Skill.**

---

## 1. Requirements
A 2D physics-based puzzle platformer with procedural level generation.

### Core Features
- Physics simulation (rigid bodies, joints, destruction) via Box2D / Matter.js
- Procedural level generation using Perlin noise + constraint solver
- Player character with double-jump, wall-slide, and magnet ability
- Puzzle mechanics: movable blocks, switches, portals, time freeze zones
- 50+ handcrafted tutorial + challenge levels + infinite procedural mode
- Multiplayer co-op (2 players) via WebRTC peer connection
- Leaderboards + replay sharing (JSON replay files)
- Custom level editor (in-game) with export/import
- Cutscenes (animated sequences) using frame-based animation

### Non-functional Requirements (targets — not measured)
- Target: 60 FPS on target hardware (integrated graphics minimum)
- Target: < 50ms physics step time for 500+ active bodies
- Target: replay file size < 5KB / minute of gameplay
- Cross-platform (Web, desktop via Electron, mobile web responsive)

---

## 2. Spec

| Area | Technology | Justification |
|------|-----------|---------------|
| Engine | Phaser 3 + Matter.js physics | Native Web + proven physics engine |
| Rendering | WebGL (Phaser 3 renderer) + custom shaders (post-processing) | Performance + visual effects |
| Audio | Web Audio API + Howler.js | Spatial audio for co-op |
| Networking | WebRTC data channels + simple signaling server (WebSocket) | Peer-to-peer for co-op, low server cost |
| State | Zustand (frontend) + Redux (editor mode) | Different state needs |
| Build | Vite + Rollup (library build for level editor plugin) | Fast development + modular output |
| Testing | Playwright E2E + custom physics replay verification | Game-specific testing |

---

## 3. UX
- **Gameplay loop:** Player enters level → solves physics puzzle → collects key → unlocks portal.
- **UI:** Minimal HUD (health, ability cooldown, timer). Cutscenes overlay with skip option.
- **Co-op:** Split-screen (desktop), stacked vertical (mobile). Shared physics world.
- **Accessibility:** Configurable physics speed (slow mode), color-blind mode, keyboard-only play.
- **Feedback loop:** Particle effects on interaction, audio cues for puzzle state changes, haptic feedback (mobile).

---

## 4. Architect
### System Diagram
```
[Level Generator] → [Level Data (JSON)]
    ↓
[Physics Engine] ← Player Input → [Animation System]
    ↓
[Rendering Pipeline] → [Post-Processing] → Canvas
    ↓
[Audio Engine] ← Game Events
    ↓
[WebRTC P2P] ↔ [Peer Client]
```

### Key Decisions
- **Physics-first design:** All objects are physics bodies — level design starts with physics constraints.
- **Replay system:** Record player input + random seed, not full physics state — deterministic replay.
- **Co-op architecture:** One player hosts physics simulation; other sends inputs only.
- **Level editor:** In-game, real-time — uses same physics engine as gameplay.

---

## 5. Planner

| Sprint | Module Focus | Key Deliverables | Duration |
|--------|--------------|------------------|----------|
| 1 | Core engine + physics | Player movement, physics world, basic rendering | 2 weeks |
| 2 | Level design + generation | Procedural generator, handcrafted level loader | 2 weeks |
| 3 | Game mechanics | Double-jump, magnet, portals, switch mechanics | 2 weeks |
| 4 | UI / HUD / cutscenes | HUD overlay, cutscene engine, accessibility options | 2 weeks |
| 5 | Multiplayer co-op | WebRTC connection, host authority, replay sync | 2 weeks |
| 6 | Level editor + replay | Editor UI, replay recording / playback, export | 2 weeks |
| 7 | Polish + performance | 60 FPS optimization, audio, visual effects | 2 weeks |

**Total:** 14 weeks (3.5 months) — 2 developers + 1 specialist (audio / visual effects).

---

## 6. Builder Lead
- **Sprint structure:** 2-week sprints, demo at end of each sprint.
- **Pairing:** Game mechanics developer + Physics specialist paired for mechanics (Sprint 3).
- **Milestones (planned):** M1 (Sprint 2): Physics + basic movement playable; M2 (Sprint 4): 5 handcrafted levels complete; M3 (Sprint 5): Co-op multiplayer working; M4 (Sprint 7): public beta target — a goal, not a released state.

---

## 7. Module: Game Engine / Physics Builder
- **Physics:** Matter.js engine configured with 16 iterations / step, 60 Hz tick rate.
- **Custom constraints:** Magnet ability creates temporary constraint; time freeze freezes all bodies except player.
- **Optimization:** Spatial partitioning (quadtree) — only update bodies within camera viewport + 2-screen buffer.
- **Replay:** Record input events with timestamp + random seed; replay by feeding same inputs to deterministic physics.

---

## 8. Module: Level Design / Procedural Generator Builder
- **Procedural algorithm:** 1) Perlin noise terrain; 2) Place puzzle elements using constraint solver; 3) Verify solvability via A* pathfinding; 4) Retry with new seed if unsolvable (max 100 attempts).
- **Handcrafted levels:** JSON format defining body shapes, constraints, event triggers.
- **Level validation:** In-editor physics simulation confirms solvability before export.

---

## 9. Module: Graphics / Rendering Builder
- **Pipeline:** Phaser 3 WebGL renderer → custom post-processing shader (bloom, chromatic aberration, vignette).
- **Animation:** Sprite atlas for character animations (idle, run, jump, fall, double-jump, wall-slide, magnet). Frame-based cutscenes using same atlas system.
- **Visual effects:** Particle emitter for block destruction, portal glow (animated shader uniform).

---

## 10. Module: Audio / Sound Builder
- **Sound design:** Procedural audio — synthesized based on impact velocity and material (no pre-recorded samples for physics impacts).
- **Music:** Dynamic layering — intensity increases with time pressure; additional layer during magnet ability.
- **Spatial audio:** Web Audio 3D panning for co-op — each player's position determines audio source direction.

---

## 11. Module: Network / Multiplayer Builder
- **Architecture:** Host-authoritative physics; peer clients send input packets only.
- **WebRTC data channel:** Binary input packets (< 20 bytes / tick).
- **Signaling server:** Minimal WebSocket server (only for connection setup, not gameplay data).
- **Replay sharing:** Replay files stored locally; share via WebRTC P2P file transfer or export to JSON.

---

## 12. Module: Editor / Tools Builder
- **In-game editor:** Toggle between Play / Edit mode. In Edit mode, click to place bodies, drag to resize, right-click for properties.
- **Properties panel:** Per-object: type, physics properties (mass, friction, restitution), event triggers.
- **Validation:** Real-time physics simulation in editor mode — level must be solvable before save.
- **Export / Import:** JSON format, versioned.

---

## 13. Module: AI / Procedural Behavior Builder
- **AI opponent (optional mode):** Simple AI calculates shortest path to key, executes same movement sequence. Used for replay ghost / leaderboards.
- **Procedural difficulty:** Difficulty score = path length / available tools. Score > 0.8 → hard level.
- **Adaptive difficulty:** If player fails 3 times, next procedural level is easier.

---

## 14. Integration
### Integration Points
- **Physics ↔ Rendering:** Physics step updates body positions; rendering reads body positions each frame. If physics lags, rendering skips frame but physics continues.
- **Editor ↔ Game:** Editor uses same physics engine; save produces level JSON; game reads and validates before loading.
- **Multiplayer ↔ Physics:** Input packets → applied to physics → physics step → state broadcast → clients apply state changes.
- **Audio ↔ Physics:** Impact events from physics trigger audio generation; audio engine uses same timestep as physics.

---

## 15. QA
- [ ] Physics: 60 FPS at 500 bodies, no physics divergence over 5-minute replay
- [ ] Gameplay: All 50 handcrafted levels solvable; procedural generator produces 100% solvable levels (to be tested over 1000 generations)
- [ ] Multiplayer: Co-op session stable for 30 minutes, input latency < 100ms
- [ ] Replay: Replay plays back identically (pixel-perfect) for deterministic levels
- [ ] Performance: Mobile browser achieves 30 FPS minimum
- [ ] Accessibility: Slow mode, keyboard-only play, screen reader labels
- [ ] Editor: Level saved / loaded / validated without data loss

---

## 16. Security (Only when network / user data boundary crossed)
- **WebRTC:** No direct P2P data without signaling handshake. Input packets contain only player actions.
- **Replay files:** JSON only — validated with JSON Schema before import. No script injection possible.
- **Level editor export:** Same validation path. User content never executed as code.
- **Leaders / sharing:** Replay files shared via P2P — no server storage of user data.

---

## 17. Review (planned — separate, non-independent passes)
- **Game design review:** Playtest with 5 external testers (Sprint 4 + Sprint 7) — planned.
- **Physics review:** Replay comparison to validate determinism — planned, not yet run.
- **Performance review:** Frame-time profiling with Chrome DevTools — planned; no performance claim
  is verified here.
- **Accessibility review:** Screen reader + slow mode to be validated — planned.
- **Security review:** Replay import / WebRTC handshake to be checked by Security specialist — planned.
- These in-team reviews are **separate, non-independent review passes**, not independent third-party
  reviews.

---

## 18. Acceptance (expected end state — not verified)
- [ ] Requirements: All core + non-functional targets met
- [ ] Spec: Engine, physics, graphics, audio, network, editor all implemented per spec
- [ ] UX: Playtested, accessibility validated, UI responsive
- [ ] QA: All checklist items pass
- [ ] Security: Replay / network / user content validated
- [ ] Review: Design + physics + performance + accessibility signed off
- **Status:** Expected (hypothetical) = accepted with public beta ready. **Not verified** — this
  example was never executed; no beta was released and nothing here is confirmed.

---

## Progressive Disclosure Note
- **Specialist roles activated by Skill:** Game Design (level generation, mechanics), Physics (custom constraints), Graphics (post-processing shaders), Audio (procedural sound), AI (procedural behavior), Network (P2P co-op).
- These roles are **not present** in `examples/web-app.md` or `examples/small-fix.md` — Skill activates them automatically when the project type / scope requires them.
- **Security** was included because multiplayer networking and user-generated content (replays, custom levels) cross security boundaries.
- For a **simple 2D arcade game** (no multiplayer, no user content, no procedural generation), Architect / Planner / Security / AI / Network roles would be **skipped**, reducing this to a `examples/normal-feature.md`-class template.
