# Team coordination via Jinx (shared memory)

This team uses **Jinx**, a shared memory accessed through MCP tools
(`pull_context`, `scan_repo`, `push_intent`, `sync`, `mark_done`). Several
teammates each run their own Copilot agent against this same repo. Your job is to
**prevent duplicated effort and maximise reuse**. Your GitHub identity is filled in
automatically — never pass a user id.

## Hard rules — on EVERY feature/implementation request

0. **Jinx check goes FIRST.** Before you ask any clarifying question, propose a
   framework/library, outline an approach, or write any code, you MUST call
   `pull_context` AND `scan_repo` and relay both verdicts to the user. If the user
   asks to build something, your very first action is the Jinx check — not a question.

1. **Normalize, then pull.** Distill the request into a short capability phrase
   (e.g. "rate limiter for the API", not the whole sentence). Call
   `pull_context(intent=<phrase>)`, then `scan_repo(intent=<phrase>)` (it auto-detects
   this repo). Relay each returned `verdict`.

2. **Act on what you find:**
   - ♻ **reusable / merged work exists** → name the repo/PR and **reuse it as the
     reference** instead of rewriting. Offer to pull it in.
   - ⚠ **overlap / in-flight** (a teammate's open PR, branch, or announced intent) →
     name them and their branch, show the similarity, and **coordinate** rather than
     duplicate. Offer to build on their branch.
   - ✅ **neither** → say it's safe to build fresh, then proceed.

3. **Announce with `push_intent`** before substantial code (and again at milestones
   with updated `work_summary` / `files_touched`) so simultaneous teammates see you and
   the team dashboard stays live.

4. **Finish** with `mark_done(intent_id=..., pr_link=...)` when merged, so the work
   becomes reusable knowledge. Use `sync()` during long sessions.

## Style
Keep coordination messages short and concrete: who, what, where (repo/branch/PR),
similarity score, recommended action. **Never silently skip the Jinx check** —
coordination is the whole point.
