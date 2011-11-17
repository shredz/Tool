/*************************  Start Global NameSpace  ***********************/

var EMailWindow;
var RegistrationWindow;


function getPointValue(action)
{
    if(action == 1)
        return 100;
    else if(action == 2)
        return 50;
    else if(action == 4)
        return 50;
    else if(action == 8)
        return 25;
    else if(action == 16)
        return 50;
    else if(action == 32)
        return 1;
    else if(action == 64)
        return 5;
    else if(action == 128)
        return 5;
    else 
        return 0;
}

function getUserActionDescription(action)
{
    if(action == 1)
        return "Login using facebook connect";
    else if(action == 2)
        return "Signup for fresh deal email";
    else if(action == 4)
        return "Submit an awesome deal";
    else if(action == 8)
        return "Share your favorite deal";
    else if(action == 16)
        return "Use a deal and save money";
    else if(action == 32)
        return "Give feedback on a deal";
    else if(action == 64)
        return "Post a comment a deal";
    else 
        return "";
}


/* Action codes and values
Unknown = 0,
Login = 1, //100
EmailSignup = 2, //100
DealSubmit = 4, //100
DealShare = 8, //50
DealUse = 16, //100
DealFeedback = 32, //25
DealComment = 64 //75
*/
function UpdateUserStatus(iAction, sActionData)
{
    return;   
}

function PostComment(sDealID, sComment)
{
    return;      
}

function UpdateHeaderStats(data)
{
    $("#header-points").text(data.d.Points + "pts");
    $("#header-level").addClass("level" + data.d.CurrentLevel.ID);
}
function DisplayCountDown(expDate, dvExpDateID, effDate)
{
        
    var usExpDateID = '_' + dvExpDateID;
    var objDivExpiryTimeContainer = $("[id$='" + usExpDateID + "']");

    var compDate = new Date();
    compDate = new Date(expDate); //mm/dd/yyyy
    
    var startDate; 
    
    if(effDate)
        startDate= new Date(effDate);
    
    if (objDivExpiryTimeContainer.length != 0) //Object is Available/Visible
    {
        var temp = '<div class="expires-in text-image"></div>'
                + '<div class="timeunits"><div class="expires-days clearfix">'
                + '<div class="time-value float">'
                + '{dn}</div>'
                + '<div class="float">{dl}</div>'
                + '</div>'
                + '<div class="expires-hours clearfix">'
                + '<div class="time-value float">'
                + '{hn}</div>'
                + '<div class="float">'
                + '{hl}</div>'
                + '</div>'
                + '<div class="expires-minutes clearfix">'
                + '<div class="time-value float">'
                + '{mn}</div>'
                + '<div class="float">'
                + '{ml}</div>'
                + '</div>'
                + '<div class="expires-seconds clearfix">'
                + '<div class="time-value float">'
                + '{sn}</div>'
                + '<div class="float">'
                + '{sl}</div>'
                + '</div>'
                + '</div>';
                
            var diff = compDate - new Date();
            var timespan = 1000 * 60 * 60 *24 * 7;
            var alreadyStarted = startDate.valueOf() < new Date().valueOf();
                        new Date().valueOf()
            if(diff > 1000 * 60 * 60 *24 * 3)
            {
                var temp;
                if(compDate.getFullYear() < 9000){   
                    //temp= "<div class='expires expires-on'>Expires on</div><div class='expires-date'>"+(compDate.getMonth() +1) + "/" + compDate.getDate() + "/" +compDate.getFullYear()+"</div>"
                        var css = !alreadyStarted ? "deal-starts" : "expires-on";
                        
                        temp = '<div class="text-image '+css+'"></div>'
                        if(!alreadyStarted)
                        {
                            temp+= '<div class="deal-start">'+(startDate.getMonth() +1) + "/" + startDate.getDate() + "/" +startDate.getFullYear()+'</div>'
                            temp+='<div  class="deal-ends">Expires '+(compDate.getMonth() +1) + "/" + compDate.getDate() + "/" +compDate.getFullYear()+'</div>'
                        }
                        else{
                            temp+='<div  class="deal-start">'+(compDate.getMonth() +1) + "/" + compDate.getDate() + "/" +compDate.getFullYear()+'</div>'
                        }
                        
                }
                else
                {
                    temp = "";
                    $("[id$='_ExpiryTimeContainer']").css("border","none");
            
                }    
                $("[id$='_ExpiryTimeContainer']").html(temp);
                return;
            }
            else if (diff<0)
            {
                var temp = "<div class='text-image expires-on'></div><div class='expires-date'>"+(compDate.getMonth()+1) + "/" + compDate.getDate() + "/" +compDate.getFullYear()+"</div>"
            
                $("[id$='_ExpiryTimeContainer']").html(temp);
                return;
            }
            else{
            //    $("[id$='_ExpiryTimeContainer']").countdown({ until: compDate, serverSync: GetCurrentServerDate, format: 'DHMS',
            $("[id$='_ExpiryTimeContainer']").countdown({ until: compDate, format: 'DHMS',
                layout: temp
            });
        }
    }
}

