$(document).ready(function()
{
    $('#lnkAddDeal').click(function(e)
    {
        if ($("[id$='_hdnAnanomusUser']").val() == '0')
        {
            window.location = '../submit';
        }
        else
        {
            window.location = '../submit';
        }
    });

});