function closeCrumb(link)
{
    var crumb = $(link.closest(".crumb"));
    var popup = $("#" + crumb.attr("popuplist"));
    
    var inputs = popup.find("input");
    for(var i = 0;i<inputs.length;i++)
    {
        var input = $(inputs[i]);
        var li = $(input.closest("li"))
        if(li.attr("crumbText") == crumb.attr("myvalue"))
        {
            input.click();
        }
    }
    
    var bttn = $(popup.find(".menu-button")[0])
    bttn.click();
    crumb.remove();
}
function UpdateBreadCrumb(button)
{
    var container = $(button.closest(".menu_inner"));
    var breadCrumb = $("#map-breadcrumb");
    breadCrumb.html("");
    var inputs = container.find("input");
    for(var i = 0;i<inputs.length;i++)
    {
        var input = $(inputs[i]);
        var selectionText = $(input.closest("li")).attr("crumbText");
        var textid = selectionText.replace(/ /gi,"-").replace("&","and").replace("%", "percent"); 
        if(input.attr('checked'))
        {
           if($("#"+ textid))
            $("#"+ textid).remove();
           CreateCrumb(textid,selectionText, container.attr("id"));
        }
        else
        { 
           if($("#"+ textid))
            $("#"+ textid).remove();
        }
    }
}
function CreateCrumb(textid, selectionText, listID)
{
    var breadCrumb = $("#map-breadcrumb");
    var html = "<div class='crumb' id = '"+textid+"' popuplist='"+listID+"' myvalue='"+selectionText+"'>"+selectionText+" <a onclick ='closeCrumb($(this))' class='close-crumb'>X</a><div>"
    breadCrumb.append(html);
}
function MainMenuClick(objCheckBox, sMenuType, selectionText) {
    var temp;
    
    var objValue = objCheckBox.value;
    var iconClass = objValue;
    
    //reset search state
    //$("#txtKeyword").val("Enter Keyword");
    
    if(iconClass.toLowerCase().indexOf("shop") > -1)
    {
        iconClass = "shoppping"
    }
    else if(iconClass.toLowerCase().indexOf("event") > -1)
    {
        iconClass = "attraction";
    }
    else if(iconClass.toLowerCase().indexOf("hotel") > -1)
    {
        iconClass = "hotel";
    }
    else if(iconClass.toLowerCase().indexOf("grocery") > -1)
    {
        iconClass = "grocery";
    }
    else if(iconClass.toLowerCase().indexOf("auto") > -1)
    {
        iconClass = "auto";
    }
    else if(iconClass.toLowerCase().indexOf("services") > -1)
    {
        iconClass = "service";
    }
    
    window.CurrentIconClass = objValue;
    
    
    
    if(selectionText == "All")
    {
        var inputs = $("#popmenu1").find('input');
        if(objCheckBox.checked){
            for(var i = 0;i<inputs.length;i++){
                var inp = $(inputs[i]);
                if(inp.closest("li").attr("crumbText") == $(objCheckBox).closest("li").attr("crumbText"))
                    continue;
                
                inp.attr("checked",false)  
                sStyle = "";
                sCategory = "";
            }
        }
    }
    else{
        $('#chkAll').attr("checked",false)
    }
    
    try{
        if(objCheckBox.checked){
            
        }
        else{
            $("#" + textid).remove();
        }
    }
    catch(e){}
    if (sMenuType == "Category") {
        /*if (sCategory.length == 0) {
            temp = "," + objValue + ",";
        }
        else {
            temp = sCategory + objValue + ',';
        }*/
        
        temp = objValue;
        if (objCheckBox.checked) {
            sCategory = temp;
        }
        else {
            var sTobeReplaced = "," + objValue + ",";
            sCategory = JSReplaceAll(sCategory, sTobeReplaced, ",");
        }
        
        var menu = $($("#lnkStyleGo").closest(".menu_inner"));
        var checks = menu.find("input");
        /*for(var i =0;i<checks.length;i++)
        {
            $(checks[i]).attr("checked",false);
        }*/
        
        sStyle = "";
        
       // setCookie('Category', sCategory, false);
    }
    else {
        /*if (sStyle.length == 0) {
            temp = "," + objValue + ",";
        }
        else {
            temp = sStyle + objValue + ',';
        }*/

        temp = objValue;
        if (objCheckBox.checked) {
            sStyle = temp;
        }
        else {
            var sTobeReplaced = "," + objValue + ",";
            sStyle = JSReplaceAll(sStyle, sTobeReplaced, ",");
        }
        
        var menu = $($("#lnkCategoryGo").closest(".menu_inner"));
        var checks = menu.find("input");
        /*for(var i =0;i<checks.length;i++)
        {
            $(checks[i]).attr("checked",false);
        }*/
        sCategory = "";
       // setCookie('Style', sStyle, false);
    }
    
    //search
    var inner = $(objCheckBox).closest(".menu_inner");
    var button = $(inner).find(".menu-button");
    button.click();
}


