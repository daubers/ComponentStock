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
    var name = $('#supName').val();
    var url = $('#supUrl').val();
    var accNo = $('#supAccNo').val();
    var accUser = $('#supUsername').val();
    var DATA = {"name": name, "url": url, "account_no": accNo, "account_username": accUser};
    $.ajax({
        url: "/supplier/add/",
        data: {'DATA': JSON.stringify(DATA), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val() },
        success: parseSuccess,
        type: "POST"
    })
    return true;
}

