$(document).ready(function (){
	if (document.getElementById("deal_listing")){
		load_deals();
	}
});

deal_page = 1;
after = true;



function apply_deal_effects(){
	$('.deal-image').mouseover(function(){
		var diff = $(this).find('.price-diff');
		diff.fadeIn();
		//$('.price-diff').fadeIn();
	});
	$('.deal-image').mouseout(function(){
		var diff = $(this).find('.price-diff');
		diff.fadeOut();
	});
}

function deal_search(str,loc){
	$.post("/spiffs/search/",{str:str,loc:loc},function(data){
		$('#content-area').html("<div id='deal_listing'>"+data+"</div>");
		//$('#deal_listing').html(data);
		apply_deal_effects();
		return;
	});
}

function load_deals(){
	$.get("/spiffs/deals/"+deal_page+"/",{},function(data){
		if (data == "<!-- END -->"){
			alert("No more deals")
		}else{
			$('#deal_listing').html(data);
			apply_deal_effects();
		}
		return;
		
		if (after){
			$('#deal_listing').append(data);
		}else{
			temp = $('#deal_listing').html()
			$('#deal_listing').html(data);
			$('#deal_listing').append(temp);
		}
	});
}

function next_deal_page(){
	deal_page++;
	after = true;
	load_deals();
}

function prev_deal_page(){
	if (deal_page > 1){
		deal_page--;
		after = false;
		load_deals();
	}
}