function mapsAPILoaded()
{
    if (google &&
        google.loader &&
        google.loader.ClientLocation)
    {
        if (google.loader.ClientLocation.address.city)
            return google.loader.ClientLocation.address.city;
        sLatitude = google.loader.ClientLocation.latitude;
        sLongitude = google.loader.ClientLocation.longitude;
    }

    if (sLocation)
        return sLocation;
}

function clearText(field)
{

    if (field.defaultValue == field.value) field.value = '';
    else if (field.value == '') field.value = field.defaultValue;

}
function Test()
{
    alert('Test');
}
function selectMenuInputs(sCategory, sStyle)
{
    if (sCategory == null)
        sCategory = '';

    if (sStyle == null)
        sStyle = '';

    var sInputs = sCategory + ',' + sStyle;
    var sinputarry = sInputs.split(",");
    var inps = document.getElementsByTagName("input");

    for (var i = 0; i < inps.length; i++)
    {
        if (inps[i].type === "checkbox")
        {
            var objCheckBox = inps[i];
            var objValue = objCheckBox.value;
            var objid = objCheckBox.id;

            for (var j = 0; j <= sinputarry.length - 1; j++)
            {

                if (objValue == sinputarry[j])
                {
                    document.getElementById(objid).checked = true;

                }
            }
        }
    }
}


function setCookie(name, value, expiresDate)
{
    $.cookie(name, null);
    var date = new Date();
    date.setTime(date.getTime() + (3 * 24 * 60 * 60 * 1000));
    $.cookie(name, value, { path: '/', expires: expiresDate ? expiresDate : date });

}

function getCookie(name)
{
    return $.cookie(name);
}

function deleteCookie(name)
{
    $.cookie(name, '', { expires: -1 });
}

function LTrim(value)
{

    var re = /\s*((\S+\s*)*)/;
    return value.replace(re, "$1");

}

// Removes ending whitespaces
function RTrim(value)
{

    var re = /((\s*\S+)*)\s*/;
    return value.replace(re, "$1");

}



/*function OpenEMailPopUp()
{
   EMailWindow = dhtmlmodal.open('agebox', 'div', 'EMailPopUp', 'Send Mail', 'width=475px,height=375px,left=300px,top=200px,resize=0,scrolling=0')
}*/

function OpenEMailPopUp(IsAbuse, sTitle, sDesc)
{

    EMailWindow = dhtmlmodal.open('agebox', 'div', 'EMailPopUp', 'Send Mail', 'width=475px,height=375px,left=300px,top=200px,resize=0,scrolling=0');
    if (IsAbuse == true)
    {
        var txtTo = $("#txtTo");
        txtTo.val('abuse@thedealmap.com');
        sTitle = "Report Abuse: " + sTitle;
    }
    var txtSubject = $("#txtSubject");
    var txtBody = $("#txtBody");

    sTitle = unescape(sTitle);
    sDesc = unescape(sDesc);

    txtSubject.val(sTitle);
    txtBody.val(sDesc);
}

function CloseEMailPopUp()
{
    EMailWindow.hide();
}

function OpenRegistrationForm()
{
    RegistrationWindow = dhtmlmodal.open('agebox', 'div', 'registerProfileDiv', 'Centerd Registration Form', 'width=400px,height=225px,left=300px,top=200px,resize=0,scrolling=0')
}

function CloseRegistrationForm()
{
    setCookie('isInterested_' + UserID, 'false');
    RegistrationWindow.hide();
}

function capitalizeMe(val)
{
    newVal = '';
    val = val.split(' ');
    for (var c = 0; c < val.length; c++)
    {
        newVal += val[c].substring(0, 1).toUpperCase() +
val[c].substring(1, val[c].length).toLowerCase() + ' ';
    }
    return newVal;
}

