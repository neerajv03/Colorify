$(document).ready(function(){

    // variables
    var $header_top = $('.header-top');
    var $nav = $('nav');



    // toggle menu
    $header_top.find('a').on('click', function() {
        $(this).parent().toggleClass('open-menu');
    });



    // fullpage customization
    $('#fullpage').fullpage({
        sectionsColor: ['#B8AE9C', '#348899', '#F2AE72', '#FDEBD0', '#B8B89F', '#348899', '#F2AE72'],
        sectionSelector: '.vertical-scrolling',
        slideSelector: '.horizontal-scrolling',
        navigation: true,
        slidesNavigation: true,
        css3: true,
        controlArrows: false,
        anchors: ['home',  'ApplicationOverview', 'UsingAlgorithmia', 'UsingOpenCV', 'TensorFlow','Metrics','About'],
        menu: '#menu',


    });
});