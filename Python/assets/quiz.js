// Reusable single-question feedback. Answering here does not record mastery.
document.querySelectorAll("[data-quiz]").forEach((form) => {
  const feedback = form.querySelector("[data-feedback]");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const selected = form.querySelector('input[type="radio"]:checked');

    if (!selected) {
      feedback.textContent = "先选一个答案，再检查。";
      feedback.dataset.state = "hint";
      return;
    }

    const correct = selected.value === form.dataset.correct;
    feedback.dataset.state = correct ? "correct" : "retry";
    feedback.textContent = `${correct ? "答对了。" : "再想一想。"}${selected.dataset.explanation}`;
  });
});