//function SendMail1(txtFrom, txtTo, txtSubject, txtBody, lblMessage) {
function SendMail()
{
    var txtFrom = $("#txtFrom");
    var txtTo = $("#txtTo");
    var txtSubject = $("#txtSubject");
    var txtBody = $("#txtBody");
    var lblMessage = $("#lblMsgEMail");

    var sFrom = LTrim(RTrim(txtFrom.val()));
    var sTo = LTrim(RTrim(txtTo.val()));
    var sSubject = LTrim(RTrim(txtSubject.val()));
    var sBody = LTrim(RTrim(txtBody.val()));
    if (sFrom == '')
    {

        lblMessage.html('<b>Enter a valid email address</b>');
        txtFrom.focus();
        return;
    }
    else
        if (!IsValidEmail(sFrom))
    {

        lblMessage.html('<b>Enter valid email address</b>');
        txtFrom.focus();
        return;
    }

    if (sTo == '')
    {
        txtTo.focus();
        return;
    }
    else
        if (!IsValidEmail(sTo))
    {

        lblMessage.html('<b>Enter valid email address</b>');
        txtTo.focus();
        return;
    }

    if (sSubject == '')
    {
        lblMessage.html('<b>Subject is required.</b>');
        txtSubject.focus();
        return;
    }

    if (sBody == '')
    {
        lblMessage.html('<b>Body cannot be empty.</b>');
        txtBody.focus();
        return;
    }

    $("#MailLoading").show();
    $.ajax({

        type: "POST",

        url: "../default.aspx/SendMail",

        data: "{'sFromEmail':'" + sFrom + "','sToEmail':'" + sTo + "','sMailSubject':'" + sSubject + "','sMailBody':'" + sBody + "'}",

        contentType: "application/json; charset=utf-8",

        dataType: "json",

        success: ResponseSendMail,
        error: function()
        {
            MailError(lblMessage, 'Error in sending EMail.');
        }
    });
}

function ResponseSendMail(data, iCurrentPage)
{
    $("#MailLoading").hide();
    alert('EMail sent successfully.');
    EMailWindow.hide();
}

function MailError(lblMessage, sMessage)
{
    $("#MailLoading").hide();
    lblMessage.html('<b>' + sMessage + '</b>');
}

function RegisterUser()
{
    var txtEMail = $("#txtEMail");
    var lblMessage = $("#lblMsgRegister");
    var sEMail = LTrim(RTrim(txtEMail.val()));

    if (sEMail == '')
    {
        lblMessage.html('<b>Enter a valid email address</b>');
        txtEMail.focus();
        return;
    }
    else
        if (!IsValidEmail(sEMail))
    {
        lblMessage.html('<b>Enter valid email address</b>');
        txtEMail.focus();
        return;
    }

    $("#RegisterLoading").show();
    $.ajax({

        type: "POST",

        url: "../default.aspx/Register",

        data: "{'sEMail':'" + sEMail + "'}",

        contentType: "application/json; charset=utf-8",

        dataType: "json",

        success: function()
        {
            ResponseRegisterUser(lblMessage, 'Congratulations, your registration to Deal Map is successful.');
        },
        error: function()
        {
            RegisterError(lblMessage, 'Your registration to Deal Map is unsuccessful. Please try again later.');
        }
    });
}


function ResponseRegisterUser(lblMessage, sMessage)
{
    $("#RegisterLoading").hide();
    alert('Congratulations, your registration to Deal Map is successful.');
    RegistrationWindow.hide();
}

function RegisterError(lblMessage, sMessage)
{
    $("#RegisterLoading").hide();
    lblMessage.html('<b>' + sMessage + '</b>');
}

function ShowMessageWindow(sMessage) {
$('#MessageWindowContainer').setTemplateURL(rootDomain + 'JTemplates/MessageWindow.htm', null, { filter_data: false });
$('#MessageWindowContainer').processTemplate(sMessage);
$("#MessageWindowContainer").fadeIn('slow');
$("#lnkClose").click(function() {
CloseDivs();
CloseMessageWindow();
return false;
});
}

function GetTimeToExpire(ExpiryDate)
{

    var currentDate = new Date(CurrentDate);
    var expiryDate = new Date(ExpiryDate);

    if (expiryDate == "Invalid Date")
        return ":::";

    diff = new Date();

    diff.setTime(Math.abs(expiryDate.getTime() - currentDate.getTime()));
    timediff = diff.getTime();

    days = Math.floor(timediff / (1000 * 60 * 60 * 24));
    timediff -= days * (1000 * 60 * 60 * 24);

    hours = Math.floor(timediff / (1000 * 60 * 60));
    timediff -= hours * (1000 * 60 * 60);

    mins = Math.floor(timediff / (1000 * 60));
    timediff -= mins * (1000 * 60);

    secs = Math.floor(timediff / 1000);
    timediff -= secs * 1000;

    return days + ":" + hours + ":" + mins + ":" + secs;
}

function GetFullDate(OldDate, returnDateTime)
{
    if (OldDate.toString().indexOf('Date') >= 0)
    {
        //here we will try to extract the ticks from the Date string in the "value" fields of JSON returned data
        tempDate = /^\/Date\((-?[0-9]+)\)\/$/.exec(OldDate);
        if (tempDate)
        {
            var dt = new Date(parseInt(tempDate[1], 10));
            
            return returnDateTime ? dt : dt.toString();
        }
    }
}
function GetShortDate(OldDate)
{
    if (OldDate != null)
    {
        if (OldDate.toString().indexOf('Date') >= 0)
        {
            //here we will try to extract the ticks from the Date string in the "value" fields of JSON returned data
            tempDate = /^\/Date\((-?[0-9]+)\)\/$/.exec(OldDate);
            if (tempDate)
            {
                var dt = new Date(parseInt(tempDate[1], 10));
                //getMonth return months with index 0 so you need to add 1 to get the correct month value.  
                return dt.getMonth() + 1 + "/" + dt.getDate() + "/" + dt.getFullYear();
            }
        }
    }
    else
        return "";
}

