$(function(){
    $(document).on("click", ".js-img-enlarge", function (event) {
        $(this).parent().find(".js-img-enlarge-container").prop("src", $(this).attr("href"));
        return event.preventDefault();
    });
});
