/**
 * Created with PyCharm.
 * User: Matt
 * Date: 11/08/13
 * Time: 20:41
 * To change this template use File | Settings | File Templates.
 */

function submitForm(){
    /*
        Submits the form using ajax and gets back the response
     */
    var name = $('#manName').val();
    var url = $('#manUrl').val();
    var DATA = {"name": name, "url": url};
    $.ajax({
        url: "/supplier/add/",
        data: {'DATA': JSON.stringify(DATA) },
        success: parseSuccess,
        type: "POST"
    })
    return true;
}

