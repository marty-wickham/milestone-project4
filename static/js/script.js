$(document).ready(function() {
    var hover = true

    if (hover === true) {
        $("#1").mouseenter(function() {
            $(this).addClass("highlight");
            $("#2").removeClass("highlight");
        });

        $("#2").mouseenter(function() {
            $("#1, #2").addClass("highlight");
            $("#3").removeClass("highlight");
        });

        $("#3").mouseenter(function() {
            $("#1, #2, #3").addClass("highlight");
            $("#4").removeClass("highlight");
        });

        $("#4").mouseenter(function() {
            $("#1, #2, #3, #4").addClass("highlight");
            $("#5").removeClass("highlight");
        });

        $("#5").mouseenter(function() {
            $("#1, #2, #3, #4, #5").addClass("highlight");
        });

        $("#star-container").mouseleave(function() {
            $(".box").removeClass("highlight");
        })
    }

    

    $(".box").click(function() {
        hover = false;
        var rating = $(this).atrr("id");
        
        $("#id_rating").val(rating);
    });

    display = false;

    $("#add-review").click(function() {

        if (display === false) {
            $("#review-form").removeClass("hide");
            display = true;
        }
        else  {
            $("#review-form").addClass("hide");
            display = false;
        }

    });
});

