const titleInput = document.querySelector('input[name="title"]');
const slugInput = document.querySelector('input[name="slug"]');

const slugify = (title) => {
  return title
    .toString()
    .toLowerCase()
    .trim()
    .replace(/&/g, "-and-") //replace & with 'and'
    .replace(/[\s\W-]+/g, "-"); //replace spaces
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.setAttribute("value", slugify(titleInput.value));
});
