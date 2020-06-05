$(document).ready(function () {


    display = false;

    $("#add-review").click(function () {

        if (display === false) {
            $("#review-form").removeClass("hide");
            display = true;
        }
        else {
            $("#review-form").addClass("hide");
            display = false;
        }

    });

    $('#video_modal').on('hidden.bs.modal', function () {
        video = $("#video");
        video.pause();    
    });


    // $(".box").on( "mouseenter", function() {
    //     var onStar = parseInt($(this).data('rating'), 10); // The star currently hovering over

    //     $(this).parent().children(".box").each(function(e){
    //         if (e < onStar) {
    //             $(this).addClass("highlight");
    //         }
    //         else {
    //             $(this).removeClass("highlight");
    //         }
    //     });
    
    // }).on("mouseout", function(){
    //     $(this).parent().children(".box").each(function(e){
    //         $(this).removeClass("highlight");
    //     });
    // });

    $( ".box" ).mouseenter(function() {
        var onStar = parseInt($(this).data('rating'), 10); // The star currently hovering over

        $( ".box" ).each(function( index, element ) {
            // element == this
            $( element ).addClass("highlight");
            if ( $( this ).is( onStar ) ) {
            
                return false;
            }
        });
    });
});