function datediff(date1, date2, interval)
{
    var second = 1000, minute = second * 60, hour = minute * 60, day = hour * 24, week = day * 7;
    date1 = new Date(date1);
    date2 = new Date(date2);
    var timediff = date2 - date1;
    if (isNaN(timediff)) return NaN;
    switch (interval)
    {
        case "years": return date2.getFullYear() - date1.getFullYear();
        case "months": return (
            (date2.getFullYear() * 12 + date2.getMonth())
            -
            (date1.getFullYear() * 12 + date1.getMonth())
        );
        case "weeks": return Math.floor(timediff / week);
        case "days": return Math.floor(timediff / day);
        case "hours": return Math.floor(timediff / hour);
        case "minutes": return Math.floor(timediff / minute);
        case "seconds": return Math.floor(timediff / second);
        default: return undefined;
    }
}


function GetImageURL(sCategory, source, dealType)
{
    var imageURL;
    
    if(!sCategory) 
    {sCategory = "";}
    
    if(!source) 
    {source = "";}
    
    if(source == "Crocs")
    {
        imageURL = "../Images/pointer_croc.png";
    }
    else if(source == "Groupon")
    {
        imageURL = "../Images/pointer_24.png";
    }
    else if(sCategory == '"Black Friday"')
    {
        imageURL = "../Images/pointer_black_friday.png";
    }
    else if (dealType && dealType == "16")
    {
        imageURL = "../Images/pointer_16.png";
    }
    else if(sCategory.toLowerCase().indexOf("kid-friendly") > -1)
    {
        imageURL = "../Images/pointer_19.png";
    }
    else if(sCategory.toLowerCase().indexOf("expires") > -1)
    {
        imageURL = "../Images/pointer_14.png";
    }
    else if(sCategory.toLowerCase().indexOf("over-50%-off") > -1)
    {
        imageURL = "../Images/pointer_15.png";
    }
    else if(sCategory.toLowerCase().indexOf("dealmap-favorites") > -1)
    {
        imageURL = "../Images/pointer_12.png";
    }
    else if(sCategory.toLowerCase().indexOf("group-friendly") > -1)
    {
        imageURL = "../Images/pointer_22.png";
    }
    else if(sCategory.toLowerCase().indexOf("romantic") > -1)
    {
        imageURL = "../Images/pointer_21.png";
    }
    else if (sCategory.toLowerCase().indexOf("restaurant") > -1 ||
        source == "Restaurant" || source == "GrubHub")
    {
        imageURL = "../Images/pointer_1.png";
    }
    else if ((sCategory.toLowerCase().indexOf("health") > -1)|| (sCategory.toLowerCase().indexOf("beauty") > -1))
    {
        imageURL = "../Images/pointer_2.png";
    }
    else if (sCategory.toLowerCase().indexOf("shopping") > -1)
    {
        imageURL = "../Images/pointer_3.png";
    }
    else if (sCategory.toLowerCase().indexOf("attraction") > -1 ||
        source == "Goldstar")
    {
        imageURL = "../Images/pointer_4.png";
    }
    else if (sCategory.toLowerCase().indexOf("hotel") > -1 ||
        source == "Hotels" || source == "Booking" || 
        source == "Expedia" || source == "TravelZoo" 
        || source == "FlyCoupon")
    {
        imageURL = "../Images/pointer_5.png";
    }
    else if (sCategory.toLowerCase().indexOf("bar") > -1)
    {
        imageURL = "../Images/pointer_1.png";
    }
    else if (sCategory.toLowerCase().indexOf("grocery") > -1)
    {
        imageURL = "../Images/pointer_6.png";
    }
    else if (sCategory.toLowerCase().indexOf("auto") > -1)
    {
        imageURL = "../Images/pointer_7.png";
    }
    else if (sCategory.toLowerCase().indexOf("service") > -1)
    {
        imageURL = "../Images/pointer_9.png";
    }
    else if (sCategory.toLowerCase().indexOf("home") > -1 ||
        sCategory.toLowerCase().indexOf("contract") > -1)
    {
        imageURL = "../Images/pointer_10.png";
    }
    else if (sCategory.toLowerCase().indexOf("medical") > -1 ||
        sCategory.toLowerCase().indexOf("dental") > -1)
    {
        imageURL = "../Images/pointer_11.png";
    }
    else if (source == "Valpak" || source == "CitySearch")
    {
        imageURL = "../Images/pointer_18.png";
    }
    else if (source == "DealMap")
    {
        imageURL = "../Images/pointer_13.png";
    }
    else
    {
        imageURL = "../Images/pointer_3.png";
    }

    return imageURL;
}

