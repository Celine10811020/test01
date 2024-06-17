function showImages() {
  const inputDate = document.getElementById('inputDate').value;
  const imageContainer = document.getElementById('imageContainer');

  const url_hoho = 'https://celine10811020.github.io/test01/hoho.json';
  const url_hoho3 = 'https://celine10811020.github.io/test01/hoho3.json';

  // Fetch images data from JSON file (or you can hardcode it in JS if preferred)
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const selectedImage = data.find(image => {
        return parseInt(inputDate) >= parseInt(image.start) && parseInt(inputDate) <= parseInt(image.end);
      });

      if (selectedImage) {
        const imagePath = selectedImage.path;
        const imageElement = document.createElement('img');
        imageElement.onload = function() {
          const containerHeight = imageElement.height; // 取得圖片的實際高度
          imageContainer.style.height = containerHeight + 'px'; // 設置容器高度為圖片高度
        };
        imageElement.src = imagePath;

        const closeButton = document.createElement('button');
        closeButton.className = 'close-btn';
        closeButton.innerHTML = 'X';
        closeButton.onclick = function() {
          imageContainer.innerHTML = '';
        };

        imageContainer.innerHTML = ''; // Clear previous images
        imageContainer.appendChild(imageElement);
        imageContainer.appendChild(closeButton);
      } else {
        imageContainer.innerHTML = '<p>找不到符合日期範圍的圖片。</p>';
      }
    })
    .catch(error => {
      console.error('Error fetching images data:', error);
      imageContainer.innerHTML = '<p>發生錯誤，無法取得圖片。</p>';
    });
}

document.getElementById("inputDate").addEventListener("keyup", function(e) {
  if (e.keyCode === 13) {
    showImages();
  }
});
