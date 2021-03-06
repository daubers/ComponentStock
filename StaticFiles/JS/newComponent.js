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
  window.adManDialog = $("div#dialogManDiv").dialog({
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

 $(function() {
  window.adSupDialog = $("div#dialogSupDiv").dialog({
        modal: true,
        autoOpen: false,
        minWidth:408,
        minHeight: 155,
        resizable: false,
        draggable: false,
        title: "New Supplier",
        buttons: [ { text: "Add", click: function() { addSup(); } } ]
    });
 });

function loadComplete(){
    /* This function is run when the page has finished loading
       it's main job is to populate the various drop down boxes
       on the page
     */
    loadManufacturers();
    loadSuppliers();
    $(function () {
        $("input#addMan").button({ label: "Add Manufacturer" });
        $("input#addSup").button({ label: "Add Supplier" });
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

function loadSuppliers(){
    /*
        Populates the manufacturers drop down
     */
    $.getJSON("/supplier/get/", function(data){
        $.each(data, function() {
            var option = new Option(this.name, this.id);
            $("#supplierSelect")[0].add(option);
        });
    });
}

function addSupOnClick(){
    /*
        Called when the add manufacturer button is clicked
     */
    $.get("/supplier/add/form/", function(data){
        $("#dialogSupDiv").html(data);
        $("div #submitFormButton").hide();
    });
    window.adSupDialog.dialog("open");
}

function addSup(){
    submitSup();
    $(function() {
        window.adSupDialog.dialog("close");
    });
}

function submitSup(){
    /*
        Submits the form using ajax and gets back the response
     */
    var name = $('#supName').val();
    var url = $('#supUrl').val();
    var accNo = $('#supAccNo').val();
    var accUser = $('#supUsername').val();
    var DATA = {"name": name, "url": url, "account_no": accNo, "account_username": accUser};
    $.ajax({
        url: "/supplier/add/",
        data: {'DATA': JSON.stringify(DATA), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val() },
        success: loadSuppliers,
        type: "POST"
    });
    return true;
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
        data: {'DATA': JSON.stringify(DATA), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val() },
        success: loadManufacturers,
        type: "POST"
    });
    return true;
}


function addManOnClick(){
    /*
        Called when the add manufacturer button is clicked
     */
    $.get("/manufacturer/add/form/", function(data){
        $("#dialogManDiv").html(data);
        $("div #submitFormButton").hide();
    });
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

function submitComponent(){
    /*
        Submits the component to the database
     */
    var name = $("#compName").val();
    var partNo = $("#partNo").val();
    var supplierId = $('#supplierSelect :selected').val();
    var cost = $("#cost").val();
    var manufacturerId = $('#manufacturerSelect :selected').val();
    var datasheetURL = $("#datasheetURL").val();
    var minQuantity = $("#minQuantity").val();
    var maxQuantity = $("#maxQuantity").val();
    var DATA = {"name": name, "cost": cost, "manufacturer": manufacturerId, "part_no": partNo,
                "datasheet_uri": datasheetURL, "supplier": supplierId, "max_quantity": maxQuantity,
                "min_quantity": minQuantity}
    $.ajax({
        url: "/component/add/",
        data: {'DATA': JSON.stringify(DATA), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val() },
        success: parseSuccess,
        type: "POST"
    });
    return true;
;
}
