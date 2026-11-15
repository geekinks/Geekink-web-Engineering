# HTML Forms

## 1. Introduction

HTML Forms allow users to enter and submit information on a website. They are commonly used for registration, login, contact pages, surveys, search boxes, and feedback forms.

The `<form>` element acts as a container for form inputs.

## 2. Basic Form Structure

```html
<form action="/submit" method="POST">
  <label for="fullname">Full Name:</label>
  <input type="text" id="fullname" name="fullname">

  <label for="email">Email Address:</label>
  <input type="email" id="email" name="email">

  <button type="submit">Submit</button>
</form>
```

### Understanding the Attributes

- `action`: Specifies where the form data should be sent.
- `method`: Specifies how the data is submitted, commonly `GET` or `POST`.
- `name`: Identifies the input field when submitting form data.
- `type`: Defines the kind of input expected.
- `id`: Uniquely identifies an element.
- `for`: Connects a label to its corresponding input.

## 3. Common HTML Form Elements

| Element | Purpose |
|---|---|
| `<input>` | Accepts user input |
| `<label>` | Describes an input field |
| `<textarea>` | Accepts longer text |
| `<select>` | Creates a dropdown |
| `<option>` | Defines dropdown options |
| `<button>` | Creates a clickable button |
| `<fieldset>` | Groups related form controls |
| `<legend>` | Provides a title for a fieldset |

## 4. Common Input Types

```html
<input type="text" placeholder="Enter your name">
<input type="email" placeholder="Enter your email">
<input type="password" placeholder="Enter password">
<input type="number" placeholder="Enter your age">
<input type="date">
<input type="tel" placeholder="Phone number">
<input type="checkbox"> I agree to the terms
<input type="radio" name="gender" value="male"> Male
<input type="file">
```

## 5. Dropdown and Textarea

**Dropdown:**

```html
<label for="course">Choose a course:</label>

<select id="course" name="course">
  <option value="">Select a course</option>
  <option value="web">Web Development</option>
  <option value="python">Python Programming</option>
  <option value="data">Data Analysis</option>
</select>
```

**Textarea:**

```html
<label for="message">Your Message:</label>

<textarea
  id="message"
  name="message"
  rows="5"
  placeholder="Write your message..."
></textarea>
```

## 6. HTML Form Validation

HTML provides built-in validation attributes to help ensure users enter valid information.

```html
<form>
  <input
    type="text"
    name="fullname"
    placeholder="Full Name"
    required
  >

  <input
    type="email"
    name="email"
    placeholder="Email Address"
    required
  >

  <input
    type="password"
    name="password"
    minlength="8"
    required
  >

  <button type="submit">Register</button>
</form>
```

Useful validation attributes:

- `required`: Makes a field compulsory.
- `minlength`: Sets the minimum number of characters.
- `maxlength`: Sets the maximum number of characters.
- `min` and `max`: Set numeric or date limits.
- `pattern`: Defines an expected input pattern.
- `readonly`: Prevents editing while allowing the value to be submitted.
- `disabled`: Disables the field and excludes it from form submission.

**Important:** HTML validation improves user experience, but backend validation is still necessary for security and data integrity.

## 7. Practical Exercise: Student Registration Form

Build a student registration form for GeekInk with the following fields:

1. Full Name
2. Email Address
3. Phone Number
4. Gender (Radio Buttons)
5. Date of Birth
6. Course Selection (Dropdown)
7. Password
8. Confirm Password
9. Terms and Conditions (Checkbox)
10. Submit Button

Requirements:
- Use semantic HTML.
- Every input must have a label.
- Use appropriate input types.
- Make required fields compulsory.
- Use HTML validation attributes.
- Group related fields using `<fieldset>` where appropriate.

## 8. Learning Challenge

After completing the exercise, answer these questions:

1. What is the purpose of the `<form>` element?
2. What is the difference between GET and POST?
3. Why should every input have a label?
4. What is the difference between `id` and `name`?
5. What does the `required` attribute do?
6. What is the difference between `disabled` and `readonly`?

## 9. Expected Outcome

By the end of this lesson, you should be able to:

- Create HTML forms.
- Use different input types.
- Group related form fields.
- Create dropdowns and text areas.
- Apply basic HTML form validation.
- Build a functional student registration form.

**Next step:** Learn how to style HTML forms using CSS to create clean, responsive and user-friendly interfaces.