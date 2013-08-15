/**
 * Created with PyCharm.
 * User: Matt
 * Date: 13/08/13
 * Time: 21:25
 * To change this template use File | Settings | File Templates.
 */
/* This file just contains functions relating to
 * creating a new component and it's related pages */

function loadComplete(){
    /* This function is run when the page has finished loading
       it's main job is to populate the various drop down boxes
       on the page
     */
    var manufacturers = $.getJSON("/manufacturer/get/", function(data){
        $.each(data, function() {
            var option = new Option(this.name, this.id);
            $("#manufacturerSelect")[0].add(option);
        });
    });

}