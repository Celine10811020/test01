function showImages() {
  const inputDate = document.getElementById('inputDate').value;
  const imageContainer = document.getElementById('imageContainer');

console.log(inputDate);

  const url = 'https://celine10811020.github.io/test01/images.json';

  // Fetch images data from JSON file (or you can hardcode it in JS if preferred)
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const selectedImage = data.find(image => {
console.log(image.start);
console.log(image.end);

        return parseInt(inputDate) >= parseInt(image.start) && parseInt(inputDate) <= parseInt(image.end);
      });

      if (selectedImage) {
        const imagePath = selectedImage.path;
        const imageElement = document.createElement('img');
        imageElement.src = imagePath;
        imageContainer.innerHTML = ''; // Clear previous images
        imageContainer.appendChild(imageElement);
      } else {
        imageContainer.innerHTML = '<p>找不到符合日期範圍的圖片。</p>';
      }
    })
    .catch(error => {
      console.error('Error fetching images data:', error);
      imageContainer.innerHTML = '<p>發生錯誤，無法取得圖片。</p>';
    });
}
