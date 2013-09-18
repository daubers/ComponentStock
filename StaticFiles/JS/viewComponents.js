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
                        "bProcessing": true,
                        "bJQueryUI": true,
                        "sAjaxSource": "/component/get/yes/",
                        "aoColumns": [
                            { "sTitle": "Name",   "mData": "name" },
                            { "sTitle": "Manufacturer", "mData": "manufacturer.0.name" },
                            { "sTitle": "Cost", "mData": "cost" },
                            { "sTitle": "Datasheet",  "mData": "datasheet_uri" },
                            { "sTitle": "Maximum Quantity", "mData": "max_quantity"},
                            { "sTitle": "Minimum Quantity", "mData": "min_quantity"}
                            ]
                        } );
    });
}