/*************************  End Global NameSpace  ************************************/
function ChangeInCategoryGoToHomePage(sLocation, sCategory)
{

    setCookie('CurrentLocation', sLocation);
    setCookie('CurrentMapType', 'Normal');
    setCookie('Category', sCategory);
    setCookie('Style', '');
    setCookie('Keyword', '');

    window.location = '../Default.aspx';
    return false;
}

function ChangeInStyleGoToHomePage(sLocation, sStyle)
{

    setCookie('CurrentLocation', sLocation);
    setCookie('CurrentMapType', 'Normal');
    setCookie('Category', '');
    setCookie('Style', sStyle);
    setCookie('Keyword', '');

    window.location = '../Default.aspx';
    return false;
}

function GoToHomePage()
{
    window.location = '../Default.aspx';
    return false;
}


function IsValidEmail(email)
{

    var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;

    return filter.test(email);

}

function GoToDealDetail(iDealId)
{
    window.open(rootDomain + 'deal/?DealId=' + iDealId);
}

function PostFaceBook(url, title, description)
{

    url = unescape(url);
    title = unescape(title);
    description = unescape(description);
    window.open('http://www.facebook.com/sharer.php?u=' + encodeURIComponent(url) + '&t=' + encodeURIComponent(title) + '&d=' + encodeURIComponent(description), 'sharer', 'toolbar=0,status=0,width=626,height=436'); return false;
    return false;
}

function PostShareThis(url, title, description, idinfo)
{
    url = unescape(url);
    title = unescape(title);
    description = unescape(description);
    var object;
    object = SHARETHIS.addEntry({
        title: title,
        summary: description,
        url: url
    },
            { button: false });

    custom(object, idinfo);
    return false;
}

function custom(sharelet, idinfo)
{

    sharelet.attachButton(idinfo);
    return false;
};


function PostTwitter(url)
{
    url = unescape(url);
    window.open('http://api.tweetmeme.com/share?url=' + url, 'sharer', 'toolbar=0,status=0,width=626,height=436');
    return false;
}

$(document).ready(function()
{

    /*************************  Start Go To Home Page  ***********************/
    $("#lnkHomePage").click(function()
    {
        GoToHomePage();
    });


    /*************************  End Go To Home Page  ***********************/


    /*************************  Start Add a Deal  ***********************/
    //    $("#lnkAddDeal").click(function() {
    //        AddDeal('');
    //    });

    function AddDeal(sDealType)
    {
        window.location = '../submit';
    }
    /*************************  End Add a Deal  ***********************/


    /*************************  End  JQuery Ajax Error Handler  ***********************/



});


function CreateUserStatusPopup(anchor)
{   
    if(!HeaderCurrentUser)
    {  
        return;
    }
    var pointsAway = HeaderCurrentUser.d.NextLevel.PointLimit - HeaderCurrentUser.d.Points;
    var status = $(document.createElement("div")).addClass("user-status");
    status.append($(document.createElement("a")).addClass("user-name").text(HeaderCurrentUser.d.Name).attr("href",rootDomain + "userprofile"));
    status.append($(document.createElement("div")).addClass("user-level").text("Level " + HeaderCurrentUser.d.CurrentLevel.ID));
    status.append($(document.createElement("div")).addClass("user-points").text(HeaderCurrentUser.d.Points +" pts"));
    status.append(CreateUserCountMessage("Badges Earned:", HeaderCurrentUser.d.Badges.length, "user-badges"));
    status.append(CreateUserCountMessage("Deals Submitted:", HeaderCurrentUser.d.DealsSubmitted, "user-deals"))
    status.append($(document.createElement("div")).addClass("user-next-level").text(pointsAway + " points to level " + HeaderCurrentUser.d.NextLevel.ID));
    
    DealMapPopup.anchor = anchor;
    DealMapPopup.html = status;
    
    DealMapPopup.extraClasses = "user-status-bubble" ;
    DealMapPopup.create();
}

function updateUPEmail()
{
    var em = $(".new-level-bubble input").val();
    var id = "";
    if(!VerifyValidEmailAddress(em) || !HeaderCurrentUser || !HeaderCurrentUser.d)
    {
        return;
    }
    id = HeaderCurrentUser.d.ID;
    $.ajax({

        type: "POST",

        url: rootDomain + "userprofile/default.aspx/AddEmail",

        data: "{'em':'" + em +"','userID':'"+id+"'}",

        contentType: "application/json; charset=utf-8",

        dataType: "json",

        success: function(data) { 
        },
        error: function (data)
        {
        }
    });
    
    $(".new-level-bubble").remove();
}

