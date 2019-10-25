$(document).ready(function () {
    $('.menu-toggle').click(function () {
        $('nav').toggleClass('active');
    })
});

$('#app').on('click', function () {
    let aplayer = $('.aplayer');
    if (aplayer.hasClass('show')) {
        aplayer.removeClass('show');
    }
});

$('.logo').on('click', function () {
    let aplayer = $('.aplayer');
    if (aplayer.hasClass('show')) {
        aplayer.removeClass('show');
    }
});

$('.music-bar').on('click', function () {
    $('.aplayer').toggleClass('show');
});

$('nav').bind({
    // 'touchstart mousedown' : function(){},
    // 'touchmove mousemove' : function(){},
    'touchend touchcancel mouseup' : function(){
       $(this).addClass('active');
    }
});