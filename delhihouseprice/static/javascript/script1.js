window.addEventListener('scroll', function () {
    var header = document.querySelector('.navbar');
    header.classList.toggle('fixed', window.scrollY > 0);
    // <!-- aarsh saxena 21bec001 -->
    var scrollPos = window.scrollY;
    if (scrollPos > 0) {
        header.style.backgroundColor = '#333'; // Change to the desired background color
        } else {
          header.style.backgroundColor = '#ffffff00'; // Change to the original background color
        }
    });
    // <!-- aarsh saxena 21bec001 -->