function SubMenuClick(parentId, objCheckBox, sMenuType, webcontrolID) {
    var temp;
    document.getElementById(parentId).checked = false;

    var objValue = objCheckBox.value;

    var txtidinfo;

    if (sMenuType == "Category") {
        if (sCategory.length == 0) {
            temp = "," + objValue + ",";
        }
        else {
            temp = sCategory + objValue + ",";
        }

        if (objCheckBox.checked) {
            sCategory = temp;
        }
        else {
            var sTobeReplaced = "," + objValue + ",";
            sCategory = JSReplaceAll(sCategory, sTobeReplaced, ",");
        }
        //setCookie('Category', sCategory, false);
    }
    else {
        if (sStyle.length == 0) {
            temp = "," + objValue + ",";
        }
        else {
            temp = sStyle + objValue + ",";
        }

        if (objCheckBox.checked) {
            sStyle = temp;
        }
        else {
            var sTobeReplaced = "," + objValue + ",";
            sStyle = JSReplaceAll(sStyle, sTobeReplaced, ",");
        }
       // setCookie('Style', sStyle, false);
    }


    var webControl = document.getElementById(webcontrolID);
    var bflag = 0;
    if (webControl != null) {
        var inpsLI = webControl.getElementsByTagName("li");

        for (var iLI = 0; iLI < inpsLI.length; iLI++) {
            var inps = inpsLI[iLI].getElementsByTagName("input");

            for (var i = 0; i < inps.length; i++) {
                if (inps[i].type === "checkbox") {
                    var objCheckBox = inps[i];

                    if (objCheckBox.checked) {
                        bflag = bflag + 1;
                    }
                    else {
                        bflag = 0;
                    }
                }
            }
        }


        if (bflag == inpsLI.length) {
            document.getElementById(parentId).checked = true;
        }
        else {
            document.getElementById(parentId).checked = false;

        }

    }
}

function SubMenuParentClick(objParentCheckBox, ulId, sMenuType) {
    var bIsparentChecked = objParentCheckBox.checked;
    var sparentcheckboxvalue = objParentCheckBox.value;
    if (sMenuType == "Category") {
        sCategory = GetSelectedCheckboxes(ulId, bIsparentChecked, sCategory, sparentcheckboxvalue);
        //setCookie('Category', sCategory, false);
    }
    else {
        sStyle = GetSelectedCheckboxes(ulId, bIsparentChecked, sStyle, sparentcheckboxvalue);
       // setCookie('Style', sStyle, false);
    }
}

function GetSelectedCheckboxes(webcontrolID, bIsParentCheckBoxChecked, strIdList, sparentcheckboxvalue) {
    if (strIdList == null || strIdList == "") {
        strIdList = ",";
    }

    var webControl = document.getElementById(webcontrolID);

    if (webControl != null) {
        var inpsLI = webControl.getElementsByTagName("li");

        for (var iLI = 0; iLI < inpsLI.length; iLI++) {
            var inps = inpsLI[iLI].getElementsByTagName("input");

            for (var i = 0; i < inps.length; i++) {
                if (inps[i].type === "checkbox") {
                    var objCheckBox = inps[i];

                    var objValue = objCheckBox.value;

                    if (bIsParentCheckBoxChecked) {
                        strIdList += objValue + ",";
                    }
                    else {
                        var textValue = "," + objValue + ",";

                        strIdList = JSReplaceAll(strIdList, textValue, ",");
                    }

                    objCheckBox.checked = bIsParentCheckBoxChecked;
                }
            }
        }
        if (bIsParentCheckBoxChecked) {
            strIdList += sparentcheckboxvalue + ",";
        }
        else {
            var textValue = "," + sparentcheckboxvalue + ",";

            strIdList = JSReplaceAll(strIdList, textValue, ",");
        }


    }

    return strIdList;
}

function JSReplaceAll(suppliedString, stringtoReplace, stringByReplace) {
    var intIndexOfMatch = suppliedString.indexOf(stringtoReplace);

    // Loop over the string value replacing out each matching
    // substring.
    while (intIndexOfMatch != -1) {
        // Relace out the current instance.
        suppliedString = suppliedString.replace(stringtoReplace, stringByReplace)

        // Get the index of any next matching substring.
        intIndexOfMatch = suppliedString.indexOf(stringtoReplace);
    }

    return suppliedString;
}

