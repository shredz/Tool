$(document).ready(function() {

	//rotation speed and timer
	var speed = 3000;
	var run = setInterval('rotate()', speed);	
	
	//grab the width and calculate left value
	var item_width = $('#slides li').outerWidth(); 
	var left_value = item_width * (0); 
        
    //move the last item before first item, just in case user click prev button
	$('#slides li:first').before($('#slides li:last'));
	
	//set the default item to the correct position 
	$('#slides ul').css({'left' : left_value});

    //if user clicked on prev button
	$('#prev').click(function() {

		//get the right position            
		var left_indent = parseInt($('#slides ul').css('left')) + item_width;

		//slide the item            
		$('#slides ul:not(:animated)').animate({'left' : left_indent}, 500,function(){    

            //move the last item and put it as first item            	
			$('#slides li:first').before($('#slides li:last'));           

			//set the default item to correct position
			$('#slides ul').css({'left' : left_value});
		
		});

		//cancel the link behavior            
		return false;
            
	});

 
    //if user clicked on next button
	$('#next').click(function() {
		
		//get the right position
		var left_indent = parseInt($('#slides ul').css('left')) - item_width;
		
		//slide the item
		$('#slides ul:not(:animated)').animate({'left' : left_indent}, 500, function () {
            
            //move the first item and put it as last item
			$('#slides li:last').after($('#slides li:first'));                 	
			
			//set the default item to correct position
			$('#slides ul').css({'left' : left_value});
		
		});
		         
		//cancel the link behavior
		return false;
		
	});        
	

        
});

$(document).ready(function() {

	//rotation speed and timer
	var speed = 3000;
	var run = setInterval('rotate1()', speed);	
	
	//grab the width and calculate left value
	var item_width = $('#slides1 li').outerWidth(); 
	var left_value = item_width * (0); 
        
    //move the last item before first item, just in case user click prev button
	$('#slides1 li:first').before($('#slides1 li:last'));
	
	//set the default item to the correct position 
	$('#slides1 ul').css({'left' : left_value});

    //if user clicked on prev button
	$('#prev1').click(function() {

		//get the right position            
		var left_indent = parseInt($('#slides1 ul').css('left')) + item_width;

		//slide the item            
		$('#slides1 ul:not(:animated)').animate({'left' : left_indent}, 500,function(){    

            //move the last item and put it as first item            	
			$('#slides1 li:first').before($('#slides1 li:last'));           

			//set the default item to correct position
			$('#slides1 ul').css({'left' : left_value});
		
		});

		//cancel the link behavior            
		return false;
            
	});

 
    //if user clicked on next button
	$('#next1').click(function() {
		
		//get the right position
		var left_indent = parseInt($('#slides1 ul').css('left')) - item_width;
		
		//slide the item
		$('#slides1 ul:not(:animated)').animate({'left' : left_indent}, 500, function () {
            
            //move the first item and put it as last item
			$('#slides1 li:last').after($('#slides1 li:first'));                 	
			
			//set the default item to correct position
			$('#slides1 ul').css({'left' : left_value});
		
		});
		         
		//cancel the link behavior
		return false;
		
	});        
	

        
});

//a simple function to click next link
//a timer will call this function, and the rotation will begin :)  
function rotate1() {
//$('#next1').click();
}   

function rotate() {
//$('#next').click();
} 