document.querySelectorAll('.read-more').forEach(button => {
    button.addEventListener('click', function () {
        const listItem = button.closest('.list-group-item');
        const descriptionTruncated = listItem.querySelector('.description-truncated');
        const descriptionFull = listItem.querySelector('.description-full');
        const readMoreButton = listItem.querySelector('.read-more');
        const readLessButton = listItem.querySelector('.read-less');

        descriptionTruncated.style.display = 'none';
        descriptionFull.style.display = 'block';
        readMoreButton.style.display = 'none';
        readLessButton.style.display = 'inline';
    });
});

document.querySelectorAll('.read-less').forEach(button => {
    button.addEventListener('click', function () {
        const listItem = button.closest('.list-group-item');
        const descriptionTruncated = listItem.querySelector('.description-truncated');
        const descriptionFull = listItem.querySelector('.description-full');
        const readMoreButton = listItem.querySelector('.read-more');
        const readLessButton = listItem.querySelector('.read-less');

        descriptionTruncated.style.display = 'block';
        descriptionFull.style.display = 'none';
        readMoreButton.style.display = 'inline';
        readLessButton.style.display = 'none';
    });
});

function togglePreview(button) {
    const listItem = button.closest('li');
    const descriptionContainer = listItem.querySelector('.question-description');
    const previewContainer = listItem.querySelector('.preview-container');
    const iframeContainer = listItem.querySelector('.iframe-container');
    const iframe = listItem.querySelector('.preview-iframe');
  
    if (previewContainer.style.display === 'none') {
      descriptionContainer.style.display = 'none';
      previewContainer.style.display = 'block';
      iframeContainer.style.display = 'block';
      button.innerText = 'Collapse Preview';
  
      const url = listItem.querySelector('a').getAttribute('href');
      iframe.src = url;
    } else {
      descriptionContainer.style.display = 'block';
      previewContainer.style.display = 'none';
      iframeContainer.style.display = 'none';
      button.innerText = 'Load Preview';
  
      iframe.src = '';
    }
  }
  
  
  function revertPreview(button) {
    const listItem = button.closest('li');
    const descriptionContainer = listItem.querySelector('.question-description');
    const previewContainer = listItem.querySelector('.preview-container');
    const iframeContainer = listItem.querySelector('.iframe-container');
    const iframe = listItem.querySelector('.preview-iframe');
  
    descriptionContainer.style.display = 'block';
    previewContainer.style.display = 'none';
    iframeContainer.style.display = 'none';
  
    iframe.src = '';
    listItem.querySelector('.load-preview').innerText = 'Load Preview';
  }
  
  document.querySelectorAll('.load-preview').forEach(button => {
    button.addEventListener('click', function() {
      togglePreview(button);
    });
  });
  
  document.querySelectorAll('.revert-preview').forEach(button => {
    button.addEventListener('click', function() {
      revertPreview(button);
    });
  });
  