function ShowSharePointsPubble()
{
    //check to ensure no others on page before rendering
    var bubbles = $(".point-bubble");
    
    if(bubbles && bubbles.length >0)
    {
        return;
    }
    var anchor = $(".fb-share-container")[0]
    if(getCookie("SharePointsBubble") || !anchor || !UserID)
        return;
    
    var status = $(document.createElement("div")).addClass("user-status");
    status.append($(document.createElement("div")).addClass("user-earned").append("Share a deal and <br /> get 20 points"));
    status.append("<div class='what-for'>(<a href = '"+rootDomain+"content/about'>What for?</a>)</div>")
    status.append($(document.createElement("div")).addClass("popout-image"));
    
    DealMapPopup.anchor = $(anchor);
    DealMapPopup.html = status;
    DealMapPopup.extraClasses = "user-status-bubble point-bubble boom";
    DealMapPopup.arrowPosition = DealMapPopupArrowPositions.bottom;
    DealMapPopup.autoDestroy = false;
    DealMapPopup.removeOtherPopups = false;
    DealMapPopup.CallBack = _ShareBubbleCallback;
    DealMapPopup.create();
    
}
function _ShareBubbleCallback()
{
    setCookie("SharePointsBubble", "1");
}

$(document).ready(function() {

    $(".deal-choice").click(function(){
        $(".menu_inner.selected-menu").removeClass("selected-menu");
        $(".deal-choice.selected").removeClass("selected");
        $(this).addClass("selected");
        
        var menuID = $(this).attr("menu");
        $("#" + menuID).addClass("selected-menu")
    })
    /*************************  Start Free EMail SignUp    *************************/
    $("#lnkSignUp1").click(function() {
    var txtSignUP2 = $('#txtSignUp1');
    if (!IsConnected) {
        ShowMessageWindow('Please login to SignUp.');
        return;
    }
        FreeEMailSignUp(txtSignUP2);
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
});

// New Clear-Text-on-Focus Function

$(document).ready(function() {
    $('input:text.inactive, textarea.inactive').each(function() { // Automatically bind to text inputs and textareas with class "inactive"
        var $this = $(this) // Cache the current object
        var example_text = $this.attr('title');
        
        $this.val(example_text);// Make sure text is reset on page load
    
        $this.focus(function() {
            if($(this).val() === example_text) {
                $(this).val('')
                    .removeClass('inactive');
            }
        });
    
        $this.blur(function() {
            if($this.val() === "") {
                $this.addClass('inactive')
                    .val(example_text);
            }
        });
    });
});

// New Promo Bar Function
$(document).ready(function() {
	/*var current_time = new Date();
	var PROMO_START_TIME = new Date(Date.UTC(2011, 3, 10, 7, 0));	// Convert to UTC for time zone precision
	var PROMO_END_TIME = new Date(Date.UTC(2011, 4, 6, 6, 59, 59));
	var show_promo = $.cookie('dealmapShowPromo');
	
	// Create and append promo bar if current time is within promo dates

	if(show_promo != 'hide' && (current_time >= PROMO_START_TIME && current_time <= PROMO_END_TIME)) {
	    var banner_markup = '<div id="promo_banner">';
	        banner_markup += '<a id="promo_link" href="http://www.facebook.com/TheDealMap?sk=app_173143722716569" target="_blank">';
	        banner_markup += '<img src="http://www.thedealmap.com/images/promo_banner/banner.png?ver=04122011.01" alt="Enter The Dealmap\'s Daily Deal Giveaway: 1 in every 10 wins a $25 restaurant gift certificate" />'
	        banner_markup += '</a>';
	        banner_markup += '<a id="close_promo_banner" href="#"><img src="http://www.thedealmap.com/images/promo_banner/close.png?ver=04122011.01" alt="Close" /></a>';
	        banner_markup += '</div>';
		
	    $('#header').append(banner_markup);
		
	    $('#close_promo_banner').click(function(event) {
	        event.preventDefault();
	        $('#promo_banner').fadeOut();
	        $.cookie('dealmapShowPromo', 'hide', {expires: 14}); // Sets cookie to not open for two weeks
	    });
	}*/

    $('#close_promo_banner').click(function(event) {
        event.preventDefault();
        $('#promo_banner').fadeOut();
        $.cookie('promotionid', $(this).attr("data-id"), { expires: 14 }); // Sets cookie to not open for two weeks
    });
    
    //Special Announcement
    $('#hide_announcement').click(function(event) {
        event.preventDefault();
        $('#announcement_banner').fadeOut();
        $.cookie('announcement', 'hide', { expires: 14 }); // Sets cookie to not open for two weeks
    });
    
});