function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const menuLinks = document.querySelector('.menu-links');
    menuLinks.classList.toggle('active')
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
  }