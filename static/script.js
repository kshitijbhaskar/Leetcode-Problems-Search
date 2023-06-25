document.querySelectorAll('.read-more').forEach(function (button) {
    button.addEventListener('click', function () {
        const listItem = button.closest('.list-group-item');
        const descriptionTruncated = listItem.querySelector('.description-truncated');
        const descriptionFull = listItem.querySelector('.description-full');

        if (descriptionTruncated.style.display === 'none') {
            descriptionTruncated.style.display = 'block';
            descriptionFull.style.display = 'none';

            button.innerHTML = 'Show More';
        }
        else {
            descriptionTruncated.style.display = 'none';
            descriptionFull.style.display = 'block';

            const fullDescription = descriptionFull.innerText;
            descriptionFull.innerHTML = fullDescription.replace(/\n/g, '<br>');
            button.innerHTML = 'Show Less';
        }

    });
});

document.querySelectorAll('.load-preview').forEach(function (button) {
    button.addEventListener('click', function () {
        const listItem = button.closest('.list-group-item');
        const previewContainer = listItem.querySelector('.preview-container');
        const frame = previewContainer.querySelector('.preview-frame');
        const reloadPreview = previewContainer.querySelector('.reload-preview')

        if (frame.style.display === '' || frame.style.display === 'none') {
            frame.style.display = 'block';
            reloadPreview.style.display = 'block';
            button.innerHTML = 'Collapse Preview';
        } else {
            frame.style.display = 'none';
            reloadPreview.style.display = 'none';
            button.innerHTML = 'Load Preview';
        }
    });
});

function reloadPreview() {
    const iframe = this.closest('.preview-container').querySelector('.preview-iframe');
    iframe.src = iframe.src;
}

document.querySelectorAll('.reload-preview').forEach(button => {
    button.addEventListener('click', reloadPreview);
});

const themeSwitch = document.getElementById('flexSwitchCheckDefault');
const htmlTag = document.querySelector('html');

const storedTheme = sessionStorage.getItem('theme');
const currentTheme = storedTheme ? storedTheme : null;

if (currentTheme === 'light') {
  themeSwitch.checked = false;
  htmlTag.setAttribute('data-bs-theme', 'light');
} else {
  themeSwitch.checked = true;
  htmlTag.setAttribute('data-bs-theme', 'dark');
}

themeSwitch.addEventListener('change', () => {
  if (htmlTag.getAttribute('data-bs-theme') === 'light') {
    htmlTag.setAttribute('data-bs-theme', 'dark');
    sessionStorage.setItem('theme', 'dark');
  } else {
    htmlTag.setAttribute('data-bs-theme', 'light');
    sessionStorage.setItem('theme', 'light');
  }
});

$(function() {
    $('.preview-frame').resizable({
      handles: 's',
    });
  });
  