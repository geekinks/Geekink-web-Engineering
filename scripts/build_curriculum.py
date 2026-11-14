#!/usr/bin/env python3
"""Build the maintained 12-week GeekInk Web Engineering curriculum."""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday"]

# slug, title, practical project, (weekday title, concepts, objective, coding activity)
WEEKS = [
 ("web-engineering-foundations", "Introduction to Web Engineering and the Internet", "Personal introduction webpage", [
  ("How the web moves information", "internet vs web; URLs; client-server roles", "Trace a school-notice request from a phone to a server and back.", "Draw the request path, identify client, server, URL, request and response, then write a one-page HTML introduction."),
  ("HTTP, HTTPS, DNS, domains and hosting", "HTTP methods and status codes; TLS; DNS resolution; hosting", "Use browser DevTools Network to inspect a request and explain its status.", "Annotate a request/response, compare HTTP and HTTPS, and map a domain name to a hosting deployment."),
  ("Browsers, DevTools and resilient local setup", "rendering pipeline; Elements, Console and Network panels; local tools", "Inspect a page, fix a broken image, and test with a throttled network.", "Create a local workspace, inspect HTML/CSS, deliberately trigger and diagnose one console error, and record a recovery note."),
  ("Git and GitHub as engineering history", "repository; commit; branch; remote; issue; pull request", "Create a repository and make small, meaningful commits.", "Publish the introduction page; create an issue, a branch, a README and a pull request or self-review."),
  ("Foundation showcase and review", "web request model; Git evidence; feedback; low-bandwidth choices", "Explain decisions and review another learner's repository with kindness.", "Demonstrate the personal webpage, verify its links locally, make a final commit, and write a reflection.")]),
 ("html-fundamentals", "HTML5 and Semantic Web Development", "Personal profile website and student registration form", [
  ("HTML documents with meaning", "doctype; head and metadata; document tree; headings; paragraphs", "Build a valid document whose structure communicates before CSS loads.", "Create the profile page skeleton with a useful title, language attribute and heading hierarchy."),
  ("Navigation, media and structured content", "links; lists; tables; images; alt text; captions", "Choose the correct HTML element for content rather than styling a generic div.", "Add keyboard-friendly navigation, profile media with alt text, and an accessible course timetable."),
  ("Semantic landmarks and accessibility", "header; nav; main; article; section; footer; keyboard access", "Use landmarks and a skip link to make a page easier to navigate.", "Refactor the profile into semantic regions; complete a keyboard-only pass and capture issues."),
  ("Forms that help people succeed", "labels; input types; fieldsets; constraints; error messages", "Build a student registration form with native validation and understandable errors.", "Implement grouped registration fields, required constraints and error guidance without relying on colour alone."),
  ("Profile and form clinic", "semantic review; validation test cases; documentation", "Test real inputs, including missing and invalid values, and give actionable code feedback.", "Submit the profile and form with a short accessibility checklist and project README.")]),
 ("css-responsive-design", "CSS3 and Responsive Web Design", "Responsive portfolio website", [
  ("CSS foundations and visual systems", "selectors; cascade; specificity; inheritance; custom properties", "Create maintainable rules and a small type, colour and spacing system.", "Style the profile using a mobile-first stylesheet and CSS variables; explain one cascade decision."),
  ("Box model, flow and typography", "box sizing; margin; padding; display; positioning; readable type", "Diagnose layout spacing in DevTools and make text comfortable to read.", "Build a portfolio card and content section with consistent sizing and semantic typography."),
  ("Flexbox and Grid", "axes; alignment; wrapping; grid tracks; minmax; auto-fit", "Choose Flexbox for a row and Grid for a collection, explaining why.", "Implement navigation with Flexbox and a project gallery with responsive Grid."),
  ("Responsive, low-bandwidth interface", "media queries; fluid sizing; responsive images; reduced motion; touch targets", "Make the same page useful at 320px and larger screens without duplicate markup.", "Add breakpoints, responsive media and reduced-motion behaviour; compress or replace an oversized asset."),
  ("Portfolio review", "visual hierarchy; responsive testing; accessibility; performance budget", "Demonstrate the portfolio on small and large viewports and respond to review feedback.", "Publish the responsive portfolio with screenshots, a device test note and an asset-size summary.")]),
 ("javascript-fundamentals", "JavaScript Programming Fundamentals", "Interactive student grading and result calculator", [
  ("Values, variables and decisions", "let and const; primitives; conversion; operators; conditionals", "Write small functions that turn marks into safe, clear outcomes.", "Create grading rules with guard clauses and test normal, boundary and invalid inputs in the console."),
  ("Functions, scope and debugging", "parameters; return values; pure functions; scope; call stack; breakpoints", "Separate calculation logic from display logic and step through it in DevTools.", "Write functions for total, average and grade; use a breakpoint to diagnose an intentional defect."),
  ("Arrays, objects and loops", "collections; object properties; iteration; data modelling", "Model student results without parallel arrays or duplicated logic.", "Represent student subjects as objects and calculate a result summary with loops and array methods."),
  ("Calculator interaction", "DOM query/update; events; form submission; validation", "Connect well-tested logic to a semantic form and keep errors accessible.", "Build the grading calculator UI, prevent invalid submission and render a result summary."),
  ("JavaScript assessment and demo", "problem decomposition; tests; code readability; review", "Explain an algorithm, demonstrate failure handling, and improve a peer's code.", "Submit the calculator with test cases, Git history and a reflection on one bug fixed.")]),
 ("javascript-browser-engineering", "JavaScript for Browser Engineering", "Task management application with browser storage", [
  ("DOM, events and form workflows", "event listeners; delegation; FormData; validation; accessible feedback", "Build an interactive task list from form data without unsafe HTML injection.", "Create, complete and remove task items through accessible controls."),
  ("Modern JavaScript and JSON", "modules; destructuring; spread; map/filter; JSON serialization", "Organize a browser app into small modules and transform task data safely.", "Refactor task operations into imported functions and serialize a sample task collection."),
  ("Storage and offline state", "localStorage; sessionStorage; IndexedDB; privacy; network state", "Decide what belongs in browser storage and show a truthful saved state.", "Persist tasks locally, restore after reload, and document what should never be stored."),
  ("Fetch, promises and failure-aware UI", "Fetch API; Promise; async/await; HTTP errors; AbortController; retries", "Consume a public API while distinguishing loading, empty, error and offline states.", "Add an optional information panel to the task app; handle slow, failed and cancelled requests."),
  ("Offline task app review", "Cache API; service workers; queued mutations; synchronisation; conflicts", "Explain why a service worker alone does not make edits safe offline.", "Deliver the task app with local persistence, a visible sync-state design and a failure-path test.")]),
 ("typescript", "TypeScript and Professional JavaScript Development", "Typed task management application", [
  ("Why types prevent expensive mistakes", "TypeScript compiler; inference; primitives; arrays; literals; tsconfig", "Add strict checking to a small JavaScript project and resolve useful errors.", "Set up TypeScript and define a Task type with status and priority constraints."),
  ("Objects, interfaces and function contracts", "interfaces; aliases; optional fields; return types; readonly", "Express the shape of application data and validator results without any.", "Type the task model, form parser and display helpers."),
  ("Unions, narrowing and generics", "discriminated unions; guards; exhaustive checks; generics", "Model loading/success/error states and safely handle unknown JSON.", "Write a typed API-result helper and use narrowing for a task import."),
  ("Type-safe async application", "Promise types; runtime validation; modules; errors; maintainable organisation", "Keep static types honest by validating values at system boundaries.", "Convert the task app's storage and fetch code; add safe parsing and error states."),
  ("TypeScript conversion review", "refactoring; tests; naming; documentation; technical debt", "Demonstrate how types made a change safer and identify remaining runtime risks.", "Submit the converted application with a before/after note and typed test cases.")]),
 ("react-fundamentals", "React Fundamentals", "React student management dashboard", [
  ("React, JSX and component thinking", "declarative UI; JSX; components; props; composition", "Turn static dashboard sections into focused reusable components.", "Create a React app and implement StudentCard, DashboardHeader and EmptyState components."),
  ("State, events and conditional UI", "useState; immutable updates; derived state; conditional rendering; lists and keys", "Manage a student list without mutating state and render useful empty states.", "Add student selection, filtering and a correctly keyed student list."),
  ("Forms and hooks", "controlled inputs; validation; focus management; useEffect basics", "Build a student form that preserves user input and announces validation feedback.", "Implement add-student flow and a small effect that synchronizes a document title or stored preference."),
  ("Dashboard feature build", "lifting state; component composition; local persistence; accessibility", "Deliver a coherent dashboard feature rather than a collection of isolated components.", "Build student add/edit/delete workflows, persist a non-sensitive draft, and test keyboard use."),
  ("React dashboard demonstration", "component boundaries; state explanation; review; test evidence", "Explain props versus state and give a user-focused demo.", "Submit the dashboard repository, component map, accessibility checks and learning reflection.")]),
 ("advanced-react", "Advanced React and Frontend Engineering", "Multi-page student portal frontend", [
  ("Effects, API integration and resilient states", "useEffect cleanup; loading/error/empty; fetch cancellation; data boundaries", "Fetch data without treating a response as automatically successful.", "Build a course-list feature with explicit loading, error, retry and offline copy."),
  ("Routing and page architecture", "React Router; nested routes; URL state; layouts; route guards as UX", "Design routes around user journeys and preserve shareable filters in the URL.", "Add portal routes for dashboard, courses and profile, including not-found behaviour."),
  ("Context, custom hooks and forms", "Context API; provider scope; custom hooks; validation; reusable controls", "Share only genuine cross-cutting state and keep forms accessible.", "Create a session/preferences context and reusable form field hook with validation."),
  ("Performance, accessibility and offline enhancement", "memoization measurement; code splitting; focus; PWA concepts; IndexedDB", "Measure before optimizing, then improve a real perceived-delay or accessibility issue.", "Lazy-load a route, add focus management, and save a portal draft locally for recovery."),
  ("Portal architecture review", "state management fundamentals; code review; API contracts; quality checklist", "Defend component and state boundaries using evidence rather than library preference.", "Demonstrate the student portal and submit architecture, API-state and offline-recovery notes.")]),
 ("nextjs-fullstack", "Next.js and Full-Stack Web Development", "Next.js student portal", [
  ("Next.js and the App Router", "file routing; layouts; pages; Server Components; Client Components", "Choose the smallest client boundary and explain server-first rendering.", "Create an App Router portal with a shared layout and one interactive client component."),
  ("Routes, data and metadata", "dynamic segments; search params; server data fetching; caching; metadata", "Build a course detail route with a documented freshness and SEO policy.", "Implement catalogue and course routes, loading UI, metadata and optimized images."),
  ("Route Handlers and Server Actions", "HTTP handlers; server validation; form actions; environment variables; secrets", "Keep privileged work on the server and validate every mutation.", "Build a validated enrolment endpoint or Server Action with success and failure feedback."),
  ("Authentication concepts and protected routes", "sessions; authorization; middleware; redirects; ownership; threat boundaries", "Distinguish a sign-in check from permission to access a particular record.", "Add a mocked protected dashboard flow and middleware redirect; document authorization rules."),
  ("Next.js deployment clinic", "error boundaries; deployment; SEO; performance; environment configuration", "Build locally, deploy safely, and explain production configuration without exposing secrets.", "Deploy the portal or prepare a deployment-ready repository with tests, README and environment example.")]),
 ("supabase", "Backend-as-a-Service with Supabase", "Supabase-powered student management application", [
  ("Backend and relational data before BaaS", "API boundary; validation; authentication vs authorization; tables; keys; joins; constraints", "Model a course-enrolment system and explain how data integrity is protected.", "Draw a data model, write sample PostgreSQL table definitions, and identify ownership rules."),
  ("Supabase setup, PostgreSQL and CRUD", "project setup; client boundaries; migrations; CRUD; relationships", "Create a Supabase project structure and apply a versioned database migration.", "Create related student, course and enrolment tables; perform safe CRUD from a Next.js feature."),
  ("Auth and Row Level Security", "sessions; auth.uid; RLS; policies; service role safety; policy tests", "Prove that one user cannot read or write another user's data.", "Implement authentication and RLS policies for student-owned records; test allowed and denied paths."),
  ("Storage, Realtime and Edge Functions", "buckets; upload policy; subscriptions; Edge Functions; server validation", "Use each service only when it has a clear product need and a security boundary.", "Add protected document upload, one realtime update, and a validated Edge Function outline."),
  ("Supabase production review", "migration workflow; secrets; audit; offline queue; conflict policy", "Explain relational strengths, RLS responsibilities and safe retry behaviour.", "Submit the student manager with migration files, policy tests, README and resilient-network notes.")]),
 ("firebase", "Backend-as-a-Service with Firebase", "Firebase-powered collaborative application", [
  ("Firebase architecture and local development", "Firebase services; SDK; project setup; Authentication; Emulator Suite", "Run a feature locally with emulators before relying on a cloud project.", "Set up Firebase Authentication and Emulator Suite for a small collaboration app."),
  ("Firestore and Realtime Database", "documents; collections; denormalization; queries; listeners; RTDB comparison", "Select Firestore or Realtime Database from access patterns, not familiarity.", "Model collaborative notes or updates in Firestore and sketch when RTDB is preferable."),
  ("Storage, Functions and Security Rules", "Firebase Storage; Cloud Functions; rules; least privilege; test rules", "Treat Security Rules as executable authorization and test both denial and success.", "Add secure file metadata, a callable/HTTP function outline, and tested user-scoped rules."),
  ("Collaboration, offline and hosting", "offline persistence; synchronization; conflicts; Hosting; graceful degradation", "Show users what is local, pending, synced or needs attention.", "Implement collaborative updates with an offline-aware status, conflict decision and hosting configuration."),
  ("Firebase versus Supabase decision lab", "SQL vs documents; realtime; offline; security; cost; lock-in; use cases", "Make an evidence-based platform recommendation for a concrete product.", "Demo the Firebase collaboration app and submit a comparison matrix with a justified backend choice.")]),
 ("production-capstone", "Production Web Engineering and Capstone", "Production-ready capstone: GeekInk Learning Platform or another local problem", [
  ("Capstone discovery and architecture", "problem statement; PRD; SRS; personas; journey; wireframes; architecture; database design", "Reduce a real problem to a testable, deliverable core flow.", "Select a problem in education, business, agriculture, healthcare or community development; draft all discovery artefacts."),
  ("Secure implementation and testing", "authorization; input validation; secrets; unit/integration tests; error handling", "Test the critical path and its unsafe or failed variants before polishing UI.", "Implement the core flow, authorization matrix, validation and a focused test plan."),
  ("Offline-first production hardening", "PWA; service worker; Cache API; IndexedDB; queued submissions; retry; sync; conflict handling", "Design recovery, sync and conflict handling as product behaviour, not a hidden promise.", "Add offline access for safe content, local drafts, visible queued work and a documented conflict strategy."),
  ("Quality, deployment and documentation", "performance; accessibility; SEO; responsive testing; Vercel; production BaaS configuration", "Audit an application on constrained network/device conditions and deploy a reproducible build.", "Run quality checks, deploy to Vercel, configure backend production settings, and complete technical documentation."),
  ("Capstone presentation and engineering review", "demo; peer review; evidence; maintenance; open source; reflection", "Present the problem, decisions, working product, limits and next steps honestly.", "Submit the deployed capstone, source, PRD/SRS, architecture, database design, tests, deployment guide and final reflection.")]),
]

