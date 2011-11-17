var is_ready = function(){
			$('.login-box').hide();
			$('.signup-form-container').hide();
			$('.parda').hide();
			$('.search-form-box').hide();
			$('#settings-menu').hide();
			$('#user-menu').hide();
			$('#marchents').hide();
			$('#company-info').hide();
			$('#follow-us').hide();
			//$('.price-diff').hide();
			
			$('.editable').click(function(){
				var data = $(this).find('.setting-value span').html();
				$(this).find('.setting-value').hide();
				$(this).find('.hidden-field').val(data);
				$(this).find('.hidden-field').show();
				return false;
			});
			
			$('#login-window-button').click(function(){
				$('.login-box').fadeIn();
			});
			$('.cross').click(function(){
				$('.login-box').fadeOut();
			});
			
			$('#signup-window-button').click(function(){
				$('.signup-form-container').fadeIn();
				$('.parda').fadeIn();
				return false;
			});
			
			$('.cross2').click(function(){
				$('.signup-form-container').fadeOut();
				$('.parda').fadeOut();
			});
			$('#search-button').click(function(){
				$('.search-form-box').fadeIn();
				return false;
			});
			$('.search-cross').click(function(){
				$('.search-form-box').fadeOut();
			});
			$('#settings').click(function(){
				$('#settings-menu').fadeIn();
				
			});
			$('#settings').blur(function(){
				$('#settings-menu').fadeOut();
			});
			$('#user').click(function(){
				$('#user-menu').fadeIn();
			});
			$('#user').blur(function(){
				$('#user-menu').fadeOut();
			});
			$('#am').click(function(){
				$('#marchents').fadeIn();
				return false;
			});
			$('#am').blur(function(){
				$('#marchents').fadeOut();
			});
			$('#companyInfo').click(function(){
				$('#company-info').fadeIn();
				return false;
			});
			$('#companyInfo').blur(function(){
				$('#company-info').fadeOut();
			});
			$('#followUs').click(function(){
				$('#follow-us').fadeIn();
				return false;
			});
			$('#followUs').blur(function(){
				$('#follow-us').fadeOut();
			});
			
			
			
			$("#b-month").change(dob);
			$("#b-day").change(dob);
			$("#b-year").change(dob);
			
			parse_dob();
			
			//Location and email collection at start
			
			$('.get-location').animate({
				top: '40%'
			});
			
			$("#close_location_box").click(function(){
				landed("","");
			})
			
			$('#form-button-1').click(function(){
				var loc_val = $("#location-collect").val();
				var e_val = $("#email-collect").val();
				
				if (loc_val && e_val){
					landed(loc_val,e_val);
				}
				return false;
			});
			$('#form-button-2').click(function(){
				var e_val = $("#email-collect").val();
				
				if (e_val){
					email = e_val;
					$('.get-email').fadeOut();
					$('.parda2').fadeOut();
					
					landed();
				}
				return false;
			});
			//------------
			
			$("#deal-search-button").click(function(){
				keyword_str = $("#keyword_str").val();
				keyword_loc = $("#search-city-field").val();
				deal_search(keyword_str,keyword_loc);	
				$('.search-form-box').fadeOut();			
			});
			
			if (document.getElementById("feed_panels")){
				$.get("/social/facebook/feed/",{},function(data){
					$("#feed_panels").append(data);
				})
				
				$.get("/social/twitter/home_timeline/",{},function(data){
					$("#feed_panels").append(data);
				})
				
			}
			
			$("#settings-submit").click(function(){
				 document.forms["settings"].submit();
			});
		};




$(document).ready(is_ready);

function remove_location(){
	$('.get-location').animate({
			top: '100%',
			opacity: 0
		},1000, function(){
			$('.get-location').fadeOut();
			
		});
	$('.parda2').fadeOut();
}

function landed (loc,email){
	$.get("/members/landed/",{"loc":loc, "email": email},function(data){
		remove_location();
		if (data == "SUCCESS"){
			$(".location-form .setting-value span").html(loc);
			$("#location-field").val(loc).hide();
		}
	});
}

function likedeal(){
	$.get($("#likedeal").attr("href"),{},function(data){
		data = $.parseJSON(data);
		alert(data.message);
		
	});
	return false;
}

function share_deal (){
			link = $("#sharedeal").attr("href");
			$("#iframe_share").html("<div><iframe src='"+link+"'></iframe></div>")
		}

function parse_dob(){
	d = $("#id_dob").val();
	if (d){
		parts = d.split("-");		
		
		//alert(parts[1]+":" + parseInt(parts[1]))
		
		$("#b-year").val(parts[0]);
		$("#b-month").val(parseInt(parts[1]));
		$("#b-day").val(parseInt(parts[2]));
	}else{
		//alert("NOT")
	}
}

function approve_deal(deal_id){
	$.get("/spiffs/deals/approve/"+deal_id+"/",{},function(data){
		data = $.parseJSON(data);
		$("#approve-deal-"+deal_id).replaceWith("<span style='color:red;'>Approved</span>");
		$("#reject-deal-"+deal_id).hide();
	});
}

function reject_deal(deal_id){
	$.get("/spiffs/deals/reject/"+deal_id+"/",{},function(data){
		data = $.parseJSON(data);
		$("#reject-deal-"+deal_id).replaceWith("<span style='color:red;'>Rejected</span>");
		$("#approve-deal-"+deal_id).hide();
	});
}

function dob (){
	month 	= $("#b-month").val();
	day	= $("#b-day").val();
	year	= $("#b-year").val();
	
	if (month != "" && day != "" && year != ""){
		$("#id_dob").val(year+"-"+month+"-"+day);
	}else{
		$("#id_dob").val("");
	}
	
	//alert(month+"/"+day+"/"+year+"||"+$("#id_dob").val());
}
