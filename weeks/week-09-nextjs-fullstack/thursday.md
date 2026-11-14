# Thursday: Authentication concepts and protected routes

**Week 9 · Build a real-world feature or mini-project.**  
**Weekly build:** Next.js student portal

## Learning objectives

- Explain and apply: sessions; authorization; middleware; redirects; ownership; threat boundaries.
- Distinguish a sign-in check from permission to access a particular record.
- Make one small, reviewable Git commit and record one test or failure-path check.

## Concepts to understand

sessions; authorization; middleware; redirects; ownership; threat boundaries. Connect each concept to a real learner or community user, including the consequences of a slow, lost or expensive connection.

## Lesson content

Start from the problem: what must the user accomplish, what data or interface state is involved, and what could fail? The instructor introduces the mental model, demonstrates a small working slice, then asks learners to predict the result before running it. Discuss accessible semantics, validation, privacy and resource use whenever the feature touches them. Keep dependencies minimal and read the relevant official documentation before copying an API.

## Guided example

1. Make the smallest version of the feature with clear names and one visible outcome.
2. Inspect it using the browser, terminal or framework tooling appropriate to the week.
3. Test a normal path and one failure, boundary or offline path.
4. Explain why the implementation is safe enough for its current scope, then commit it.

## Practical coding activity

Add a mocked protected dashboard flow and middleware redirect; document authorization rules.

## Independent exercises

- Rebuild one portion without copying the guided solution.
- Add an empty, loading, invalid-input or unavailable-network state where relevant.
- Improve one accessibility, performance or low-bandwidth detail and describe the trade-off in the README.

## Expected output

A working, committed slice of **Next.js student portal**; a short README note covering setup, what was tested, and what happens when the network or input is unavailable.

## Homework / assignment

Finish the feature, push it to GitHub, and submit a link plus one screenshot or local evidence, one test case, and a two-to-four sentence reflection. Friday submissions also include peer code-review feedback.

## Recommended learning resources

- [https://nextjs.org/docs](https://nextjs.org/docs)
