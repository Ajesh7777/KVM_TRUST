$(document).on('click', '.dropdown-menu', function (e) {
  e.stopPropagation();
});
// make it as accordion for smaller screens
if ($(window).width() < 992) {
  $('.dropdown-menu a').click(function(e){
    // e.preventDefault();
      if($(this).next('.submenu').length){
        $(this).next('.submenu').toggle();
      }
      $('.dropdown').on('hide.bs.dropdown', function () {
     $(this).find('.submenu').hide();
  })
  });
}
$('.dropdown-menu a').click(function(e){
  // e.preventDefault();
    if($(this).next('.submenu').length){
      $(this).next('.submenu').toggle();
    }
   
});

$('.dropdown').on('hide.bs.dropdown', function () {
  $(this).find('.submenu').hide();
})

$('.dropdown-menu li').not(".subli").click(function () {
  $(this).siblings('.subli').children(".submenu").hide();
});



// $('li').not(".subli").hover(function(e){
//   e.preventDefault();
//   window.getElementByClassName('submenu').style.display = 'none';

//     if($(this).next('.submenu').length){
//       $(this).next('.submenu').hide();
//     }
   
// })


// $(":not(.subli)").click((e)=>{
//   e.preventDefault();
//   $(this).find('.submenu').hide();
// })