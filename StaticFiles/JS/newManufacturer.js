/**
 * Created with PyCharm.
 * User: Matt
 * Date: 04/08/13
 * Time: 20:43
 * To change this template use File | Settings | File Templates.
 */

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = $.cookie('csrftoken');

$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function submitForm(){
    /*
        Submits the form using ajax and get's back the response
     */
    var name = $('#manName').val();
    var url = $('#manUrl').val();
    var DATA = {"name": name, "url": url};
    $.ajax({
        url: "/manufacturer/add/",
        data: {'DATA': JSON.stringify(DATA) },
        success: parseSuccess,
        type: "POST"
    })
    return true;
}

function parseSuccess(data){
    $.each(data, function(key, val) {
       alert('key: ' + key + ' val: ' + val);
    });
}
