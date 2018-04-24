window.onload = function (){
  var slideIndex = 1;
  showSlides(slideIndex);
  console.log('executing js');

  const prevButton =  document.querySelector('a.prev');
  const nextButton =  document.querySelector('a.next');
  const thumbNails = document.querySelectorAll('span.dot');

  prevButton.addEventListener('click', () => {
    showSlides(slideIndex -= 1);
  },);
  nextButton.addEventListener('click', () => {
    showSlides(slideIndex += 1);
  },);

  for (let i = 0; i < thumbNails.length; i++) {
      thumbNails[i].addEventListener('click', () => {
        currentSlide(i+1);
      });
  }
  // Thumbnail image controls
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }

  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1;}
    if (n < 1) {slideIndex = slides.length;}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
  }
};
