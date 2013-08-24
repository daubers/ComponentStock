/**
 * Created with PyCharm.
 * User: Matt
 * Date: 04/08/13
 * Time: 20:43
 * To change this template use File | Settings | File Templates.
 */




function submitForm(){
    /*
        Submits the form using ajax and get's back the response
     */
    var name = $('#manName').val();
    var url = $('#manUrl').val();
    var DATA = {"name": name, "url": url};
    $.ajax({
        url: "/manufacturer/add/",
        data: {'DATA': JSON.stringify(DATA), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val() },
        success: parseSuccess,
        type: "POST"
    })
    return true;
}
