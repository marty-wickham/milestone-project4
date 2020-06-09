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


    $(".box").mouseenter(function() {
        var onStar = parseInt($(this).attr("id"), 10); // The star currently hovering over

        $(".box").parent().children(".box").each(function(e) {
            
            if (e < onStar) {
                $(this).addClass("highlight");
            }
            else {
                $(this).removeClass("highlight");
            }
        }).mouseout(function(){
            $(this).parent().children(".box").each(function(e){
                $(this).removeClass("highlight");
            });
        });
    });

    $( ".box" ).click(function() {
        var onStar = $(this).attr("id"); // The star currently selected

        $( ".box" ).each(function( index, element ) {
            // element == this
            $( element ).addClass('selected');
            if ( $( this ).attr("id") > onStar ) {
                $( element ).removeClass('selected');
            }
        });

        $("#id_rating").val([onStar]);
    });

});
