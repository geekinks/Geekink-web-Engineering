# Day 093: Web security essentials

**Module:** 10 — Production Web Engineering and Capstone  
**Build thread:** Community Learning Hub, a small application students improve throughout the program.

## Learning objectives

- Explain XSS, CSRF, injection, secrets, dependencies, headers, and input validation in plain language and identify its engineering trade-offs.
- Apply the concept in a small, observable change rather than copying an unexplained recipe.
- Record one assumption, one failure path, and one accessibility or low-resource consideration.

## Prerequisites

Complete the previous day and keep its work in Git. Use the browser and local tools already installed; do not block progress on a cloud account or a paid service.

## Concept explanation

Today focuses on **XSS, CSRF, injection, secrets, dependencies, headers, and input validation**. Start with the user-facing behaviour, then locate the boundary that makes that behaviour possible: browser, UI, network, server, or data store. Good engineering makes the normal path clear and makes failure understandable. Name the data entering the boundary, validate it, and decide what a user sees if it is unavailable.

## Practical examples

For the Community Learning Hub, perform a focused security review. Keep the first implementation deliberately small: use one meaningful name, one visible state, and one assertion you can verify in DevTools or a test. Prefer semantic HTML and stable, local sample data before adding remote dependencies.

```tsx
await user.type(screen.getByLabelText(/task/i), "Study offline caching");
await user.click(screen.getByRole("button", { name: /save/i }));
expect(screen.getByText(/saved locally/i)).toBeVisible();
```

Explain each line before expanding it. A real application must not treat an absent value, a network failure, and an unauthorized request as the same condition.

## Step-by-step implementation

1. Write a one-sentence acceptance criterion for the behaviour you will change.
2. Create a branch or local checkpoint named `day-093`.
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