function UserAchievedNewLevel()
{
    if(!HeaderCurrentUser || !HeaderCurrentUser.d || !HeaderCurrentUser.d.CurrentLevel || !HeaderCurrentUser.d.NextLevel)
        return;
        
        
    var closeBubble = function(){
        $(".new-level-bubble").remove();
    };
    var bubble = createDOMElement("div", "new-level-bubble clearfix");
    
    var closeContainer = createDOMElement("div", "close-x-container");
    var closex = createDOMElement("a", "close-x");
    closex.click(function(){
        closeBubble();
    })
    
    closeContainer.append(closex);
    bubble.append(closeContainer);
    
    var message = createDOMElement("div", "new-level-message");
    var currentlLevel = HeaderCurrentUser.d.CurrentLevel.ID;
    var nextLevel = HeaderCurrentUser.d.NextLevel.ID;
    var nextPoints = HeaderCurrentUser.d.NextLevel.PointLimit - HeaderCurrentUser.d.Points;
    message.text("Congrats! The Deal Hero Council has approved your status as a Level "+currentlLevel+" Deal Hero. (Only "+nextPoints+" more to Level "+nextLevel+").  Please give us your email address so we can update you when you earn rewards.");
    bubble.append(message);

    var actions = createDOMElement("div", "new-level-actions clearfix");
    
    var input = createDOMElement("input","rounded-text-input float");
    input.attr("type", "text");
    var DefaultVal = "Enter email address";
    input.val(DefaultVal);
    input.focus(function(){
        var me = $(this);
        if(me.val()== DefaultVal)
        {
            me.val("");
        } 
        else
        {
            me.select();
        }
    });
    actions.append(input);
    
    var button = createDOMElement("a", "submit-button float");
    button.click(function(){
        updateUPEmail();
    })
    actions.append(button);
    
    bubble.append(actions);
     
    $("body").append(bubble);
}

function GiveUserPoints(anchor, points, data)
{
    var pointsAway = data.d.NextLevel.PointLimit - data.d.Points;
    var status = $(document.createElement("div")).addClass("user-status");
    status.append($(document.createElement("div")).addClass("user-earned").text("You just earned"));
    status.append($(document.createElement("div")).addClass("user-earned-points").text(points + " " + (points !=1 ? "points" : "point")));
    status.append($(document.createElement("div")).addClass("user-next-level").text("(only "+pointsAway+" points to level "+data.d.NextLevel.ID+")"));
    status.append($(document.createElement("div")).addClass("popout-image"));
    
    DealMapPopup.anchor = anchor;
    DealMapPopup.html = status;
    
    var statusClasses = new Array();
    statusClasses[0] = "pow";
    statusClasses[1] = "snap";
    statusClasses[2] = "poof";
    statusClasses[3] = "zap";
    statusClasses[4] = "boom";
    statusClasses[5] = "bang";
    statusClasses[5] = "shazzaam";
    statusClasses[6] = "splat";
    
    var rand = Math.floor(Math.random() * statusClasses.length);
    var pointClass = statusClasses[rand]
    
    DealMapPopup.extraClasses = "user-status-bubble point-bubble " + pointClass ;
    DealMapPopup.create();
    
    //check to see if user has achieved a new level
    
    try{
        if(HeaderCurrentUser && HeaderCurrentUser.d && data && data.d && HeaderCurrentUser.d.NextLevel.ID != data.d.NextLevel.ID)
        {
            UserAchievedNewLevel();
        }   
    }
    catch(e){}
    HeaderCurrentUser = data;
}


function _SigninBubbleCallback()
{
    setCookie("HeaderSignInPointsBubble", "1")
}

function CreateUserCountMessage(message, count, className)
{
    var div = $(document.createElement("div")).addClass(className + " user-counts");
    var message = $(document.createElement("span")).text(message);
    var count = $(document.createElement("span")).addClass("count").text(count);
    div.append(message).append(count);
    
    return div;
}

var HeaderCurrentUser;
function SetCurrentUser()
{
    if(!UserID)
        return;
        
    $.ajax({

        type: "POST",

        url: rootDomain + "userprofile/default.aspx/GetUserStatus",

        data: "{'sUserID':'" + UserID +"'}",

        contentType: "application/json; charset=utf-8",

        dataType: "json",

        success: function(data) {
            HeaderCurrentUser = data;  
        },
        error: function (data)
        {
            //document.write(data.responseText);
        }
    });   
}

SetCurrentUser();
//Auto completer stuff
function SetUpAutocompleter(url,
                            params,
                            elementID, 
                            width, 
                            parseFunction, 
                            onItemSelectCallback)
{

    if(!parseFunction)
        parseFunction = SetUpAutocompleter_ParseJson;
        
    var options = 
    {
        width:width, 
        extraParams:params,
        onItemSelected:onItemSelectCallback,
        cacheLength:10,
        parse:parseFunction
    };
    $("#" + elementID).autocomplete(url, options);
}
function SetUpAutocompleter_ParseJson(data)
{
    var parsed = [];
    var results = eval(data);
    for(var i = 0;i<results.length;i++)
    {   
        var parts = results[i].split(",");
        var row = results[i];
        var arr = new Array();
        arr.push(row);
        
        parsed[parsed.length] = {
			data: arr,
			value: row,
			result: row
		};
    }
    
    return parsed;
}
function VerifyValidEmailAddress(email)
{
    var emailpat = /^([a-zA-Z0-9])+([\.a-zA-Z0-9_-])*@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-]+)+$/;
    if(!email){return false;}
    else{
        return emailpat.test(email)
    }
}

