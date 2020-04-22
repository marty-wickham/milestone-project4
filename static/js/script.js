$(document).ready(function() {

    $("#star1").mouseenter(function() {
        $(this).addClass("highlight");
        $("#star2").removeClass("highlight");
        $("#star3").removeClass("highlight");
        $("#star4").removeClass("highlight");
        $("#star5").removeClass("highlight");
    });

    $("#star2").mouseenter(function() {
        $(this).addClass("highlight");
        $("#star1").addClass("highlight");
        $("#star3").removeClass("highlight");
        $("#star4").removeClass("highlight");
        $("#star5").removeClass("highlight");
    });

    $("#star3").mouseenter(function() {
        $(this).addClass("highlight");
        $("#star1").addClass("highlight");
        $("#star2").addClass("highlight");
        $("#star4").removeClass("highlight");
        $("#star5").removeClass("highlight");
    });

    $("#star4").mouseenter(function() {
        $(this).addClass("highlight");
        $("#star1").addClass("highlight");
        $("#star2").addClass("highlight");
        $("#star3").addClass("highlight");
        $("#star5").removeClass("highlight");
    });

    $("#star5").mouseenter(function() {
        $(this).addClass("highlight");
        $("#star1").addClass("highlight");
        $("#star2").addClass("highlight");
        $("#star3").addClass("highlight");
        $("#star4").addClass("highlight");
    });

    $("#star-container").mouseleave(function() {
        $("#star1").removeClass("highlight");
        $("#star2").removeClass("highlight");
        $("#star3").removeClass("highlight");
        $("#star4").removeClass("highlight");
        $("#star5").removeClass("highlight");
    })

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