RESOURCES = {"Web and HTML": ["https://developer.mozilla.org/en-US/docs/Learn", "https://docs.github.com/en/get-started"], "CSS and JavaScript": ["https://developer.mozilla.org/en-US/docs/Web/CSS", "https://developer.mozilla.org/en-US/docs/Web/JavaScript"], "TypeScript": ["https://www.typescriptlang.org/docs/"], "React": ["https://react.dev/learn"], "Next.js": ["https://nextjs.org/docs"], "Supabase": ["https://supabase.com/docs"], "Firebase": ["https://firebase.google.com/docs"], "Production": ["https://web.dev/learn/", "https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps"]}
def put(relative, content):
 path = ROOT / relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(dedent(content).strip() + "\n", encoding="utf-8")
def group(week):
 return "Web and HTML" if week <= 2 else "CSS and JavaScript" if week <= 5 else "TypeScript" if week == 6 else "React" if week <= 8 else "Next.js" if week == 9 else "Supabase" if week == 10 else "Firebase" if week == 11 else "Production"
def lesson(week, day, title, concepts, objective, activity, project):
 links = "\n".join(f"- [{url}]({url})" for url in RESOURCES[group(week)])
 approach = {"monday":"Introduce concepts and explain fundamentals.","tuesday":"Deepen understanding through guided examples.","wednesday":"Implement and practise with code.","thursday":"Build a real-world feature or mini-project.","friday":"Assess, review, demonstrate and reflect."}[day]
 return f'''# {day.title()}: {title}

**Week {week} · {approach}**  
**Weekly build:** {project}

## Learning objectives

- Explain and apply: {concepts}.
- {objective}
- Make one small, reviewable Git commit and record one test or failure-path check.

## Concepts to understand

{concepts}. Connect each concept to a real learner or community user, including the consequences of a slow, lost or expensive connection.

## Lesson content

Start from the problem: what must the user accomplish, what data or interface state is involved, and what could fail? The instructor introduces the mental model, demonstrates a small working slice, then asks learners to predict the result before running it. Discuss accessible semantics, validation, privacy and resource use whenever the feature touches them. Keep dependencies minimal and read the relevant official documentation before copying an API.

## Guided example

1. Make the smallest version of the feature with clear names and one visible outcome.
2. Inspect it using the browser, terminal or framework tooling appropriate to the week.
3. Test a normal path and one failure, boundary or offline path.
4. Explain why the implementation is safe enough for its current scope, then commit it.

## Practical coding activity

{activity}

## Independent exercises

- Rebuild one portion without copying the guided solution.
- Add an empty, loading, invalid-input or unavailable-network state where relevant.
- Improve one accessibility, performance or low-bandwidth detail and describe the trade-off in the README.

## Expected output

A working, committed slice of **{project}**; a short README note covering setup, what was tested, and what happens when the network or input is unavailable.

## Homework / assignment

Finish the feature, push it to GitHub, and submit a link plus one screenshot or local evidence, one test case, and a two-to-four sentence reflection. Friday submissions also include peer code-review feedback.

## Recommended learning resources

{links}
'''
def build():
 for index, (slug, title, project, sessions) in enumerate(WEEKS, 1):
  base = Path("weeks") / f"week-{index:02d}-{slug}"
  rows = "\n".join(f"| {day.title()} | [{item[0]}]({day}.md) | {item[1]} |" for day, item in zip(WEEKDAYS, sessions))
  put(base / "README.md", f'''# Week {index}: {title}

**Outcome:** By Friday, students can deliver **{project}** and explain the engineering decisions behind it.

Monday to Friday are structured learning sessions. Saturday is optional revision, project completion or mentorship; Sunday is rest and preparation.

| Session | Topic | Key concepts |
| --- | --- | --- |
{rows}

## Weekly deliverables

- A GitHub repository with small commits and a clear README.
- The week's practical project, including normal and failure-path evidence.
- A Friday reflection and one peer-review contribution.

## Offline-first thread

Each week considers a realistic constraint: limited data, interrupted electricity, modest hardware, unreliable requests, locally saved work, or safe synchronization. See [resources.md](resources.md) and the programme [offline-first guide](../../docs/offline-first-web-engineering.md).

## Assessment

Use the [weekly assessment template](../../assessments/weekly-assessments/template.md). The mini-project is assessed against functionality, clarity, accessibility, resilience and documentation.
''')
  for day, session in zip(WEEKDAYS, sessions): put(base / f"{day}.md", lesson(index, day, *session, project))
  put(base / "resources.md", f'''# Week {index} resources

Read the official documentation before using a package or copying a snippet.

## Primary

{chr(10).join(f'- [{url}]({url})' for url in RESOURCES[group(index)])}

## Practice and resilience

- [Offline-first engineering](../../docs/offline-first-web-engineering.md)
- [Low-resource development](../../docs/low-resource-development.md)
- [Project guidelines](../../docs/project-guidelines.md)
''')
  put(base / "exercises/README.md", f"# Week {index} exercises\n\nUse the independent exercises in each weekday lesson. Save attempts, tests and questions in the weekly repository.\n")
  put(base / "assignments/README.md", f"# Week {index} assignment\n\nComplete **{project}**. Follow the [submission guidelines](../../../docs/submission-guidelines.md) and use the assessment template.\n")
if __name__ == "__main__":
 build(); print("Built 12 weekly curriculum directories and 60 weekday lessons.")
