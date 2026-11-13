#!/usr/bin/env python3
"""Generate the maintained Markdown learning materials for GeekInk Web Engineering.

The curriculum data below is intentionally specific: it is the source of truth for the
100 lessons, project briefs, and cohort documents. Run this script after changing it,
then run validate_curriculum.py.
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    ("Introduction to Web Engineering", "Web foundations", [
        ("The web, the internet, and a useful mental model", "internet protocols, the World Wide Web, and URLs", "Map a familiar web request from browser to server and back."),
        ("Clients, servers, and requests", "client-server architecture and request/response boundaries", "Draw a request path for a school noticeboard."),
        ("Browsers and the rendering pipeline", "parsing HTML and CSS, JavaScript execution, and DevTools", "Inspect and change a page safely with DevTools."),
        ("Domains, DNS, and hosting", "domain names, DNS resolution, IP addresses, and hosting", "Trace the records needed to point a domain at a site."),
        ("HTTP, HTTPS, and status codes", "methods, headers, status codes, TLS, and secure transport", "Use the Network panel to identify a failed request."),
        ("Development environment and terminal", "VS Code, Node.js, a browser, and command-line navigation", "Create a local workspace and run a static server."),
        ("Git: local history and recovery", "repositories, commits, branches, and meaningful checkpoints", "Make a reversible checkpoint for a web page."),
        ("GitHub collaboration", "remotes, pull requests, issues, and code review", "Open a practice pull request with a review checklist."),
        ("Developer tools and debugging", "Elements, Console, Sources, Network, and accessibility inspectors", "Diagnose a broken image and a JavaScript error."),
        ("Foundation checkpoint: publish a web profile", "planning, repository hygiene, and static deployment", "Publish a small profile with a README and recovery notes."),
    ]),
    ("HTML5 and Semantic Web Development", "HTML and accessible content", [
        ("HTML documents and the document tree", "doctype, html, head, body, metadata, and nesting", "Create a valid document with a meaningful title."),
        ("Text content with meaning", "headings, paragraphs, emphasis, quotations, and document outline", "Turn unstructured text into an understandable article."),
        ("Links and navigation", "relative URLs, absolute URLs, landmarks, and skip links", "Build keyboard-friendly site navigation."),
        ("Lists, tables, and structured data", "when lists and data tables communicate meaning", "Create an accessible course timetable table."),
        ("Images, audio, and video", "alt text, captions, responsive media, and attribution", "Add media with useful alternatives."),
        ("Forms and user input", "labels, input types, fieldsets, names, and form submission", "Build a student registration form."),
        ("Native validation and helpful errors", "constraints, required fields, patterns, and error messaging", "Validate a form without hiding errors from screen readers."),
        ("Semantic page regions", "header, nav, main, article, section, aside, and footer", "Refactor a div-heavy page into semantic landmarks."),
        ("Accessibility foundations", "keyboard access, names, roles, values, contrast, and progressive enhancement", "Audit a page with keyboard-only navigation."),
        ("SEO and HTML platform APIs", "metadata, structured discoverability, dialogs, details, and progressive features", "Ship an accessible event page with metadata."),
    ]),
    ("CSS3 and Responsive Web Design", "CSS and responsive layout", [
        ("CSS rules, cascade, and inheritance", "selectors, declarations, cascade order, and inherited properties", "Style a semantic page without fighting the cascade."),
        ("Selectors and specificity", "selector matching, specificity, and maintainable naming", "Resolve a conflicting style with the simplest selector."),
        ("The box model", "content, padding, border, margin, sizing, and overflow", "Build consistent card spacing with box-sizing."),
        ("Colour, typography, and design tokens", "readability, font stacks, relative units, and custom properties", "Define a small accessible visual system."),
        ("Display, flow, and positioning", "block, inline, normal flow, relative, absolute, sticky, and fixed", "Position a notification without breaking layout."),
        ("Flexible one-dimensional layouts", "Flexbox axes, wrapping, alignment, and gap", "Build a responsive navigation and card row."),
        ("Two-dimensional layouts with Grid", "tracks, minmax, auto-fit, areas, and intrinsic sizing", "Build a dashboard grid without device-specific hacks."),
        ("Mobile-first responsive design", "fluid sizing, breakpoints, touch targets, and content priority", "Make a page useful at 320px before enhancing it."),
        ("Media queries and responsive media", "media features, prefers-reduced-motion, container-aware thinking, and images", "Respect user motion preferences."),
        ("Transitions, animation, and CSS checkpoint", "transitions, keyframes, performance-friendly properties, and restraint", "Deliver a responsive landing page with accessible motion."),
    ]),
    ("JavaScript Programming", "JavaScript foundations", [
        ("JavaScript execution and values", "scripts, strict mode, variables, primitives, and expressions", "Write and inspect small programs in the console."),
        ("Variables, types, and conversions", "let, const, strings, numbers, booleans, null, undefined, and coercion", "Normalize form values without surprising conversions."),
        ("Operators, comparisons, and decisions", "operators, equality, truthiness, conditionals, and guard clauses", "Choose validation messages from user input."),
        ("Loops and repetition", "for, while, for...of, iteration, and avoiding infinite loops", "Render repeated tasks from a small data set."),
        ("Functions and parameters", "declarations, expressions, parameters, return values, and pure functions", "Extract calculation logic from UI code."),
        ("Arrays and collection thinking", "indexes, mutation, iteration, and collection operations", "Build a list filter without duplicating code."),
        ("Objects and modeling data", "properties, methods, references, and nested data", "Model a learner profile and render it safely."),
        ("Scope, closures, and debugging", "lexical scope, closures, call stacks, and breakpoints", "Explain why a handler retains a value."),
        ("The DOM as a programming interface", "querying, creating, updating, and removing elements", "Build a dynamic task list with semantic elements."),
        ("Events and interactive forms", "event listeners, delegation, default behaviour, and form events", "Implement accessible form feedback and a mini app."),
    ]),
    ("Advanced JavaScript and Browser Engineering", "Browser engineering", [
        ("Modern JavaScript syntax", "template literals, optional chaining, nullish coalescing, and concise syntax", "Refactor safely while preserving behaviour."),
        ("Destructuring, spread, and rest", "immutable updates, destructuring, rest parameters, and shallow copies", "Update a UI state object without accidental mutation."),
        ("Array methods and data pipelines", "map, filter, reduce, find, sort, and non-mutating patterns", "Transform API-like data into view models."),
        ("Objects, prototypes, and defensive data", "object utilities, prototypes, ownership, and safe property access", "Normalize incomplete records before rendering."),
        ("Modules and application boundaries", "import, export, dependency direction, and browser modules", "Split a task app into cohesive modules."),
        ("Errors and failure-aware interfaces", "throw, try/catch/finally, Error objects, and user-safe error states", "Add an error boundary pattern to vanilla JavaScript."),
        ("Promises and the event loop", "pending, fulfilled, rejected, microtasks, chaining, and concurrency", "Sequence dependent work and handle a failure."),
        ("Async/await and Fetch", "async functions, HTTP failure checks, cancellation, Fetch API, and JSON", "Fetch, validate, and render public data."),
        ("Browser storage", "localStorage, sessionStorage, serialization, quotas, and privacy", "Persist a draft without storing secrets."),
        ("IndexedDB, service workers, and offline UX", "structured local data, caching, manifests, queues, retries, and browser limits", "Build an offline draft flow with an honest sync state."),
    ]),
    ("TypeScript and Professional JavaScript Engineering", "TypeScript", [
        ("Why TypeScript?", "static checking, compilation, tsconfig, and gradual adoption", "Add a strict TypeScript check to a small JavaScript app."),
        ("Primitive types, arrays, tuples, and literals", "annotations, inference, readonly data, tuples, and literal unions", "Model a safe task priority field."),
        ("Objects, interfaces, and type aliases", "structural typing, optional properties, interfaces, and aliases", "Describe a learner record without `any`."),
        ("Function types and reusable contracts", "parameter and return types, callbacks, overload alternatives, and void", "Type a validator and its result."),
        ("Union and intersection types", "discriminated unions, intersections, and exhaustive handling", "Model loading, success, empty, and error states."),
        ("Generics", "type parameters, constraints, reusable data containers, and inference", "Write a typed API-result helper."),
        ("Narrowing and type guards", "typeof, in, instanceof, predicates, and runtime validation", "Safely handle unknown JSON."),
        ("Utility types and enums alternatives", "Partial, Pick, Omit, Record, satisfies, and string unions", "Create a safe update payload."),
        ("Async and API response typing", "Promise types, unknown, decoding, validation, and error contracts", "Type a fetch layer without trusting the network."),
        ("Modules, testing, and TypeScript checkpoint", "project boundaries, linting, tests, and maintainable organization", "Convert a browser project into a typed, tested module."),
    ]),
    ("React.js Engineering", "React", [
        ("React's model and JSX", "declarative UI, JSX, rendering, and Vite development", "Render a component from data."),
        ("Components, props, and composition", "single responsibility, props, children, and component boundaries", "Compose a reusable course card."),
        ("State and event handling", "useState, event handlers, immutable updates, and derived state", "Build an interactive counter with clear state."),
        ("Conditional UI and lists", "conditional rendering, keys, empty states, and list updates", "Render an accessible filtered list."),
        ("Controlled forms", "controlled inputs, validation, submission, and focus management", "Build a robust task form."),
        ("Effects and data synchronization", "useEffect, dependencies, cleanup, fetching, and race conditions", "Fetch data while handling cancellation and errors."),
        ("Refs, memoization, and performance", "useRef, useMemo, useCallback, profiling, and when not to optimize", "Fix an avoidable render cost after measuring it."),
        ("Context and state boundaries", "Context API, provider design, local versus shared state, and testability", "Add a theme or session context without global sprawl."),
        ("Custom hooks and routing", "custom hook contracts, React Router, nested routes, and URL state", "Create a reusable local-storage hook and routes."),
        ("React architecture and testing", "feature boundaries, error boundaries, React Testing Library, and user-focused tests", "Ship a tested React mini application."),
    ]),
    ("Next.js Full-Stack Development", "Next.js App Router", [
        ("React versus Next.js", "framework responsibilities, rendering, routing, and App Router setup", "Create a Next.js application and explain the difference."),
        ("App Router structure", "app directory, pages, layouts, route groups, and colocated files", "Design a route tree for a learning platform."),
        ("Server and Client Components", "server-first rendering, client boundaries, serialization, and interactivity", "Move interactivity to the smallest client component."),
        ("Routing and dynamic segments", "links, params, search params, dynamic routes, and notFound", "Build a course detail route from a slug."),
        ("Data fetching and caching", "server fetching, cache behaviour, revalidation, and request failure", "Fetch a catalogue with an explicit freshness policy."),
        ("Route Handlers and API design", "HTTP methods, validation, responses, and server-only secrets", "Implement a small validated Route Handler."),
        ("Server Actions and mutations", "forms, server actions, validation, optimistic UI, and mutation safety", "Submit a form with server-side validation."),
        ("Loading, errors, and resilience", "loading.tsx, error.tsx, retry, not-found states, and graceful failure", "Design stateful feedback for a route."),
        ("Metadata, fonts, and images", "Metadata API, Open Graph, next/font, next/image, and accessibility", "Add accurate page metadata and optimized imagery."),
        ("Deployment and Next.js checkpoint", "environment variables, builds, observability, and performance budgets", "Deploy a documented App Router application."),
    ]),
    ("Backend-as-a-Service and Data Engineering", "BaaS and data", [
        ("Backend fundamentals before BaaS", "HTTP APIs, validation, authentication, authorization, and trust boundaries", "Trace what happens between browser, API, and database."),
        ("Relational data and SQL", "tables, rows, keys, joins, normalization, constraints, and transactions", "Design a course-enrolment schema and query it."),
        ("PostgreSQL design and indexes", "relationships, query plans, indexes, migrations, and data integrity", "Choose an index from an access pattern, not a guess."),
        ("Supabase architecture", "Postgres, Auth, Storage, Realtime, CLI, migrations, and client boundaries", "Connect a sample app without exposing privileged credentials."),
        ("Supabase Auth and Row Level Security", "identity, sessions, RLS policies, ownership checks, and service-role safety", "Write and test an ownership policy for notes."),
        ("Supabase data, storage, realtime, and Edge Functions", "CRUD, buckets, subscriptions, server functions, and secure validation", "Build a protected upload and document its policy."),
        ("Firebase architecture and Authentication", "Firebase SDK, Auth providers, client-server limits, and Emulator Suite", "Run an Auth flow against local emulators."),
        ("Firestore, Realtime Database, and data models", "documents, collections, denormalization, queries, listeners, and offline cache", "Model courses in Firestore and explain trade-offs."),
        ("Firebase Storage, Functions, and Security Rules", "Storage, callable/HTTP functions, rules, validation, and least privilege", "Test a rule that isolates each learner's files."),
        ("Supabase versus Firebase integration lab", "SQL versus documents, security, cost, realtime, offline behaviour, and lock-in", "Implement and compare a user/course feature in both platforms."),
    ]),
    ("Production Web Engineering and Capstone", "Production and capstone", [
        ("Full-stack architecture and capstone planning", "requirements, boundaries, data flow, ADRs, and threat modeling", "Choose a capstone scope with measurable outcomes."),
        ("Authentication and authorization", "sessions, roles, ownership, authorization checks, and secure redirects", "Document and test an authorization matrix."),
        ("Web security essentials", "XSS, CSRF, injection, secrets, dependencies, headers, and input validation", "Perform a focused security review."),
        ("Frontend and component testing", "unit tests, React Testing Library, fixtures, accessibility assertions, and test value", "Add tests for a critical user flow."),
        ("Integration and end-to-end testing", "contract tests, browser automation, test data, and failure paths", "Test a sign-in-to-save journey."),
        ("Web performance engineering", "Core Web Vitals, profiling, bundle analysis, caching, images, and budgets", "Measure then improve a real bottleneck."),
        ("Accessibility auditing", "WCAG-oriented checks, keyboard journeys, semantic checks, and assistive technology", "Record and fix accessibility findings."),
        ("SEO, deployment, and CI/CD", "production builds, deployment previews, checks, rollback, and release notes", "Automate quality checks before deployment."),
        ("Monitoring, documentation, and handover", "logs, error tracking concepts, runbooks, README quality, and maintenance", "Write an operations and recovery guide."),
        ("Capstone presentation and engineering review", "demo storytelling, evidence, peer review, reflection, and next steps", "Present a production-ready application and defend its decisions."),
    ]),
]

def put(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(text).strip() + "\n", encoding="utf-8")

def lesson(day, module, track, title, concepts, action):
    examples = {
        1: ("html", '<a href="/courses">Browse courses</a>\n<!-- The browser requests this resource using HTTP. -->'),
        2: ("html", '<main><article><h1>Community workshop</h1><p>Bring your questions.</p></article></main>'),
        3: ("css", ':root { --space: 1rem; }\n.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); gap: var(--space); }'),
        4: ("js", 'form.addEventListener("submit", (event) => {\n  event.preventDefault();\n  const data = new FormData(form);\n  console.log(data.get("title"));\n});'),
        5: ("js", 'const response = await fetch("/api/courses");\nif (!response.ok) throw new Error(`Request failed: ${response.status}`);\nconst courses = await response.json();'),
        6: ("ts", 'type LoadState<T> = { status: "loading" } | { status: "ready"; data: T } | { status: "error"; message: string };'),
        7: ("tsx", 'function SaveButton() {\n  const [saved, setSaved] = useState(false);\n  return <button aria-pressed={saved} onClick={() => setSaved(!saved)}>{saved ? "Saved" : "Save"}</button>;\n}'),
        8: ("tsx", 'export default async function Page({ params }: { params: Promise<{ slug: string }> }) {\n  const { slug } = await params;\n  return <h1>{slug}</h1>;\n}'),
        9: ("sql", 'alter table public.notes enable row level security;\ncreate policy "owners read own notes" on public.notes for select to authenticated\nusing ((select auth.uid()) = user_id);'),
        10: ("tsx", 'await user.type(screen.getByLabelText(/task/i), "Study offline caching");\nawait user.click(screen.getByRole("button", { name: /save/i }));\nexpect(screen.getByText(/saved locally/i)).toBeVisible();'),
    }
    language, code = examples[module]
    return f'''# Day {day:03}: {title}

**Module:** {module:02} — {track}  
**Build thread:** Community Learning Hub, a small application students improve throughout the program.

## Learning objectives

- Explain {concepts} in plain language and identify its engineering trade-offs.
- Apply the concept in a small, observable change rather than copying an unexplained recipe.
- Record one assumption, one failure path, and one accessibility or low-resource consideration.

## Prerequisites

Complete the previous day and keep its work in Git. Use the browser and local tools already installed; do not block progress on a cloud account or a paid service.

## Concept explanation

Today focuses on **{concepts}**. Start with the user-facing behaviour, then locate the boundary that makes that behaviour possible: browser, UI, network, server, or data store. Good engineering makes the normal path clear and makes failure understandable. Name the data entering the boundary, validate it, and decide what a user sees if it is unavailable.

## Practical examples

For the Community Learning Hub, {action.lower()} Keep the first implementation deliberately small: use one meaningful name, one visible state, and one assertion you can verify in DevTools or a test. Prefer semantic HTML and stable, local sample data before adding remote dependencies.

```{language}
{code}
```

Explain each line before expanding it. A real application must not treat an absent value, a network failure, and an unauthorized request as the same condition.

## Step-by-step implementation

1. Write a one-sentence acceptance criterion for the behaviour you will change.
2. Create a branch or local checkpoint named `day-{day:03}`.
3. Implement the smallest version of the concept in the Community Learning Hub.
4. Test the expected path, an empty or invalid input, and a failure/interruption path.
5. Inspect the result with the relevant browser, TypeScript, test, or network tool.
6. Commit a concise explanation of what changed and why.

## Hands-on exercises

1. Complete the guided build above with your own content or data.
2. Change one input deliberately and explain the observed output.
3. Add a visible loading, empty, error, or success state appropriate to this feature.

## Mini challenge

Extend the feature for a learner with a slow or unreliable connection. Preserve unsent input where useful, avoid duplicate actions, and make the current state honest. Document one browser or platform limitation you discovered rather than promising unsupported background work.

## Expected output

A small working feature, a readable commit, and a short note showing the normal and failure paths. The result should be usable by keyboard and should not require a fast connection to understand its essential content.

## Assessment criteria

| Criterion | Weight |
| --- | ---: |
| Correct use of today’s concept | 35% |
| Clear, maintainable implementation | 25% |
| Failure, validation, and edge-case handling | 20% |
| Accessibility and low-resource decisions | 10% |
| Evidence and reflection | 10% |

## Common mistakes

- Starting from a framework snippet without being able to explain the browser or server work beneath it.
- Treating a successful network response as proof that the data is valid or authorized.
- Hiding errors in the console instead of giving the user a useful next step.
- Testing only on a wide screen and only while connected.

## Additional learning resources

- [MDN Web Docs](https://developer.mozilla.org/)
- [Web.dev Learn](https://web.dev/learn/)
- [Offline-first web engineering](../../../docs/offline-first-web-engineering.md)
- [Low-resource development](../../../docs/low-resource-development.md)

## Submission instructions

Use the [submission template](../../../task/submission-template.md). Include the module/day, repository or patch link, one screenshot or written verification, tests run, connectivity condition tested, and one lesson learned. Screenshots and source code are accepted when a video upload is impractical.
'''

def module_readme(number, title, outcome, days):
    rows = "\n".join(f"| {number * 10 - 10 + i:03} | [{name}](day-{number * 10 - 10 + i:03}/) | {concepts} |" for i, (name, concepts, _) in enumerate(days, 1))
    return f'''# Module {number:02}: {title}

## Outcome

{outcome}. Complete each daily lesson, then submit the module checkpoint with a README, evidence of testing, and reflection.

| Day | Lesson | Focus |
| ---: | --- | --- |
{rows}

## Module checkpoint

Integrate the final three days into a small, accessible Community Learning Hub milestone. Explain the user problem, decisions, test evidence, and an offline or low-resource consideration.
'''

def project(name, level, summary, stack):
    slug = name.lower().replace(" ", "-").replace("/", "-")
    return f'''# {name}

**Level:** {level}  
**Suggested stack:** {stack}

## Problem statement

{summary} Build for a real person with constrained time, data, and device capability—not an imaginary perfect connection.

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
'''

def main():
    # Root and shared documentation
    put(ROOT / "README.md", '''# GeekInk Web Engineering

**100 Days. 100 Builds. Production-minded web engineers.**

GeekInk Innovations Ltd — *Builders Who Leave a Mark.*

## Mission

GeekInk Web Engineering is a practical 100-day curriculum for people moving from web fundamentals to production-ready full-stack applications. It teaches the web beneath the tools: semantic HTML, CSS, JavaScript, TypeScript, React, modern Next.js App Router, data systems, Supabase, Firebase, security, testing, deployment, and offline-first thinking.

## Start here

1. Read the [student guide](docs/student-guide.md) and [environment setup](docs/environment-setup.md).
2. Begin with [Day 001](curriculum/module-01/day-001/).
3. Build, test, commit, and submit work using the [task guide](task/README.md).
4. Use the [capstone package](student-engineering-project/) for the final project.

## Curriculum

| Module | Days | Focus |
| --- | ---: | --- |
| 01 | 001–010 | Web engineering foundations |
| 02 | 011–020 | Semantic HTML, accessibility, SEO |
| 03 | 021–030 | CSS, responsive design, motion |
| 04 | 031–040 | JavaScript programming and DOM |
| 05 | 041–050 | Async JavaScript, browser APIs, offline |
| 06 | 051–060 | TypeScript and maintainable systems |
| 07 | 061–070 | React engineering and testing |
| 08 | 071–080 | Next.js App Router full-stack development |
| 09 | 081–090 | Backend-as-a-Service and data engineering |
| 10 | 091–100 | Production practices and capstone |

See the complete [curriculum index](curriculum/README.md), [projects](projects/), and [documentation hub](docs/index.md).

## Engineering standard

Fundamentals first. Build practically. Engineer for everyone. Every learner considers accessibility, security, performance, maintainability, and unreliable connectivity—not as optional polish, but as engineering constraints.

## Legacy material

The original six-week course materials remain in `week1/`, `week2/`, and `Pdf/` for historical reference. The 100-day pathway above is the active cohort curriculum.

## Quality checks

```bash
python3 scripts/validate_curriculum.py
python3 scripts/validate_links.py
```

## License

[CC BY 4.0](LICENSE). Keep attribution when adapting course material.
''')
    put(ROOT / "LICENSE", '''Creative Commons Attribution 4.0 International

This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy, visit https://creativecommons.org/licenses/by/4.0/.
''')
    put(ROOT / "curriculum/README.md", "# 100-Day Curriculum\n\nTen modules, ten days each. Follow them in order; later modules assume earlier concepts.\n\n" + "\n".join(f"- [Module {n:02}: {t}](module-{n:02}/)" for n, (t, _, _) in enumerate(MODULES, 1)))
    for m, (title, outcome, days) in enumerate(MODULES, 1):
        put(ROOT / f"curriculum/module-{m:02}/README.md", module_readme(m, title, outcome, days))
        for i, (title2, concepts, action) in enumerate(days, 1):
            day = (m-1)*10+i
            put(ROOT / f"curriculum/module-{m:02}/day-{day:03}/README.md", lesson(day, m, title, title2, concepts, action))

    docs = {
      "index.md": "# Documentation Hub\n\n- [Student guide](student-guide.md)\n- [Instructor guide](instructor-guide.md)\n- [Environment setup](environment-setup.md)\n- [Roadmap](web-development-roadmap.md)\n- [Assessment rubric](assessment-rubric.md)\n- [Projects](project-guidelines.md)\n- [Capstone](capstone-guidelines.md)\n- [Offline-first](offline-first-web-engineering.md)\n- [Low-resource development](low-resource-development.md)\n- [Troubleshooting](troubleshooting.md)\n",
      "student-guide.md": "# Student Guide\n\nLearn in order, build daily, and keep small Git checkpoints. Read each lesson, implement the exercise, test normal and failure paths, then submit evidence. Ask for help with a minimal reproduction and what you expected versus observed. Source code and screenshots are valid evidence when connectivity makes video unsuitable.\n",
      "instructor-guide.md": "# Instructor Guide\n\nOpen each session by connecting the day to the prior build. Demonstrate a small working slice, then coach reasoning rather than providing completed solutions. Review requirements, accessibility, failure paths, commits, and reflection. Sample work on modest devices and intermittent connectivity; grade evidence, not bandwidth. Use the rubric consistently and document any accommodation.\n",
      "environment-setup.md": "# Environment Setup\n\nInstall Node.js 20.9 or later, Git, VS Code, and a current browser. Verify with `node --version`, `npm --version`, and `git --version`. On Windows, use PowerShell or Git Bash; on macOS/Linux, use a terminal. Use `nvm`, `fnm`, or the platform's supported version manager to keep Node versions per project. Install project dependencies from each lockfile with `npm ci` (or the documented package manager), copy `.env.example` to `.env.local`, and never commit secrets.\n\nCreate a Next.js app with `npx create-next-app@latest`; use the App Router and confirm current defaults in the [official installation guide](https://nextjs.org/docs/app/getting-started/installation). Register Firebase web apps and use the modular SDK following [Firebase's official setup guide](https://firebase.google.com/docs/web/setup). Supabase CLI v3 changed local/hosted defaults, so run `supabase --help` and check the [changelog](https://supabase.com/changelog.md) before cohort commands. Cache dependencies after a successful install, keep local copies of docs, and commit before power interruptions.\n",
      "web-development-roadmap.md": "# Web Development Roadmap\n\nThe sequence is deliberate: web foundations → semantic HTML → CSS → JavaScript → browser/async systems → TypeScript → React → Next.js → backend/data services → production capstone. React never substitutes for JavaScript fluency, and BaaS never substitutes for understanding HTTP, authorization, and data modeling.\n",
      "assessment-rubric.md": "# Assessment Rubric\n\n| Dimension | Weight | Evidence |\n| --- | ---: | --- |\n| Conceptual understanding | 20% | Explanation and decisions |\n| Functionality | 25% | Acceptance criteria and test evidence |\n| Engineering quality | 20% | Structure, types, validation, Git |\n| Accessibility, security, resilience | 20% | Audits and failure paths |\n| Documentation and reflection | 15% | README, submission, learning notes |\n\nAssess as emerging, developing, proficient, or exemplary. A visually attractive product cannot pass if it exposes secrets, excludes keyboard users, or loses important work on failure.\n",
      "learning-resources.md": "# Learning Resources\n\nPrefer official documentation: MDN, web.dev, TypeScript Handbook, React, Next.js, Supabase, Firebase, W3C/WAI, and GitHub Docs. Download material during reliable connectivity for offline study. Re-check framework and platform commands against their official documentation before teaching them.\n",
      "project-guidelines.md": "# Project Guidelines\n\nEvery project begins with a problem statement, users, requirements, success measures, data model, threat model, test plan, and deployment plan. Keep scope small enough to test. A backend service is a trust boundary: browser code has public configuration only; privileged credentials belong in server-side environments.\n",
      "capstone-guidelines.md": "# Capstone Guidelines\n\nUse the student engineering project package. A capstone must solve a meaningful problem, include an accessible core flow, authorization-aware data access, documented testing, deployment instructions, and an offline or degraded-network strategy. Present what works, what fails safely, and what you would improve.\n",
      "offline-first-web-engineering.md": "# Offline-First Web Engineering\n\nOffline-first means the core experience remains honest and useful without assuming a request can finish. Cache safe reads with a Service Worker and Cache API; persist drafts or structured local state in IndexedDB; show `Saved locally`, `Pending sync`, `Synced`, or `Needs attention`. Queue only idempotent mutations with an operation ID, retry deliberately, and define a conflict rule. Background Sync is not uniformly available, so provide a foreground retry path and never promise invisible delivery. Do not cache private data blindly; define logout and retention behaviour.\n",
      "low-resource-development.md": "# Low-Resource Development\n\nDesign mobile-first, ship small images, lazy-load nonessential work, reduce requests, avoid dependency bloat, and test on modest hardware. Cache packages and documentation after a successful online setup. Use Git commits as recovery points; keep local backups and a short resume checklist for unexpected shutdowns. Build and test locally before consuming paid cloud resources.\n",
      "troubleshooting.md": "# Troubleshooting\n\nStart with the smallest reproducible case. Check versions, lockfile, terminal output, browser Console and Network panels, and environment-variable names (never share values). For build failures, restore the last known-good commit and install from the lockfile. For authorization failures, verify the user identity, resource ownership, and RLS/Security Rule—not just whether a request returns data.",
      "implementation-progress.md": "# Implementation Progress\n\n- [x] Inspected existing GeekInk curriculum patterns and legacy web material\n- [x] Designed the 10-module, 100-day web pathway\n- [x] Authored 100 daily lesson documents with required teaching sections\n- [x] Added exercises, project briefs, specializations, templates, cohort documentation, and capstone package\n- [x] Added GitHub templates, CI, and structural/link validation\n- [x] Validated generated repository structure\n\nFuture revisions should improve lessons from classroom evidence while preserving prerequisite order.\n"
    }
    for path, text in docs.items(): put(ROOT / "docs" / path, text)
    # Exercises/templates/specializations
    for group, examples in {"html-css":["semantic-event-page","responsive-card-grid"],"javascript":["task-list-dom","fetch-error-states"],"typescript":["typed-api-client","state-union"],"react":["accessible-task-form","custom-storage-hook"],"nextjs":["app-router-catalog","server-action-form"]}.items():
        for ex in examples:
            put(ROOT / f"exercises/{group}/{ex}/README.md", f"# {ex.replace('-', ' ').title()}\n\n## Goal\nPractice the relevant module concept with an accessible, testable slice.\n\n## Requirements\nUse semantic UI, validate input, describe failure states, and write manual or automated test evidence. Do not place secrets in client code.\n\n## Done when\nThe README explains setup, expected result, tests, and one low-resource or offline decision.\n")
    for name in ["html-css-starter","javascript-starter","typescript-starter","react-starter","nextjs-starter"]:
        put(ROOT / f"templates/{name}/README.md", f"# {name.replace('-', ' ').title()}\n\nA small starting convention, not a finished solution. Add a README, `.env.example` when needed, accessible UI states, tests, and dependency lockfile before sharing.\n")
    for name in ["frontend-engineering","react-engineering","nextjs-engineering","backend-as-a-service","supabase","firebase","offline-first-web","web-security","web-performance","accessibility","web-devops"]:
        put(ROOT / f"specializations/{name}/README.md", f"# {name.replace('-', ' ').title()} Specialization\n\nDeepen this area after the core pathway. Build one focused project, read the relevant official documentation, and publish a design note covering requirements, trade-offs, tests, accessibility, security, performance, and operational ownership.\n")
    # Projects
    projects = {
      "beginner": [("Personal Portfolio Website", "Present skills and work through a semantic, responsive, accessible personal site.", "HTML, CSS, JavaScript"), ("Responsive Landing Page", "Explain a community product clearly on any screen size.", "HTML, CSS"), ("Student Registration Form", "Collect and validate student registration information without losing input.", "HTML, CSS, JavaScript"), ("Calculator", "Perform predictable calculations with keyboard-friendly controls.", "HTML, CSS, JavaScript"), ("Quiz Application", "Deliver questions, feedback, and a fair score summary.", "HTML, CSS, JavaScript"), ("To-Do Application", "Manage tasks locally with clear empty, error, and completion states.", "HTML, CSS, JavaScript"), ("Digital Business Card", "Share professional contact information accessibly.", "HTML, CSS"), ("Simple Blog Interface", "Present readable articles with semantic navigation and responsive layout.", "HTML, CSS, JavaScript")],
      "intermediate": [("Weather Application", "Show forecast data while handling unavailable location, API, and network states.", "TypeScript, React, public API"), ("Expense Tracker", "Record and summarize personal spending with local persistence.", "TypeScript, React"), ("Student Management Dashboard", "Manage learners through role-aware dashboard workflows.", "React, TypeScript, Supabase or Firebase"), ("Blog Application with Authentication", "Let authors safely create and manage their own posts.", "Next.js, Auth, Supabase or Firebase"), ("E-commerce Frontend", "Create a responsive browsing and cart journey without unsafe checkout claims.", "React, TypeScript"), ("Notes Application", "Save, search, and recover notes locally with an offline-first design.", "React, IndexedDB"), ("Job Listing Application", "Browse and filter opportunities with accessible search states.", "React, API"), ("Community Discussion Platform", "Support moderated discussion with secure data ownership.", "Next.js, Supabase or Firebase")],
      "advanced": [("Learning Management System", "Support courses, enrolment, and learner progress with role-aware data access.", "Next.js, Supabase or Firebase"), ("Community Social Network", "Support profiles and posts while protecting users and moderating risk.", "Next.js, Auth, BaaS"), ("E-commerce Full-Stack Platform", "Model catalogue, orders, and secure user workflows; payments are optional and must use a provider.", "Next.js, BaaS"), ("Project Management Application", "Coordinate projects and tasks with real-time, offline-aware updates.", "Next.js, BaaS"), ("Inventory Management System", "Track stock changes with validation and audit-oriented design.", "Next.js, PostgreSQL/Supabase"), ("Online Examination Platform", "Deliver assessments fairly with accessibility, privacy, and recovery paths.", "Next.js, BaaS"), ("Community Resource Management Platform", "Connect communities with resources using trusted, accountable workflows.", "Next.js, BaaS"), ("Offline-First Educational Web Application", "Keep learning content and learner drafts useful across unreliable connectivity.", "Next.js or React, IndexedDB, BaaS")]
    }
    for level, entries in projects.items():
        for name, summary, stack in entries: put(ROOT / f"projects/{level}/{name.lower().replace(' ', '-').replace('/', '-')}/README.md", project(name, level.title(), summary, stack))
    # Capstone package
    cap = {
      "README.md":"# Student Engineering Project\n\nThis package turns a capstone idea into testable engineering work. Complete documents in order, keep them updated as decisions change, and link evidence rather than making unsupported claims.\n",
      "PROJECT-SPECIFICATION.md":"# Project Specification\n\nState the problem, target users, scope, out-of-scope work, success measures, risks, architecture, data ownership, deployment plan, and definition of done.\n",
      "PRD.md":"# Product Requirements Document\n\nDefine personas, jobs-to-be-done, user stories, acceptance criteria, prioritization, success metrics, accessibility needs, and non-goals.\n",
      "SRS.md":"# Software Requirements Specification\n\nSpecify functional flows, interfaces, data validation, reliability, privacy, security, performance, browser support, and operational requirements.\n",
      "USER-JOURNEY.md":"# User Journey\n\nMap the happy path and loading, empty, invalid, unauthorized, offline, conflict, and recovery states.\n",
      "LEARNING-REQUIREMENTS.md":"# Learning Requirements\n\nList concepts learned, evidence of use, and the curriculum days that support each implementation decision.\n",
      "ENGINEERING-RUBRIC.md":"# Engineering Rubric\n\nAssess requirements traceability (15%), functionality (25%), architecture (20%), security/accessibility/resilience/performance (25%), and testing/documentation/presentation (15%).\n",
      "MILESTONES.md":"# Milestones\n\nDiscovery → static accessible core → data and authorization → quality hardening → deployment and presentation. Each milestone has acceptance criteria and a rollback/recovery note.\n",
      "ARCHITECTURE-REQUIREMENTS.md":"# Architecture Requirements\n\nDraw components, trust boundaries, data flow, authentication, authorization, secrets, dependencies, and failure recovery. Record decisions with alternatives and trade-offs.\n",
      "SECURITY-REQUIREMENTS.md":"# Security Requirements\n\nKeep secrets server-side, validate untrusted input, authorize each resource access, enable and test RLS or Security Rules, review dependencies, and document incident response.\n",
      "TESTING-REQUIREMENTS.md":"# Testing Requirements\n\nTest core flows, validation, authorization, accessibility, responsive layout, slow/offline behaviour, and regression risks. Record commands, devices/browsers, results, and known gaps.\n",
      "SUBMISSION-GUIDELINES.md":"# Submission Guidelines\n\nSubmit the repository, deployed URL where applicable, setup steps, environment-variable names only, screenshots, demo or written walkthrough, tests, architecture, limitations, and retrospective.\n\n## Traceability matrix\n\n| Product requirement | Learning concept | Curriculum days | Milestone | Assessment evidence |\n| --- | --- | --- | --- | --- |\n| User signs in and sees only their records | Auth, authorization, RLS/Rules | 081–090, 092 | Data integration | Policy/rule tests and demo |\n| User work survives interruption | IndexedDB, service workers, idempotency | 049–050, 096 | Quality hardening | Offline/retry test |\n| Core flow works for keyboard users | Semantic HTML, React testing, audit | 018–020, 070, 097 | Static core + quality | Audit findings and fixes |\n"
    }
    for p,t in cap.items(): put(ROOT / "student-engineering-project" / p,t)
    # Task, infrastructure, governance and CI
    put(ROOT / "task/README.md", "# Student Submissions\n\nDo not create student directories in this repository until a cohort policy explicitly requests it. Submit through a GitHub issue or pull request using the template. Mentors review requirements, working evidence, accessibility, security, failure handling, code clarity, and reflection—not just appearance.\n")
    put(ROOT / "task/submission-template.md", "# Submission\n\n- Student name:\n- GitHub username:\n- Module / day:\n- Task title:\n- Project repository:\n- Live deployment (if applicable):\n- Screenshots or written verification:\n- Implementation description:\n- Tests and connectivity condition:\n- Challenges encountered:\n- Concepts learned:\n- Lessons learned:\n\n## Mentor review\n\n- [ ] Requirements and evidence are complete\n- [ ] Accessibility and failure paths considered\n- [ ] No secrets or unsafe credentials committed\n- [ ] Feedback is specific and actionable\n")
    put(ROOT / "task/students/README.md", "# Student Work Area\n\nReserved for cohort-approved submissions. Do not add individual directories until an instructor requests the contribution workflow.\n")
    for name in ["local-development","offline-package-cache","local-learning-server","offline-testing","backup-guides"]:
        put(ROOT / f"infrastructure/{name}/README.md", f"# {name.replace('-', ' ').title()}\n\nDocument a lightweight, repeatable workflow. Cache dependencies after a known-good install, keep local documentation and backups, use local servers for exercises, and record the smallest offline or interruption test that protects learner work.\n")
    put(ROOT / "CODE_OF_CONDUCT.md", "# Code of Conduct\n\nWe are committed to a welcoming, respectful learning community. Harassment, discrimination, and unsafe conduct are not accepted. Report concerns privately to the GeekInk programme lead; protect confidentiality and avoid retaliation.\n")
    put(ROOT / "CONTRIBUTING.md", "# Contributing\n\nOpen an issue before significant curriculum changes. Preserve prerequisite order, cite authoritative sources for version-sensitive material, write accessible Markdown, run both validation scripts, and submit focused pull requests. Never commit learner data, keys, tokens, or private screenshots.\n")
    put(ROOT / "SECURITY.md", "# Security Policy\n\nDo not file public issues for suspected vulnerabilities or exposed credentials. Contact GeekInk privately with reproduction steps, impact, and affected paths. Revoke exposed keys immediately; client-side code must never contain service-role, Firebase Admin, or other privileged credentials.\n")
    put(ROOT / "CHANGELOG.md", "# Changelog\n\n## Unreleased\n\n- Introduced the 100-day GeekInk Web Engineering curriculum and cohort operating materials.\n")
    put(ROOT / ".github/PULL_REQUEST_TEMPLATE.md", "## Summary\n\n## Validation\n\n- [ ] `python3 scripts/validate_curriculum.py`\n- [ ] `python3 scripts/validate_links.py`\n- [ ] Links and accessibility reviewed\n\n## Checklist\n\n- [ ] No secrets or learner data\n- [ ] Prerequisites and links are correct\n- [ ] Version-sensitive claims cite official sources\n")
    put(ROOT / ".github/ISSUE_TEMPLATE/bug_report.md", "---\nname: Curriculum issue\nabout: Report an inaccurate, inaccessible, or broken learning resource\n---\n\n## Location\n\n## Expected and actual behaviour\n\n## Suggested correction\n")
    put(ROOT / ".github/ISSUE_TEMPLATE/feature_request.md", "---\nname: Curriculum proposal\nabout: Propose an improvement grounded in learner needs\n---\n\n## Learner problem\n\n## Proposed change\n\n## Prerequisites, accessibility, and offline impact\n")
    put(ROOT / ".github/dependabot.yml", "version: 2\nupdates:\n  - package-ecosystem: github-actions\n    directory: /\n    schedule:\n      interval: monthly\n")
    put(ROOT / ".github/workflows/validate.yml", "name: Validate curriculum\non: [pull_request, push]\njobs:\n  docs:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.12'\n      - run: python3 scripts/validate_curriculum.py\n      - run: python3 scripts/validate_links.py\n")

if __name__ == "__main__": main()