function GenerateEmailCapture(city, location)
{
    
    if(getCookie("hideemailcapture"))
        return;
        
    try
    {
        $(".email-capture").remove();
    }
    catch(err){}
        
    var container = createDOMElement("div", "heavy-border-bubble email-capture clearfix");
    
    var tl = createDOMElement("div", "tl black-corner")
    var tr = createDOMElement("div", "tr black-corner");
    var tb = createDOMElement("div", "border top-border");
    var bb = createDOMElement("div", "border bottom-border");
    var rb = createDOMElement("div", "border right-border");
    var lb = createDOMElement("div", "border left-border");
    var closeX = createDOMElement("a", "close-x");
    closeX.click(function(){closeEmailCapture(false)})
    
    container.append(tl).append(tr).append(bb).append(tb).append(rb).append(lb).append(closeX);
    
    var leftRail = createDOMElement("div", "left-rail float");
    
    var message = createDOMElement("div", "capture-message");
    message.text("Get the " + capitalizeMe(city) + " Daily Deals email");
    leftRail.append(message);
    
    
    var description = createDOMElement("div", "email-description");
    description.text("The best deals all in one email.  Save up to 90% on great local businesses");
    leftRail.append(description);
    
    /*<input type="text" name="textfield" size="20" value="Enter your email address" id="emailCaptureText" class="input float signup-input">*/
    var input = createDOMElement("input", "input float signup-input");
    input.attr("id", "email-capture-input").attr("name", "textfield").attr("value", "Enter your email address").attr("type", "text");
    input.focus(function(){$(this).val("")})
    
    leftRail.append(input);
    
    var signupButton = createDOMElement("a", "float sign-up-button")
    signupButton.click(function(){CreateEmailSignup(location);})
    leftRail.append(signupButton);
    
    var actionLinks = createDOMElement("div", "float close-links-container clearfix");
    var later =createDOMElement("a", "close-email-link close-later").text("Remind me later");
    later.click(function(){
        closeEmailCapture(false);
    })
    actionLinks.append(later);
    
    var noThanks = createDOMElement("a", "close-email-link close-no-thanks").text("No thanks");
    noThanks.click(function(){
        closeEmailCapture(true);
    })
    actionLinks.append(noThanks);
    leftRail.append(actionLinks);
    
    leftRail.append("<div class='clear'></div>")
    
    var disclaimer = createDOMElement("div","email-disclaimer");
    var discMessage = createDOMElement("span").text("We won't share your email with anyone.  View our ");
    disclaimer.append(discMessage);
    
    var discLink = createDOMElement("a");
    discLink.attr("href", rootDomain + "content/privacy/").attr("target", "_blank").text("privacy policy");
    disclaimer.append(discLink);
    
    leftRail.append(disclaimer);
    container.append(leftRail);
    
    var rightRail = createDOMElement("div", "right-rail float")
    
    var followMessage = createDOMElement("div", "follow-message").text("And follow us to get great deals");
    rightRail.append(followMessage);
    
    var socailContainer = createDOMElement("div", "clearfix follow-links");
    var twitter = createDOMElement("a", "social-icon twitter").attr("target", "_blank").attr("href", "http://twitter.com/thedealmap");
    var fb = createDOMElement("a", "social-icon facebook").attr("target", "_blank").attr("href", "http://www.facebook.com/pages/The-Dealmap/109344502435944?v=wall");
    socailContainer.append(twitter).append(fb);
    
    rightRail.append(socailContainer);
    container.append(rightRail);
    
    $("body").append(container);
    
    var autoClose = function()
    {
        try
        {
            container.hide();
        }
        catch(err){}
    }
    
    setTimeout(autoClose, 1000 * 60)
}

function closeEmailCapture(setHideCookie)
{
    $(".email-capture").remove();
    
    if(setHideCookie)
    {
        setCookie("hideemailcapture", "1");
    }
}

function createDOMElement(el, css)
{
    return $(document.createElement(el)).addClass(css);
}

function ___trck(sType, sCity, sState, sBusinessName, sTitle, sSource, sID)
{
    if(!_gat)
        return;

    if(sType && sCity && sState && sBusinessName && sTitle && sSource && sID)
    {
        try
        {
            var trurl = sType + "/" + sCity.toLowerCase().replace(/ /g, '-').replace(/,/g, '') + "-" + sState.toLowerCase() + "/" + sSource.toLowerCase() + "/"  + sBusinessName.toLowerCase().replace(/ /g, '-') + "/" + sTitle.toLowerCase().replace(/ /g, '-') + "/" + sID;
            var pageTracker = _gat._getTracker("UA-1109899-8");
            if(pageTracker)
                pageTracker._trackPageview(trurl);  
        }
        catch(err)
        {
        }
        
        return true;
    }
}

