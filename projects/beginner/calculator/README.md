# Calculator

**Level:** Beginner  
**Suggested stack:** HTML, CSS, JavaScript

## Problem statement

Perform predictable calculations with keyboard-friendly controls. Build for a real person with constrained time, data, and device capability—not an imaginary perfect connection.

## Product objectives

- Deliver a clear, accessible core user journey.
- Preserve user work during interruption where appropriate.
- Demonstrate deliberate data, security, performance, and deployment choices.

## User personas

- **Primary user:** needs to complete the core task quickly on a mobile browser.
- **Maintainer:** needs understandable code, documented setup, and safe operational controls.

## Functional requirements

Document user stories, acceptance criteria, validation rules, empty/loading/error states, and a data ownership model before coding.

## Non-functional and UI/UX requirements

Use semantic HTML, keyboard access, readable contrast, responsive layouts, small assets, and a measured performance budget. Do not require video submissions or a premium device.

## Suggested architecture and database design

Draw client, server/API, authentication, data, and storage boundaries. Define entities, identifiers, relationships, indexes, retention, and migration plan. For BaaS, document RLS or Security Rules; never place service-role/admin credentials in browser code.

## API, security, and offline requirements

Validate on the server boundary, authorize every record access, protect secrets with environment variables, and handle failed requests. Cache safe read data; save drafts locally; queue only idempotent operations with stable IDs and a visible retry/conflict state.

## Implementation milestones

1. Discovery, PRD, wireframe, and architecture decision.
2. Accessible static core journey and test plan.
3. Data/API integration with authorization tests.
4. Offline/resilience, performance, accessibility, and security review.
5. Deployment, documentation, demo, and retrospective.

## Testing and deployment requirements

Test critical paths, validation, authorization, keyboard navigation, slow/offline behaviour, and at least one small viewport. Deploy from a reproducible build; document environment variables by name only and provide a rollback/recovery note.

## Evaluation rubric

| Area | Weight |
| --- | ---: |
| Problem fit and requirements traceability | 15% |
| Functionality and data correctness | 25% |
| Code architecture and maintainability | 20% |
| Security, accessibility, resilience, performance | 25% |
| Tests, documentation, and presentation | 15% |

## Extension challenges

Add role-aware workflows, robust conflict resolution, a local-first sync queue, audit history, analytics that respect privacy, or an import/export path. Explain the trade-off before adding scope.
