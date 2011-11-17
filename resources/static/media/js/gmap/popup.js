var DealMapPopupArrowPositions = {top:"top", left:"left", bottom:"bottom", topLeft:"top-left"};
var DealMapPopup =
{
    html:"",
    title:"",
    titleClick:null,
    anchor:null,
    extraClasses:"",
    autoDestroy:true,
    arrowPosition: DealMapPopupArrowPositions.top,
    allowFixedPosition:true,
    BubblePosition:null,
    RenderBubble:true,
    removeOtherPopups: true,
    CallBack: null,
    HideAllPopups:function()
    {
        try{
            var bubbles = $(".popup-bubble");
            
            for(var i = 0;i<bubbles.length;i++)
            {
                $(bubbles[i]).remove();
            }
        }
        catch(e){}
    },
    create:function()
    {
        if(!this.anchor)
            return;
        if(this.removeOtherPopups)
            this.HideAllPopups();
        var bubble = $(document.createElement("div")).addClass("popup-bubble clearfix").addClass(this.arrowPosition + "-arrow");
        
        bubble.achorElement = this.anchor;
        var anch = this.anchor;
        
        
        if(bubble.achorElement && $(bubble.achorElement).attr('id') && this.openBubblesAnchors[bubble.achorElement.attr('id')])
            return;
            
        var fixedCheck = function()
            {
                if(bubble && anch)
                    DealMapPopup.setFixedPosition(bubble, anch);
            }
        fixedCheck();
        
        $(window).scroll(fixedCheck);
        
        var wrapper = $(document.createElement("div")).addClass("bubble-wrapper");
        
        if(this.RenderBubble){
        /*
        wrapper.append($(document.createElement("div")).addClass("tr corner"));
        wrapper.append($(document.createElement("div")).addClass("br corner"));
        wrapper.append($(document.createElement("div")).addClass("tl corner"));
        wrapper.append($(document.createElement("div")).addClass("bl corner"));
        
        wrapper.append($(document.createElement("div")).addClass("top-border border"));
        wrapper.append($(document.createElement("div")).addClass("left-border border"));
        wrapper.append($(document.createElement("div")).addClass("right-border border"));
        wrapper.append($(document.createElement("div")).addClass("bottom-border border"));
        */
        
        var cb = this.CallBack;
        var dest = function(){
            DealMapPopup.destroy(bubble);
            if(cb)
                cb();
        };
        var closelink = $(document.createElement("a")).addClass("close-x").text("");
        closelink.click(dest);
        }
        if(this.autoDestroy)
            setTimeout(dest,5000);
        
        wrapper.append($(document.createElement("div")).addClass("arrow"));
        
        if(this.title)
            wrapper.append(this.createHeading(this.titleClick));
        
        var inner =   $(document.createElement("div")).addClass("inner");
        inner.append(closelink);
        inner.append(this.html);
        wrapper.append(inner);
        bubble.append(wrapper);
        
        if(this.extraClasses) { bubble.addClass(this.extraClasses) }
        
        //insert the bubble at the end of the body.
        if(DealMapPopup.RenderBubble)
        {
            $("body").append(bubble);
        
        
            var p = this.getBubblePosition(bubble);
            
            bubble.css("left",p.left);
            bubble.css("top", p.top);
            
            this.openBubblesAnchors[bubble.achorElement.attr('id')] = bubble;
        }
        this.reset();
        
        return bubble;
    },
    createHeading: function(clickFunc)
    {
        var heading = $(document.createElement("div")).addClass("title-heading clearfix");
        var message = $(document.createElement("div")).addClass("title-message float").text(this.title);
        heading.append(message);
        
        if(clickFunc)
        {
            var arrows = $(document.createElement("div")).addClass("title-arrows float-right");
            arrows.click(clickFunc)
            heading.append(arrows);
        }
        return heading;
    },
    getBubblePosition:function(bubble)
    {
            
        var isFixed = this.checkFixedPosition();
            
        var p = this.BubblePosition ? this.BubblePosition : $(this.anchor).offset();
        
        if(this.arrowPosition == DealMapPopupArrowPositions.top)
        {
            if(!isFixed)
            {
                p.left += this.anchor.width()-(bubble.width() -20);
                p.top += this.anchor.height()+15;
            }
            else
            {
                p.top = 25;
                p.left += this.anchor.width()-(bubble.width() +20);
            }
        }
        else if(this.arrowPosition == DealMapPopupArrowPositions.left)
        {
            if(!isFixed)
            {
                
                p.left += this.anchor.width()+ 15;
                p.top += this.anchor.height()-100;
            }
            else
            {
                p.top = 25;
                p.left += this.anchor.width()+15;
            }
        }
        else if(this.arrowPosition == DealMapPopupArrowPositions.bottom)
        {
            if(!isFixed)
            {
                p.left += this.anchor.width()-(bubble.width() -20);
                p.top += this.anchor.height()-bubble.height() - 40;
            }
            else
            {
                p.top = 25;
                p.left += this.anchor.width()-(bubble.width() +20);
            }
        }
        
        else if(this.arrowPosition == DealMapPopupArrowPositions.topLeft)
        {
            if(!isFixed)
            {
                //p.left += this.anchor.width() + (bubble.width() -20);
                p.top += this.anchor.height()+15;
            }
            else
            {
                p.top = 25;
                //p.left += this.anchor.width()-(bubble.width() +20);
            }    
        }
        return p;
    },
    setFixedPosition:function(bubble, anch)
    {
        //check to see if it should be static
        if(this.checkFixedPosition(anch))
            bubble.addClass("static-bubble");
        else
            bubble.removeClass("static-bubble");
    },
    checkFixedPosition:function(anch)
    {
        if(!this.allowFixedPosition)
            return false;
            
        var scroll = $(window).scrollTop() - 25;
        var elm = anch ? anch : this.anchor;

        var anchortop = elm.offset().top;
            
        return (scroll>anchortop? true : false);
    },
    openBubblesAnchors: new Array(),
    destroy: function(bubble)
    {
        try
        {
            bubble.fadeOut();
            
            if(this.openBubblesAnchors[bubble.achorElement.attr('id')])
                this.openBubblesAnchors[bubble.achorElement.attr('id')] = null;
            
            var dest = function(){bubble.remove();}
            setTimeout(dest,5000);
        }
        catch(err){};
    },
    reset:function()
    {
        this.html = "";
        this.anchor = null;
        this.title = null;
        this.extraClasses = "";
        this.BubblePosition = null;
        this.RenderBubble = true;
        this.arrowPosition = DealMapPopupArrowPositions.top;
        this.autoDestroy = true;
        this.CallBack = null;
        
    }
}