/* header email signup section */
function HideHeaderSignup(DropCookie)
{
    var container = $("#HeaderEmailSignup");
    
    
    $(".signup-arrow").removeClass("arrow-close").addClass("arrow-open")
    
    container.hide();
    
    if(DropCookie)
    {
        var date = new Date();
        date.setTime(date.getTime() + (30 * 24 * 60 * 60 * 1000)); //30 day cookie
        setCookie("hideHeaderSignup", "1", date);
    }
}

function ShowHeaderSignup()
{
    var container = $("#HeaderEmailSignup");
    
    $(".signup-arrow").removeClass("arrow-open").addClass("arrow-close");
    
    container.show();
    
    deleteCookie("hideHeaderSignup");
}

function ToggleHeaderSignup()
{
    var container = $("#HeaderEmailSignup");
    
    if(container.css("display") == "none")
    {
        ShowHeaderSignup();   
    }
    else{
        HideHeaderSignup();
    }
}

function HeaderSignupEmail()
{
    var location = $('#HeaderSignupLocation').val();
    var email = $("#HeaderEmailSignup .email-input").val();
    
    if(!VerifyValidEmailAddress(email))
    {
        alert("Please enter a valid email address for The Dealmap daily deals emails");
        return;
    }
    
    var url = rootDomain + "signup/emails/?em=" + email;
    window.open(url);   
}


function CheckSupportedCity(location, callback)
{
    var d = "{'sLocation':'" +location + "'}";
            
    $.ajax({
        type: "POST",
        url: rootDomain + "default.aspx/CheckSupportedCity",
        data: d,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            var city = data.d;
            callback(city, location);
        }
    });
}

function _UpdateHeaderEmailSignupLocation(city, location)
{
    if(!city){ return; }
    var cityName = city.CityName;
    var twitterID = city.TwitterID;
    var fburl = city.FacebookURL;
    if(cityName)
    {   
        $("#HeaderSignupLocation").val(location);
        
        var html = "Get the <span class='city-display'>"+cityName+"</span> Daily Deals Email:";
        $('#headerLocationMessage').html(html);
    }
    else
    {
        $("#HeaderSignupLocation").val("");
        
        var html = "Get the Daily Deals Email:";
        $('.header-signup-text').html(html);
    }
    
    
    var tb = $(".header-follow-container .twitter")
    if(twitterID)
    {
        var url = "http://twitter.com/" + twitterID.toLowerCase();
        tb.attr("href", url)
    }
    else{
        var url = "http://twitter.com/thedealmap";
        tb.attr("href", url)
    }
    
    var fb = $(".header-follow-container .facebook")
    if(fburl)
    {
        fb.attr("href", fburl);
    }
    else{
        fb.attr("href", "http://www.facebook.com/thedealmap");
    }
    
    $(".header .city-display").text(cityName);
}

function UpdateHeaderEmailSignupLocation(location)
{
    //update the rss feed
    try{
        var rss = $('.rss');
        var cleanedLocation = location.replace(/ /g, "-").replace(/,/g,"").toLowerCase();
        var rssURL = "http://www.thedealmap.com/cities/"+cleanedLocation+"/deals/rss";
        rss.attr("href", rssURL);
    }
    catch(Error){}
    
    CheckSupportedCity(location, _UpdateHeaderEmailSignupLocation);
}

function hideIphoneBubble()
{
    $(".header-alert-message").remove();
    
    //set the cookies
    setCookie("HideBlackFridayMessage", "1");
}

/* Fake Select */
function setUpFakeSelect()
{
    var select = $(".fake-select");
    var options = $(".fake-select .fake-option")
    var item = $(".fake-select .selected-item");
    
    var setItem = function(setOpt){
        select.find(".selected").removeClass("selected");
        item.text(setOpt.text()).attr("optvalue", setOpt.attr("optvalue"));
        setOpt.addClass("selected");
    }
    
    //set up the first value
    setItem($(options[0]));
    
    for(var i = 0;i<options.length;i++)
    {
        var opt = $(options[i]);
        opt.click(function(){
            setItem($(this));
            $(this).closest(".fake-select").removeClass("opened");
        })
    }
    
    $(".fake-select-wrapper .select-arrow, .fake-select-wrapper .selected-item").click(function(){
        $($($(this).closest(".fake-select-wrapper")).find(".fake-select")).toggleClass("opened");
    })
}

function getFakeSelectValue(fakeSelect)
{
    var val = $($(fakeSelect).find(".fake-select .selected-item")).attr("optvalue");
    return val;
}