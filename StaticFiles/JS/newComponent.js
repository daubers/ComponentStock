/**
 * Created with PyCharm.
 * User: Matt
 * Date: 13/08/13
 * Time: 21:25
 * To change this template use File | Settings | File Templates.
 */
/* This file just contains functions relating to
 * creating a new component and it's related pages */

// Create the dialogs here so we can open/close them at will
 $(function() {
  window.adManDialog = $("div#dialogDiv").dialog({
        modal: true,
        autoOpen: false,
        minWidth:408,
        minHeight: 155,
        resizable: false,
        draggable: false,
        title: "New Manufacturer",
        buttons: [ { text: "Add", click: function() { addMan(); } } ]
    });
 });

function loadComplete(){
    /* This function is run when the page has finished loading
       it's main job is to populate the various drop down boxes
       on the page
     */
    loadManufacturers();
    $(function () {
        $("input#addMan").button({ label: "Add Manufacturer" });
    });
}

function loadManufacturers(){
    /*
        Populates the manufacturers drop down
     */
    $.getJSON("/manufacturer/get/", function(data){
        $.each(data, function() {
            var option = new Option(this.name, this.id);
            $("#manufacturerSelect")[0].add(option);
        });
    });
}

function submitMan(){
    /*
        Submits the manufacturer form using ajax and update the drop down
     */
    var name = $('#manName').val();
    var url = $('#manUrl').val();
    var DATA = {"name": name, "url": url};
    $.ajax({
        url: "/manufacturer/add/",
        data: {'DATA': JSON.stringify(DATA) },
        success: loadManufacturers,
        type: "POST"
    })
    return true;
}


function addManOnClick(){
    /*
        Called when the add manufacturer button is clicked
     */
    $.get("/manufacturer/add/form/", function(data){
        $("#dialogDiv").html(data);
        $("div #submitFormButton").hide();
    })
    window.adManDialog.dialog("open");
}

function addMan(){
    /*
        Called when the submit button is pressed for adding a manufacturer
     */
    submitMan();
    $(function() {
        window.adManDialog.dialog("close");
    });
}