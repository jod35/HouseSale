const menu_open_button=document.querySelector('.menu-open-btn');
const menu_close_button=document.querySelector('.menu-close-btn');
const mobile_menu=document.querySelector('.mobile-nav-items');
const mobile_links=document.querySelector('.nav-items');

menu_open_button.addEventListener('click',displayMobileNav);


function displayMobileNav(){
    menu_open_button.style.display="none";
    mobile_links.style.width="100vw";
    mobile_menu.style.height="100vh";
    
    mobile_links.style.display="block";
    menu_close_button.style.display="block";
}

menu_close_button.addEventListener('click',closeMobileNav);


function closeMobileNav(){
    menu_close_button.style.display="none";
    // mobile_menu.style.display="none";
    mobile_links.style.display="none";
    mobile_menu.style.height="0vh";
    mobile_menu.style.width="0vh";

    menu_open_button.style.display="block";
}