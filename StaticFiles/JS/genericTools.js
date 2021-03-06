/**
 * Created with PyCharm.
 * User: Matt
 * Date: 11/08/13
 * Time: 20:42
 * To change this template use File | Settings | File Templates.
 */

function parseSuccess(data){
   if (data['HTTPRESPONSE']==null){
       $("div#resultMessage").addClass('ui-state-error');
       $("div#resultMessage").html('<p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: .3em;"></span> A generic error has occured </p>');
   }
   else if (isNaN(data['HTTPRESPONSE'])){
       $("div#resultMessage").addClass('ui-state-error');
       $("div#resultMessage").html('<p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: .3em;"></span> Error'+data['HTTPRESPONSE']+'has occured </p>');
   }
   else {
       $("div#resultMessage").addClass('ui-state-highlight');
       $("div#resultMessage").html('<p><span class="ui-icon ui-icon-info" style="float: left; margin-right: .3em;"></span> Entry added successfully </p>');
   }
}
