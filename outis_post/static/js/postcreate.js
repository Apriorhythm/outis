
function inputInitialize() {
    $("#id_category_id").attr("class", "form-control");
    $("#id_title").attr("class", "form-control").attr("placeholder", "Title")
        .attr("aria-describedby", "basic-addon1");
    $("#id_link").attr("class", "form-control").attr("placeholder", "Link")
        .attr("aria-describedby", "basic-addon1");
    $("#id_description").attr("class", "form-control").attr("placeholder", "Description")
        .attr("aria-describedby", "basic-addon1");
    $("#id_tag").attr("class", "form-control").attr("placeholder", "Tag")
        .attr("aria-describedby", "basic-addon1");
    $("#id_attraction").attr("class", "form-control");
}



$(function() {
    inputInitialize();
})

