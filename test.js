var windowwidth = window.innerWidth || document.documentElement.clientWidth || 0;
var responsiveImage = [{src : 'https://images.colorpea.com/f44acd911f7d45ceaa5f420a3ecc0d58_480.jpg'},
                       {src : 'https://images.colorpea.com/54448a14dd834123b61ad206fc93474b_480.jpg'},
                       {src : 'https://images.colorpea.com/5f9b3bb015d94a308c4d5538bc40f7e9_480.jpg'},];

$('#slider').vegas({
   overlay: true,
   transition: 'blur',
   transitionDuration: 2000,
   delay: 10000,
   animationDuration: 20000,
   animation: 'kenburns',
   slides: responsiveImage,
});