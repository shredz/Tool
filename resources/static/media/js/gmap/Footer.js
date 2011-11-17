
$(document).ready(function() {

    /*************************  Start Free EMail SignUp    *************************/
    $("#lnkSignUp2").click(function() {
    /*var txtSignUP2 = $('#txtSignUp2');
    if (!IsConnected) {
        ShowMessageWindow('Please login to SignUp.');
        return;
    }
        FreeEMailSignUp(txtSignUP2);*/
        
        var email = $("#txtSignUp2").val();
        var location = $("#FooterSignupLocationSelect").val();
        $("#FooterEmailError").hide();
        
        if(!VerifyValidEmailAddress(email))
        {   
            $("#FooterEmailError").show();
            return;
        }
        var url = rootDomain + "signup/emails/?em=" + email + "&city=" + location;
        window.open(url);
    });


    function FreeEMailSignUp(txtSignUp) {

        var sEmail = $(txtSignUp).val();
        if (sEmail == '') {
            ShowMessageWindow('Email address required');
            txtSignUp.focus();
            return;
        }
        else
            if (!IsValidEmail(sEmail)) {
            ShowMessageWindow('Enter a valid email address');
            txtSignUp.focus();
            return;
        }
        else {
            var url = rootDomain + "?signupEmail=" + sEmail;
            document.location.href = (url);
            /*$.ajax({

                type: "POST",

                url: "../default.aspx/Subscription",

                data: "{'sEMail':'" + sEmail + "'}",

                contentType: "application/json; charset=utf-8",

                dataType: "json",

                success: ResponseFreeEMailSignUp,

                error: function() {
                    MailError('Email registration failed.');
                }

            });*/
        }
    }

    function ResponseFreeEMailSignUp(data, status) {
        ShowMessageWindow('Email registered.');
    }
    /*************************  End Free EMail SignUp    *************************/

    /*************************  Start Close Message Window  ***********************/

    function ShowMessageWindow(sMessage) {
        $('#MessageWindowContainer').setTemplateURL('../JTemplates/MessageWindow.htm', null, { filter_data: false });
        $('#MessageWindowContainer').processTemplate(sMessage);
        $("#lnkClose").click(function() {
            CloseMessageWindow();
        });
        $("#MessageWindowContainer").fadeIn('slow');
    }
    function CloseMessageWindow() {
        //$("#InnerMessageWindow").remove();
        $("#MessageWindowContainer").fadeOut('slow');
    }
    /*************************  End Close Message Window  ***********************/



    /*************************  Start JQuery Ajax Error Handler  ***********************/

    function MailError(sMessage) {
        ShowMessageWindow(sMessage);
    }
    /*************************  End  JQuery Ajax Error Handler  ***********************/
    /*************************  End Free EMail SignUp      *************************/
});