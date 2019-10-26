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
    'touchend touchcancel mouseup': function () {
        $(this).removeClass('active');
    }
});

var date_time = new Date();

if (date_time.getHours() >= 15)
    $('#app').css('background', 'rgba(252, 223, 176, 0.8)');
if (date_time.getHours() >= 18)
    $('#app').css('background', 'rgba(44, 42, 42, 1)');
