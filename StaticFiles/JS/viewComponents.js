/**
 * Created with PyCharm.
 * User: Matt
 * Date: 23/08/13
 * Time: 20:05
 * To change this template use File | Settings | File Templates.
 */

function createComponentsTable(){
    /*
        Gets the components and places them in the relevant table
     */
    $(function() {$('#componentsTable').dataTable( {
                        "bJQueryUI": true,
                        "sAjaxSource": "/component/get/yes/",
                        "aoColumns": [
                            { "sTitle": "Name",   "mData": "name" },
                            { "sTitle": "Datasheet",  "mData": "datasheet_uri" },
                            { "sTitle": "Maximum Quantity", "mData": "max_quantity"},
                            { "sTitle": "Minimum Quantity", "mData": "min_quantity"}
                            ]
                        } );
    });
}