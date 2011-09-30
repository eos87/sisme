$(window).load(function(){
    $("#carrusel-container").carousel( {
        dispItems: 5,
        loop: 'true',
        prevBtn: '<div class="carrusel-button-prev" id="#mycarousel-prev"></div>',
        nextBtn: '<div class="carrusel-button-next" id="#mycarousel-next"></div>',
        btnsPosition: 'outside'
    });
});
