# Module Contract Specification (`/spec`)

As outlined in the [AgriPreneurs Code and Maintenance Guide](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/code-and-maintenance-guide.md), every module and shared service must publish a clear, versioned contract in `spec/`.

## Why Contracts Matter
1. **One Job, One Contract:** Other Tribes can build on top of your module without reading internal code.
2. **Never Touch Database Internals:** Modules communicate only via **Contract Calls** (REST/gRPC/function APIs) and **Domain Events** (fire-and-forget message emissions).
3. **Additive Changes vs Breaking Changes:** Keep contracts stable. Additive fields don't break consumers; renamings or removals require a major version bump (`/v2/`).

---

## What Goes Here
- `contract.json` / `openapi.yaml`: Your REST or JSON-RPC API specification.
- `events.json`: Schemas for domain events emitted by your service (e.g. `farmer.registered.v1`, `price.alert_sent.v1`, `crop.photo_diagnosed.v1`).
